# utils.py
# import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

def infer_feature_types(df):
    """Split features into continuous and categorical"""
    continuous_features = []
    categorical_features = []
    for col in df.columns:
        if is_numeric_dtype(df[col]):
            continuous_features.append(col)
        else:
            categorical_features.append(col)
    return continuous_features, categorical_features

def matches_rule(row, rule, target_column):
    """Check if a row matches rule conditions"""
    for feature, value in rule.items():
        if feature == target_column:
            continue
        if isinstance(value, tuple):
            min_val, max_val = value
            if not (min_val <= row[feature] <= max_val):
                return False
        else:
            if row[feature] != value:
                return False
    return True

# utils.py
def format_rule_for_human(rule, metrics, history):
    """Format a rule and its metrics into a readable string"""
    lines = []
    lines.append("=" * 50)

    # Format conditions
    lines.append("Rule Conditions:")
    for feature, value in rule.items():
        if isinstance(value, tuple):
            lines.append(f"  {feature}: {value[0]:.1f} to {value[1]:.1f}")
        else:
            lines.append(f"  {feature}: {value}")

    # Format key metrics
    lines.append("\nPerformance:")
    lines.append(f"  Score: {metrics['score']:.3f}")
    lines.append(f"  Coverage: {metrics['coverage']:.3f} ({metrics['matching_samples']} samples)")
    lines.append(f"  Dominant Class: {metrics['dominant_class']}")

    # Format pruning history
    if history:
        lines.append("\nPruning Steps:")
        for step in history:
            lines.append(f"  Removed: {step['removed_feature']} "
                        f"(improvement: {step['improvement']:.3f})")

    return "\n".join(lines) + "\n"

def save_rules_to_file(rules, filename='rules_output.txt'):
    """Save rules to a text file"""
    with open(filename, 'w') as f:
        f.write(f"Generated Rules Report\n")
        f.write(f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for i, (rule, metrics, history) in enumerate(rules, 1):
            f.write(f"Rule {i}\n")
            f.write(format_rule_for_human(rule, metrics, history))
            f.write("\n")
