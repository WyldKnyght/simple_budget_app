# src\data_access\db_category_operations.py
from ..database_manager import DatabaseManager
from configs.db_constants import (
    TABLE_CATEGORIES, FIELD_CATEGORY_ID, FIELD_CATEGORY_NAME, FIELD_PARENT_ID,
    SQL_INSERT_CATEGORY, SQL_SELECT_CATEGORY_BY_ID, SQL_SELECT_ALL_CATEGORIES,
    SQL_UPDATE_CATEGORY, SQL_DELETE_CATEGORY, SQL_SELECT_SUBCATEGORIES
)

class CategoryOperations:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def create_category(self, category_name, parent_id=None):
        query = SQL_INSERT_CATEGORY.format(
            table=TABLE_CATEGORIES,
            name=FIELD_CATEGORY_NAME,
            parent=FIELD_PARENT_ID
        )
        params = (category_name, parent_id)
        cursor = self.db_manager.execute_query(query, params)
        return cursor.lastrowid

    def get_category_by_id(self, category_id):
        query = SQL_SELECT_CATEGORY_BY_ID.format(table=TABLE_CATEGORIES, id=FIELD_CATEGORY_ID)
        cursor = self.db_manager.execute_query(query, (category_id,))
        return cursor.fetchone()

    def get_all_categories(self):
        query = SQL_SELECT_ALL_CATEGORIES.format(table=TABLE_CATEGORIES)
        cursor = self.db_manager.execute_query(query)
        return cursor.fetchall()

    def update_category(self, category_id, category_name, parent_id=None):
        query = SQL_UPDATE_CATEGORY.format(
            table=TABLE_CATEGORIES,
            name=FIELD_CATEGORY_NAME,
            parent=FIELD_PARENT_ID,
            id=FIELD_CATEGORY_ID
        )
        params = (category_name, parent_id, category_id)
        self.db_manager.execute_query(query, params)

    def delete_category(self, category_id):
        query = SQL_DELETE_CATEGORY.format(table=TABLE_CATEGORIES, id=FIELD_CATEGORY_ID)
        self.db_manager.execute_query(query, (category_id,))

    def get_subcategories(self, parent_id):
        query = SQL_SELECT_SUBCATEGORIES.format(
            table=TABLE_CATEGORIES,
            parent=FIELD_PARENT_ID
        )
        cursor = self.db_manager.execute_query(query, (parent_id,))
        return cursor.fetchall()