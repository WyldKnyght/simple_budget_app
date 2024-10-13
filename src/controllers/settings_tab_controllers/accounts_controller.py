# src/controllers/settings_tab_controllers/accounts_controller.py
from ..common.entity_controller import EntityController
from utils.custom_logging import logger, error_handler
from typing import Dict, Any, Optional, List, Tuple

class AccountsController(EntityController):
    def __init__(self, db_ops):
        try:
            schema_controller = db_ops.schema_controller
            table_name = schema_controller.get_table_name_by_prefix("account")
            if not table_name:
                raise ValueError("Account table not found in the database")
            super().__init__(db_ops, table_name)
            
            # Ensure indexes for frequently queried columns
            schema_controller.ensure_indexes(table_name, ["account_name", "account_number"])
        except Exception as e:
            logger.error(f"Error initializing AccountsController: {e}")
            raise

    @error_handler
    def get_account_by_name(self, account_name: str) -> Optional[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE account_name = ?"
        result = self.db_ops.fetch_one(query, (account_name,))
        return dict(zip([col['name'] for col in self.columns], result)) if result else None

    @error_handler
    def get_account_by_number(self, account_number: str) -> Optional[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE account_number = ?"
        result = self.db_ops.fetch_one(query, (account_number,))
        return dict(zip([col['name'] for col in self.columns], result)) if result else None

    @error_handler
    def get_all_accounts(self) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name}"
        results = self.db_ops.fetch_all(query)
        return [dict(zip([col['name'] for col in self.columns], row)) for row in results]

    @error_handler
    def create_account(self, **account_data) -> int:
        columns = ', '.join(account_data.keys())
        placeholders = ', '.join(['?' for _ in account_data])
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        cursor = self.db_ops.execute_query(query, tuple(account_data.values()))
        return cursor.lastrowid

    @error_handler
    def update_account(self, account_id: int, account_data: Dict[str, Any]) -> bool:
        self.update_entity(account_id, account_data)
        return True

    @error_handler
    def delete_account(self, account_id: int) -> bool:
        self.remove_entity(account_id)
        return True

    @error_handler
    def backup_accounts(self, backup_path: str) -> Tuple[bool, str]:
        return self.db_ops.schema_controller.backup_database(backup_path)