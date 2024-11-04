# src\data_access\db_connections.py
import sqlite3
from utils.custom_logging import logger, error_handler
from configs.path_config import DB_PATH
from configs.error_config import DB_CONNECTION_ERROR, DB_CLOSE_ERROR
from .db_custom_exceptions import ConnectionError

class DatabaseConnections:
    def __init__(self):
        self.connection = None

    @error_handler
    def get_connection(self):
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(DB_PATH)
                return self.connection
            except sqlite3.Error as e:
                logger.error(f"Error connecting to database: {e}")
                raise ConnectionError(DB_CONNECTION_ERROR.format(str(e))) from e
        return self.connection
       

    @error_handler
    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
                self.connection = None
            except sqlite3.Error as e:
                logger.error(f"Error closing database connection: {e}")
                raise ConnectionError(DB_CLOSE_ERROR.format(str(e))) from e

    @error_handler
    def close_all_connections(self):
        self.close_connection()