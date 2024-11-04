# src/controllers/ui_main_window_manager.py
from data_access.database_manager import DatabaseManager
from controllers.validation_manager import ValidationManager
from controllers.message_manager import MessageManager
from .services.menu_bar_service import MenuBarService
from .services.ui_initializer_service import UIInitializerService
from .services.ui_validator_service import UIValidatorService
from user_interface.dialogs.show_about_dialog import show_about_dialog

class MainWindowManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.message_manager = MessageManager()
        self.menu_bar_service = MenuBarService(self.db_manager, self.message_manager)
        self.validation_manager = ValidationManager(self.db_manager, self.message_manager)
        self.ui_initializer_service = UIInitializerService()
        self.ui_validator_service = UIValidatorService(self.validation_manager, self.message_manager)

    def check_and_validate_database(self, parent):
        return self.ui_validator_service.check_and_validate_database(parent)

    def get_warning_message(self):
        return self.ui_validator_service.get_warning_message()

    def get_tab_structure(self):
        return self.ui_initializer_service.get_tab_structure()

    def get_warning_label_style(self):
        return self.ui_initializer_service.get_warning_label_style()

    def load_database(self):
        return self.menu_bar_service.load_database()

    def new_database(self):
        return self.menu_bar_service.new_database()

    def reset_database(self):
        return self.menu_bar_service.reset_database()

    def show_about(self, parent):
        show_about_dialog(parent)

    def show_help(self):
        print("Help functionality not implemented yet")