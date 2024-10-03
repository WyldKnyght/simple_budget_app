# src/controllers/database_modules/category_operations.py

class CategoryOperations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Category operations
    def add_category(self, category_name, parent_id=None):
        query = "INSERT INTO Categories (category_name, parent_id) VALUES (?, ?)"
        self.db_manager.execute_query(query, (category_name, parent_id))
        return self.db_manager.cursor.lastrowid  # Return the ID of the newly inserted category

    def get_categories(self):
        query = "SELECT * FROM Categories"
        return self.db_manager.fetch_all(query)

    def remove_category(self, category_id):
        query = "DELETE FROM Categories WHERE id = ?"
        self.db_manager.execute_query(query, (category_id,))

    def update_category(self, category_id, category_name, parent_id=None):
        query = "UPDATE Categories SET category_name = ?, parent_id = ? WHERE id = ?"
        self.db_manager.execute_query(query, (category_name, parent_id, category_id))