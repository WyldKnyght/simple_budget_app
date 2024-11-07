# src/controllers/services/menu_bar_service.py

from configs.messages_config import DB_RESET_SUCCESS, DB_RESET_ERROR, DB_RESET_CONFIRM
from utils.custom_logging import logger
from user_interface.dialogs.show_about_dialog import show_about_dialog
from PyQt6.QtWidgets import QMessageBox

class MenuBarService:
    def __init__(self, db_manager, message_manager):
        self.db_manager = db_manager
        self.message_manager = message_manager

    def reset_database(self):
        logger.info("Attempting to reset database")

        # Ask for confirmation
        confirm = self.message_manager.show_question_message(
            None, 
            "Confirm Database Reset", 
            DB_RESET_CONFIRM
        )

        if confirm == QMessageBox.StandardButton.Yes:
            success, message = self.db_manager.reset_database()
            if success:
                self.message_manager.show_info_message(None, "Database Reset", DB_RESET_SUCCESS)
                logger.info("Database reset successfully")
            else:
                self.message_manager.show_error_message(None, "Database Reset Error", DB_RESET_ERROR)
                logger.error(f"Database reset failed: {message}")
            return success
        else:
            logger.info("Database reset cancelled by user")
            return False

    def show_about(self, parent):
        show_about_dialog(parent)