# src/user_interface/settings_tab_modules/accounts_tab_modules/accounts_manager.py
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from .accounts_model import AccountsModel
from utils.custom_logging import logger
from controllers.settings_tab_controllers.accounts_controller import AccountsController
from .accounts_dialog import AccountDialog

class AccountsManager:
    def __init__(self, accounts_tab, accounts_controller):
        self.accounts_tab = accounts_tab
        self.accounts_controller = accounts_controller

    def load_accounts(self):
        accounts = self.accounts_controller.get_entities()
        try:
            accounts = self.db_ops.get_entities()
            self.model = AccountsModel(accounts, self.db_ops.columns)
            self.accounts_tab.table_view.setModel(self.model)
        except Exception as e:
            logger.error(f"Error loading accounts: {e}")
            QMessageBox.critical(self.accounts_tab, "Error", f"Failed to load accounts: {str(e)}")

    def add_account(self):
        try:
            dialog = AccountDialog(self.accounts_tab, self.accounts_controller.columns)
            if dialog.exec() == AccountDialog.DialogCode.Accepted:
                account_data = dialog.get_data()
                self.accounts_controller.add_entity(account_data)
                self.load_accounts()
        except Exception as e:
            logger.error(f"Error adding account: {e}")
            QMessageBox.critical(self.accounts_tab, "Error", f"Failed to add account: {str(e)}")

    def remove_account(self):
        try:
            if selected_account := self.get_selected_account():
                self.confirm_and_remove_account(selected_account)
        except Exception as e:
            logger.error(f"Error removing account: {e}")
            QMessageBox.critical(self.accounts_tab, "Error", f"Failed to remove account: {str(e)}")

    def get_selected_account(self):
        try:
            if (
                selected_indexes := self.accounts_tab.accounts_view.selectionModel().selectedRows()
            ):
                selected_row = selected_indexes[0].row()
                account_name_column = next(i for i, col in enumerate(self.db_ops.columns) if col['name'].lower() == 'account_name')
                return selected_row, self.accounts_tab.accounts_view.model().data(
                    self.accounts_tab.accounts_view.model().index(
                        selected_row, account_name_column
                    ),
                    Qt.ItemDataRole.DisplayRole,
                )
            return None, None
        except Exception as e:
            logger.error(f"Error getting selected account: {e}")
            return None, None

    def confirm_and_remove_account(self, account_name):
        try:
            confirm = QMessageBox.question(self.accounts_tab, "Confirm Deletion", f"Are you sure you want to delete the account '{account_name}'?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.remove_account_from_database(account_name)
        except Exception as e:
            logger.error(f"Error confirming account removal: {e}")
            QMessageBox.critical(self.accounts_tab, "Error", f"Failed to confirm account removal: {str(e)}")

    def remove_account_from_database(self, account_name):
        try:
            id_column = next(i for i, col in enumerate(self.db_ops.columns) if col['name'].lower() == 'id')
            account_id = self.accounts_tab.accounts_view.model()._accounts_list[0][id_column]
            self.db_ops.remove_account(account_id)
            self.load_accounts()
        except Exception as e:
            logger.error(f"Error removing account from database: {e}")
            QMessageBox.critical(self.accounts_tab, "Error", f"Failed to remove account from database: {str(e)}")