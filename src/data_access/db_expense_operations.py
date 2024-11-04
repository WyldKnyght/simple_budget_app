# src\data_access\db_expense_operations.py
from .database_manager import DatabaseManager
from configs.db_constants import (
    TABLE_EXPENSES, FIELD_EXPENSE_ID, FIELD_EXPENSE_NAME, FIELD_CATEGORY_ID,
    FIELD_DUE_DATE, FIELD_FREQUENCY, FIELD_AMOUNT,
    SQL_INSERT_EXPENSE, SQL_SELECT_EXPENSE_BY_ID, SQL_SELECT_ALL_EXPENSES,
    SQL_UPDATE_EXPENSE, SQL_DELETE_EXPENSE
)

class ExpenseOperations:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def create_expense(self, expense_name, category_id, due_date, frequency, amount):
        query = SQL_INSERT_EXPENSE.format(
            table=TABLE_EXPENSES,
            name=FIELD_EXPENSE_NAME,
            category=FIELD_CATEGORY_ID,
            due_date=FIELD_DUE_DATE,
            frequency=FIELD_FREQUENCY,
            amount=FIELD_AMOUNT
        )
        params = (expense_name, category_id, due_date, frequency, amount)
        cursor = self.db_manager.execute_query(query, params)
        return cursor.lastrowid

    def get_expense_by_id(self, expense_id):
        query = SQL_SELECT_EXPENSE_BY_ID.format(table=TABLE_EXPENSES, id=FIELD_EXPENSE_ID)
        cursor = self.db_manager.execute_query(query, (expense_id,))
        return cursor.fetchone()

    def get_all_expenses(self):
        query = SQL_SELECT_ALL_EXPENSES.format(table=TABLE_EXPENSES)
        cursor = self.db_manager.execute_query(query)
        return cursor.fetchall()

    def update_expense(self, expense_id, expense_name, category_id, due_date, frequency, amount):
        query = SQL_UPDATE_EXPENSE.format(
            table=TABLE_EXPENSES,
            name=FIELD_EXPENSE_NAME,
            category=FIELD_CATEGORY_ID,
            due_date=FIELD_DUE_DATE,
            frequency=FIELD_FREQUENCY,
            amount=FIELD_AMOUNT,
            id=FIELD_EXPENSE_ID
        )
        params = (expense_name, category_id, due_date, frequency, amount, expense_id)
        self.db_manager.execute_query(query, params)

    def delete_expense(self, expense_id):
        query = SQL_DELETE_EXPENSE.format(table=TABLE_EXPENSES, id=FIELD_EXPENSE_ID)
        self.db_manager.execute_query(query, (expense_id,))