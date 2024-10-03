# src/user_interface/transactions_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QPushButton, QHBoxLayout, QTableWidgetItem
from controllers.settings_tab_controller import SettingsTabController

class TransactionsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = SettingsTabController()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.transactions_table = QTableWidget()
        layout.addWidget(self.transactions_table)

        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Transaction")
        self.edit_button = QPushButton("Edit Transaction")
        self.delete_button = QPushButton("Delete Transaction")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_transaction)
        self.edit_button.clicked.connect(self.edit_transaction)
        self.delete_button.clicked.connect(self.delete_transaction)

        self.load_transactions()

    def load_transactions(self):
        # Clear existing data
        self.transactions_table.clear()
        
        # Set up table headers
        self.transactions_table.setColumnCount(7)
        self.transactions_table.setHorizontalHeaderLabels([
            "ID", "Account", "Date", "Payee", "Category", "Payment", "Deposit"
        ])

        # Fetch transactions from the database
        transactions = self.controller.get_transactions()

        # Populate the table with transaction data
        self.transactions_table.setRowCount(len(transactions))
        for row, transaction in enumerate(transactions):
            for col, value in enumerate(transaction):
                self.transactions_table.setItem(row, col, QTableWidgetItem(str(value)))

        # Resize columns to content
        self.transactions_table.resizeColumnsToContents()

    def add_transaction(self):
        # Implement add transaction logic
        # For now, just refresh the transactions
        self.load_transactions()

    def edit_transaction(self):
        # Implement edit transaction logic
        # For now, just refresh the transactions
        self.load_transactions()

    def delete_transaction(self):
        # Implement delete transaction logic
        # For now, just refresh the transactions
        self.load_transactions()