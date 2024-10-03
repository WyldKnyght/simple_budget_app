# src/user_interface/settings_tab_components/expenses_tab.py

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QPushButton, 
                             QHBoxLayout, QTableWidgetItem, QMessageBox)
from .expense_dialog import ExpenseDialog

class ExpensesTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.expenses_table = QTableWidget()
        self.expenses_table.setColumnCount(5)  # Reduced from 6 to 5
        self.expenses_table.setHorizontalHeaderLabels(["Expense Name", "Category", "Due Date", "Frequency", "Amount"])
        layout.addWidget(self.expenses_table)

        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Expense")
        self.edit_button = QPushButton("Edit Expense")
        self.remove_button = QPushButton("Remove Expense")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.remove_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_expense)
        self.edit_button.clicked.connect(self.edit_expense)
        self.remove_button.clicked.connect(self.remove_expense)

        self.load_expenses()

    def load_expenses(self):
        expenses = self.controller.get_expenses()
        self.expenses_table.setRowCount(len(expenses))
        for row, expense in enumerate(expenses):
            for col, value in enumerate(expense[1:]):  # Skip the first column (ID)
                self.expenses_table.setItem(row, col, QTableWidgetItem(str(value)))

    def add_expense(self):
        dialog = ExpenseDialog(self, self.controller.get_categories())
        if dialog.exec() == ExpenseDialog.DialogCode.Accepted:
            expense_name = dialog.name_input.text()
            category_id = dialog.category_input.currentData()
            due_date = dialog.due_date_input.date().toString("yyyy-MM-dd")
            frequency = dialog.frequency_input.currentText()
            amount = float(dialog.amount_input.text())
            
            self.controller.add_expense(expense_name, category_id, due_date, frequency, amount)
            self.load_expenses()

    def edit_expense(self):
        if not (
            selected_rows := self.expenses_table.selectionModel().selectedRows()
        ):
            return
        selected_row = selected_rows[0].row()
        expense_name = self.expenses_table.item(selected_row, 0).text()
        expense = self.controller.get_expense_by_name(expense_name)

        dialog = ExpenseDialog(self, self.controller.get_categories(), expense)
        if dialog.exec() == ExpenseDialog.DialogCode.Accepted:
            self._extracted_from_edit_expense_(dialog, expense)

    # TODO Rename this here and in `edit_expense`
    def _extracted_from_edit_expense_(self, dialog, expense):
        new_name = dialog.name_input.text()
        category_id = dialog.category_input.currentData()
        due_date = dialog.due_date_input.date().toString("yyyy-MM-dd")
        frequency = dialog.frequency_input.currentText()
        amount = float(dialog.amount_input.text())

        self.controller.update_expense(expense['id'], new_name, category_id, due_date, frequency, amount)
        self.load_expenses()

    def remove_expense(self):
        if selected_rows := self.expenses_table.selectionModel().selectedRows():
            selected_row = selected_rows[0].row()
            expense_name = self.expenses_table.item(selected_row, 0).text()

            confirm = QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to delete the expense '{expense_name}'?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                self.controller.remove_expense_by_name(expense_name)
                self.load_expenses()