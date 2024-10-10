# src/user_interface/main_window.py
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QMessageBox
from controllers.ui_operations.main_window_controller import MainWindowController
from .common.show_progress_dialog import show_progress_dialog
from .main_window_modules.create_menu_bar import create_menu_bar

from .settings_tab import SettingsTab

class MainWindow(QMainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Family Expense and Income Tracker")

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.settings_tab = SettingsTab(self.db_manager)
        self.tab_widget.addTab(self.settings_tab, "Settings")

        self.controller = MainWindowController(self, self.db_manager)

        self.setMenuBar(create_menu_bar(self))
        self.controller.load_settings()

    def reset_database(self):
        progress_dialog = show_progress_dialog(self, "Resetting Database", "Please wait...", 100)
        self.controller.reset_database(progress_dialog)
        progress_dialog.setValue(100)

    def closeEvent(self, event):
        self.controller.save_settings()
        super().closeEvent(event)

    def refresh_all_tabs(self):
        self.settings_tab.refresh()

    def show_about_dialog(self):
        QMessageBox.about(self, "About", "Family Expense and Income Tracker\nVersion 1.0")
