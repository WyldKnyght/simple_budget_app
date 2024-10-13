# src/user_interface/settings_tab_modules/accounts_tab_modules/accounts_manager.py
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from .accounts_model import AccountsModel
from utils.custom_logging import logger
from .accounts_dialog import AccountDialog

class AccountsManager:
    def __init__(self, accounts_tab, accounts_controller):
        self.accounts_tab = accounts_tab
        self.accounts_controller = accounts_controller
        self.model = None

    def load_accounts(self):
        try:
            accounts = self.accounts_controller.get_entities()
            self.model = AccountsModel(accounts, self.accounts_controller.columns)
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

    def edit_account(self):
        try:
            if (
                selected_indexes := self.accounts_tab.table_view.selectionModel().selectedRows()
            ):
                selected_row = selected_indexes[0].row()
                account_id = self.model.data(self.model.index(selected_row, 0), Qt.ItemDataRole.DisplayRole)
                if account_data := self.accounts_controller.get_entity(account_id):
                    dialog = AccountDialog(self.accounts_tab, self.accounts_controller.columns, account_data)
                    if dialog.exec() == AccountDialog.DialogCode.Accepted:
                        updated_data = dialog.get_data()
                        self.accounts_controller.update_entity(account_id, updated_data)
                        self.load_accounts()
                else:
                    QMessageBox.warning(self.accounts_tab, "Warning", "Failed to retrieve account data.")
            else:
                QMessageBox.warning(self.accounts_tab, "Warning", "Please select an account to edit.")
        except Exception as e:
            logger.error(f"Error editing account: {e}")
            QMessageBox.critical(self.accounts_tab, "Error", f"Failed to edit account: {str(e)}")

    def remove_account(self):
        try:
            if (
                selected_indexes := self.accounts_tab.table_view.selectionModel().selectedRows()
            ):
                selected_row = selected_indexes[0].row()
                account_id = self.model.data(self.model.index(selected_row, 0), Qt.ItemDataRole.DisplayRole)
                account_name = self.model.data(self.model.index(selected_row, 1), Qt.ItemDataRole.DisplayRole)

                confirm = QMessageBox.question(self.accounts_tab, "Confirm Deletion", 
                                               f"Are you sure you want to delete the account '{account_name}'?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                if confirm == QMessageBox.StandardButton.Yes:
                    self.accounts_controller.remove_entity(account_id)
                    self.load_accounts()
            else:
                QMessageBox.warning(self.accounts_tab, "Warning", "Please select an account to remove.")
        except Exception as e:
            logger.error(f"Error removing account: {e}")
            QMessageBox.critical(self.accounts_tab, "Error", f"Failed to remove account: {str(e)}")