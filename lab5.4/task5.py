"""
Machine Learning Classification Example (Responsible AI Edition)

This script trains a simple classification model using scikit-learn and
demonstrates responsible ML practices with inline guidance.

Responsible use quick-start:
- Purpose limitation: Use this model only for educational demos or low-risk
  tasks. It is not validated for medical, legal, financial, or high-stakes use.
- Data sensitivity: Do not include personally identifiable information (PII)
  or protected attributes in training data unless you have legal basis and
  a clear mitigation plan. This demo uses public toy datasets without PII.
- Performance & limitations: Evaluate accuracy, precision, recall, F1, and
  AUC across splits. Expect variance. Small datasets are prone to overfitting
  and may not generalize.
- Bias & fairness: Even when protected attributes are absent, proxies may
  exist. Evaluate subgroup performance if any sensitive attributes are present.
  Use fairness-aware evaluation/mitigations where appropriate.
- Explainability: We surface feature coefficients/importance as a basic form
  of explainability. Treat this as a guide, not ground truth causality.
- Reproducibility: Fix random seeds, log versions, and save artifacts.
- Security & privacy: Avoid logging raw data. Store only necessary artifacts.

How to run:
1) Train and evaluate (default dataset: breast_cancer):
   python task5.py --dataset breast_cancer --model logistic --test-size 0.2

2) Save artifacts (model and metrics written under ./artifacts):
   python task5.py --save-artifacts

3) Optional: change dataset (iris) or model (random_forest):
   python task5.py --dataset iris --model random_forest --explain

Outputs:
- Console metrics (accuracy, precision, recall, f1, auc if applicable)
- Confusion matrix summary
- Optional simple explainability via feature importances/coefficients
- artifacts/model.pkl, artifacts/metrics.json (if --save-artifacts)
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Optional, Tuple
import importlib


@dataclass
class DatasetBundle:
    features: Any
    labels: Any
    feature_names: List[str]
    target_names: Optional[List[str]]


def _require_module(module_name: str, install_hint: str):
    try:
        return importlib.import_module(module_name)
    except ImportError as exc:
        raise SystemExit(
            f"Missing dependencies. Please install with: pip install {install_hint}"
        ) from exc


def load_dataset(name: str) -> DatasetBundle:
    """Load a toy dataset with no PII for ethical demo purposes.

    Accepts: "breast_cancer" (default) or "iris".
    """
    # Local imports to avoid hard dependency at module import time
    numpy = _require_module("numpy", "numpy")
    sk_datasets = _require_module("sklearn.datasets", "scikit-learn")

    name = name.lower()
    if name == "iris":
        data = sk_datasets.load_iris()
    else:
        data = sk_datasets.load_breast_cancer()

    features = numpy.asarray(data.data, dtype=float)
    labels = numpy.asarray(data.target, dtype=int)
    feature_names = [str(n) for n in data.feature_names]
    target_names = [str(n) for n in getattr(data, "target_names", [])] if hasattr(data, "target_names") else None
    return DatasetBundle(features, labels, feature_names, target_names)


def create_pipeline(model_name: str) -> Any:
    """Create a simple, readable sklearn pipeline.

    Standardizes continuous inputs; supports logistic regression and random forest.
    """
    # Local imports
    sk_pre = _require_module("sklearn.preprocessing", "scikit-learn")
    sk_lin = _require_module("sklearn.linear_model", "scikit-learn")
    sk_ens = _require_module("sklearn.ensemble", "scikit-learn")
    sk_pipe = _require_module("sklearn.pipeline", "scikit-learn")

    model_name = model_name.lower()
    if model_name == "random_forest":
        model = sk_ens.RandomForestClassifier(n_estimators=200, random_state=42)
        steps = [("scaler", sk_pre.StandardScaler()), ("clf", model)]
    else:
        model = sk_lin.LogisticRegression(max_iter=10_000, n_jobs=None, solver="lbfgs", random_state=42)
        steps = [("scaler", sk_pre.StandardScaler()), ("clf", model)]
    return sk_pipe.Pipeline(steps)


def compute_metrics(y_true: Any, y_pred: Any, y_proba: Optional[Any]) -> Dict[str, float]:
    """Compute core metrics; AUC only if probabilistic outputs available and binary/multiclass supported."""
    # Local imports
    sk_metrics = _require_module("sklearn.metrics", "scikit-learn")

    metrics: Dict[str, float] = {
        "accuracy": float(sk_metrics.accuracy_score(y_true, y_pred)),
        "precision_macro": float(sk_metrics.precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "recall_macro": float(sk_metrics.recall_score(y_true, y_pred, average="macro", zero_division=0)),
        "f1_macro": float(sk_metrics.f1_score(y_true, y_pred, average="macro", zero_division=0)),
    }
    try:
        if y_proba is not None:
            # Normalize probability shape for ROC-AUC
            if y_proba.ndim == 1:
                # Already probabilities for positive class
                metrics["roc_auc_ovr"] = float(sk_metrics.roc_auc_score(y_true, y_proba))
            elif y_proba.shape[1] == 1:
                # Single-column probabilities
                metrics["roc_auc_ovr"] = float(sk_metrics.roc_auc_score(y_true, y_proba.ravel()))
            elif y_proba.shape[1] == 2:
                # Binary: use positive class probability
                metrics["roc_auc_ovr"] = float(sk_metrics.roc_auc_score(y_true, y_proba[:, 1]))
            else:
                # Multiclass: pass full probability matrix
                metrics["roc_auc_ovr"] = float(sk_metrics.roc_auc_score(y_true, y_proba, multi_class="ovr"))
    except Exception:
        # AUC not available; this is acceptable for quick demos
        pass
    return metrics


def get_feature_contributions(pipeline: Any, feature_names: List[str]) -> List[Tuple[str, float]]:
    """Return a simple list of (feature, importance) for explainability.

    For LogisticRegression uses absolute value of coefficients per class aggregated.
    For RandomForest uses feature_importances_. Values are normalized for readability.
    """
    # Local imports
    try:
        numpy = importlib.import_module("numpy")
    except Exception:
        return []

    model = pipeline.named_steps.get("clf")
    # Duck-typing to avoid importing sklearn classes at module scope
    if hasattr(model, "coef_"):
        coef = getattr(model, "coef_", None)
        if coef is None:
            return []
        agg = numpy.linalg.norm(coef, axis=0)
        if numpy.sum(agg) > 0:
            agg = agg / numpy.sum(agg)
        return list(zip(feature_names, agg.tolist()))
    if hasattr(model, "feature_importances_"):
        imp = getattr(model, "feature_importances_", None)
        if imp is None:
            return []
        if numpy.sum(imp) > 0:
            imp = imp / numpy.sum(imp)
        return list(zip(feature_names, imp.tolist()))
    return []


def train_and_evaluate(
    dataset_name: str,
    model_name: str,
    test_size: float,
    random_state: int,
    explain: bool,
) -> Dict[str, Any]:
    """Train, evaluate, and optionally explain the model. Returns a result dict.

    Notes on responsibility:
    - This trains on toy datasets without PII. For real data, validate data
      provenance and obtain necessary consent.
    - The resulting metrics are indicative only; run repeated CV and assess
      subgroup performance before deployment.
    """
    # Local imports
    sk_ms = _require_module("sklearn.model_selection", "scikit-learn")
    sk_metrics = _require_module("sklearn.metrics", "scikit-learn")

    bundle = load_dataset(dataset_name)

    X_train, X_test, y_train, y_test = sk_ms.train_test_split(
        bundle.features,
        bundle.labels,
        test_size=test_size,
        random_state=random_state,
        stratify=bundle.labels,
    )

    pipeline = create_pipeline(model_name)
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    y_proba: Optional[Any] = None
    if hasattr(pipeline, "predict_proba"):
        try:
            y_proba = pipeline.predict_proba(X_test)
        except Exception:
            y_proba = None

    metrics = compute_metrics(y_test, y_pred, y_proba)
    cm = sk_metrics.confusion_matrix(y_test, y_pred)
    report = sk_metrics.classification_report(
        y_test,
        y_pred,
        target_names=bundle.target_names if bundle.target_names else None,
        zero_division=0,
    )

    result: Dict[str, Any] = {
        "dataset": dataset_name,
        "model": model_name,
        "random_state": random_state,
        "test_size": test_size,
        "metrics": metrics,
        "confusion_matrix": cm.tolist(),
        "classification_report": report,
    }

    if explain:
        contributions = get_feature_contributions(pipeline, bundle.feature_names)
        # Sort descending by contribution
        contributions = sorted(contributions, key=lambda x: x[1], reverse=True)
        result["feature_contributions"] = contributions

    result["pipeline"] = pipeline
    result["feature_names"] = bundle.feature_names
    result["target_names"] = bundle.target_names
    return result


def save_artifacts(result: Mapping[str, Any], out_dir: str = "artifacts") -> None:
    """Persist model and metrics. Do not store raw data or PII."""
    os.makedirs(out_dir, exist_ok=True)

    # Save model
    model_path = os.path.join(out_dir, "model.pkl")
    joblib = _require_module("joblib", "joblib")
    joblib.dump(result["pipeline"], model_path)

    # Save metrics and summary (exclude the pipeline object)
    serializable = {k: v for k, v in result.items() if k not in {"pipeline"}}
    metrics_path = os.path.join(out_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2)


def print_summary(result: Mapping[str, Any], show_explain: bool) -> None:
    """Human-readable console output.

    We keep the printouts concise to avoid leaking data. Only aggregate
    metrics and high-level model info are displayed.
    """
    print("\n=== Training Summary ===")
    print(f"Dataset: {result['dataset']}")
    print(f"Model:   {result['model']}")
    print(f"Test size: {result['test_size']}")
    print("\nMetrics:")
    for k, v in result["metrics"].items():
        print(f"  {k}: {v:.4f}")
    print("\nConfusion matrix:")
    for row in result["confusion_matrix"]:
        print("  ", row)
    print("\nClassification report:\n")
    print(result["classification_report"])  # pre-formatted

    if show_explain and "feature_contributions" in result:
        print("Top features (importance ~ relative influence):")
        for name, score in result["feature_contributions"][:10]:
            print(f"  {name}: {score:.4f}")

    print("\nResponsible use notes:")
    print("- Metrics are indicative only; validate with repeated CV and holdouts.")
    print("- Evaluate subgroup performance to detect potential biases.")
    print("- Use feature importances for guidance, not causal claims.")
    print("- Do not train or infer on PII without consent and safeguards.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Train a simple classifier with responsible AI guidance. "
            "Supports logistic regression and random forest on toy datasets."
        )
    )
    parser.add_argument("--dataset", choices=["breast_cancer", "iris"], default="breast_cancer")
    parser.add_argument("--model", choices=["logistic", "random_forest"], default="logistic")
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument("--explain", action="store_true", help="Print simple explainability outputs")
    parser.add_argument("--save-artifacts", action="store_true", help="Save model and metrics to ./artifacts")

    args = parser.parse_args()

    result = train_and_evaluate(
        dataset_name=args.dataset,
        model_name=args.model,
        test_size=args.test_size,
        random_state=args.random_state,
        explain=args.explain,
    )

    print_summary(result, show_explain=args.explain)

    if args.save_artifacts:
        save_artifacts(result)
        print("\nArtifacts saved to ./artifacts (model.pkl, metrics.json)")


if __name__ == "__main__":
    main()


