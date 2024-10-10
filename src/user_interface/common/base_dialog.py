# src/user_interface/common/base_dialog.py
from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QHBoxLayout

class BaseDialog(QDialog):
    def __init__(self, parent=None, columns=None):
        super().__init__(parent)
        self.columns = columns or []
        self.inputs = {}
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        for column in self.columns:
            if column['name'] != 'id':
                self.inputs[column['name']] = QLineEdit()
                layout.addRow(f"{column['name'].capitalize()}:", self.inputs[column['name']])

        buttons = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        buttons.addWidget(self.ok_button)
        buttons.addWidget(self.cancel_button)

        layout.addRow(buttons)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_data(self):
        return {name: input.text() for name, input in self.inputs.items()}