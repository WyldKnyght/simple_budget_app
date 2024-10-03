# src/user_interface/settings_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from .settings_tab_components.accounts_tab import AccountsTab
from .settings_tab_components.categories_tab import CategoriesTab
from .settings_tab_components.expenses_tab import ExpensesTab
from controllers.settings_tab_controller import SettingsTabController

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = SettingsTabController()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.settings_tabs = QTabWidget()
        self.accounts_tab = AccountsTab(self.controller)
        self.categories_tab = CategoriesTab(self.controller)
        self.expenses_tab = ExpensesTab(self.controller)

        self.settings_tabs.addTab(self.accounts_tab, "Accounts")
        self.settings_tabs.addTab(self.categories_tab, "Categories")
        self.settings_tabs.addTab(self.expenses_tab, "Expenses")

        layout.addWidget(self.settings_tabs)
        self.setLayout(layout)

    def load_accounts(self):
        self.accounts_tab.load_accounts()

    def load_categories(self):
        self.categories_tab.load_categories()

    def load_expenses(self):
        self.expenses_tab.load_expenses()