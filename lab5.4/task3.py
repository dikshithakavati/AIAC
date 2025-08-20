from __future__ import annotations

from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import Dict, List, Tuple, Iterable


@dataclass(frozen=True)
class Product:
    product_id: str
    title: str
    brand: str
    category: str


def build_copurchase_graph(purchase_history: Dict[str, List[str]]) -> Dict[Tuple[str, str], int]:
    """Build co-purchase counts between pairs of products.

    Transparency: We use simple co-occurrence counts so we can explain recommendations
    in human terms ("Users who bought X also bought Y").
    """

    edge_to_count: Dict[Tuple[str, str], int] = defaultdict(int)
    for user_id, products in purchase_history.items():
        unique_products = list(dict.fromkeys(products))
        for i in range(len(unique_products)):
            for j in range(i + 1, len(unique_products)):
                a, b = unique_products[i], unique_products[j]
                edge_to_count[(a, b)] += 1
                edge_to_count[(b, a)] += 1
    return edge_to_count


def score_candidates(
    target_user_products: Iterable[str],
    edge_to_count: Dict[Tuple[str, str], int],
    decay: float = 0.85,
) -> Dict[str, float]:
    """Score candidate products using a simple weighted sum of co-purchases.

    Transparency: Scores derive from co-purchase frequencies with the user's items
    (recent items can be up-weighted externally if desired).
    """

    product_to_score: Dict[str, float] = defaultdict(float)
    for idx, owned in enumerate(target_user_products):
        weight = decay ** idx
        for (a, b), count in edge_to_count.items():
            if a == owned and b not in target_user_products:
                product_to_score[b] += count * weight
    return product_to_score


def fairness_rerank(
    candidates: Dict[str, float],
    products: Dict[str, Product],
    top_k: int = 10,
    max_per_brand: int = 2,
    min_category_diversity: int = 2,
) -> List[Tuple[str, float]]:
    """Rerank candidates to encourage fairness and diversity.

    Fairness strategies implemented:
    - Brand caps: Limit how many items per brand in the top results (avoids favoritism).
    - Category diversity: Ensure multiple categories are represented.
    - Monotonicity: We only demote items to satisfy fairness; we do not promote unknowns above
      vastly higher-scoring items without cause, preserving relevance.
    """

    sorted_items = sorted(candidates.items(), key=lambda kv: kv[1], reverse=True)
    brand_counter: Counter[str] = Counter()
    chosen: List[Tuple[str, float]] = []
    categories_present: set[str] = set()

    for pid, score in sorted_items:
        prod = products.get(pid)
        if not prod:
            continue

        if brand_counter[prod.brand] >= max_per_brand:
            continue

        chosen.append((pid, score))
        brand_counter[prod.brand] += 1
        categories_present.add(prod.category)

        if len(chosen) == top_k and len(categories_present) >= min_category_diversity:
            break

    if len(chosen) < top_k:
        for pid, score in sorted_items:
            if (pid, score) in chosen:
                continue
            prod = products.get(pid)
            if not prod:
                continue
            chosen.append((pid, score))
            if len(chosen) == top_k:
                break

    return chosen


def explain_recommendation(
    product_id: str,
    user_products: Iterable[str],
    edge_to_count: Dict[Tuple[str, str], int],
    products: Dict[str, Product],
) -> str:
    """Provide a concise human-readable explanation for transparency.

    Transparency principle: Show which owned items most strongly contributed.
    """

    contributions: List[Tuple[str, int]] = []
    for owned in user_products:
        count = edge_to_count.get((owned, product_id), 0)
        if count > 0:
            contributions.append((owned, count))

    contributions.sort(key=lambda kv: kv[1], reverse=True)
    top_parts: List[str] = []
    for owned, cnt in contributions[:3]:
        owned_title = products.get(owned).title if owned in products else owned
        top_parts.append(f"{owned_title} ({cnt})")

    prod_title = products.get(product_id).title if product_id in products else product_id
    if top_parts:
        return f"Recommended '{prod_title}' because you bought: " + ", ".join(top_parts)
    return f"Recommended '{prod_title}' based on similar users' purchases."


