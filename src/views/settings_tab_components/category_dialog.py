# src/views/settings_tab_components/dialogs.py
from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QHBoxLayout

class CategoryDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        self.name_input = QLineEdit()
        self.sub_name_input = QLineEdit()
        
        layout.addRow("Category Name:", self.name_input)
        layout.addRow("Sub-Category Name:", self.sub_name_input)
        
        buttons = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        buttons.addWidget(ok_button)
        buttons.addWidget(cancel_button)
        
        layout.addRow(buttons)
        self.setLayout(layout)

    def get_category_info(self):
        return self.name_input.text(), self.sub_name_input.text()

