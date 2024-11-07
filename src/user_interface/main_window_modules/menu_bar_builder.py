# src/user_interface/main_window_modules/menu_bar_builder.py
from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction
from utils.custom_logging import logger
from configs.ui_constants import (
    MENU_FILE, MENU_TOOLS,
    ACTION_RESET_DB, ACTION_EXIT
)

class MenuBarBuilder:
    def __init__(self, parent, ui_controller):
        self.parent = parent
        self.ui_controller = ui_controller
        self.menu_bar = QMenuBar(parent)

    def build(self):
        self.create_file_menu()
        self.create_tools_menu()
        self.connect_actions()
        return self.menu_bar

    def create_file_menu(self):
        self.exit_action = self.create_menu_with_action(MENU_FILE, ACTION_EXIT)

    def create_tools_menu(self):
        self.reset_db_action = self.create_menu_with_action(MENU_TOOLS, ACTION_RESET_DB)

    def create_menu_with_action(self, menu_name, action_name):
        menu = self.menu_bar.addMenu(menu_name)
        action = QAction(action_name, self.parent)
        menu.addAction(action)
        return action

    def connect_actions(self):
        self.exit_action.triggered.connect(self.parent.close)
        self.reset_db_action.triggered.connect(self.ui_controller.reset_database)

def create_menu_bar(parent, ui_controller):
    logger.debug("Creating menu bar")
    return MenuBarBuilder(parent, ui_controller).build()