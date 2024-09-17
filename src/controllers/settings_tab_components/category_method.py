# src/controllers/settings_tab_components/category_method.py
from utils.custom_logging import logger

class CategoryMethod:
    def __init__(self, database_controller):
        self.db_controller = database_controller
        logger.debug("CategoryMethod initialized")

    def get_categories(self):
        return self.db_controller.category_ops.get_categories()

    def add_category(self, category_name, parent_id=None):
        return self.db_controller.category_ops.add_category(category_name, parent_id)

    def update_category(self, category_id, category_name, parent_id=None):
        return self.db_controller.category_ops.update_category(category_id, category_name, parent_id)

    def delete_category(self, category_id):
        return self.db_controller.category_ops.delete_category(category_id)

    def get_subcategories(self, parent_id):
        return self.db_controller.category_ops.get_subcategories(parent_id)

    def get_category_tree(self):
        categories = self.get_categories()
        logger.debug(f"Retrieved {len(categories)} categories for tree building")
        tree = self._build_category_tree(categories)
        logger.debug(f"Built category tree with {len(tree)} top-level categories")
        return tree

    def _build_category_tree(self, categories, parent_id=None):
        logger.debug(f"Building tree for parent_id: {parent_id}")
        tree = [
            {
                'id': category[0],
                'name': category[1],
                'subcategories': self._build_category_tree(categories, category[0])
            }
            for category in categories
            if category[2] == parent_id
        ]
        logger.debug(f"Built tree for parent_id {parent_id} with {len(tree)} items")
        return tree

    def _build_category_tree(self, categories, parent_id=None):
        logger.debug(f"Building tree for parent_id: {parent_id}")
        tree = [
            {
                'id': category[0],
                'name': category[1],
                'subcategories': self._build_category_tree(categories, category[0])
            }
            for category in categories
            if category[2] == parent_id
        ]
        logger.debug(f"Built tree for parent_id {parent_id}: {tree}")
        return tree

    def print_category_tree(self):
        tree = self.get_category_tree()
        self._print_tree_recursively(tree)

    def _print_tree_recursively(self, categories, level=0):
        for category in categories:
            logger.debug(f"{'  ' * level}{category['name']} (ID: {category['id']})")
            self._print_tree_recursively(category['subcategories'], level + 1)