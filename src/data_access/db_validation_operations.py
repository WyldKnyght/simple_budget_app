# src/data_access/db_validation_operations.py
import os
from utils.custom_logging import error_handler

class ValidationOperations:
    def __init__(self, database_manager):
        self.database_manager = database_manager

    @error_handler
    def validate_schema(self):
        if not self.database_exists():
            return False
        current_schema = self.get_current_schema()
        expected_schema = self.database_manager.schema_manager.load_schema()
        return current_schema == expected_schema

    @error_handler
    def database_exists(self):
        return os.path.exists(self.database_manager.db_path)

    @error_handler
    def get_current_schema(self):
        query = "SELECT sql FROM sqlite_master WHERE type='table';"
        results = self.database_manager.execute_query(query)
        return '\n'.join(result[0] for result in results if result[0] is not None)

    def initialize_database(self):
        self.database_manager.initialize_database()

    def reset_database(self):
        return self.database_manager.reset_database()

    def refresh(self):
        # Clear any cached schema information
        if hasattr(self, '_current_schema'):
            del self._current_schema
        if hasattr(self, '_expected_schema'):
            del self._expected_schema
            
    def close_all_connections(self):
        self.database_manager.close_all_connections()