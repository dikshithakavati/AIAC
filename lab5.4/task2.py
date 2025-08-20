import re
from typing import Dict, List, Tuple


# Minimal lexicon for demo purposes. In production, use a vetted, larger lexicon
# and measure performance/bias across domains and demographics.
SENTIMENT_LEXICON: Dict[str, float] = {
    "good": 1.0,
    "great": 1.4,
    "excellent": 1.8,
    "amazing": 1.6,
    "love": 1.5,
    "like": 0.8,
    "happy": 1.2,
    "pleasant": 1.0,
    "bad": -1.0,
    "poor": -1.0,
    "terrible": -1.8,
    "awful": -1.6,
    "hate": -1.5,
    "dislike": -0.8,
    "sad": -1.2,
    "angry": -1.1,
}

NEGATIONS = {"not", "no", "never", "none", "cannot", "cant", "can't", "won't", "wont", "isn't", "isnt", "don't", "dont"}
INTENSIFIERS = {"very": 1.5, "extremely": 1.8, "really": 1.3, "so": 1.2, "super": 1.4}
DEINTENSIFIERS = {"slightly": 0.6, "somewhat": 0.7, "kinda": 0.8, "kind": 0.8, "a": 0.9, "bit": 0.9}


def tokenize_text(text: str) -> List[str]:
    # Simple tokenizer; for robust handling use a proper NLP tokenizer.
    return [t for t in re.split(r"[^a-zA-Z']+", text.lower()) if t]


def analyze_sentiment(text: str) -> Dict[str, float | str]:
    """Return a simple sentiment analysis for the given text.

    Bias notes (read before using on real data):
    - Lexicon bias: Word lists encode cultural and domain biases. Validate/curate lexicons
      with diverse stakeholders and domain experts; allow overrides per domain.
    - Dataset skew: When training data is used, check class balance and representation across
      demographics/domains. Use stratified metrics and confusion matrices by subgroup.
    - Offensive/identity terms: Identity words can correlate spuriously with negative labels.
      Consider masking identity terms for training or using counterfactual data augmentation
      (swap identity terms) to reduce bias. Measure with counterfactual evaluation.
    - Mitigations: Balance classes via reweighting or resampling; remove/replace slurs in labels;
      add neutral and positive examples featuring reclaimed/identity terms; perform bias audits.
    """

    tokens = tokenize_text(text)

    running_score: float = 0.0
    matched_terms: int = 0
    pending_negation: bool = False
    intensity_multiplier: float = 1.0

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token in NEGATIONS:
            pending_negation = not pending_negation
            i += 1
            continue

        if token in INTENSIFIERS:
            intensity_multiplier *= INTENSIFIERS[token]
            i += 1
            continue

        if token in DEINTENSIFIERS:
            intensity_multiplier *= DEINTENSIFIERS[token]
            i += 1
            continue

        if token in SENTIMENT_LEXICON:
            word_score = SENTIMENT_LEXICON[token]
            if pending_negation:
                word_score *= -1
                pending_negation = False

            word_score *= intensity_multiplier
            # Decay intensity so only adjacent terms are strongly affected.
            intensity_multiplier = 1.0

            running_score += word_score
            matched_terms += 1

        i += 1

    # Normalize by number of matched sentiment terms to avoid long-text bias.
    if matched_terms == 0:
        normalized = 0.0
    else:
        normalized = max(-1.0, min(1.0, running_score / (matched_terms * 1.5)))

    if normalized > 0.25:
        label = "positive"
    elif normalized < -0.25:
        label = "negative"
    else:
        label = "neutral"

    return {
        "score": round(normalized, 4),
        "label": label,
        "matched_terms": matched_terms,
    }


# Suggestions for bias detection and handling in model development:
# - Data audit: Quantify class balance and representation across sensitive attributes (when available).
#   Run per-group precision/recall/F1 and error rates; manually review false positives/negatives.
# - Rebalancing: Use class weights or resampling (oversample minority classes, undersample majority).
# - Offensive content handling: Remove or relabel slur-only samples that leak label shortcuts; keep
#   neutral and positive examples containing identity terms to avoid proxy discrimination.
# - Counterfactual evaluation: Swap identity tokens (e.g., group A -> group B) and verify predictions
#   are stable when sentiment is unchanged.
# - Domain adaptation: If deploying to a new domain/dialect, collect targeted validation sets and
#   fine-tune/calibrate rather than relying on generic datasets.
# - Human-in-the-loop: Periodically sample and review model outputs; create an escalation path for
#   impacted users to report harms and for quick dataset/model updates.


if __name__ == "__main__":
    try:
        user_text = input("Enter a sentence to analyze sentiment: ").strip()
    except EOFError:
        user_text = ""

    if not user_text:
        print("No input provided.")
    else:
        result = analyze_sentiment(user_text)
        print(f"Input: {user_text}")
        print("Sentiment:", result)


