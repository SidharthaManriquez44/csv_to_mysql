import time
import pymysql
import logging
from sqlalchemy import text

logging.basicConfig(level=logging.INFO)

def wait_for_mysql(host, port, user, password, db_name, timeout=60):
    """
    Wait until MySQL database is ready and accepting connections.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            conn = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=db_name,
                connect_timeout=5
            )
            conn.close()
            logging.info("✅ MySQL is ready and accepting connections.")
            return
        except pymysql.err.OperationalError as e:
            logging.info(f"⏳ Waiting for MySQL... ({str(e)})")
            time.sleep(2)

    raise RuntimeError("❌ MySQL did not become ready in time.")


def drop_table_if_exists(engine, table_name):
    """
    Drop the table if it exists in the database.
    """
    logging.info(f"⚠️ Dropping table if exists: {table_name}")
    with engine.connect() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS `{table_name}`;"))
        conn.commit()
    logging.info(f"✅ Table '{table_name}' dropped (if existed).")
