# src/user_interface/settings_tab_modules/categories_tab_modules/categories_manager.py
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from .categories_dialog import CategoryDialog
from .categories_model import CategoriesModel
from utils.custom_logging import logger, error_handler

class CategoriesManager:
    def __init__(self, categories_tab, categories_controller):
        self.categories_tab = categories_tab
        self.controller = categories_controller
        self.model = None

    @error_handler
    def load_categories(self, tree_view):
        logger.info("Loading categories")
        categories = self.controller.get_category_tree()
        self.model = CategoriesModel(categories, self.controller.columns)
        tree_view.setModel(self.model)
        tree_view.setHeaderHidden(False)

    @error_handler
    def add_category(self):
        logger.info("Adding new category")
        parent_categories = self.controller.get_entities()
        dialog = CategoryDialog(self.categories_tab, self.controller.columns, parent_categories=parent_categories)
        if dialog.exec() == CategoryDialog.DialogCode.Accepted:
            category_data = dialog.get_category_data()
            self.controller.add_entity(category_data)
            self.load_categories(self.categories_tab.tree_view)

    @error_handler
    def edit_category(self):
        logger.info("Editing category")
        index = self.categories_tab.tree_view.currentIndex()
        if index.isValid():
            category_id = self.model.getCategoryId(index)
            current_data = self.controller.get_entity(category_id)
            parent_categories = self.controller.get_entities()
            dialog = CategoryDialog(self.categories_tab, self.controller.columns, current_data, parent_categories)
            if dialog.exec() == CategoryDialog.DialogCode.Accepted:
                category_data = dialog.get_category_data()
                self.controller.update_entity(category_id, category_data)
                self.load_categories(self.categories_tab.tree_view)

    @error_handler
    def delete_category(self):
        logger.info("Deleting category")
        index = self.categories_tab.tree_view.currentIndex()
        if index.isValid():
            category_id = self.model.getCategoryId(index)
            category_name = self.model.data(index, Qt.ItemDataRole.DisplayRole)
            confirm = QMessageBox.question(self.categories_tab, "Confirm Deletion", 
                                           f"Are you sure you want to delete the category '{category_name}'?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.controller.remove_entity(category_id)
                self.load_categories(self.categories_tab.tree_view)