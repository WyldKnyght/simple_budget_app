# src\data_access\db_connections.py
import sqlite3
from utils.custom_logging import logger
from configs.path_config import DB_PATH
from .db_custom_exceptions import ConnectionError

class DatabaseConnections:
    @staticmethod
    def get_connection():
        try:
            return sqlite3.connect(DB_PATH)
        except sqlite3.Error as e:
            logger.error(f"Error connecting to database: {e}")
            raise ConnectionError(f"Failed to connect to database: {e}") from e
