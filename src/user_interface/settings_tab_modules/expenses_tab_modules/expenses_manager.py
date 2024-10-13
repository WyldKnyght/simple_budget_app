# src/user_interface/settings_tab_modules/expenses_tab_modules/expenses_manager.py
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QStandardItem
from .expense_dialog import ExpenseDialog
from utils.custom_logging import logger, error_handler
from configs.constants import EXPENSE_TABLE_HEADERS

class ExpensesManager:
    def __init__(self, expenses_tab, expenses_controller):
        self.expenses_tab = expenses_tab
        self.controller = expenses_controller

    @error_handler
    def load_expenses(self, model, table_view):
        logger.info("Loading expenses")
        expenses = self.controller.get_expenses()
        model.clear()
        model.setHorizontalHeaderLabels(EXPENSE_TABLE_HEADERS)
        for expense in expenses:
            row = [QStandardItem(str(item)) for item in expense]
            model.appendRow(row)
        table_view.hideColumn(0)  # Hide ID column

    @error_handler
    def add_expense(self):
        logger.info("Adding new expense")
        categories = self.controller.get_categories()
        dialog = ExpenseDialog(self.expenses_tab, categories)
        if dialog.exec() == ExpenseDialog.DialogCode.Accepted:
            expense_data = dialog.get_expense_data()
            self.controller.add_expense(**expense_data)
            self.load_expenses(self.expenses_tab.model, self.expenses_tab.table_view)

    @error_handler
    def edit_expense(self):
        logger.info("Editing expense")
        selected_rows = self.expenses_tab.table_view.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self.expenses_tab, "No Selection", "Please select an expense to edit.")
            return

        selected_row = selected_rows[0].row()
        expense_id = self.expenses_tab.model.item(selected_row, 0).text()
        
        expense = self.controller.get_expense(expense_id)
        categories = self.controller.get_categories()
        dialog = ExpenseDialog(self.expenses_tab, categories, expense)
        if dialog.exec() == ExpenseDialog.DialogCode.Accepted:
            expense_data = dialog.get_expense_data()
            self.controller.update_expense(expense_id, **expense_data)
            self.load_expenses(self.expenses_tab.model, self.expenses_tab.table_view)

    @error_handler
    def remove_expense(self):
        logger.info("Removing expense")
        selected_rows = self.expenses_tab.table_view.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self.expenses_tab, "No Selection", "Please select an expense to remove.")
            return

        selected_row = selected_rows[0].row()
        expense_id = self.expenses_tab.model.item(selected_row, 0).text()
        expense_name = self.expenses_tab.model.item(selected_row, 1).text()

        confirm = QMessageBox.question(
            self.expenses_tab,
            "Confirm Deletion",
            f"Are you sure you want to delete the expense '{expense_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if confirm == QMessageBox.StandardButton.Yes:
            self.controller.remove_expense(expense_id)
            self.load_expenses(self.expenses_tab.model, self.expenses_tab.table_view)