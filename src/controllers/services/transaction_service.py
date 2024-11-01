# src/controllers/services/transaction_service.py
from data_access.db_transaction_operations import TransactionOperations
from data_access.schema_manager import SchemaManager
from configs.constants import TABLE_TRANSACTIONS
from utils.custom_logging import error_handler

class TransactionService:
    def __init__(self):
        self.transaction_operations = TransactionOperations()
        self.schema_manager = SchemaManager()

    @error_handler
    def create_transaction(self, account_id, date, payee=None, memo=None,
                           category_id=None, payment=None,
                           deposit=None, account_balance=None,
                           note=None):
        """
        Create a new transaction after validating the input data.
        """
        self._validate_transaction_data(account_id)
        return self.transaction_operations.create_transaction(
            account_id, date, payee or "", memo or "", category_id or None,
            payment or 0.0, deposit or 0.0,
            account_balance or 0.0,note or ""
        )

    @error_handler
    def get_transaction_by_id(self, transaction_id):
        """
        Retrieve a transaction by its ID.
        """
        return self.transaction_operations.get_transaction_by_id(transaction_id)

    @error_handler
    def get_all_transactions(self):
        """
        Retrieve all transactions.
        """
        return self.transaction_operations.get_all_transactions()

    @error_handler
    def update_transaction(self, transaction_id, account_id,date,payee=None,memo=None,
                           category_id=None,payment=None,deposit=None,
                           account_balance=None,note=None):
        """
        Update an existing transaction after validating the input data.
        """
        self._validate_transaction_data(account_id)
        self.transaction_operations.update_transaction(
            transaction_id ,account_id ,date ,payee or "" ,memo or "" ,
            category_id or None ,payment or 0.0 ,deposit or 0.0 ,
            account_balance or 0.0 ,note or ""
       )

    @error_handler
    def delete_transaction(self ,transaction_id):
       """
       Delete a transaction by its ID.
       """
       self.transaction_operations.delete_transaction(transaction_id)

    def _validate_transaction_data(self ,account_id):
       """
       Validate transaction data before creating or updating a transaction.
       """
       if not account_id:
           raise ValueError("Account ID is required")
       
       # Additional validation can be added here if needed