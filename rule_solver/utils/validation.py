# validation.py

import pandas as pd
import numpy as np
from typing import Dict, List, Union, Optional, Tuple

def validate_dataframe(df: pd.DataFrame) -> bool:
    """
    Validate input DataFrame requirements.

    Args:
        df: Input DataFrame

    Returns:
        True if valid, raises ValueError otherwise
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    if len(df) == 0:
        raise ValueError("DataFrame is empty")

    if df.isnull().values.any():
        raise ValueError("DataFrame contains null values")

    return True

def validate_target(df: pd.DataFrame,
                   target_var: str,
                   direction: str) -> bool:
    """
    Validate target variable and direction specifications.

    Args:
        df: Input DataFrame
        target_var: Target variable name
        direction: 'maximize'/'minimize' for continuous, category for categorical

    Returns:
        True if valid, raises ValueError otherwise
    """
    if target_var not in df.columns:
        raise ValueError(f"Target variable '{target_var}' not found in DataFrame")

    is_numeric = np.issubdtype(df[target_var].dtype, np.number)

    if is_numeric and direction not in ['maximize', 'minimize']:
        raise ValueError(
            f"Direction must be 'maximize' or 'minimize' for numeric target, got '{direction}'"
        )

    if not is_numeric and direction not in df[target_var].unique():
        raise ValueError(
            f"Direction must be a valid category for categorical target, got '{direction}'"
        )

    return True

def validate_rule(rule: Dict,
                 df: pd.DataFrame,
                 min_samples: int = 3) -> Tuple[bool, str]:
    """
    Validate a rule's structure and coverage.

    Args:
        rule: Rule dictionary to validate
        df: Input DataFrame
        min_samples: Minimum samples required to match rule

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not rule:
        return False, "Rule is empty"

    # Check features exist
    for feature in rule.keys():
        if feature not in df.columns:
            return False, f"Feature '{feature}' not found in DataFrame"

    # Validate conditions
    for feature, condition in rule.items():
        if isinstance(condition, tuple):
            if len(condition) != 2:
                return False, f"Invalid interval for feature '{feature}'"
            if not isinstance(condition[0], (int, float)) or not isinstance(condition[1], (int, float)):
                return False, f"Non-numeric interval bounds for feature '{feature}'"
            if condition[0] > condition[1]:
                return False, f"Invalid interval bounds for feature '{feature}': min > max"
        elif isinstance(condition, list):
            if not condition:
                return False, f"Empty category list for feature '{feature}'"
            if not all(cat in df[feature].unique() for cat in condition):
                return False, f"Invalid categories for feature '{feature}'"
        else:
            if condition not in df[feature].unique():
                return False, f"Invalid value for feature '{feature}'"

    # Check coverage
    mask = pd.Series(True, index=df.index)
    for feature, condition in rule.items():
        if isinstance(condition, tuple):
            mask &= (df[feature] >= condition[0]) & (df[feature] <= condition[1])
        elif isinstance(condition, list):
            mask &= df[feature].isin(condition)
        else:
            mask &= (df[feature] == condition)

    matching_samples = mask.sum()
    if matching_samples < min_samples:
        return False, f"Rule matches only {matching_samples} samples (minimum {min_samples})"

    return True, ""

def validate_hyperrect_bounds(bounds: Dict[str, Union[Tuple[float, float], str]],
                            df: pd.DataFrame) -> bool:
    """
    Validate hyperrectangle bounds against DataFrame.

    Args:
        bounds: Dictionary of feature bounds
        df: Input DataFrame

    Returns:
        True if valid, raises ValueError otherwise
    """
    for feature, bound in bounds.items():
        if feature not in df.columns:
            raise ValueError(f"Feature '{feature}' not found in DataFrame")

        if isinstance(bound, tuple):
            if not np.issubdtype(df[feature].dtype, np.number):
                raise ValueError(f"Feature '{feature}' is not numeric but has interval bounds")
            if len(bound) != 2:
                raise ValueError(f"Invalid interval for feature '{feature}'")
            if not isinstance(bound[0], (int, float)) or not isinstance(bound[1], (int, float)):
                raise ValueError(f"Non-numeric interval bounds for feature '{feature}'")
            if bound[0] > bound[1]:
                raise ValueError(f"Invalid interval bounds for feature '{feature}': min > max")
        else:
            if bound not in df[feature].unique():
                raise ValueError(f"Invalid value '{bound}' for feature '{feature}'")

    return True

def validate_reduction_params(min_features: int,
                            num_features: int,
                            min_improvement: float) -> bool:
    """
    Validate dimensionality reduction parameters.

    Args:
        min_features: Minimum features to keep
        num_features: Current number of features
        min_improvement: Minimum improvement threshold

    Returns:
        True if valid, raises ValueError otherwise
    """
    if min_features < 1:
        raise ValueError("min_features must be at least 1")

    if min_features >= num_features:
        raise ValueError("min_features must be less than number of features")

    if min_improvement < 0:
        raise ValueError("min_improvement must be non-negative")

    return True
