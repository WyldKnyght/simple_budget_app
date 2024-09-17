# src/views/settings_tab_components/dialogs.py
from PyQt6.QtWidgets import QDialog, QFormLayout, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QDateEdit
from PyQt6.QtCore import QDate

class ExpenseDialog(QDialog):
    def __init__(self, categories, frequencies, common_expense_names):
        super().__init__()
        self.categories = categories
        self.frequencies = frequencies
        self.common_expense_names = common_expense_names
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        
        self.name_input = QComboBox()
        self.name_input.setEditable(True)
        self.name_input.addItems(self.common_expense_names)
        
        self.category_input = QComboBox()
        self.category_input.addItems([cat[1] for cat in self.categories])
        
        self.due_date_input = QDateEdit()
        self.due_date_input.setDate(QDate.currentDate())
        
        self.frequency_input = QComboBox()
        self.frequency_input.addItems(self.frequencies)
        
        self.amount_input = QLineEdit()
        
        layout.addRow("Expense Name:", self.name_input)
        layout.addRow("Category:", self.category_input)
        layout.addRow("Due Date:", self.due_date_input)
        layout.addRow("Frequency:", self.frequency_input)
        layout.addRow("Amount:", self.amount_input)
        
        buttons = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        buttons.addWidget(ok_button)
        buttons.addWidget(cancel_button)
        
        layout.addRow(buttons)
        self.setLayout(layout)

    def get_expense_info(self):
        category_id = self.categories[self.category_input.currentIndex()][0]
        return (
            self.name_input.currentText(),
            category_id,
            self.due_date_input.date().toString("yyyy-MM-dd"),
            self.frequency_input.currentText(),
            float(self.amount_input.text())
        )