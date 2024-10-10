# src/controllers/ui_operations/main_window_controller.py
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from controllers.db_operations.database_initializer import DatabaseInitializer
from .settings_tab_controller import SettingsTabController
from utils.custom_logging import logger

class MainWindowController:
    def __init__(self, window: QMainWindow, db_manager):
        self.window = window
        self.db_manager = db_manager
        self.settings_tab_controller = SettingsTabController(db_manager)

    def load_settings(self):
        try:
            self.main_window.restoreGeometry(self.settings.value("geometry"))
            self.main_window.restoreState(self.settings.value("windowState"))
            logger.info("Main window settings loaded successfully")
        except Exception as e:
            logger.error(f"Error loading main window settings: {e}")

    def save_settings(self):
        try:
            self.settings.setValue("geometry", self.main_window.saveGeometry())
            self.settings.setValue("windowState", self.main_window.saveState())
            logger.info("Main window settings saved successfully")
        except Exception as e:
            logger.error(f"Error saving main window settings: {e}")

    def reset_database(self):
        DatabaseInitializer.reset_database(self.db_manager)
        self.settings_tab_controller.refresh()

    def show_about_dialog(self):
        QMessageBox.about(self.window, "About", "Family Expense and Income Tracker\nVersion 1.0")

    def exit_application(self):
        self.save_settings()
        self.main_window.close()