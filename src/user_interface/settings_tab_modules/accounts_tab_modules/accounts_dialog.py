# src/user_interface/settings_tab_modules/accounts_tab_modules/accounts_dialog.py
from PyQt6.QtWidgets import (QPushButton, QHBoxLayout, QDialog, QFormLayout, QLineEdit)
from utils.custom_logging import logger, error_handler
from ...common.base_dialog import BaseDialog

class AccountDialog(BaseDialog):
    def __init__(self, parent=None, columns=None):
        super().__init__(parent, columns)
        self.setWindowTitle("Add/Edit Account")
        self.columns = columns
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        self.inputs = {}

        for column in self.columns:
            if column['name'] != 'id':
                if column['type'].upper() == 'VARCHAR':
                    self.inputs[column['name']] = QLineEdit()
                elif column['type'].upper() == 'TEXT':
                    self.inputs[column['name']] = QLineEdit()
                # Add more type checks as needed

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

    @error_handler
    def get_account_data(self):
        logger.info("Getting account data")
        return {name: input.text() for name, input in self.inputs.items()}