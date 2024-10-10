# src/user_interface/settings_tab_modules/categories_tab_modules/categories_manager.py

from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from .categories_dialog import CategoryDialog
from controllers.db_operations.database_manager import DatabaseManager
from utils.custom_logging import logger, error_handler
from .categories_model import CategoriesModel

class CategoriesManager:
    def __init__(self, categories_tab):
        self.categories_tab = categories_tab
        self.db_manager = DatabaseManager
        self.model = None

    def _get_categories(self):
        categories_operations = self.db_manager.get_operation('categories')
        return categories_operations.get_category_tree()

    @error_handler
    def load_categories(self, categories_view):
        logger.info("Loading categories")
        try:
            categories = self._get_categories()
            self.model = CategoriesModel(categories, self.db_manager.get_operation('categories').columns)
            categories_view.setModel(self.model)
        except Exception as e:
            logger.error(f"Failed to load categories: {str(e)}")

    @error_handler
    def add_category(self):
        logger.info("Adding new category")
        parent_categories = self.categories_operations.get_categories()
        dialog = CategoryDialog(self, self.categories_operations.columns, parent_categories=parent_categories)
        if dialog.exec() == CategoryDialog.DialogCode.Accepted:
            category_data = dialog.get_category_data()
            try:
                self.categories_operations.add_category(**category_data)
                self.load_categories()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to add new category: {str(e)}")

    @error_handler
    def edit_category(self):
        logger.info("Editing category")
        index = self.categories_view.currentIndex()
        if index.isValid():
            category_id = self.model.getCategoryId(index)
            try:
                current_data = self.categories_operations.get_category(category_id)
                parent_categories = self.categories_operations.get_categories()
                dialog = CategoryDialog(self, self.categories_operations.columns, current_data, parent_categories)
                if dialog.exec() == CategoryDialog.DialogCode.Accepted:
                    category_data = dialog.get_category_data()
                    self.categories_operations.update_category(category_id, **category_data)
                    self.load_categories()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to update category: {str(e)}")

    @error_handler
    def delete_category(self):
        logger.info("Deleting category")
        index = self.categories_view.currentIndex()
        if index.isValid():
            category_id = self.model.getCategoryId(index)
            category_name = self.model.data(index, Qt.ItemDataRole.DisplayRole)
            confirm = QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to delete the category '{category_name}'?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                try:
                    self.categories_operations.remove_category(category_id)
                    self.load_categories()
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Failed to delete category: {str(e)}")