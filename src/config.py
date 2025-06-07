from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from src.logger import logger
from sqlalchemy.exc import SQLAlchemyError
import re

class MySQLConnection:
    def __init__(self, user=None, password=None, host=None, port=None, db_name=None):
        """
        Initializes a MySQLConnection instance with provided credentials or environment variables.

        :param user: MySQL username. If None, loads from environment variable DB_USER.
        :param password: MySQL password. If None, loads from environment variable DB_PASSWORD.
        :param host: Hostname or IP address of the MySQL server. If None, loads from DB_HOST.
        :param port: Port number of the MySQL server. Defaults to 3306 if not provided.
        :param db_name: Name of the target database. If None, loads from DB_NAME.
        :raises ValueError: If any input field contains unsafe characters.
        """
        load_dotenv()

        self.USER = user or os.getenv("DB_USER")
        self.PASSWORD = password or os.getenv("DB_PASSWORD")
        self.HOST = host or os.getenv("DB_HOST")
        self.PORT = port or os.getenv("DB_PORT")
        self.NAME = db_name or os.getenv("DB_NAME")

        for field in [self.USER, self.PASSWORD, self.HOST, self.NAME]:
            if not self._is_safe(field):
                raise ValueError(f"Invalid or suspicious value: {field}")

    def get_engine(self):
        """
        Creates and returns a SQLAlchemy engine for connecting to the MySQL database.

        :returns: SQLAlchemy Engine instance.
        :raises SQLAlchemyError: If connection to the database fails.
        """
        try:
            connection_string = f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"
            engine = create_engine(connection_string)

            with engine.connect():
                logger.info(f"Connection to the database established successfully.")
            return engine
        except SQLAlchemyError as e:
            logger.error("Error connecting to database: %s", e)
            raise

    @staticmethod
    def _is_safe(value: str) -> bool:
        """
        Checks whether the provided string contains only safe characters.

        :param value: Input string to validate.
        :return: True if the value contains only allowed characters, False otherwise.
        """
        pattern = re.compile(r"^[a-zA-Z0-9_\-@.]+$")
        return bool(pattern.match(value))
