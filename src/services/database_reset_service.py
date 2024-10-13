# src/services/database_reset_service.py
from typing import List, Dict, Any, Generator, Tuple
from configs.default_settings import DEFAULT_ACCOUNT_TYPES, DEFAULT_CATEGORIES
from utils.custom_logging import logger
from controllers.schema_controllers.schema_exceptions import SchemaError, SchemaApplicationError

class DatabaseResetService:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.schema_controller = db_manager.schema_controller
        self.account_controller = db_manager.get_operation('accounts')
        self.category_controller = db_manager.get_operation('categories')

    def reset_database(self) -> Generator[Tuple[int, int], None, None]:
        total_steps = 4 + len(DEFAULT_ACCOUNT_TYPES) + self._count_categories(DEFAULT_CATEGORIES)
        progress = 0

        try:
            yield progress, total_steps
            self._drop_all_tables()
            progress += 1
            yield progress, total_steps

            self._create_tables()
            progress += 1
            yield progress, total_steps

            yield from self._initialize_default_accounts(progress, total_steps)
            progress += len(DEFAULT_ACCOUNT_TYPES)

            yield from self._initialize_default_categories(progress, total_steps)

            logger.info("Database reset successfully")
        except SchemaError as e:
            logger.error(f"Schema error while resetting database: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error while resetting database: {e}")
            raise SchemaError(f"Failed to reset database: {str(e)}") from e

    def _drop_all_tables(self):
        tables = self.schema_controller.get_table_names()
        for table in tables:
            self.db_manager.execute_query(f"DROP TABLE IF EXISTS {table};")
        logger.info(f"Dropped {len(tables)} tables")

    def _create_tables(self):
        success, message = self.schema_controller.apply_schema_changes()
        if not success:
            logger.error(f"Failed to create tables: {message}")
            raise SchemaApplicationError(f"Failed to create tables: {message}")
        logger.info("Tables created successfully")

    def _initialize_default_accounts(self, progress: int, total_steps: int) -> Generator[Tuple[int, int], None, None]:
        columns = self.account_controller.columns
        for account_type in DEFAULT_ACCOUNT_TYPES:
            account_data = {col['name']: '' for col in columns if col['name'] != 'id'}
            account_data['account_name'] = account_type
            account_data['account_type'] = account_type
            account_data['account_number'] = f"DEFAULT-{account_type.upper()}"
            self.account_controller.add_entity(account_data)
            progress += 1
            yield progress, total_steps
        logger.info(f"Added {len(DEFAULT_ACCOUNT_TYPES)} default accounts")

    def _initialize_default_categories(self, progress: int, total_steps: int) -> Generator[Tuple[int, int], None, None]:
        yield from self._add_categories(DEFAULT_CATEGORIES, None, progress, total_steps)
        logger.info(f"Added {self._count_categories(DEFAULT_CATEGORIES)} default categories")

    def _add_categories(self, categories: List[Dict[str, Any]], parent_id: int, progress: int, total_steps: int) -> Generator[Tuple[int, int], None, None]:
        for category in categories:
            if isinstance(category, dict):
                new_category = {
                    'category_name': category['name'],
                    'parent_id': parent_id
                }
                new_id = self.category_controller.add_entity(new_category)
                progress += 1
                yield progress, total_steps
                if 'subcategories' in category:
                    yield from self._add_categories(category['subcategories'], new_id, progress, total_steps)
            elif isinstance(category, str):
                self.category_controller.add_entity({
                    'category_name': category,
                    'parent_id': parent_id
                })
                progress += 1
                yield progress, total_steps
            else:
                logger.warning(f"Unexpected category type: {type(category)}")

    def _count_categories(self, categories: List[Dict[str, Any]]) -> int:
        count = 0
        for category in categories:
            if isinstance(category, dict):
                count += 1
                if 'subcategories' in category:
                    count += self._count_categories(category['subcategories'])
            elif isinstance(category, str):
                count += 1
        return count