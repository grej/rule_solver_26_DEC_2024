# utils.py
import numpy as np
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

def matches_rule(row, rule, target_var):
    """Check if a row matches rule conditions"""
    for feature, value in rule.items():
        if feature == target_var:
            continue
        if isinstance(value, tuple):
            min_val, max_val = value
            if not (min_val <= row[feature] <= max_val):
                return False
        else:
            if row[feature] != value:
                return False
    return True

def create_unicode_histogram(values, bins=10, width=30):
    """Create a simple unicode histogram."""
    hist, bin_edges = np.histogram(values, bins=bins)
    max_count = max(hist)

    # Unicode block characters from least to most filled
    blocks = ' ▁▂▃▄▅▆▇█'

    lines = []
    for count, edge in zip(hist, bin_edges[:-1]):
        bar_len = int((count / max_count) * width)
        bar = blocks[-1] * bar_len
        lines.append(f"{edge:6.2f} | {bar:<{width}} | {count:3d}")

    return '\n'.join(lines)

def visualize_rule_impact(df, rule, target_var, direction):
    """Create text visualization of rule's impact on target variable distribution."""
    matching_mask = df.apply(lambda row: matches_rule(row, rule, target_var), axis=1)
    matching_df = df[matching_mask]
    non_matching_df = df[~matching_mask]
    total_matching = len(matching_df)

    lines = [
        "Rule Impact Analysis",
        "=" * 50,
        f"\nMatching Samples: {total_matching} ({total_matching/len(df):.1%} of data)"
    ]

    # Show target variable distribution
    if direction in ['maximize', 'minimize']:
        matching_median = np.median(matching_df[target_var])
        non_matching_median = np.median(non_matching_df[target_var])

        lines.append(f"\n{target_var} Distribution:")
        lines.append(f"Matching samples median: {matching_median:.2f}")
        lines.append("\nMatching samples:")
        hist = create_unicode_histogram(matching_df[target_var].values)
        lines.append(hist)

        lines.append(f"\nNon-matching samples median: {non_matching_median:.2f}")
        lines.append("Non-matching samples:")
        hist = create_unicode_histogram(non_matching_df[target_var].values)
        lines.append(hist)

        improvement = ((matching_median - non_matching_median) / non_matching_median * 100
                      if direction == 'maximize' else
                      (non_matching_median - matching_median) / non_matching_median * 100)
        lines.append(f"\nImprovement: {improvement:+.1f}%")

    else:
        # For categorical target
        matching_counts = matching_df[target_var].value_counts(normalize=True)
        non_matching_counts = non_matching_df[target_var].value_counts(normalize=True)

        lines.append(f"\n{target_var} Distribution:")
        lines.append("\nMatching samples:")
        for cat, pct in matching_counts.items():
            lines.append(f"{cat:12} | {'█' * int(pct * 20):<20} | {pct:.1%}")

        lines.append("\nNon-matching samples:")
        for cat, pct in non_matching_counts.items():
            lines.append(f"{cat:12} | {'█' * int(pct * 20):<20} | {pct:.1%}")

        target_improvement = (matching_counts.get(direction, 0) -
                            non_matching_counts.get(direction, 0)) * 100
        lines.append(f"\nTarget class improvement: {target_improvement:+.1f}%")

    # Show distribution for all continuous features
    continuous_features = [f for f, v in rule.items() if isinstance(v, tuple)]
    if continuous_features:
        lines.append("\nFeature Distributions (Matching Samples):")
        for feature in continuous_features:
            lines.append(f"\n{feature}:")
            hist = create_unicode_histogram(matching_df[feature].values)
            lines.append(hist)
            if feature in rule:
                min_val, max_val = rule[feature]
                lines.append(f"Rule range: [{min_val:.2f}, {max_val:.2f}]")

    return '\n'.join(lines)

# utils.py (update the format_rule_for_human function)

# utils.py
def format_rule_for_human(rule, metrics, history):
    """Format a rule and its metrics into a readable string."""
    lines = []
    lines.append("=" * 50)

    # Format conditions
    lines.append("Rule Conditions:")
    rule_dict = rule if isinstance(rule, dict) else dict(rule)
    for feature, value in rule_dict.items():
        if isinstance(value, tuple):
            try:
                # Convert numpy values to float for cleaner printing
                min_val = round(float(value[0]), 3)
                max_val = round(float(value[1]), 3)
                lines.append(f"  {feature}: {min_val} to {max_val}")
            except:
                lines.append(f"  {feature}: {value[0]} to {value[1]}")
        else:
            lines.append(f"  {feature}: {value}")

    # Format key metrics
    lines.append("\nPerformance:")
    lines.append(f"  Score: {metrics['score']:.3f}")
    lines.append(f"  Direction Score: {metrics['direction_score']:.3f}")
    lines.append(f"  Coverage: {metrics['coverage']:.3f} ({metrics['matching_samples']} samples)")

    # Add target variable statistics if available
    if 'target_stats' in metrics:
        lines.append("\nTarget Variable Statistics:")
        stats = metrics['target_stats']
        if stats['matching_median'] is not None:
            lines.append(f"  Matching Median: {stats['matching_median']:.3f}")
            lines.append(f"  Non-matching Median: {stats['non_matching_median']:.3f}")
        if stats['matching_rate'] is not None:
            lines.append(f"  Matching Rate: {stats['matching_rate']:.3f}")
            lines.append(f"  Non-matching Rate: {stats['non_matching_rate']:.3f}")

    # Format history - handle both pruning and optimization steps
    if history:
        lines.append("\nRule Evolution:")
        for step in history:
            if 'removed_feature' in step:
                lines.append(f"  Pruned: {step['removed_feature']} "
                          f"(improvement: {step['improvement']:.3f})")
            elif 'step' in step and step['step'] == 'optimization':
                if 'change' in step:
                    lines.append(f"  Optimization: {step['change']} on {step['feature']} "
                              f"improved score from {step['initial_score']:.3f} "
                              f"to {step['final_score']:.3f} "
                              f"(gain: {step['improvement']:.3f})")
                else:
                    lines.append(f"  Optimization: score improved from {step['initial_score']:.3f} "
                              f"to {step['final_score']:.3f} "
                              f"(gain: {step['improvement']:.3f})")

    return '\n'.join(lines) + '\n'

def save_rules_to_file(rules, df, filename='rules_output.txt', target_var=None, direction=None):
    """Save rules to a text file with visualizations."""
    with open(filename, 'w') as f:
        f.write(f"Generated Rules Report\n")
        f.write(f"Target: {target_var} ({direction})\n")
        f.write(f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for i, (rule, metrics, history) in enumerate(rules, 1):
            f.write(f"Rule {i}\n")
            f.write(format_rule_for_human(rule, metrics, history))
            f.write("\nDistribution Analysis:\n")
            f.write(visualize_rule_impact(df, rule, target_var, direction))
            f.write("\n\n")
