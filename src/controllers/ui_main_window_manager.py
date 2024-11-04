# src/controllers/ui_main_window_manager.py
from data_access.database_manager import DatabaseManager
from .services.check_and_validate_database import CheckAndValidateDatabase
from .services.menu_bar_service import MenuBarService
from user_interface.dialogs.show_about_dialog import show_about_dialog

class MainWindowManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.menu_bar_service = MenuBarService(self.db_manager)
        self.check_and_validate_database = CheckAndValidateDatabase()

    def check_and_validate_database(self, parent):
        return self.check_and_validate_database.check_and_validate(parent)

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