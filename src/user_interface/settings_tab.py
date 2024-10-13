# src/user_interface/settings_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from .settings_tab_modules.accounts_tab import AccountsTab
from .settings_tab_modules.categories_tab import CategoriesTab
from .settings_tab_modules.expenses_tab import ExpensesTab
from configs.constants import APP_TITLE

class SettingsTab(QWidget):
    def __init__(self, db_manager, settings_tab_controller):
        super().__init__()
        self.db_manager = db_manager
        self.settings_tab_controller = settings_tab_controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.tab_widget = QTabWidget()
        
        self.accounts_tab = AccountsTab(self.db_manager, self.settings_tab_controller)
        self.categories_tab = CategoriesTab(self.db_manager, self.settings_tab_controller)
        self.expenses_tab = ExpensesTab(self.db_manager, self.settings_tab_controller)
        
        self.tab_widget.addTab(self.accounts_tab, "Accounts")
        self.tab_widget.addTab(self.categories_tab, "Categories")
        self.tab_widget.addTab(self.expenses_tab, "Expenses")
        
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

        self.setWindowTitle(f"{APP_TITLE} - Settings")

    def refresh(self):
        self.settings_tab_controller.refresh()
        for index in range(self.tab_widget.count()):
            tab = self.tab_widget.widget(index)
            if hasattr(tab, 'refresh'):
                tab.refresh()