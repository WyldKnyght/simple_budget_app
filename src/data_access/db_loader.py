# src/data_access/db_loader.py

from utils.custom_logging import logger, error_handler
from configs.error_config import (
    DB_LOAD_ERROR,
    DB_DOES_NOT_EXIST_ERROR,
    DB_CONNECTION_ERROR,
    SCHEMA_VALIDATION_ERROR,
    DB_INIT_SUCCESS
)

class DatabaseLoader:
    def __init__(self, database_manager):
        self.database_manager = database_manager
    
    @error_handler
    def load_database(self):
        connections = self.database_manager.connections
        validation_operations = self.database_manager.validation_operations

        if not validation_operations.database_exists():
            logger.error(DB_DOES_NOT_EXIST_ERROR)
            return False, DB_DOES_NOT_EXIST_ERROR

        try:
            connection = connections.get_connection()
            if connection is None:
                logger.error(DB_CONNECTION_ERROR.format("Unknown reason"))
                return False, DB_CONNECTION_ERROR.format("Unknown reason")

            if not validation_operations.validate_schema():
                connections.close_connection()
                logger.error(SCHEMA_VALIDATION_ERROR)
                return False, SCHEMA_VALIDATION_ERROR

            logger.info(DB_INIT_SUCCESS)
            return True, DB_INIT_SUCCESS
        except Exception as e:
            connections.close_connection()
            logger.error(DB_LOAD_ERROR.format(str(e)))
            return False, DB_LOAD_ERROR.format(str(e))