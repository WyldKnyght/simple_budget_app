# src/controllers/validation_manager.py
from data_access.db_validation_operations import ValidationOperations

class ValidationManager:
    # No defined functions, only imports and initialization
    def __init__(self, database_manager):
        self.database_manager = database_manager
        self.validation_operations = ValidationOperations()

    def validate_database_schema(self):
        return self.validation_operations.validate_schema()
