# src/user_interface/settings_tab_modules/expenses_tab_modules/expense_dialog.py
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit, 
                             QComboBox, QPushButton, QDateEdit, QDoubleSpinBox, QMessageBox)
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
        self.name_input.setPlaceholderText("Enter expense name")

        self.category_input = QComboBox()
        self.category_input.addItems([cat[1] for cat in self.categories])

        self.due_date_input = QDateEdit()
        self.due_date_input.setCalendarPopup(True)
        self.due_date_input.setDate(QDate.currentDate())  # Set default to today

        self.frequency_input = QComboBox()
        self.frequency_input.addItems(DEFAULT_EXPENSE_FREQUENCIES)

        self.amount_input = QDoubleSpinBox()
        self.amount_input.setRange(0, 1000000)
        self.amount_input.setDecimals(2)
        self.amount_input.setPrefix("$")

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

        self.ok_button.clicked.connect(self.validate_and_accept)
        self.cancel_button.clicked.connect(self.reject)

        if self.expense:
            self.populate_fields()

    def populate_fields(self):
        self.name_input.setText(self.expense['expense_name'])
        self.category_input.setCurrentIndex(self.category_input.findText(self.expense['category_name']))
        self.due_date_input.setDate(QDate.fromString(self.expense['due_date'], "yyyy-MM-dd"))
        self.frequency_input.setCurrentIndex(self.frequency_input.findText(self.expense['frequency']))
        self.amount_input.setValue(float(self.expense['amount']))

    def validate_and_accept(self):
        if not self.name_input.text():
            QMessageBox.warning(self, "Invalid Input", "Please enter an expense name.")
            return
        if self.amount_input.value() == 0:
            QMessageBox.warning(self, "Invalid Input", "Please enter a non-zero amount.")
            return
        self.accept()

    def get_expense_data(self):
        return {
            'expense_name': self.name_input.text(),
            'category_id': self.categories[self.category_input.currentIndex()][0],
            'category_name': self.category_input.currentText(),
            'due_date': self.due_date_input.date().toString("yyyy-MM-dd"),
            'frequency': self.frequency_input.currentText(),
            'amount': self.amount_input.value()
        }