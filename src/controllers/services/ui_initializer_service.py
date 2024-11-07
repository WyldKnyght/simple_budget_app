from PyQt6.QtWidgets import QWidget, QVBoxLayout
from configs.ui_constants import (
    TAB_DASHBOARD, TAB_ACCOUNTS, TAB_CATEGORIES, TAB_TRANSACTIONS, TAB_EXPENSES, TAB_REPORTS
)
from utils.custom_logging import logger

class UIInitializerService:
    @staticmethod
    def get_tab_structure():
        logger.info("Getting tab structure...")
        return [
            TAB_DASHBOARD,
            TAB_ACCOUNTS,
            TAB_CATEGORIES,
            TAB_TRANSACTIONS,
            TAB_EXPENSES,
            TAB_REPORTS
        ]

    @staticmethod
    def get_warning_label_style():
        logger.info("Getting warning label style...")
        return "background-color: yellow; color: red;"

    @staticmethod
    def create_placeholder_tab():
        logger.info("Creating placeholder tab...")
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QWidget())
        tab.setLayout(layout)
        return tab