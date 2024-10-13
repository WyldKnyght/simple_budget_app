# src/user_interface/settings_tab_modules/expenses_tab.py
from PyQt6.QtWidgets import QVBoxLayout, QTableView, QPushButton, QHBoxLayout
from PyQt6.QtGui import QStandardItemModel
from ..common.base_tab import BaseTab
from .expenses_tab_modules.expenses_manager import ExpensesManager
from controllers.settings_tab_controllers.expenses_controller import ExpensesController
from configs.constants import (EXPENSE_TAB_TITLE, ADD_EXPENSE_BUTTON_TEXT,
                               EDIT_EXPENSE_BUTTON_TEXT, DELETE_EXPENSE_BUTTON_TEXT)
from utils.custom_logging import logger

class ExpensesTab(BaseTab):
    def __init__(self, db_manager, settings_tab_controller):
        super().__init__(db_manager, ExpensesController)
        self.settings_tab_controller = settings_tab_controller
        self.expenses_manager = ExpensesManager(self, self.controller)
        self.init_ui()

    def init_ui(self):
        try:
            layout = QVBoxLayout()

            self.model = QStandardItemModel()
            self.table_view = QTableView()
            self.table_view.setModel(self.model)
            self.table_view.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
            layout.addWidget(self.table_view)

            button_layout = QHBoxLayout()
            self.add_button = QPushButton(ADD_EXPENSE_BUTTON_TEXT)
            self.edit_button = QPushButton(EDIT_EXPENSE_BUTTON_TEXT)
            self.delete_button = QPushButton(DELETE_EXPENSE_BUTTON_TEXT)
            button_layout.addWidget(self.add_button)
            button_layout.addWidget(self.edit_button)
            button_layout.addWidget(self.delete_button)
            layout.addLayout(button_layout)

            self.setLayout(layout)

            self.add_button.clicked.connect(self.expenses_manager.add_expense)
            self.edit_button.clicked.connect(self.expenses_manager.edit_expense)
            self.delete_button.clicked.connect(self.expenses_manager.remove_expense)

            self.setWindowTitle(EXPENSE_TAB_TITLE)
            self.load_expenses()
        except Exception as e:
            logger.error(f"Error in ExpensesTab init_ui: {e}")

    def load_expenses(self):
        try:
            self.expenses_manager.load_expenses(self.model, self.table_view)
        except Exception as e:
            logger.error(f"Error loading expenses: {e}")

    def refresh(self):
        self.load_expenses()