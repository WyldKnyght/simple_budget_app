# src/controllers/transactions_tab_controller.py
class TransactionsTabController:
    def __init__(self, model_manager):
        self.model_manager = model_manager

    def add_transaction(self, account_id, date, payee, memo, category_id, payment, deposit):
        return self.model_manager.add_transaction(account_id, date, payee, memo, category_id, payment, deposit)

    def get_transactions(self, account_id=None, start_date=None, end_date=None):
        return self.model_manager.get_transactions(account_id, start_date, end_date)

    # Add other transaction-related methods as needed