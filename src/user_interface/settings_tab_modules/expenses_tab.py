# src/user_interface/settings_tab_modules/expenses_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView, QPushButton, QHBoxLayout
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from user_interface.settings_tab_modules.expenses_tab_modules.expenses_manager import ExpensesManager

class ExpensesTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.expenses_ops = self.db_manager.get_operation('expenses')
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.model = QStandardItemModel()
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        layout.addWidget(self.table_view)

        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Expense")
        self.edit_button = QPushButton("Edit Expense")
        self.delete_button = QPushButton("Delete Expense")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.load_expenses()

        # Initialize ExpensesManager
        self.expenses_manager = ExpensesManager(self)
        
        # Connect buttons to controller methods
        self.add_button.clicked.connect(self.expenses_manager.add_expense)
        self.edit_button.clicked.connect(self.expenses_manager.edit_expense)
        self.delete_button.clicked.connect(self.expenses_manager.remove_expense)

    def load_expenses(self):
        expenses = self.expenses_ops.get_expenses()
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["ID", "Name", "Category", "Due Date", "Frequency", "Amount"])
        for expense in expenses:
            row = [QStandardItem(str(item)) for item in expense]
            self.model.appendRow(row)
        self.table_view.hideColumn(0)  # Hide ID column