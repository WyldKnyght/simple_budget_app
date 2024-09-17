# src/views/transactions_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from utils.custom_logging import logger

class TransactionsTab(QWidget):
    def __init__(self, model_manager):
        super().__init__()
        self.model_manager = model_manager
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        # Add your Transactions-related widgets here
        self.setLayout(layout)
        logger.info("Transactions tab UI initialized")