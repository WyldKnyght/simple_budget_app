# src/controllers/services/expense_service.py
from data_access.db_expense_operations import ExpenseOperations
from data_access.schema_manager import SchemaManager
from utils.custom_logging import error_handler

class ExpenseService:
    def __init__(self):
        self.expense_operations = ExpenseOperations()
        self.schema_manager = SchemaManager()

    @error_handler
    def create_expense(self, expense_name, category_id, due_date, frequency, amount):
        """
        Create a new expense after validating the input data.
        """
        self._validate_expense_data(expense_name, amount)
        return self.expense_operations.create_expense(expense_name, category_id, due_date, frequency, amount)

    @error_handler
    def get_expense_by_id(self, expense_id):
        """
        Retrieve an expense by its ID.
        """
        return self.expense_operations.get_expense_by_id(expense_id)

    @error_handler
    def get_all_expenses(self):
        """
        Retrieve all expenses.
        """
        return self.expense_operations.get_all_expenses()

    @error_handler
    def update_expense(self, expense_id, expense_name, category_id, due_date, frequency, amount):
        """
        Update an existing expense after validating the input data.
        """
        self._validate_expense_data(expense_name, amount)
        self.expense_operations.update_expense(expense_id, expense_name, category_id, due_date, frequency, amount)

    @error_handler
    def delete_expense(self, expense_id):
        """
        Delete an expense by its ID.
        """
        self.expense_operations.delete_expense(expense_id)

    def _validate_expense_data(self, expense_name, amount):
        """
        Validate expense data before creating or updating an expense.
        """
        if not expense_name:
            raise ValueError("Expense name is required")
        if amount is None or amount < 0:
            raise ValueError("Amount must be a non-negative number")
        
        # Additional validation can be added here if needed