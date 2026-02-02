from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, RobustScaler, StandardScaler


@dataclass(frozen=True)
class PreprocessResult:
    X: np.ndarray
    y: Optional[np.ndarray]
    pipeline: ColumnTransformer
    feature_names: Tuple[str, ...]


def _build_scaler(name: str):
    name_lower = name.lower()
    if name_lower == "standard":
        return StandardScaler()
    if name_lower == "minmax":
        return MinMaxScaler()
    if name_lower == "robust":
        return RobustScaler()
    raise ValueError("scaler must be one of: standard, minmax, robust")


def preprocess_csv(
    csv_path: str,
    *,
    target_column: Optional[str] = None,
    numeric_strategy: str = "median",
    categorical_strategy: str = "most_frequent",
    scaler: str = "standard",
    drop_columns: Optional[Iterable[str]] = None,
) -> PreprocessResult:
    """
    Load a CSV, handle missing values, and scale numeric features.

    Args:
        csv_path: Path to the CSV file.
        target_column: Optional target column to separate from features.
        numeric_strategy: Imputation strategy for numeric columns.
        categorical_strategy: Imputation strategy for categorical columns.
        scaler: Scaling method: standard, minmax, or robust.
        drop_columns: Optional list of columns to drop before processing.

    Returns:
        PreprocessResult containing the transformed features, target, pipeline,
        and feature names.
    """
    df = pd.read_csv(csv_path)

    if drop_columns:
        df = df.drop(columns=list(drop_columns), errors="ignore")

    y: Optional[np.ndarray] = None
    if target_column:
        if target_column not in df.columns:
            raise ValueError(f"target_column '{target_column}' not found in CSV")
        y = df[target_column].to_numpy()
        df = df.drop(columns=[target_column])

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = [c for c in df.columns if c not in numeric_cols]

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy=numeric_strategy)),
            ("scaler", _build_scaler(scaler)),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy=categorical_strategy)),
            (
                "onehot",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
            ),
        ]
    )

    transformer = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_cols),
            ("cat", categorical_pipeline, categorical_cols),
        ],
        remainder="drop",
    )

    X = transformer.fit_transform(df)

    feature_names: Tuple[str, ...]
    try:
        feature_names = tuple(transformer.get_feature_names_out())
    except AttributeError:
        feature_names = tuple()

    return PreprocessResult(X=X, y=y, pipeline=transformer, feature_names=feature_names)
