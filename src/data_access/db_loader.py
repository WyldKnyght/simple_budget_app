# src/data_access/db_loader.py
from utils.custom_logging import error_handler
from configs.error_config import DB_LOAD_ERROR

class DatabaseLoader:
    def __init__(self, database_manager):
        self.database_manager = database_manager
    
    @error_handler
    def load_database(self):
        connections = self.database_manager.connections
        schema_validator = self.database_manager.schema_validator

        if not schema_validator.database_exists():
            return False, "Database does not exist"

        try:
            connection = connections.get_connection()
            if connection is None:
                return False, "Failed to connect to the database"

            if not schema_validator.validate_schema():
                connections.close_connection()
                return False, "Database schema is invalid"

            return True, "Database loaded successfully"
        except Exception as e:
            connections.close_connection()
            return False, DB_LOAD_ERROR.format(str(e))