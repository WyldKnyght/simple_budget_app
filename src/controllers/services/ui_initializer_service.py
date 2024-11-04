from configs.ui_constants import (
    TAB_DASHBOARD, TAB_ACCOUNTS, TAB_CATEGORIES, TAB_TRANSACTIONS, TAB_EXPENSES, TAB_REPORTS
)

class UIInitializerService:
    @staticmethod
    def get_tab_structure():
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
        return "background-color: yellow; color: red;"