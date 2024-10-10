# src/user_interface/settings_tab_modules/accounts_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from .accounts_tab_modules.accounts_manager import AccountsManager
from ..common.table_widget import TableWidget, ButtonLayout

class AccountsTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.accounts_ops = self.db_manager.get_operation('accounts')
        self.manager = AccountsManager(self)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table_view = TableWidget()
        layout.addWidget(self.table_view)

        button_layout = ButtonLayout("Add Account", "Edit Account", "Delete Account")
        layout.addLayout(button_layout)

        self.load_accounts()

    def load_accounts(self):
        self.manager.load_accounts()