# src/controllers/settings_tab_controller.py

from .settings_tab_components.account_method import AccountMethod
from .settings_tab_components.category_method import CategoryMethod
from .settings_tab_components.expense_method import ExpenseMethod
from utils.custom_logging import logger


class SettingsTabController:
    def __init__(self, database_controller):
        self.db_controller = database_controller
        self.account = AccountMethod(database_controller)
        self.category = CategoryMethod(database_controller)
        self.expense = ExpenseMethod(database_controller)

    def print_category_tree(self):
        logger.debug("Printing category tree:")
        self.category.print_category_tree()