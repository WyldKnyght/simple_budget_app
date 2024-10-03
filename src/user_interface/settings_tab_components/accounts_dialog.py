# src/user_interface/settings_tab_components/accounts_dialog.py

from PyQt6.QtWidgets import (QPushButton, 
                                QHBoxLayout, QDialog, QFormLayout, 
                                QLineEdit, QComboBox)
from configs.default_settings import DEFAULT_ACCOUNT_TYPES

class AccountDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Account")
        layout = QFormLayout()

        self.name_input = QLineEdit()
        self.number_input = QLineEdit()
        self.type_input = QComboBox()
        self.type_input.addItems(DEFAULT_ACCOUNT_TYPES)

        layout.addRow("Account Name:", self.name_input)
        layout.addRow("Account Number:", self.number_input)
        layout.addRow("Account Type:", self.type_input)

        buttons = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        buttons.addWidget(self.ok_button)
        buttons.addWidget(self.cancel_button)

        layout.addRow(buttons)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)