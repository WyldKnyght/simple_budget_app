# src/user_interface/settings_tab_components/expense_dialog.py
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit, 
                             QComboBox, QPushButton, QDateEdit)
from PyQt6.QtCore import QDate
from configs.default_settings import DEFAULT_EXPENSE_FREQUENCIES

class ExpenseDialog(QDialog):
    def __init__(self, parent=None, categories=None, expense=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Expense")
        self.categories = categories or []
        self.expense = expense
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()

        self.name_input = QLineEdit()
        self.category_input = QComboBox()
        self.due_date_input = QDateEdit()
        self.due_date_input.setCalendarPopup(True)
        self.frequency_input = QComboBox()
        self.amount_input = QLineEdit()

        self.category_input.addItems([cat[1] for cat in self.categories])
        self.frequency_input.addItems(DEFAULT_EXPENSE_FREQUENCIES)

        layout.addRow("Expense Name:", self.name_input)
        layout.addRow("Category:", self.category_input)
        layout.addRow("Due Date:", self.due_date_input)
        layout.addRow("Frequency:", self.frequency_input)
        layout.addRow("Amount:", self.amount_input)

        button_layout = QVBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addRow(button_layout)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        if self.expense:
            self.populate_fields()

    def populate_fields(self):
        self.name_input.setText(self.expense['expense_name'])
        self.category_input.setCurrentIndex(self.category_input.findText(self.expense['category_name']))
        self.due_date_input.setDate(QDate.fromString(self.expense['due_date'], "yyyy-MM-dd"))
        self.frequency_input.setCurrentIndex(self.frequency_input.findText(self.expense['frequency']))
        self.amount_input.setText(str(self.expense['amount']))