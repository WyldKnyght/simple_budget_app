# src/controllers/settings_tab_controllers/expenses_controller.py
from ..common.entity_controller import EntityController
from utils.schema_utils import get_table_name_by_prefix
from utils.custom_logging import logger, error_handler
import sqlite3
from typing import Dict, Any, List

class ExpensesController(EntityController):
    def __init__(self, db_ops):
        table_name = get_table_name_by_prefix("expense")
        super().__init__(db_ops, table_name)
        self._ensure_indexes()

    def _ensure_indexes(self):
        try:
            self.db_ops.execute_query(f"CREATE INDEX IF NOT EXISTS idx_{self.table_name}_category_id ON {self.table_name} (category_id)")
            self.db_ops.execute_query(f"CREATE INDEX IF NOT EXISTS idx_{self.table_name}_due_date ON {self.table_name} (due_date)")
        except sqlite3.Error as e:
            logger.error(f"Error creating indexes: {e}")

    @error_handler
    def add_expense(self, **expense_data):
        return self.add_entity(expense_data)

    def get_expenses(self, page: int = 1, per_page: int = 100) -> List[Dict[str, Any]]:
        offset = (page - 1) * per_page
        query = f"SELECT * FROM {self.table_name} LIMIT ? OFFSET ?"
        try:
            results = self.db_ops.fetch_all(query, (per_page, offset))
            return [dict(zip([col['name'] for col in self.columns], row)) for row in results]
        except sqlite3.Error as e:
            logger.error(f"Error fetching expenses: {e}")
            return []

    def get_expense(self, expense_id: int) -> Dict[str, Any]:
        query = f"SELECT * FROM {self.table_name} WHERE id = ?"
        try:
            if result := self.db_ops.fetch_one(query, (expense_id,)):
                return dict(zip([col['name'] for col in self.columns], result))
            raise ValueError(f"No expense found with id {expense_id}")
        except sqlite3.Error as e:
            logger.error(f"Error fetching expense: {e}")
            raise

    def update_expense(self, expense_id: int, **expense_data) -> None:
        self.update_entity(expense_id, expense_data)

    def remove_expense(self, expense_id: int) -> None:
        self.remove_entity(expense_id)

    def get_expenses_by_category(self, category_id: int) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE category_id = ?"
        return self._fetch_expenses(query, (category_id,))

    def get_expenses_by_date_range(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE due_date BETWEEN ? AND ?"
        return self._fetch_expenses(query, (start_date, end_date))

    def _fetch_expenses(self, query: str, params: tuple) -> List[Dict[str, Any]]:
        try:
            results = self.db_ops.fetch_all(query, params)
            return [dict(zip([col['name'] for col in self.columns], row)) for row in results]
        except sqlite3.Error as e:
            logger.error(f"Error fetching expenses: {e}")
            return []