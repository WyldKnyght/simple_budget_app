# src/data_access/db_modules/db_initializer.py

from configs.path_config import DB_PATH, SCHEMA_PATH
from configs.messages_config import (
    DB_ALREADY_EXISTS_ERROR,
    DB_INIT_SUCCESS, DB_INIT_ERROR
)
from utils.custom_logging import logger, error_handler
from .db_custom_exceptions import InitializationError
from ..schema_manager import SchemaManager

class DatabaseInitializer:
    def __init__(self, connections, validation_operations):
        self.db_path = DB_PATH
        self.schema_path = SCHEMA_PATH
        self.connections = connections
        self.validation_operations = validation_operations
        self.schema_manager = SchemaManager()

    @error_handler
    def initialize_database(self): 
        logger.info("Initializing database...")
        conn = None
        try:
            conn = self.connections.get_connection()
            
            # Load and execute the schema script only if it does not exist
            schema_script = self.schema_manager.load_schema()
            if not schema_script:
                raise InitializationError("Failed to load schema script")
            
            # Execute schema script only if tables do not exist
            if not self.validation_operations.database_exists() or not self.validation_operations.validate_schema():
                conn.executescript(schema_script)
                conn.commit()
                logger.info(DB_INIT_SUCCESS)
                return True, DB_INIT_SUCCESS
            else:
                logger.info("Database already initialized and valid. No changes made.")
                return False, "Database already initialized and valid."
        except Exception as e:
            error_message = DB_INIT_ERROR.format(str(e))
            logger.error(error_message)
            if conn:
                conn.rollback()
            raise InitializationError(error_message) from e
        finally:
            if conn:
                self.connections.close_connection()

    @error_handler
    def new_database(self):
        logger.info("Creating new database...")
        if self.validation_operations.database_exists():
            logger.warning(DB_ALREADY_EXISTS_ERROR)
            return False, DB_ALREADY_EXISTS_ERROR
        
        # Call initialize_database directly since it's a new database creation.
        return self.initialize_database()