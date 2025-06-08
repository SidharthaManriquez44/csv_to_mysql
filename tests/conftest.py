import os
import pytest
from tests.db_utils import wait_for_mysql, drop_table_if_exists
from src.config import MySQLConnection

@pytest.fixture(scope="session")
def test_db_config():
    return {
        "user": "test_user",
        "password": "test_password",
        "host": "localhost",
        "port": 3307,
        "db_name": "test_db"
    }

@pytest.fixture(scope="session", autouse=True)
def wait_for_db_ready(test_db_config):
    """
    Wait for the database to be ready once per test session.
    """
    if not os.getenv("RUN_DB_TESTS"):
        return
    wait_for_mysql(
        host=test_db_config["host"],
        port=test_db_config["port"],
        user=test_db_config["user"],
        password=test_db_config["password"],
        db_name=test_db_config["db_name"],
        timeout=60
    )

@pytest.fixture(scope="function", autouse=True)
def clean_sample_table(test_db_config):
    """
    Automatically clean the 'sample' table before each test.
    """
    if not os.getenv("RUN_DB_TESTS"):
        yield
        return

    connection = MySQLConnection(**test_db_config)
    engine = connection.get_engine()
    drop_table_if_exists(engine, "sample")

    yield
