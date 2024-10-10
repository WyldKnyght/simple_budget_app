# src/controllers/validators/expense_validator.py

from utils.custom_logging import logger
from datetime import datetime

class ExpenseValidator:
    def __init__(self, schema_columns):
        self.schema_columns = schema_columns

    def validate_expense_data(self, expense_data):
        for column in self.schema_columns:
            if column != 'id' and column not in expense_data:
                raise ValueError(f"Missing required field: {column}")
            if column in expense_data:
                self.validate_field(column, expense_data[column])

    def validate_field(self, field_name, value):
        if field_name == 'expense_name':
            if not isinstance(value, str) or not value.strip():
                raise ValueError("Expense name must be a non-empty string")
        elif field_name == 'category_id':
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Category ID must be a positive integer")
        elif field_name == 'due_date':
            try:
                datetime.strptime(value, '%Y-%m-%d')
            except ValueError as e:
                raise ValueError("Due date must be in YYYY-MM-DD format") from e
        elif field_name == 'frequency':
            valid_frequencies = ['once', 'daily', 'weekly', 'monthly', 'yearly']
            if value not in valid_frequencies:
                raise ValueError(f"Frequency must be one of: {', '.join(valid_frequencies)}")
        elif field_name == 'amount':
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError("Amount must be a non-negative number")

    def validate_expense_id(self, expense_id):
        if not isinstance(expense_id, int) or expense_id <= 0:
            raise ValueError("Expense ID must be a positive integer")

logger.info("ExpenseValidator initialized")