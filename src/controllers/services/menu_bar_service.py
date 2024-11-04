# src/controllers/services/menu_bar_service.py

from configs.error_config import (
    DB_LOAD_SUCCESS, DB_LOAD_FAILURE, 
    NEW_DB_CREATED_SUCCESS, NEW_DB_CREATION_FAILURE, DB_ALREADY_EXISTS_ERROR,
    DB_RESET_SUCCESS, DB_RESET_FAILURE
)

class MenuBarService:
    def __init__(self, db_manager, message_manager):
        self.db_manager = db_manager
        self.message_manager = message_manager

    def get_menu_state(self):
        db_exists = self.db_manager.validation_operations.database_exists()
        return {
            'open_db': db_exists,
            'new_db': not db_exists,
            'reset_db': db_exists
        }

    def load_database(self):
        success, message = self.db_manager.load_database()
        if success:
            self.message_manager.show_info_message(None, "Database Loaded", DB_LOAD_SUCCESS)
        else:
            self.message_manager.show_error_message(None, "Database Load Error", DB_LOAD_FAILURE.format(message))
        return success

    def new_database(self):
        if not self.db_manager.validation_operations.database_exists():
            success = self.db_manager.initialize_database()
            if success:
                self.message_manager.show_info_message(None, "Database Created", NEW_DB_CREATED_SUCCESS)
            else:
                self.message_manager.show_error_message(None, "Database Creation Error", NEW_DB_CREATION_FAILURE)
            return success
        else:
            self.message_manager.show_warning_message(None, "Database Exists", DB_ALREADY_EXISTS_ERROR)
            return False

    def reset_database(self):
        success, message = self.db_manager.reset_database()
        if success:
            self.message_manager.show_info_message(None, "Database Reset", DB_RESET_SUCCESS)
        else:
            self.message_manager.show_error_message(None, "Database Reset Error", DB_RESET_FAILURE.format(message))
        return success

    def show_about(self, parent):
        # Implementation for showing about dialog
        pass

    def show_help(self):
        # Implementation for showing help
        pass