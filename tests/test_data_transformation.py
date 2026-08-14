from pathlib import Path

import pandas as pd

from src.components.data_transformation import Datatransformation


def test_initiate_data_transformation_creates_arrays(tmp_path):
    train_df = pd.DataFrame(
        {
            "gender": ["female", "male", "female", "male", "female"],
            "race_ethnicity": ["group A", "group B", "group A", "group C", "group B"],
            "parental_level_of_education": ["bachelor's degree", "some college", "master's degree", "associate's degree", "high school"],
            "lunch": ["standard", "free/reduced", "standard", "standard", "free/reduced"],
            "test_prepration_course": ["completed", "none", "completed", "none", "completed"],
            "writing_score": [78, 65, 84, 72, 88],
            "reading_score": [80, 66, 86, 71, 90],
            "math_score": [85, 63, 89, 70, 92],
        }
    )
    test_df = pd.DataFrame(
        {
            "gender": ["male", "female"],
            "race_ethnicity": ["group C", "group A"],
            "parental_level_of_education": ["high school", "bachelor's degree"],
            "lunch": ["standard", "free/reduced"],
            "test_prepration_course": ["none", "completed"],
            "writing_score": [75, 82],
            "reading_score": [73, 85],
            "math_score": [76, 88],
        }
    )

    train_path = tmp_path / "train.csv"
    test_path = tmp_path / "test.csv"
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    train_arr, test_arr, preprocessor_path = Datatransformation().initiate_data_transformation(
        str(train_path), str(test_path)
    )

    assert train_arr.shape[0] == len(train_df)
    assert test_arr.shape[0] == len(test_df)
    assert train_arr.shape[1] == test_arr.shape[1]
    assert Path(preprocessor_path).exists()
