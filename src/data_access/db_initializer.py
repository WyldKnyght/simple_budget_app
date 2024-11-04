# src/data_access/db_initializer.py
import os
from configs.path_config import DB_PATH, SCHEMA_PATH
from configs.error_config import (
    DB_INITIALIZATION_ERROR, DB_RESET_ERROR, DB_INIT_SUCCESS,
    DB_RESET_SUCCESS, DB_REMOVED_SUCCESS, DB_ALREADY_EXISTS_ERROR,
    NEW_DB_CREATED_SUCCESS
)
from .db_custom_exceptions import InitializationError
from utils.custom_logging import logger, error_handler
from utils.file_operations import read_schema_file

class DatabaseInitializer:
    def __init__(self, connections, validation_operations):
        self.db_path = DB_PATH
        self.schema_path = SCHEMA_PATH
        self.connections = connections
        self.validation_operations = validation_operations

    @error_handler
    def initialize_database(self):
        conn = None
        try:
            conn = self.connections.get_connection()
            schema_script = read_schema_file(self.schema_path)
            conn.executescript(schema_script)
            conn.commit()
            logger.info(DB_INIT_SUCCESS)
        except Exception as e:
            logger.error(DB_INITIALIZATION_ERROR.format(str(e)))
            if conn:
                conn.rollback()
            raise InitializationError(DB_INITIALIZATION_ERROR.format(str(e))) from e
        finally:
            if conn:
                self.connections.close_connection()

    @error_handler
    def reset_database(self):
        try:
            self.connections.close_all_connections()
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
                logger.info(DB_REMOVED_SUCCESS)
            self.initialize_database()
            logger.info(DB_RESET_SUCCESS)
            self.validation_operations.refresh()
            return True, DB_RESET_SUCCESS
        except Exception as e:
            logger.error(DB_RESET_ERROR.format(str(e)))
            return False, DB_RESET_ERROR.format(str(e))

    @error_handler
    def new_database(self):
        if self.validation_operations.database_exists():
            return False, DB_ALREADY_EXISTS_ERROR
        self.initialize_database()
        return True, NEW_DB_CREATED_SUCCESS