# src/user_interface/settings_tab_modules/categories_tab_modules/categories_dialog.py

from PyQt6.QtWidgets import (QPushButton, QHBoxLayout, QDialog, QFormLayout, 
                             QLineEdit, QComboBox)

class CategoryDialog(QDialog):
    def __init__(self, parent=None, columns=None, category_data=None, parent_categories=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Category")
        self.columns = columns or []
        self.category_data = category_data or {}
        self.parent_categories = parent_categories or []
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        self.inputs = {}

        for column in self.columns:
            if column['name'] not in ['id', 'parent_id']:
                if column['type'].upper() in ['VARCHAR', 'TEXT']:
                    self.inputs[column['name']] = QLineEdit()
                    if self.category_data:
                        self.inputs[column['name']].setText(str(self.category_data.get(column['name'], '')))
                # Add more type checks as needed
                layout.addRow(f"{column['name'].capitalize()}:", self.inputs[column['name']])

        self.parent_input = QComboBox()
        self.parent_input.addItem("None", None)
        for parent in self.parent_categories:
            self.parent_input.addItem(parent['name'], parent['id'])
        if self.category_data and 'parent_id' in self.category_data:
            index = self.parent_input.findData(self.category_data['parent_id'])
            if index >= 0:
                self.parent_input.setCurrentIndex(index)
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

    def get_category_data(self):
        data = {name: input.text() for name, input in self.inputs.items()}
        data['parent_id'] = self.parent_input.currentData()
        return data