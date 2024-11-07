# src/data_access/db_modules/reset_database.py
import os
from configs.path_config import DB_PATH
from configs.messages_config import DB_RESET_SUCCESS, DB_REMOVED_SUCCESS, DB_RESET_ERROR
from utils.custom_logging import logger, error_handler
from ..schema_manager import SchemaManager
from .db_custom_exceptions import InitializationError, QueryExecutionError

class ResetDatabase:
    def __init__(self, connections):
        self.db_path = DB_PATH
        self.connections = connections
        self.schema_manager = SchemaManager()

    @error_handler
    def reset_database(self):
        logger.info("Resetting database...")
        conn = None
        try:
            # Close all connections before removing the database file
            self.connections.close_all_connections()
            if os.path.exists(self.db_path):
                logger.info(f"Removing existing database file: {self.db_path}")
                os.remove(self.db_path)
                logger.info(DB_REMOVED_SUCCESS)
            else:
                logger.warning(f"Database file not found at {self.db_path}")

            # Load schema and create new database
            logger.info("Creating new database with schema.")
            conn = self.connections.get_connection()
            schema_script = self.schema_manager.load_schema()
            if not schema_script:
                raise InitializationError("Failed to load schema script.")

            # Execute the schema script to create tables
            conn.executescript(schema_script)
            conn.commit()
            logger.info(DB_RESET_SUCCESS)
            return True, DB_RESET_SUCCESS
            
        except InitializationError as ie:
            error_msg = f"Initialization error: {str(ie)}"
            logger.error(error_msg)
            return False, error_msg
        except QueryExecutionError as qee:
            error_msg = f"Query execution error: {str(qee)}"
            logger.error(error_msg)
            return False, error_msg
        except Exception as e:
            error_msg = f"Unexpected error during database reset: {str(e)}"
            logger.error(error_msg)
            return False, DB_RESET_ERROR.format(error_msg)
        finally:
            if conn:
                conn.close()  # Ensure connection is closed after operation