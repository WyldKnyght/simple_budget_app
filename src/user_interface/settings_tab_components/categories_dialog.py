# src/user_interface/settings_tab_components/categories_dialog.py
from PyQt6.QtWidgets import (QPushButton, 
                             QHBoxLayout, QDialog, QFormLayout, 
                             QLineEdit, QComboBox)
from controllers.database_controllers import db_manager

class CategoryDialog(QDialog):
    def __init__(self, parent=None, category_name=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Category")
        layout = QFormLayout()

        self.name_input = QLineEdit()
        if category_name:
            self.name_input.setText(category_name)

        self.parent_input = QComboBox()
        self.parent_input.addItem("None", None)
        categories = db_manager.get_categories()
        for cat_id, cat_name, _ in categories:
            self.parent_input.addItem(cat_name, cat_id)

        layout.addRow("Category Name:", self.name_input)
        layout.addRow("Parent Category:", self.parent_input)

        buttons = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        buttons.addWidget(self.ok_button)
        buttons.addWidget(self.cancel_button)

        layout.addRow(buttons)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)