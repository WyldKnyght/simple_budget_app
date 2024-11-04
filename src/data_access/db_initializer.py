# src\data_access\db_initializer.py
import os
import sqlite3
from configs.path_config import DB_PATH, SCHEMA_PATH
from configs.error_config import DB_INITIALIZATION_ERROR, DB_RESET_ERROR, SCHEMA_FILE_READ_ERROR
from .db_custom_exceptions import InitializationError
from utils.custom_logging import logger, error_handler

class DatabaseInitializer:
    def __init__(self, connections, schema_validator):
        self.db_path = DB_PATH
        self.schema_path = SCHEMA_PATH
        self.connections = connections
        self.schema_validator = schema_validator

    @error_handler
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
            raise InitializationError(DB_INITIALIZATION_ERROR.format(str(e))) from e
        except IOError as e:
            logger.error(f"Error reading schema file: {e}")
            raise InitializationError(SCHEMA_FILE_READ_ERROR.format(str(e))) from e
        finally:
            if conn:
                conn.close()

    @error_handler
    def reset_database(self):
        try:
            self.connections.close_all_connections()
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
                logger.info("Existing database removed")
            self.initialize_database()
            logger.info("Database reset successfully")
            self.schema_validator.refresh()  # Refresh the schema validator
            return True, "Database reset successfully"
        except Exception as e:
            logger.error(f"Error resetting database: {e}")
            return False, DB_RESET_ERROR.format(str(e))


    @error_handler
    def new_database(self):
        if self.schema_validator.database_exists():
            return False, "Database already exists"
        self.initialize_database()
        return True, "New database created successfully"
        