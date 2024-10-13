# src/controllers/settings_tab_controllers/expenses_controller.py
from ..common.entity_controller import EntityController
from utils.custom_logging import logger, error_handler
from typing import Dict, Any, List, Optional, Tuple
from controllers.db_operations.database_manager import DatabaseManager

class ExpensesController(EntityController):
    def __init__(self, db_ops: DatabaseManager):
        try:
            schema_controller = db_ops.schema_controller
            table_name = schema_controller.get_table_name_by_prefix("expense")
            if not table_name:
                raise ValueError("Expense table not found in the database")
            super().__init__(db_ops, table_name)
            self._ensure_indexes()
        except Exception as e:
            logger.error(f"Error initializing ExpensesController: {e}")
            raise

    def _ensure_indexes(self) -> None:
        self.db_ops.schema_controller.ensure_indexes(self.table_name, ['category_id', 'due_date'])

    @error_handler
    def create_expense(self, **expense_data) -> int:
        return self.add_entity(expense_data)

    @error_handler
    def get_expenses(self, page: int = 1, per_page: int = 100) -> List[Dict[str, Any]]:
        offset = (page - 1) * per_page
        query = f"SELECT * FROM {self.table_name} LIMIT ? OFFSET ?"
        return self._fetch_expenses(query, (per_page, offset))

    @error_handler
    def get_expense(self, expense_id: int) -> Optional[Dict[str, Any]]:
        return self.get_entity(expense_id)

    @error_handler
    def update_expense(self, expense_id: int, **expense_data) -> bool:
        self.update_entity(expense_id, expense_data)
        return True

    @error_handler
    def delete_expense(self, expense_id: int) -> bool:
        self.remove_entity(expense_id)
        return True

    @error_handler
    def get_expenses_by_category(self, category_id: int) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE category_id = ?"
        return self._fetch_expenses(query, (category_id,))

    @error_handler
    def get_expenses_by_date_range(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE due_date BETWEEN ? AND ?"
        return self._fetch_expenses(query, (start_date, end_date))

    def _fetch_expenses(self, query: str, params: tuple) -> List[Dict[str, Any]]:
        results = self.db_ops.fetch_all(query, params)
        return [dict(zip([col['name'] for col in self.columns], row)) for row in results]

    @error_handler
    def get_total_expenses(self) -> float:
        query = f"SELECT SUM(amount) FROM {self.table_name}"
        result = self.db_ops.fetch_one(query)
        return result[0] if result and result[0] is not None else 0.0

    @error_handler
    def get_expenses_summary(self) -> Dict[str, Any]:
        query = f"""
        SELECT 
            COUNT(*) as total_count, 
            SUM(amount) as total_amount, 
            AVG(amount) as average_amount,
            MIN(amount) as min_amount,
            MAX(amount) as max_amount
        FROM {self.table_name}
        """
        result = self.db_ops.fetch_one(query)
        return dict(zip(['total_count', 'total_amount', 'average_amount', 'min_amount', 'max_amount'], result)) if result else {}

    @error_handler
    def backup_expenses(self, backup_path: str) -> Tuple[bool, str]:
        return self.db_ops.schema_controller.backup_database(backup_path)