# src/views/settings_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from .settings_tab_components.accounts_tab import AccountsTab
from .settings_tab_components.categories_tab import CategoriesTab
from .settings_tab_components.expenses_tab import ExpensesTab

class SettingsTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.tab_widget = QTabWidget()
        
        self.accounts_tab = AccountsTab(self.controller)
        self.categories_tab = CategoriesTab(self.controller)
        self.expenses_tab = ExpensesTab(self.controller)
        
        self.tab_widget.addTab(self.accounts_tab, "Accounts")
        self.tab_widget.addTab(self.categories_tab, "Categories")
        self.tab_widget.addTab(self.expenses_tab, "Expenses")
        
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)