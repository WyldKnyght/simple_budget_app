# src/controllers/services/validation_service.py
from PyQt6.QtWidgets import QMessageBox

class ValidationService:
    def __init__(self, message_manager):
        self.message_manager = message_manager

    def check_and_validate_database(self, validation_operations, parent):
        try:
            if not validation_operations.database_exists():
                return self._handle_non_existent_database(validation_operations, parent)
            elif not validation_operations.validate_schema():
                return self._handle_invalid_schema(validation_operations, parent)
            return True
        finally:
            validation_operations.close_all_connections()

    def get_warning_message(self):
        return self.message_manager.get_message('DB_VALIDATION_WARNING')

    def _handle_non_existent_database(self, validation_operations, parent):
        if self._prompt_create_database(parent):
            validation_operations.initialize_database()
            self.message_manager.show_info_message(parent, "Database Created", "New database created")
            return True
        self._show_warning_message(parent)
        return False

    def _handle_invalid_schema(self, validation_operations, parent):
        if self._prompt_reset_database(parent):
            success, message = validation_operations.reset_database()
            if success:
                self.message_manager.show_info_message(parent, "Database Reset", "Database reset")
                return True
            else:
                self._show_warning_message(parent)
                return False
        self._show_warning_message(parent)
        return False

    def _show_warning_message(self, parent, custom_message=None):
        message = custom_message or self.get_warning_message()
        self.message_manager.show_warning_message(parent, 'Database Issue', message)

    def _prompt_create_database(self, parent):
        return self.message_manager.show_question_message(
            parent, 
            'Create Database', 
            self.message_manager.get_message('DB_CREATE_PROMPT')
        ) == QMessageBox.StandardButton.Yes

    def _prompt_reset_database(self, parent):
        return self.message_manager.show_question_message(
            parent, 
            'Outdated Database', 
            self.message_manager.get_message('DB_RESET_PROMPT')
        ) == QMessageBox.StandardButton.Yes