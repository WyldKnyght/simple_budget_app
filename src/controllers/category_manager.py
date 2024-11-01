from .services.category_service import CategoryService

class CategoryManager:
    def __init__(self):
        self.category_service = CategoryService()

    def create_category(self, category_name, parent_id=None):
        """
        Coordinate the creation of a new category.
        """
        return self.category_service.create_category(category_name, parent_id)

    def get_category_by_id(self, category_id):
        """
        Coordinate retrieving a category by its ID.
        """
        return self.category_service.get_category_by_id(category_id)

    def get_all_categories(self):
        """
        Coordinate retrieving all categories.
        """
        return self.category_service.get_all_categories()

    def update_category(self, category_id, category_name, parent_id=None):
        """
        Coordinate updating an existing category.
        """
        self.category_service.update_category(category_id, category_name, parent_id)

    def delete_category(self, category_id):
        """
        Coordinate deleting a category by its ID.
        """
        self.category_service.delete_category(category_id)

    def get_subcategories(self, parent_id):
        """
        Coordinate retrieving subcategories for a given parent category.
        """
        return self.category_service.get_subcategories(parent_id)