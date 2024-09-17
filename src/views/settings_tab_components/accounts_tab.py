# src/views/settings_tab_components/accounts_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from .account_dialog import AccountDialog

class AccountsTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller.account  # Now points directly to AccountMethod
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.accounts_table = QTableWidget()
        self.accounts_table.setColumnCount(4)
        self.accounts_table.setHorizontalHeaderLabels(["ID", "Account Name", "Account Number", "Account Type"])
        
        add_button = QPushButton("Add Account")
        add_button.clicked.connect(self.add_account)
        
        layout.addWidget(self.accounts_table)
        layout.addWidget(add_button)
        self.setLayout(layout)
        
        self.load_accounts()

    def load_accounts(self):
        accounts = self.controller.get_accounts()
        self.accounts_table.setRowCount(len(accounts))
        for row, account in enumerate(accounts):
            self.accounts_table.setItem(row, 0, QTableWidgetItem(str(account[0])))
            self.accounts_table.setItem(row, 1, QTableWidgetItem(account[1]))
            self.accounts_table.setItem(row, 2, QTableWidgetItem(account[2]))
            self.accounts_table.setItem(row, 3, QTableWidgetItem(account[3]))

    def add_account(self):
        account_types = self.controller.get_account_types()
        dialog = AccountDialog(account_types, self.controller.add_account_type)
        if dialog.exec():
            account_name, account_number, account_type = dialog.get_account_info()
            self.controller.add_account(account_name, account_number, account_type)
            self.load_accounts()