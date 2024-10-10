# src/user_interface/settings_tab.py
from PyQt6.QtWidgets import QTabWidget
from controllers.settings_tab_controllers.accounts_controller import AccountsController
from controllers.settings_tab_controllers.categories_controller import CategoriesController
from controllers.settings_tab_controllers.expenses_controller import ExpensesController
from controllers.ui_operations.settings_tab_controller import SettingsTabController
from .common.base_tab import BaseTab

class SettingsTab(BaseTab):
    def __init__(self, db_manager):
        super().__init__(db_manager, SettingsTabController) 
        self.db_manager = db_manager
        
    def init_ui(self):
        super().init_ui()
        self.settings_tabs = QTabWidget()

        self.accounts_tab = BaseTab(self.db_manager, AccountsController)
        self.categories_tab = BaseTab(self.db_manager, CategoriesController)
        self.expenses_tab = BaseTab(self.db_manager, ExpensesController)

        self.settings_tabs.addTab(self.accounts_tab, "Accounts")
        self.settings_tabs.addTab(self.categories_tab, "Categories")
        self.settings_tabs.addTab(self.expenses_tab, "Expenses")

        self.layout().addWidget(self.settings_tabs)