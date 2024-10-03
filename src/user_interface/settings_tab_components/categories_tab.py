# src/user_interface/settings_tab_components/categories_tab.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QMessageBox,
                             QPushButton, QHBoxLayout, QInputDialog)

class CategoriesTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
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
        categories = self.controller.get_categories()
        category_dict = {cat[0]: (cat[1], cat[2], QTreeWidgetItem()) for cat in categories}
        
        for cat_id, (cat_name, parent_id, item) in category_dict.items():
            item.setText(0, cat_name)
            item.setData(0, 100, cat_id)
            if parent_id is None:
                self.categories_tree.addTopLevelItem(item)
            else:
                category_dict[parent_id][2].addChild(item)

    def add_category(self):
        name, ok = QInputDialog.getText(self, "Add Category", "Enter category name:")
        if ok and name:
            parent_item = self.categories_tree.currentItem()
            parent_id = parent_item.data(0, 100) if parent_item else None
            try:
                self.controller.add_category(name, parent_id)
                self.load_categories()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to add new category: {str(e)}")

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
            confirm = QMessageBox.question(self, "Confirm Deletion", "Are you sure you want to delete this category?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.controller.remove_category(category_id)
                self.load_categories()