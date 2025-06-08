import pytest
import pandas as pd
from src.converter.csv_to_sql import convert_csv_to_sql
from sqlalchemy import create_engine

@pytest.fixture
def sample_csv(tmp_path):
    file = tmp_path / "sample.csv"
    df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    df.to_csv(file, index=False)
    return str(file)

@pytest.fixture
def sqlite_engine():
    return create_engine("sqlite:///:memory:")

@pytest.mark.integration
def test_convert_csv_to_sql_creates_table(sample_csv, test_db_config, clean_sample_table):
    table_name = convert_csv_to_sql(sample_csv, test_db_config)
    assert table_name == "sample"

def test_convert_csv_to_sql_sqlite(sample_csv, sqlite_engine):
    table_name = convert_csv_to_sql(sample_csv, sqlite_engine)
    assert table_name == "sample"

def test_convert_csv_to_sql_only_logic(mocker, sample_csv, sqlite_engine):
    mock_to_sql = mocker.patch("pandas.DataFrame.to_sql", return_value=None)

    table_name = convert_csv_to_sql(sample_csv, sqlite_engine)
    assert table_name == "sample"

    mock_to_sql.assert_called_once()
