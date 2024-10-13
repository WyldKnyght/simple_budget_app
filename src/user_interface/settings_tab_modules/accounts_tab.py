# src/user_interface/settings_tab_modules/accounts_tab.py
from PyQt6.QtWidgets import QVBoxLayout, QTableView, QPushButton, QHBoxLayout, QMessageBox
from ..common.base_tab import BaseTab
from .accounts_tab_modules.accounts_manager import AccountsManager
from controllers.settings_tab_controllers.accounts_controller import AccountsController
from configs.constants import ACCOUNT_TAB_TITLE, ADD_ACCOUNT_BUTTON_TEXT, EDIT_ACCOUNT_BUTTON_TEXT, REMOVE_ACCOUNT_BUTTON_TEXT
from utils.custom_logging import logger

class AccountsTab(BaseTab):
    def __init__(self, db_manager, settings_tab_controller):
        try:
            self.settings_tab_controller = settings_tab_controller
            super().__init__(db_manager, AccountsController)
            self.accounts_manager = AccountsManager(self, self.controller)
            self.init_ui()
        except Exception as e:
            logger.error(f"Error initializing AccountsTab: {e}")
            QMessageBox.critical(self, "Error", f"Failed to initialize Accounts Tab: {str(e)}")

    def init_ui(self):
        try:
            layout = QVBoxLayout()

            self.table_view = QTableView()
            layout.addWidget(self.table_view)

            button_layout = QHBoxLayout()
            self.add_button = QPushButton(ADD_ACCOUNT_BUTTON_TEXT)
            self.edit_button = QPushButton(EDIT_ACCOUNT_BUTTON_TEXT)
            self.remove_button = QPushButton(REMOVE_ACCOUNT_BUTTON_TEXT)
            button_layout.addWidget(self.add_button)
            button_layout.addWidget(self.edit_button)
            button_layout.addWidget(self.remove_button)
            layout.addLayout(button_layout)

            self.setLayout(layout)

            self.add_button.clicked.connect(self.accounts_manager.add_account)
            self.edit_button.clicked.connect(self.accounts_manager.edit_account)
            self.remove_button.clicked.connect(self.accounts_manager.remove_account)

            self.setWindowTitle(ACCOUNT_TAB_TITLE)
        except Exception as e:
            logger.error(f"Error in AccountsTab init_ui: {e}")
            QMessageBox.critical(self, "Error", f"Failed to initialize Accounts Tab UI: {str(e)}")

    def refresh(self):
        try:
            self.accounts_manager.load_accounts()
        except Exception as e:
            logger.error(f"Error refreshing AccountsTab: {e}")
            QMessageBox.critical(self, "Error", f"Failed to refresh Accounts Tab: {str(e)}")