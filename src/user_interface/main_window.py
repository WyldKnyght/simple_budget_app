# src/user_interface/main_window.py
from PyQt6.QtWidgets import QMainWindow, QTabWidget
from PyQt6.QtGui import QCloseEvent
from .common.show_progress_dialog import show_progress_dialog
from .common.show_about_dialog import show_about_dialog
from controllers.ui_operations.main_window_controller import MainWindowController
from .main_window_modules.create_menu_bar import create_menu_bar
from .settings_tab import SettingsTab
from controllers.ui_operations.settings_tab_controller import SettingsTabController
from configs.constants import APP_TITLE, APP_VERSION
from configs.settings_manager import SettingsManager

class MainWindow(QMainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.settings_manager = SettingsManager()
        
        self.setWindowTitle(f"{APP_TITLE} v{APP_VERSION}")

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self._init_controllers()
        self._init_tabs()
        self._init_menu_bar()

        self.controller.load_settings()
        self.settings_manager.load_window_settings(self)

    def _init_controllers(self):
        self.settings_tab_controller = SettingsTabController(self.db_manager)
        self.controller = MainWindowController(self, self.db_manager, self.settings_tab_controller)

    def _init_tabs(self):
        self.settings_tab = SettingsTab(self.db_manager, self.settings_tab_controller)
        self.tab_widget.addTab(self.settings_tab, "Settings")

    def _init_menu_bar(self):
        self.setMenuBar(create_menu_bar(self))

    def reset_database(self):
        progress_dialog = show_progress_dialog(self, "Resetting Database", "Please wait...", 100)
        self.controller.reset_database(progress_dialog)

    def closeEvent(self, event: QCloseEvent):
        self.controller.save_settings()
        self.settings_manager.save_window_settings(self)
        super().closeEvent(event)

    def refresh_all_tabs(self):
        self.settings_tab.refresh()

    def show_about_dialog(self):
        show_about_dialog(self)

    def validate_schema(self):
        self.controller.validate_schema()

    def apply_schema_changes(self):
        self.controller.apply_schema_changes()

    def backup_database(self):
        self.controller.backup_database()