from .services.transaction_service import TransactionService

class TransactionManager:
    def __init__(self):
        self.transaction_service = TransactionService()

    def create_transaction(self, account_id, date, payee=None, memo=None,
                           category_id=None, payment=None,
                           deposit=None, account_balance=None,
                           note=None):
        """
        Coordinate the creation of a new transaction.
        """
        return self.transaction_service.create_transaction(
            account_id, date, payee, memo,
            category_id, payment,
            deposit, account_balance,
            note
        )

    def get_transaction_by_id(self, transaction_id):
        """
        Coordinate retrieving a transaction by its ID.
        """
        return self.transaction_service.get_transaction_by_id(transaction_id)

    def get_all_transactions(self):
        """
        Coordinate retrieving all transactions.
        """
        return self.transaction_service.get_all_transactions()

    def update_transaction(self, transaction_id, account_id, date, payee=None, memo=None,
                           category_id=None, payment=None, deposit=None,
                           account_balance=None, note=None):
        """
        Coordinate updating an existing transaction.
        """
        self.transaction_service.update_transaction(
            transaction_id, account_id, date, payee, memo,
            category_id, payment, deposit,
            account_balance, note
        )

    def delete_transaction(self, transaction_id):
        """
        Coordinate deleting a transaction by its ID.
        """
        self.transaction_service.delete_transaction(transaction_id)