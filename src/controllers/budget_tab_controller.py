# src/controllers/budget_tab_controller.py

from utils.custom_logging import logger

class BudgetTabController:
    def __init__(self, model_manager):
        self.model_manager = model_manager

    def get_all_accounts(self):
        accounts = self.model_manager.get_all_accounts()
        logger.info(f"Retrieved {len(accounts)} accounts.")
        return accounts

    def add_account(self, account_name, account_type):
        return self.model_manager.add_account(account_name, account_type)