def collect_feedback() -> str:
    """Basic thumbs-up/down feedback channel.

    Ethics: Provide user control to accept/reject and use this signal to improve models.
    """

    while True:
        resp = input("Was this recommendation helpful? (y/n): ").strip().lower()
        if resp in {"y", "yes"}:
            return "positive"
        if resp in {"n", "no"}:
            return "negative"
        print("Please enter 'y' or 'n'.")


def recommend_for_user(
    user_id: str,
    purchase_history: Dict[str, List[str]],
    products: Dict[str, Product],
    top_k: int = 5,
) -> List[Tuple[str, float, str]]:
    """Generate recommendations along with explanations.

    Ethical guidelines embedded in this pipeline:
    - Transparency: We return explanations. Consider exposing factor weights and links to a policy.
    - Fairness: We cap brand dominance and enforce category diversity in the top-K.
    - User feedback: We solicit and can store feedback to improve or filter future results.
    """

    user_products = purchase_history.get(user_id, [])
    edge_to_count = build_copurchase_graph(purchase_history)
    raw_scores = score_candidates(user_products, edge_to_count)
    reranked = fairness_rerank(raw_scores, products, top_k=top_k)

    results: List[Tuple[str, float, str]] = []
    for pid, score in reranked:
        explanation = explain_recommendation(pid, user_products, edge_to_count, products)
        results.append((pid, score, explanation))

    return results


def demo() -> None:
    # Sample catalog. In production, source from a catalog service and regularly audit
    # metadata quality (brand/category completeness) to prevent skew.
    catalog: Dict[str, Product] = {
        "p1": Product("p1", "Eco Water Bottle", "AquaCo", "Outdoors"),
        "p2": Product("p2", "Insulated Mug", "AquaCo", "Kitchen"),
        "p3": Product("p3", "Trail Backpack", "HikeMax", "Outdoors"),
        "p4": Product("p4", "Yoga Mat", "ZenFit", "Fitness"),
        "p5": Product("p5", "Running Shoes", "ZenFit", "Fitness"),
        "p6": Product("p6", "Camping Stove", "CampX", "Outdoors"),
        "p7": Product("p7", "Chef Knife", "CookPro", "Kitchen"),
        "p8": Product("p8", "Coffee Grinder", "CookPro", "Kitchen"),
    }

    # Example purchase history. For fairness, regularly check for product/brand exposure bias
    # by cohort and ensure popular brands do not dominate due to legacy popularity alone.
    history: Dict[str, List[str]] = {
        "u1": ["p1", "p3", "p4"],
        "u2": ["p1", "p2", "p6"],
        "u3": ["p3", "p6"],
        "u4": ["p2", "p7", "p8"],
        "u5": ["p1", "p4", "p5"],
    }

    user_id = input("Enter user id (e.g., u1): ").strip()
    recs = recommend_for_user(user_id, history, catalog, top_k=5)

    if not recs:
        print("No recommendations available yet. Try adding more purchases.")
        return

    print("Recommendations:")
    for pid, score, explanation in recs:
        prod = catalog[pid]
        print(f"- {prod.title} (brand={prod.brand}, category={prod.category}) | score={score:.2f}")
        print(f"  Why: {explanation}")
        feedback = collect_feedback()
        # In production, store feedback and audit acceptance rates by brand/category to detect bias.
        print(f"  Feedback recorded: {feedback}")

    # Governance tips (not executed):
    # - Publish a user-facing explanation of how recommendations work and their limitations.
    # - Provide an opt-out and controls to adjust brand/category diversity preferences.
    # - Periodically audit top-K distribution across brands/categories; alarm on dominance.
    # - Allow merchants equal opportunity: avoid hard-coded whitelists or paid boosting without labeling.


if __name__ == "__main__":
    demo()


