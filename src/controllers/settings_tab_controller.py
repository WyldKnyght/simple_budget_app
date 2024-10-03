# src/controllers/settings_tab_controller.py

from .database_controllers import db_manager
from .database_modules.account_operations import AccountOperations
from .database_modules.expense_operations import ExpenseOperations
from .database_modules.category_operations import CategoryOperations
from utils.custom_logging import logger

class SettingsTabController:
    def __init__(self):
        self.db_manager = db_manager
        self.account_ops = AccountOperations(self.db_manager)
        self.expense_ops = ExpenseOperations(self.db_manager)
        self.category_ops = CategoryOperations(self.db_manager)

    def get_accounts(self):
        return self.account_ops.get_accounts()

    def add_account(self, account_name, account_number, account_type):
        try:
            result = self.account_ops.add_account(account_name, account_number, account_type)
            logger.info(f"Account added: {account_name}")
            return result
        except Exception as e:
            logger.error(f"Error adding account: {e}")
            raise

    def remove_account(self, account_name):
        return self.account_ops.remove_account_by_name(account_name)

    def get_categories(self):
        return self.category_ops.get_categories()

    def add_category(self, category_name, parent_id=None):
        return self.category_ops.add_category(category_name, parent_id)

    def update_category(self, category_id, category_name, parent_id=None):
        return self.acccategory_opsount_ops.update_category(category_id, category_name, parent_id)

    def remove_category(self, category_id):
        return self.category_ops.remove_category(category_id)

    def get_expenses(self):
        return self.expense_ops.get_expenses()

    def get_expense(self, expense_id):
        return self.expense_ops.get_expense(expense_id)

    def add_expense(self, expense_name, category_id, due_date, frequency, amount):
        return self.expense_ops.add_expense(expense_name, category_id, due_date, frequency, amount)

    def update_expense(self, expense_id, expense_name, category_id, due_date, frequency, amount):
        return self.expense_ops.update_expense(expense_id, expense_name, category_id, due_date, frequency, amount)

    def remove_expense(self, expense_name):
        return self.expense_ops.remove_expense_by_name(expense_name)
    
    def get_category_tree(self):
        categories = self.get_categories()
        return self._build_category_tree(categories)

    def _build_category_tree(self, categories, parent_id=None):
        tree = []
        for cat in categories:
            if cat[2] == parent_id:
                subcategories = self._build_category_tree(categories, cat[0])
                tree.append({
                    'id': cat[0],
                    'name': cat[1],
                    'subcategories': subcategories
                })
        return tree

    def validate_account(self, account_name, account_number, account_type):
        # Add validation logic here
        pass

    def validate_category(self, category_name, parent_id=None):
        # Add validation logic here
        pass

    def validate_expense(self, expense_name, category_id, due_date, frequency, amount):
        # Add validation logic here
        pass

    def get_summary_statistics(self):
        total_accounts = len(self.get_accounts())
        total_categories = len(self.get_categories())
        total_expenses = len(self.get_expenses())
        return {
            'total_accounts': total_accounts,
            'total_categories': total_categories,
            'total_expenses': total_expenses
        }

    def get_transactions(self):
        return self.db_manager.get_transactions()
    