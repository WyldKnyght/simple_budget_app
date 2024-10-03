# src/user_interface/settings_tab_components/accounts_tab.py

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QPushButton, 
                             QHBoxLayout, QTableWidgetItem, QMessageBox)
from .accounts_dialog import AccountDialog

class AccountsTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.accounts_table = QTableWidget()
        self.accounts_table.setColumnCount(3)  # Reduced from 4 to 3
        self.accounts_table.setHorizontalHeaderLabels(["Account Name", "Account Number", "Account Type"])
        layout.addWidget(self.accounts_table)

        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Account")
        self.remove_button = QPushButton("Remove Account")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.remove_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_account)
        self.remove_button.clicked.connect(self.remove_account)

        self.load_accounts()

    def load_accounts(self):
        accounts = self.controller.get_accounts()
        self.accounts_table.setRowCount(len(accounts))
        for row, account in enumerate(accounts):
            for col, value in enumerate(account[1:]):  # Skip the first column (ID)
                self.accounts_table.setItem(row, col, QTableWidgetItem(str(value)))

    def add_account(self):
        dialog = AccountDialog(self)
        if dialog.exec() == AccountDialog.DialogCode.Accepted:
            account_name = dialog.name_input.text()
            account_number = dialog.number_input.text()
            account_type = dialog.type_input.currentText()
            
            self.controller.add_account(account_name, account_number, account_type)
            self.load_accounts()

    def remove_account(self):
        if selected_rows := self.accounts_table.selectionModel().selectedRows():
            selected_row = selected_rows[0].row()
            account_name = self.accounts_table.item(selected_row, 0).text()

            confirm = QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to delete the account '{account_name}'?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.controller.remove_account(account_name)
                self.load_accounts()