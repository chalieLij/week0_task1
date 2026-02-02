import numpy as np
import pandas as pd

from src.preprocessing import preprocess_csv


def test_preprocess_csv_handles_missing_and_scaling(tmp_path):
    data = pd.DataFrame(
        {
            "age": [10, 20, None, 40],
            "city": ["a", "b", "a", None],
            "target": [0, 1, 0, 1],
        }
    )
    csv_path = tmp_path / "sample.csv"
    data.to_csv(csv_path, index=False)

    result = preprocess_csv(
        str(csv_path),
        target_column="target",
        numeric_strategy="median",
        categorical_strategy="most_frequent",
        scaler="standard",
    )

    assert result.y is not None
    assert result.X.shape[0] == 4
    assert np.isfinite(result.X).all()
