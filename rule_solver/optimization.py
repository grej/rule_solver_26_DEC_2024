# optimization.py
"""
Rule optimization and stabilization using iterative improvement.
"""
from typing import Dict, List, Tuple, Optional
import numpy as np
import pandas as pd
from .scoring import calculate_directional_score

class RuleOptimizer:
    def __init__(self, df: pd.DataFrame, target_var: str, direction: str):
        """
        Initialize rule optimizer.
        """
        self.df = df
        self.target_var = target_var
        self.direction = direction

        # Compute dataset statistics once
        self.feature_ranges = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            self.feature_ranges[col] = {
                'min': df[col].min(),
                'max': df[col].max(),
                'median': df[col].median(),
                'q1': df[col].quantile(0.25),
                'q3': df[col].quantile(0.75)
            }

    def validate_rule(self, rule: Dict) -> bool:
        """Check if a rule matches any data points."""
        if not rule:
            return False

        try:
            matching_mask = self.df.apply(
                lambda row: self._matches_rule(row, rule), axis=1)
            matches = matching_mask.sum() >= max(3, len(self.df) * 0.01)  # At least 3 samples or 1%
            return matches
        except:
            return False

    def optimize_rule(self, rule: Dict,
                     min_improvement: float = 0.0001,  # Much lower threshold
                     max_iterations: int = 20) -> Tuple[Dict, List]:
        """
        Optimize a rule through iterative boundary adjustments.
        """
        print(f"\nStarting optimization with rule: {rule}")
        optimization_history = []

        # Start with base rule and score
        current_rule = rule.copy()
        if not self.validate_rule(current_rule):
            print("Initial rule validation failed")
            return current_rule, optimization_history

        try:
            base_metrics = calculate_directional_score(self.df, current_rule,
                                                     self.target_var, self.direction)
            base_score = base_metrics.get('score', 0)
            print(f"Initial score: {base_score:.4f}")
        except Exception as e:
            print(f"Error calculating base score: {e}")
            return current_rule, optimization_history

        for iteration in range(max_iterations):
            print(f"\nIteration {iteration + 1}:")
            made_improvement = False
            best_improvement = 0
            best_rule = None
            best_history_entry = None

            # Try more aggressive variations
            for feature, condition in list(current_rule.items()):
                if not isinstance(condition, tuple):
                    continue

                try:
                    min_val = float(condition[0])
                    max_val = float(condition[1])
                    feature_range = max_val - min_val

                    # Get feature statistics
                    if feature in self.feature_ranges:
                        feat_stats = self.feature_ranges[feature]

                        # More aggressive variations
                        variations = [
                            # Large expansions
                            (min_val - feature_range*0.5, max_val + feature_range*0.5),
                            (min_val - feature_range*0.3, max_val + feature_range*0.3),

                            # Large contractions
                            (min_val + feature_range*0.3, max_val - feature_range*0.3),
                            (min_val + feature_range*0.2, max_val - feature_range*0.2),

                            # Shifts
                            (min_val - feature_range*0.5, max_val - feature_range*0.5),
                            (min_val + feature_range*0.5, max_val + feature_range*0.5),

                            # Data-driven bounds
                            (feat_stats['q1'], feat_stats['q3']),
                            (feat_stats['min'], feat_stats['q3']),
                            (feat_stats['q1'], feat_stats['max']),

                            # Original boundaries with small adjustments
                            (min_val * 0.9, max_val * 1.1),
                            (min_val * 1.1, max_val * 0.9)
                        ]

                        print(f"\nTrying variations for {feature}")
                        for idx, new_bounds in enumerate(variations):
                            test_rule = current_rule.copy()
                            test_rule[feature] = new_bounds

                            if not self.validate_rule(test_rule):
                                continue

                            try:
                                new_metrics = calculate_directional_score(
                                    self.df, test_rule, self.target_var, self.direction)
                                improvement = new_metrics.get('score', 0) - base_score

                                if improvement > 0:
                                    print(f"  Variation {idx}: improvement = {improvement:.6f}")

                                if improvement > best_improvement:
                                    best_improvement = improvement
                                    best_rule = test_rule.copy()
                                    best_history_entry = {
                                        'step': 'optimization',
                                        'feature': str(feature),
                                        'change': 'interval_adjustment',
                                        'initial_score': base_score,
                                        'final_score': base_score + improvement,
                                        'improvement': improvement,
                                        'old_bounds': condition,
                                        'new_bounds': new_bounds
                                    }
                            except Exception as e:
                                print(f"Error testing variation: {e}")
                                continue

                except Exception as e:
                    print(f"Error processing feature {feature}: {e}")
                    continue

            # Apply best improvement found in this iteration
            if best_improvement > min_improvement and best_rule is not None:
                current_rule = best_rule
                base_score += best_improvement
                optimization_history.append(best_history_entry)
                made_improvement = True
                print(f"\nMade improvement: {best_improvement:.6f}")
                print(f"New rule: {current_rule}")
            else:
                print("No improvement found in this iteration")

            if not made_improvement:
                break

        print(f"\nOptimization complete. Final score: {base_score:.4f}")
        return current_rule, optimization_history

    def optimize_rules(self, rules: List[Dict]) -> List[Tuple[Dict, List]]:
        """Optimize a list of rules."""
        return [self.optimize_rule(rule) for rule in rules]
