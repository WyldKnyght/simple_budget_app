# src/controllers/validation_manager.py
from data_access.db_modules.db_validation_operations import ValidationOperations
from .services.validation_service import ValidationService

class ValidationManager:
    def __init__(self, db_manager, message_manager):
        self.validation_operations = ValidationOperations(db_manager)
        self.validation_service = ValidationService(message_manager)

    def check_and_validate_database(self, parent):
        return self.validation_service.check_and_validate_database(
            self.validation_operations, parent)