# src/controllers/settings_tab_controllers/accounts_controller.py
from ..common.entity_controller import EntityController
from utils.schema_utils import get_table_name_by_prefix
from utils.custom_logging import logger
from typing import Dict, Any

class AccountsController(EntityController):
    def __init__(self, db_ops):
        table_name = get_table_name_by_prefix("account")
        super().__init__(db_ops, table_name)

    def get_account_by_name(self, account_name: str) -> Dict[str, Any]:
        query = f"SELECT * FROM {self.table_name} WHERE account_name = ?"
        try:
            if result := self.db_ops.fetch_one(query, (account_name,)):
                return dict(zip([col['name'] for col in self.columns], result))
            return None
        except Exception as e:
            logger.error(f"Error fetching account by name: {e}")
            return None
