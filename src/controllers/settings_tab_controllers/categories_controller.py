# src/controllers/settings_tab_controllers/categories_controller.py
from ..common.entity_controller import EntityController
from utils.schema_utils import get_table_name_by_prefix
from typing import Dict, Any, List

class CategoriesController(EntityController):
    def __init__(self, db_ops):
        table_name = get_table_name_by_prefix("categor")
        super().__init__(db_ops, table_name)

    def get_category_tree(self) -> List[Dict[str, Any]]:
        categories = self.get_entities()
        category_dict = {cat['id']: cat for cat in categories}
        root_categories = []

        for cat in categories:
            parent_id = cat.get('parent_id')
            if parent_id is None:
                root_categories.append(cat)
            elif parent := category_dict.get(parent_id):
                parent.setdefault('subcategories', []).append(cat)

        return root_categories