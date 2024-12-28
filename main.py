# main.py
import pandas as pd
import numpy as np
from rule_solver.rules import find_best_rules, calculate_directional_score  # Add this import
from rule_solver.utils import save_rules_to_file
from rule_solver.optimization import RuleOptimizer


def format_rule(rule):
    """Helper to format rule values to reasonable precision."""
    formatted = {}
    for k, v in rule.items():
        # Convert numpy string types to regular strings
        key = str(k) if hasattr(k, 'dtype') else k

        if isinstance(v, tuple):
            # Round numeric values to 3 decimal places and handle numpy types
            try:
                min_val = round(float(v[0]), 3)
                max_val = round(float(v[1]), 3)
                formatted[key] = (min_val, max_val)
            except:
                formatted[key] = v
        else:
            # Handle non-tuple values
            formatted[key] = str(v) if hasattr(v, 'dtype') else v
    return formatted

def main():
    # Load data
    df = pd.read_parquet('./data/iris.parquet')
    print("Loaded data with shape:", df.shape)

    # Example 1: Find rules that maximize sepal_length
    print("\nFinding rules to maximize sepal_length...")
    results = find_best_rules(df, num_rules=3, target_var='sepal_length', direction='maximize')

    # Create optimizer instance
    optimizer = RuleOptimizer(df, target_var='sepal_length', direction='maximize')

    # Optimize each rule
    optimized_results = []
    for rule, metrics, history in results:
        print(f"\nOriginal rule: {format_rule(rule)}")
        print(f"Original score: {metrics['score']:.4f}")

        # Optimization returns (rule, history)
        opt_rule, opt_history = optimizer.optimize_rule(rule)

        # Get new metrics for optimized rule
        new_metrics = calculate_directional_score(df, opt_rule, 'sepal_length', 'maximize')

        print(f"Optimized rule: {format_rule(opt_rule)}")
        print(f"Final score: {new_metrics['score']:.4f}")
        print(f"Total improvement: {new_metrics['score'] - metrics['score']:.4f}")

        if opt_history:
            print("\nOptimization steps:")
            for step in opt_history:
                if 'old_bounds' in step:
                    print(f"  {step['feature']}: {step['old_bounds']} -> {step['new_bounds']}")
                    print(f"  Improvement: {step['improvement']:.4f}")

        # Combine histories
        combined_history = history + opt_history

        optimized_results.append((opt_rule, new_metrics, combined_history))

if __name__ == "__main__":
    main()
