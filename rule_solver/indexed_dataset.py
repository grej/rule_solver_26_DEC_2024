# indexed_dataset.py
"""
Memory-efficient indexed dataset implementation for fast rule discovery.
"""
import numpy as np
from typing import Tuple, List, Dict
import pandas as pd

class IndexedDataset:
    def __init__(self, data: np.ndarray, outcome_column_index: int):
        """
        Preprocesses and indexes the dataset for efficient queries.

        Parameters:
            data: The dataset to index
            outcome_column_index: The column index used for the outcome
        """
        self.n_features = data.shape[1]
        self.outcome_column_index = outcome_column_index
        self.indices = []
        self.sorted_features = []
        self.cumulative_sums = []
        self.outcome = data[:, outcome_column_index]

        # Preprocess each column
        for i in range(self.n_features):
            if i == outcome_column_index:
                continue

            # Sort the feature and compute cumulative sums
            sorted_indices = np.argsort(data[:, i])
            sorted_feature = data[sorted_indices, i]
            sorted_outcome = self.outcome[sorted_indices]
            cumulative_sum = np.cumsum(sorted_outcome)

            self.indices.append(sorted_indices)
            self.sorted_features.append(sorted_feature)
            self.cumulative_sums.append(cumulative_sum)

    def query(self, feature_index: int) -> Tuple[float, float, float, np.ndarray]:
        """
        Finds the best rule for a given feature index using precomputed indices and sums.

        Parameters:
            feature_index: The index of the feature to query

        Returns:
            tuple: (A, B, max_separation, indices_in_rule)
        """
        sorted_feature = self.sorted_features[feature_index]
        cumulative_sum = self.cumulative_sums[feature_index]
        total_sum = cumulative_sum[-1]

        best_start = 0
        best_end = 0
        max_separation = float('-inf')
        start = 0

        for end in range(len(sorted_feature)):
            inside_sum = cumulative_sum[end] - (cumulative_sum[start - 1] if start > 0 else 0)
            outside_sum = total_sum - inside_sum

            # Calculate separation (difference between inside and outside sums)
            separation = inside_sum - outside_sum

            if separation > max_separation:
                max_separation = separation
                best_start = start
                best_end = end

            # If current interval becomes negative, start new interval
            if separation < 0:
                start = end + 1

        A = sorted_feature[best_start]
        B = sorted_feature[best_end]
        indices_in_rule = self.indices[feature_index][best_start:best_end + 1]

        return A, B, max_separation, indices_in_rule

    def query_with_conditions(self, feature_index: int,
                            conditions: Dict[int, Tuple[float, float]]) -> Tuple[float, float, float, np.ndarray]:
        """
        Queries a feature while respecting existing conditions on other features.

        Parameters:
            feature_index: Index of feature to query
            conditions: Dictionary mapping feature indices to (min, max) bounds

        Returns:
            tuple: (A, B, max_separation, indices_in_rule)
        """
        # Create mask for all conditions
        mask = np.ones(len(self.outcome), dtype=bool)
        for feat_idx, (min_val, max_val) in conditions.items():
            if feat_idx != feature_index:
                feat_data = self.sorted_features[feat_idx]
                feat_indices = self.indices[feat_idx]
                condition_mask = (feat_data >= min_val) & (feat_data <= max_val)
                mask[feat_indices[~condition_mask]] = False

        # Apply mask to feature data and recalculate
        sorted_indices = self.indices[feature_index][mask[self.indices[feature_index]]]
        sorted_feature = self.sorted_features[feature_index][mask[self.indices[feature_index]]]
        sorted_outcome = self.outcome[sorted_indices]
        cumulative_sum = np.cumsum(sorted_outcome)

        # Find best interval on filtered data
        total_sum = cumulative_sum[-1] if len(cumulative_sum) > 0 else 0
        best_start = 0
        best_end = 0
        max_separation = float('-inf')
        start = 0

        for end in range(len(sorted_feature)):
            inside_sum = cumulative_sum[end] - (cumulative_sum[start - 1] if start > 0 else 0)
            outside_sum = total_sum - inside_sum
            separation = inside_sum - outside_sum

            if separation > max_separation:
                max_separation = separation
                best_start = start
                best_end = end

            if separation < 0:
                start = end + 1

        A = sorted_feature[best_start] if len(sorted_feature) > 0 else None
        B = sorted_feature[best_end] if len(sorted_feature) > 0 else None
        indices_in_rule = sorted_indices[best_start:best_end + 1] if len(sorted_indices) > 0 else np.array([])

        return A, B, max_separation, indices_in_rule
