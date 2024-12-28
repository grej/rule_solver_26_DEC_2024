# feature_utils.py

import pandas as pd
import numpy as np
from typing import List, Tuple, Dict, Set
from dataclasses import dataclass

@dataclass
class FeatureInfo:
    """Container for feature information"""
    name: str
    dtype: str
    is_numeric: bool
    unique_values: int
    missing_values: int
    range: Tuple[float, float] = None  # For numeric features
    categories: Set[str] = None        # For categorical features

class FeatureAnalyzer:
    """
    Analyzes and manages feature types and properties.
    """
    def __init__(self, df: pd.DataFrame):
        """
        Initialize feature analyzer.

        Args:
            df: Input DataFrame
        """
        self.df = df
        self.feature_info = self._analyze_features()

    def _analyze_features(self) -> Dict[str, FeatureInfo]:
        """Analyze all features in DataFrame."""
        feature_info = {}

        for column in self.df.columns:
            is_numeric = np.issubdtype(self.df[column].dtype, np.number)

            info = FeatureInfo(
                name=column,
                dtype=str(self.df[column].dtype),
                is_numeric=is_numeric,
                unique_values=self.df[column].nunique(),
                missing_values=self.df[column].isnull().sum()
            )

            if is_numeric:
                info.range = (
                    float(self.df[column].min()),
                    float(self.df[column].max())
                )
            else:
                info.categories = set(self.df[column].unique())

            feature_info[column] = info

        return feature_info

    def get_continuous_features(self) -> List[str]:
        """Get list of continuous feature names."""
        return [name for name, info in self.feature_info.items()
                if info.is_numeric]

    def get_categorical_features(self) -> List[str]:
        """Get list of categorical feature names."""
        return [name for name, info in self.feature_info.items()
                if not info.is_numeric]

    def get_feature_range(self, feature: str) -> Tuple[float, float]:
        """Get range of values for a numeric feature."""
        info = self.feature_info.get(feature)
        if not info or not info.is_numeric:
            raise ValueError(f"Feature '{feature}' is not numeric")
        return info.range

    def get_feature_categories(self, feature: str) -> Set[str]:
        """Get set of categories for a categorical feature."""
        info = self.feature_info.get(feature)
        if not info or info.is_numeric:
            raise ValueError(f"Feature '{feature}' is not categorical")
        return info.categories

    def is_numeric(self, feature: str) -> bool:
        """Check if feature is numeric."""
        return self.feature_info[feature].is_numeric

    def suggest_categorical_threshold(self, max_categories: int = 10) -> List[str]:
        """
        Suggest numeric features that might be better treated as categorical.

        Args:
            max_categories: Maximum number of unique values to consider categorical

        Returns:
            List of numeric feature names that might be categorical
        """
        return [name for name, info in self.feature_info.items()
                if info.is_numeric and info.unique_values <= max_categories]

    def calculate_feature_importance(self, target: str, features: List[str]) -> Dict[str, float]:
        """
        Calculate simple feature importance scores based on correlation or chi-square.
        Args:
            target: Target variable name
            features: List of feature names
        Returns:
            Dictionary mapping features to importance scores
        """
        importance = {}
        target_is_numeric = np.issubdtype(self.df[target].dtype, np.number)

        for feature in features:
            feature_is_numeric = np.issubdtype(self.df[feature].dtype, np.number)

            if feature_is_numeric and target_is_numeric:
                # Both numeric: use correlation
                corr = abs(self.df[feature].corr(self.df[target]))
                importance[feature] = corr
            else:
                # At least one is categorical: use chi-square
                try:
                    contingency = pd.crosstab(self.df[feature], self.df[target])
                    from scipy.stats import chi2_contingency
                    chi2, p, dof, expected = chi2_contingency(contingency)
                    n = len(self.df)
                    max_classes = min(len(self.df[feature].unique()),
                                    len(self.df[target].unique()))
                    if max_classes > 1:
                        importance[feature] = np.sqrt(chi2 / (n * (max_classes - 1)))
                    else:
                        importance[feature] = 0
                except Exception as e:
                    # If chi-square fails, use normalized category count
                    importance[feature] = len(self.df[feature].unique()) / len(self.df)
        return importance

    def detect_redundant_features(df: pd.DataFrame,
                                features: List[str],
                                correlation_threshold: float = 0.95) -> List[Tuple[str, str, float]]:
        """
        Detect highly correlated feature pairs.

        Args:
            df: Input DataFrame
            features: List of feature names to check
            correlation_threshold: Correlation threshold for considering features redundant

        Returns:
            List of tuples (feature1, feature2, correlation)
        """
        numeric_features = [f for f in features
                        if np.issubdtype(df[f].dtype, np.number)]

        if len(numeric_features) < 2:
            return []

        corr_matrix = df[numeric_features].corr().abs()
        redundant = []

        for i in range(len(numeric_features)):
            for j in range(i + 1, len(numeric_features)):
                correlation = corr_matrix.iloc[i, j]
                if correlation > correlation_threshold:
                    redundant.append((
                        numeric_features[i],
                        numeric_features[j],
                        correlation
                    ))

        return redundant
