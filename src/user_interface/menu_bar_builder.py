# src/user_interface/menu_bar_builder.py
from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction
from configs.ui_constants import (
    MENU_FILE, MENU_TOOLS, MENU_HELP,
    ACTION_NEW_DB, ACTION_OPEN_DB, ACTION_RESET_DB, ACTION_EXIT,
    ACTION_ABOUT, ACTION_HELP
)

class MenuBarBuilder:
    def __init__(self, parent, ui_controller):
        self.parent = parent
        self.ui_controller = ui_controller
        self.menu_bar = QMenuBar(parent)

    def build(self):
        self.create_file_menu()
        self.create_tools_menu()
        self.create_help_menu()
        self.connect_actions()
        self.update_menu_state()
        return self.menu_bar

    def create_file_menu(self):
        file_menu = self.menu_bar.addMenu(MENU_FILE)
        self.open_db_action = QAction(ACTION_OPEN_DB, self.parent)
        self.new_db_action = QAction(ACTION_NEW_DB, self.parent)
        self.reset_db_action = QAction(ACTION_RESET_DB, self.parent)
        self.exit_action = QAction(ACTION_EXIT, self.parent)
        file_menu.addActions([self.open_db_action, self.new_db_action, self.reset_db_action, self.exit_action])

    def create_tools_menu(self):
        tools_menu = self.menu_bar.addMenu(MENU_TOOLS)
        self.populate_test_data_action = QAction("Populate Test Data", self.parent)
        tools_menu.addAction(self.populate_test_data_action)

    def create_help_menu(self):
        help_menu = self.menu_bar.addMenu(MENU_HELP)
        self.about_action = QAction(ACTION_ABOUT, self.parent)
        self.help_action = QAction(ACTION_HELP, self.parent)
        help_menu.addActions([self.about_action, self.help_action])

    def connect_actions(self):
        self.open_db_action.triggered.connect(self.ui_controller.load_database)
        self.new_db_action.triggered.connect(self.ui_controller.new_database)
        self.reset_db_action.triggered.connect(self.ui_controller.reset_database)
        self.exit_action.triggered.connect(self.parent.close)
        self.about_action.triggered.connect(lambda: self.ui_controller.show_about(self.parent))
        self.help_action.triggered.connect(self.ui_controller.show_help)

    def update_menu_state(self):
        db_exists = self.ui_controller.db_manager.validation_operations.database_exists()
        self.open_db_action.setEnabled(db_exists)
        self.new_db_action.setEnabled(not db_exists)
        self.reset_db_action.setEnabled(db_exists)

def create_menu_bar(parent, ui_controller):
    return MenuBarBuilder(parent, ui_controller).build()