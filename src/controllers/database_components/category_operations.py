# src/controllers/database_components/category_operations.py
from utils.custom_logging import logger

class CategoryOperations:
    def __init__(self, db_service):
        self.db_service = db_service

    def add_category(self, category_name, parent_id=None):
        sql = "INSERT INTO Categories (category_name, parent_id) VALUES (?, ?)"
        cursor = self.db_service.execute_query(sql, (category_name, parent_id))
        return cursor.lastrowid if cursor else None

    def get_categories(self):
        sql = "SELECT * FROM Categories"
        categories = self.db_service.fetch_all_records(sql)
        logger.debug(f"Fetched {len(categories)} categories from database")
        if categories:
            logger.debug(f"Sample category: {categories[0]}")
        else:
            logger.debug("No categories found in the database")
        return categories

    def update_category(self, category_id, category_name, parent_id=None):
        sql = "UPDATE Categories SET category_name = ?, parent_id = ? WHERE id = ?"
        return self.db_service.execute_query(sql, (category_name, parent_id, category_id))

    def delete_category(self, category_id):
        sql = "DELETE FROM Categories WHERE id = ?"
        return self.db_service.execute_query(sql, (category_id,))

    def get_subcategories(self, parent_id):
        sql = "SELECT * FROM Categories WHERE parent_id = ?"
        return self.db_service.fetch_all_records(sql, (parent_id,))

    def delete_all_categories(self):
        sql = "DELETE FROM Categories"
        return self.db_service.execute_query(sql)
    
    def get_category_id(self, category_name):
        sql = "SELECT id FROM Categories WHERE name = ?"
        if result := self.db_service.execute_query(sql, (category_name,)):
            return result.fetchone()[0]
        return None