# src/controllers/services/category_service.py
from data_access.db_category_operations import CategoryOperations
from data_access.schema_manager import SchemaManager
from configs.db_constants import TABLE_CATEGORIES, FIELD_CATEGORY_NAME
from utils.custom_logging import error_handler

class CategoryService:
    def __init__(self):
        self.category_operations = CategoryOperations()
        self.schema_manager = SchemaManager()

    @error_handler
    def create_category(self, category_name, parent_id=None):
        """
        Create a new category after validating the input data.
        """
        self._validate_category_data(category_name)
        return self.category_operations.create_category(category_name, parent_id)

    @error_handler
    def get_category_by_id(self, category_id):
        """
        Retrieve a category by its ID.
        """
        return self.category_operations.get_category_by_id(category_id)

    @error_handler
    def get_all_categories(self):
        """
        Retrieve all categories.
        """
        return self.category_operations.get_all_categories()

    @error_handler
    def update_category(self, category_id, category_name, parent_id=None):
        """
        Update an existing category after validating the input data.
        """
        self._validate_category_data(category_name)
        self.category_operations.update_category(category_id, category_name, parent_id)

    @error_handler
    def delete_category(self, category_id):
        """
        Delete a category by its ID.
        """
        self.category_operations.delete_category(category_id)

    @error_handler
    def get_subcategories(self, parent_id):
        """
        Retrieve all subcategories for a given parent category.
        """
        return self.category_operations.get_subcategories(parent_id)

    def _validate_category_data(self, category_name):
        """
        Validate category data before creating or updating a category.
        """
        if not category_name:
            raise ValueError("Category name is required")
        
        # Additional validation can be added here if needed