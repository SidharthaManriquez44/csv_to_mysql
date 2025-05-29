from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

class MySQLConnection:
    def __init__(self, user=None, password=None, host=None, port=None, db_name=None):
        load_dotenv()

        self.USER = user or os.getenv("DB_USER")
        self.PASSWORD = password or os.getenv("DB_PASSWORD")
        self.HOST = host or os.getenv("DB_HOST")
        self.PORT = port or os.getenv("DB_PORT")
        self.NAME = db_name or os.getenv("DB_NAME")

    def get_engine(self):
        connection_string = f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"
        return create_engine(connection_string)
