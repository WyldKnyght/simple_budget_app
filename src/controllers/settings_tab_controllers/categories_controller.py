# src/controllers/settings_tab_controllers/categories_controller.py
from ..common.entity_controller import EntityController
from utils.custom_logging import logger, error_handler
from typing import Dict, Any, List, Optional, Tuple
from controllers.db_operations.database_manager import DatabaseManager

class CategoriesController(EntityController):
    def __init__(self, db_ops: DatabaseManager):
        try:
            schema_controller = db_ops.schema_controller
            table_name = schema_controller.get_table_name_by_prefix("categor")
            if not table_name:
                raise ValueError("Category table not found in the database")
            super().__init__(db_ops, table_name)
            
            # Ensure indexes for frequently queried columns
            schema_controller.ensure_indexes(table_name, ["parent_id", "category_name"])
        except Exception as e:
            logger.error(f"Error initializing CategoriesController: {e}")
            raise

    @error_handler
    def get_category_tree(self) -> List[Dict[str, Any]]:
        categories = self.get_entities()
        return self._build_category_tree(categories)

    @error_handler
    def get_categories(self) -> List[Dict[str, Any]]:
        return self.get_entities()
    
    def _build_category_tree(self, categories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        category_dict = {cat['id']: cat for cat in categories}
        root_categories = []

        for cat in categories:
            parent_id = cat.get('parent_id')
            if parent_id is None:
                root_categories.append(cat)
            elif parent := category_dict.get(parent_id):
                parent.setdefault('subcategories', []).append(cat)

        return root_categories

    @error_handler
    def create_category(self, **category_data) -> int:
        return self.add_entity(category_data)

    @error_handler
    def update_category(self, category_id: int, category_data: Dict[str, Any]) -> bool:
        self.update_entity(category_id, category_data)
        return True

    @error_handler
    def delete_category(self, category_id: int) -> bool:
        self.remove_entity(category_id)
        return True

    @error_handler
    def get_category_by_name(self, category_name: str) -> Optional[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE name = ?"
        result = self.db_ops.fetch_one(query, (category_name,))
        return dict(zip([col['name'] for col in self.columns], result)) if result else None

    @error_handler
    def get_subcategories(self, parent_id: int) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE parent_id = ?"
        results = self.db_ops.fetch_all(query, (parent_id,))
        return [dict(zip([col['name'] for col in self.columns], row)) for row in results]

    @error_handler
    def backup_categories(self, backup_path: str) -> Tuple[bool, str]:
        return self.db_ops.schema_controller.backup_database(backup_path)