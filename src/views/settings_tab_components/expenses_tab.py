# src/views/settings_tab_components/expenses_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from .expense_dialog import ExpenseDialog

class ExpensesTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller.expense  # Now points directly to ExpenseMethod
        self.category_controller = controller.category  # We need this for getting categories
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.expenses_table = QTableWidget()
        self.expenses_table.setColumnCount(6)
        self.expenses_table.setHorizontalHeaderLabels(["ID", "Expense Name", "Category", "Due Date", "Frequency", "Amount"])
        
        add_button = QPushButton("Add Expense")
        add_button.clicked.connect(self.add_expense)
        
        layout.addWidget(self.expenses_table)
        layout.addWidget(add_button)
        self.setLayout(layout)
        
        self.load_expenses()

    def load_expenses(self):
        expenses = self.controller.get_expenses()
        self.expenses_table.setRowCount(len(expenses))
        for row, expense in enumerate(expenses):
            self.expenses_table.setItem(row, 0, QTableWidgetItem(str(expense[0])))
            self.expenses_table.setItem(row, 1, QTableWidgetItem(expense[1]))
            self.expenses_table.setItem(row, 2, QTableWidgetItem(str(expense[2])))
            self.expenses_table.setItem(row, 3, QTableWidgetItem(expense[3]))
            self.expenses_table.setItem(row, 4, QTableWidgetItem(expense[4]))
            self.expenses_table.setItem(row, 5, QTableWidgetItem(str(expense[5])))

    def add_expense(self):
        dialog = ExpenseDialog(
            self.category_controller.get_categories(),
            self.controller.get_expense_frequencies(),
            self.controller.get_common_expense_names()
        )
        if dialog.exec():
            expense_info = dialog.get_expense_info()
            self.controller.add_expense(*expense_info)
            self.load_expenses()