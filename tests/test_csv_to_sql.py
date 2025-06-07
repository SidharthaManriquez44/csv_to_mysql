import os
import pytest
import pandas as pd
from src.converter.csv_to_sql import convert_csv_to_sql

@pytest.fixture
def test_db_config():
    return {
        "user": "test_user",
        "password": "test_password",
        "host": "localhost",
        "port": 3306,
        "db_name": "test_db"
    }

@pytest.fixture
def sample_csv(tmp_path):
    file = tmp_path / "sample.csv"
    df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    df.to_csv(file, index=False)
    return str(file)

def test_convert_csv_to_sql_creates_table(sample_csv, test_db_config):
    # Skip test if test_db not configured
    if not os.getenv("RUN_DB_TESTS"):
        pytest.skip("Skipping DB test. Set RUN_DB_TESTS=1 to enable.")

    table_name = convert_csv_to_sql(sample_csv, test_db_config)
    assert table_name == "sample"
