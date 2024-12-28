# hyperrect.py

import pandas as pd
import numpy as np
from typing import Dict, Tuple, List, Union, Optional

class HyperRectangle:
    """
    Creates and manages hyperrectangles from data points.
    A hyperrectangle represents a rule with intervals for numeric features
    and specific values for categorical features.
    """
    def __init__(self, continuous_features: List[str], categorical_features: List[str]):
        """
        Initialize hyperrectangle manager.

        Args:
            continuous_features: List of continuous feature names
            categorical_features: List of categorical feature names
        """
        self.continuous_features = continuous_features
        self.categorical_features = categorical_features
        self.bounds: Dict[str, Union[Tuple[float, float], str]] = {}

    def create_from_points(self,
                          point1: pd.Series,
                          point2: pd.Series,
                          margin: float = 0.1) -> Dict[str, Union[Tuple[float, float], str]]:
        """
        Create hyperrectangle from two points.

        Args:
            point1: First data point
            point2: Second data point
            margin: Margin to add around numeric intervals (as fraction of range)

        Returns:
            Dictionary representing the hyperrectangle
        """
        self.bounds = {}

        # Handle continuous features
        for feature in self.continuous_features:
            if pd.isna(point1[feature]) or pd.isna(point2[feature]):
                continue

            min_val = min(point1[feature], point2[feature])
            max_val = max(point1[feature], point2[feature])

            # Add margin
            range_size = max_val - min_val
            if range_size == 0:  # If points have same value
                range_size = abs(min_val) * 0.1 if min_val != 0 else 0.1

            margin_size = range_size * margin
            self.bounds[feature] = (
                min_val - margin_size,
                max_val + margin_size
            )

        # Handle categorical features
        for feature in self.categorical_features:
            if pd.isna(point1[feature]) or pd.isna(point2[feature]):
                continue

            if point1[feature] == point2[feature]:
                self.bounds[feature] = point1[feature]

        return self.bounds

    def contains_point(self, point: pd.Series) -> bool:
        """
        Check if a point falls within the hyperrectangle.

        Args:
            point: Data point to check

        Returns:
            True if point is contained in hyperrectangle
        """
        for feature, bound in self.bounds.items():
            if pd.isna(point[feature]):
                return False

            if isinstance(bound, tuple):
                if not (bound[0] <= point[feature] <= bound[1]):
                    return False
            else:  # Categorical feature
                if point[feature] != bound:
                    return False
        return True

    def get_coverage(self, df: pd.DataFrame) -> pd.Series:
        """
        Get boolean mask of points covered by hyperrectangle.

        Args:
            df: DataFrame to check coverage against

        Returns:
            Boolean series indicating which points are covered
        """
        mask = pd.Series(True, index=df.index)

        for feature, bound in self.bounds.items():
            if isinstance(bound, tuple):
                mask &= (df[feature] >= bound[0]) & (df[feature] <= bound[1])
            else:
                mask &= (df[feature] == bound)

        return mask

    def merge_with(self, other: 'HyperRectangle') -> Optional['HyperRectangle']:
        """
        Attempt to merge with another hyperrectangle.
        Only merges if categorical features match exactly.

        Args:
            other: Another HyperRectangle instance

        Returns:
            New merged HyperRectangle or None if merge not possible
        """
        # Check categorical features match
        for feature in self.categorical_features:
            if (feature in self.bounds and feature in other.bounds and
                self.bounds[feature] != other.bounds[feature]):
                return None

        merged = HyperRectangle(self.continuous_features, self.categorical_features)
        merged.bounds = {}

        # Merge categorical features (take any that exist in either)
        for feature in self.categorical_features:
            if feature in self.bounds:
                merged.bounds[feature] = self.bounds[feature]
            elif feature in other.bounds:
                merged.bounds[feature] = other.bounds[feature]

        # Merge continuous features by taking union of intervals
        for feature in self.continuous_features:
            if feature in self.bounds and feature in other.bounds:
                min_val = min(self.bounds[feature][0], other.bounds[feature][0])
                max_val = max(self.bounds[feature][1], other.bounds[feature][1])
                merged.bounds[feature] = (min_val, max_val)
            elif feature in self.bounds:
                merged.bounds[feature] = self.bounds[feature]
            elif feature in other.bounds:
                merged.bounds[feature] = other.bounds[feature]

        return merged

    def to_dict(self) -> Dict[str, Union[Tuple[float, float], str]]:
        """Convert hyperrectangle to dictionary representation."""
        return self.bounds.copy()

    @staticmethod
    def from_dict(bounds: Dict[str, Union[Tuple[float, float], str]],
                 continuous_features: List[str],
                 categorical_features: List[str]) -> 'HyperRectangle':
        """
        Create HyperRectangle from dictionary representation.

        Args:
            bounds: Dictionary of feature bounds
            continuous_features: List of continuous feature names
            categorical_features: List of categorical feature names

        Returns:
            New HyperRectangle instance
        """
        rect = HyperRectangle(continuous_features, categorical_features)
        rect.bounds = bounds.copy()
        return rect
