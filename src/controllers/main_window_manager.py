# src/controllers/main_window_manager.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from configs.ui_constants import TAB_STRUCTURE, WARNING_LABEL_STYLE
from data_access.database_manager import DatabaseManager
from controllers.validation_manager import ValidationManager
from controllers.message_manager import MessageManager
from controllers.menu_bar_manager import MenuBarManager
from utils.custom_logging import logger

class MainWindowManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.message_manager = MessageManager()
        self.validation_manager = ValidationManager(self.db_manager, self.message_manager)
        self.menu_bar_manager = MenuBarManager(self.db_manager, self.message_manager)

    def initialize_database(self, parent):
        logger.info("Starting database initialization process")
        if not self.db_manager.database_exists():
            logger.info("Database does not exist, creating new database")
            success, message = self.db_manager.new_database()
        elif not self.db_manager.validate_schema():
            logger.info("Schema validation failed, attempting to reset database")
            self.message_manager.show_warning_message(parent, "Schema Mismatch", "Database schema does not match. Recreating database.")
            success, message = self.db_manager.reset_database()
            logger.info(f"Database reset result: success={success}, message={message}")
        else:
            logger.info("Database exists and schema is valid")
            success, message = True, "Database is valid and up to date."
        
        if success:
            self.message_manager.show_info_message(parent, "Database Initialization", message)
        else:
            self.message_manager.show_error_message(parent, "Database Initialization Error", message)
        
        logger.info(f"Database initialization process completed: success={success}, message={message}")
        return success

    def validate_database(self):
        return self.db_manager.validate_schema()

    def get_tab_structure(self):
        logger.info("Getting tab structure...")
        return TAB_STRUCTURE

    def get_warning_label_style(self):
        logger.info("Getting warning label style...")
        return WARNING_LABEL_STYLE

    def reset_database(self):
        logger.info("MainWindowManager: Initiating database reset")
        success = self.menu_bar_manager.reset_database()
        if success:
            logger.info("Database reset successful. Updating UI...")
            # Add any UI update logic here if needed
        else:
            logger.info("Database reset was cancelled or failed")
        return success

    def show_about(self, parent):
        self.menu_bar_manager.show_about(parent)

    def create_placeholder_tab(self, tab_name):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        label = QLabel(f"Placeholder for {tab_name}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        return tab