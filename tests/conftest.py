import pytest
import os
import time
import pymysql
import logging
from sqlalchemy import text
from src.config import MySQLConnection

# Enable logging
logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="session")
def test_db_config():
    """
    Provides the database configuration, adjusting for CI or local.
    """
    is_ci = os.getenv("CI") == "true"

    host = "127.0.0.1"
    port = 3307  # default mapped port in docker-compose

    # If running in GitHub Actions and using service, override
    if is_ci and os.getenv("GITHUB_ACTIONS") == "true":
        # assuming you're using services: mysql-test
        host = "mysql-test"
        port = 3306

    return {
        "user": "test_user",
        "password": "test_password",
        "host": host,
        "port": port,
        "db_name": "test_db"
    }


@pytest.fixture(scope="session", autouse=True)
def wait_for_mysql_ready(test_db_config):
    """
    Wait until MySQL is ready before starting the test session.
    """
    logging.info("🔍 Waiting for MySQL to be ready...")
    timeout = 60
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            conn = pymysql.connect(
                host=test_db_config["host"],
                port=test_db_config["port"],
                user=test_db_config["user"],
                password=test_db_config["password"],
                database=test_db_config["db_name"],
                connect_timeout=60
            )
            conn.close()
            logging.info("✅ MySQL is ready and accepting connections.")
            return
        except pymysql.err.OperationalError as e:
            logging.info(f"⏳ Waiting for MySQL... ({str(e)})")
            time.sleep(2)

    raise RuntimeError("❌ MySQL did not become ready in time.")


@pytest.fixture(scope="function")
def clean_sample_table(test_db_config, wait_for_mysql_ready):
    """
    Clean the sample table before each test that needs it.
    """
    connection = MySQLConnection(**test_db_config)
    engine = connection.get_engine()
    logging.info("⚠️ Dropping table if exists: sample")

    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS `sample`;"))
        conn.commit()

    logging.info("✅ Table 'sample' dropped (if existed).")
    yield
