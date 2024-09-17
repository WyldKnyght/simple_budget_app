# src/views/settings_tab_components/categories_tab.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QMessageBox,
                             QPushButton, QHBoxLayout, QInputDialog)
from utils.custom_logging import logger

class CategoriesTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller.category
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.categories_tree = QTreeWidget()
        self.categories_tree.setHeaderLabels(["Category"])
        
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add Category")
        add_button.clicked.connect(self.add_category)
        edit_button = QPushButton("Edit Category")
        edit_button.clicked.connect(self.edit_category)
        delete_button = QPushButton("Delete Category")
        delete_button.clicked.connect(self.delete_category)
        
        button_layout.addWidget(add_button)
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        
        layout.addWidget(self.categories_tree)
        layout.addLayout(button_layout)
        self.setLayout(layout)
        
        self.load_categories()

    def load_categories(self):
        self.categories_tree.clear()
        categories = self.controller.get_category_tree()
        logger.debug(f"Loaded category tree with {len(categories)} top-level categories")
        for category in categories:
            self._add_category_to_tree(self.categories_tree.invisibleRootItem(), category)
        logger.debug(f"Categories loaded into tree widget. Total items: {self.categories_tree.topLevelItemCount()}")

    def _add_category_to_tree(self, parent, category):
        item = QTreeWidgetItem(parent, [category['name']])
        item.setData(0, 100, category['id'])
        logger.debug(f"Added category to tree: {category['name']} (ID: {category['id']})")
        for subcategory in category.get('subcategories', []):
            self._add_category_to_tree(item, subcategory)

    def add_category(self):
        name, ok = QInputDialog.getText(self, "Add Category", "Enter category name:")
        if ok and name:
            parent_item = self.categories_tree.currentItem()
            parent_id = parent_item.data(0, 100) if parent_item else None
            if new_id := self.controller.add_category(name, parent_id):
                # Add the new category to the tree without reloading all categories
                new_item = QTreeWidgetItem([name])
                new_item.setData(0, 100, new_id)
                if parent_item:
                    parent_item.addChild(new_item)
                else:
                    self.categories_tree.addTopLevelItem(new_item)
                # Expand the parent item if it exists
                if parent_item:
                    parent_item.setExpanded(True)
            else:
                # Handle the case where adding the category failed
                QMessageBox.warning(self, "Error", "Failed to add new category.")

    def edit_category(self):
        if item := self.categories_tree.currentItem():
            category_id = item.data(0, 100)
            name, ok = QInputDialog.getText(self, "Edit Category", "Enter new category name:", text=item.text(0))
            if ok and name:
                parent_item = item.parent()
                parent_id = parent_item.data(0, 100) if parent_item else None
                self.controller.update_category(category_id, name, parent_id)
                self.load_categories()

    def delete_category(self):
        if item := self.categories_tree.currentItem():
            category_id = item.data(0, 100)
            self.controller.delete_category(category_id)
            self.load_categories()