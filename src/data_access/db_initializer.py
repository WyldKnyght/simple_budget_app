# src\data_access\db_initializer.py
import sqlite3
from utils.custom_logging import logger
from configs.path_config import DB_PATH, SCHEMA_PATH
from .db_custom_exceptions import InitializationError

class DatabaseInitializer:
    def __init__(self):
        self.db_path = DB_PATH
        self.schema_path = SCHEMA_PATH

    def initialize_database(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            with open(self.schema_path, 'r') as schema_file:
                schema_script = schema_file.read()
            conn.executescript(schema_script)
            logger.info("Database initialized successfully")
        except sqlite3.Error as e:
            logger.error(f"Error initializing database: {e}")
            raise InitializationError(f"Failed to initialize database: {e}") from e
        except IOError as e:
            logger.error(f"Error reading schema file: {e}")
            raise InitializationError(f"Failed to read schema file: {e}") from e
        finally:
            if conn:
                conn.close()