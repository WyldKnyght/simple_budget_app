# src/user_interface/settings_tab_modules/categories_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class CategoriesTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.categories_ops = self.db_manager.get_operation('categories')
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.model = QStandardItemModel()
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.setEditTriggers(QTreeView.EditTrigger.NoEditTriggers)
        layout.addWidget(self.tree_view)

        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Category")
        self.edit_button = QPushButton("Edit Category")
        self.delete_button = QPushButton("Delete Category")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.load_categories()

    def load_categories(self):
        categories = self.categories_ops.get_category_tree()
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["Category"])
        self.populate_tree(categories, self.model.invisibleRootItem())

    def populate_tree(self, categories, parent_item):
        for category in categories:
            item = QStandardItem(category['category_name'])
            item.setData(category['id'], Qt.ItemDataRole.UserRole)
            parent_item.appendRow(item)
            if 'subcategories' in category:
                self.populate_tree(category['subcategories'], item)