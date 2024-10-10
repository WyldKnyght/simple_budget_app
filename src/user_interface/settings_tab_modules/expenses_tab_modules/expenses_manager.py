# src/user_interface/settings_tab_modules/expenses_tab_modules/expenses_manager.py
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt6.QtCore import Qt
from .expense_dialog import ExpenseDialog
from controllers.settings_tab_controllers.expenses_controller import ExpensesController

class ExpensesManager:
    def __init__(self, expenses_tab):
        self.expenses_tab = expenses_tab
        self.expenses_ops = ExpensesController

    def load_expenses(self):
        """Load and display all expenses in the table."""
        expenses = self.expenses_ops.get_expenses()
        self.expenses_tab.expenses_table.setRowCount(len(expenses))
        for row, expense in enumerate(expenses):
            for col, value in enumerate(expense[1:], start=1):  # Skip ID column
                item = QTableWidgetItem(str(value))
                item.setData(Qt.ItemDataRole.UserRole, expense[0])  # Store ID in UserRole
                self.expenses_tab.expenses_table.setItem(row, col, item)

    def add_expense(self):
        """Open a dialog to add a new expense."""
        dialog = ExpenseDialog(self, self.categories_ops.get_categories())
        if dialog.exec() == ExpenseDialog.DialogCode.Accepted:
            expense_data = dialog.get_expense_data()
            self.expenses_ops.add_expense(**expense_data)
            self.load_expenses()

    def edit_expense(self):
        """Open a dialog to edit the selected expense."""
        selected_rows = self.expenses_tab.expenses_table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "No Selection", "Please select an expense to edit.")
            return

        selected_row = selected_rows[0].row()
        expense_id = self.expenses_tab.expenses_table.item(selected_row, 0).data(Qt.ItemDataRole.UserRole)
        
        try:
            expense = self.expenses_ops.get_expense(expense_id)
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        dialog = ExpenseDialog(self, self.categories_ops.get_categories(), expense)
        if dialog.exec() == ExpenseDialog.DialogCode.Accepted:
            self.update_expense_from_dialog(dialog, expense)

    def remove_expense(self):
        """Remove the selected expense after confirmation."""
        selected_rows = self.expenses_tab.expenses_table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "No Selection", "Please select an expense to remove.")
            return

        selected_row = selected_rows[0].row()
        expense_id = self.expenses_tab.expenses_table.item(selected_row, 0).data(Qt.ItemDataRole.UserRole)

        confirm = QMessageBox.question(
            self,
            "Confirm Deletion",
            "Are you sure you want to delete this expense?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if confirm == QMessageBox.StandardButton.Yes:
            try:
                self.expenses_ops.remove_expense(expense_id)
                self.load_expenses()
            except ValueError as e:
                QMessageBox.critical(self, "Error", str(e))

    def update_expense_from_dialog(self, dialog, expense):
        """Update the expense with data from the dialog."""
        expense_data = dialog.get_expense_data()
        self.expenses_ops.update_expense(expense['id'], **expense_data)
        self.load_expenses()