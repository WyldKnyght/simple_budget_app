# src/views/budget_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from utils.custom_logging import logger

class BudgetTab(QWidget):
    def __init__(self, model_manager):
        super().__init__()
        self.model_manager = model_manager
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        # Add your budget-related widgets here
        self.setLayout(layout)
        logger.info("Budget tab UI initialized")