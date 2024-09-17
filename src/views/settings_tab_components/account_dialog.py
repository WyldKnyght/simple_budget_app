# src/views/settings_tab_components/account_dialogs.py
from PyQt6.QtWidgets import QDialog, QInputDialog, QFormLayout, QLineEdit, QComboBox, QPushButton, QHBoxLayout

class AccountDialog(QDialog):
    def __init__(self, account_types, add_account_type_callback):
        super().__init__()
        self.account_types = account_types
        self.add_account_type_callback = add_account_type_callback
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        self.name_input = QLineEdit()
        self.number_input = QLineEdit()
        self.type_input = QComboBox()
        self.type_input.addItems(self.account_types + ["Other"])
        self.type_input.currentTextChanged.connect(self.on_type_changed)
        
        layout.addRow("Account Name:", self.name_input)
        layout.addRow("Account Number:", self.number_input)
        layout.addRow("Account Type:", self.type_input)
        
        buttons = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        buttons.addWidget(ok_button)
        buttons.addWidget(cancel_button)
        
        layout.addRow(buttons)
        self.setLayout(layout)

    def on_type_changed(self, text):
        if text == "Other":
            new_type, ok = QInputDialog.getText(self, "Custom Account Type", "Enter new account type:")
            if ok and new_type:
                self.add_account_type_callback(new_type)
                self.type_input.removeItem(self.type_input.count() - 1)  # Remove "Other"
                self.type_input.addItem(new_type)
                self.type_input.addItem("Other")
                self.type_input.setCurrentText(new_type)

    def get_account_info(self):
        return self.name_input.text(), self.number_input.text(), self.type_input.currentText()
            
