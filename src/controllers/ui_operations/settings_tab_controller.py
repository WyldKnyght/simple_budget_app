# src/controllers/tab_operations/settings_tab_operations.py

from utils.custom_logging import logger

class SettingsTabController:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_category_tree(self):
        return self.db_manager.categories_ops.get_category_tree()

    def format_account_display(self, account):
        return f"{account['account_name']} ({account['account_number']})"

    def format_expense_display(self, expense):
        return f"{expense['expense_name']} - {expense['amount']} (Due: {expense['due_date']})"

    def get_accounts(self):
        return self.db_manager.accounts_ops.get_accounts()

    def get_expenses(self):
        return self.db_manager.expenses_ops.get_expenses()

    def add_account(self, account_data):
        return self.db_manager.accounts_ops.add_account(**account_data)

    def update_account(self, account_id, account_data):
        return self.db_manager.accounts_ops.update_account(account_id, **account_data)

    def delete_account(self, account_id):
        return self.db_manager.accounts_ops.remove_account(account_id)

    def add_category(self, category_data):
        return self.db_manager.categories_ops.add_category(**category_data)

    def update_category(self, category_id, category_data):
        return self.db_manager.categories_ops.update_category(category_id, **category_data)

    def delete_category(self, category_id):
        return self.db_manager.categories_ops.remove_category(category_id)

    def add_expense(self, expense_data):
        return self.db_manager.expenses_ops.add_expense(**expense_data)

    def update_expense(self, expense_id, expense_data):
        return self.db_manager.expenses_ops.update_expense(expense_id, **expense_data)

    def delete_expense(self, expense_id):
        return self.db_manager.expenses_ops.remove_expense(expense_id)

logger.info("SettingsTabOperations initialized")