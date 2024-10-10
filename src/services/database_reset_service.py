# src/services/database_reset_service.py
from typing import List, Dict, Any
from configs.default_settings import DEFAULT_ACCOUNT_TYPES, DEFAULT_CATEGORIES
from utils.custom_logging import logger

class DatabaseResetService:
    def __init__(self, db_manager, account_controller, category_controller):
        self.db_manager = db_manager
        self.account_controller = account_controller
        self.category_controller = category_controller

    def reset_database(self):
        try:
            self._initialize_default_accounts()
            self._initialize_default_categories()
            logger.info("Database reset successfully")
        except Exception as e:
            logger.error(f"Error resetting database: {e}")
            raise

def _initialize_default_accounts(self):
    columns = self.account_ops.columns
    column_names = [col['name'] for col in columns]

    for account_type in DEFAULT_ACCOUNT_TYPES:
        account_data = {col: '' for col in column_names}
        account_data['account_name'] = account_type
        account_data['account_type'] = account_type
        self.account_ops.add_account(account_data)

    logger.info(f"Added {len(DEFAULT_ACCOUNT_TYPES)} default accounts")

    def _initialize_default_categories(self):
        categories_to_add = self._flatten_categories(DEFAULT_CATEGORIES)
        self.category_ops.batch_add_categories(categories_to_add)
        logger.info(f"Added {len(categories_to_add)} default categories")

    def _flatten_categories(self, categories: List[Dict[str, Any]], parent_id: int = None) -> List[Dict[str, Any]]:
        flattened = []
        for category in categories:
            if isinstance(category, dict):
                new_category = {
                    'category_name': category['name'],
                    'parent_id': parent_id
                }
                flattened.append(new_category)
                if 'subcategories' in category:
                    flattened.extend(self._flatten_categories(category['subcategories'], len(flattened)))
            elif isinstance(category, str):
                flattened.append({
                    'category_name': category,
                    'parent_id': parent_id
                })
            else:
                logger.warning(f"Unexpected category type: {type(category)}")
        return flattened