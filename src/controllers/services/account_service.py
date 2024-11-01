# src/controllers/services/account_service.py
from data_access.db_account_operations import AccountOperations
from data_access.schema_manager import SchemaManager
from configs.constants import TABLE_ACCOUNTS, FIELD_ACCOUNT_TYPE
from utils.custom_logging import error_handler

class AccountService:
    def __init__(self):
        self.account_operations = AccountOperations()
        self.schema_manager = SchemaManager()

    @error_handler
    def create_account(self, account_name, account_number, account_type):
        """
        Create a new account after validating the input data.
        """
        self._validate_account_data(account_name, account_number, account_type)
        return self.account_operations.create_account(account_name, account_number, account_type)

    @error_handler
    def get_account_by_id(self, account_id):
        """
        Retrieve an account by its ID.
        """
        return self.account_operations.get_account_by_id(account_id)

    @error_handler
    def get_all_accounts(self):
        """
        Retrieve all accounts.
        """
        return self.account_operations.get_all_accounts()

    @error_handler
    def update_account(self, account_id, account_name, account_number, account_type):
        """
        Update an existing account after validating the input data.
        """
        self._validate_account_data(account_name, account_number, account_type)
        self.account_operations.update_account(account_id, account_name, account_number, account_type)

    @error_handler
    def delete_account(self, account_id):
        """
        Delete an account by its ID.
        """
        self.account_operations.delete_account(account_id)

    def _validate_account_data(self, account_name, account_number, account_type):
        """
        Validate account data before creating or updating an account.
        """
        if not account_name or not account_number or not account_type:
            raise ValueError("All fields (account_name, account_number, account_type) are required")
        
        allowed_types = self.schema_manager.get_allowed_values(TABLE_ACCOUNTS, FIELD_ACCOUNT_TYPE)
        if allowed_types and account_type not in allowed_types:
            raise ValueError(f"Invalid account type. Allowed types are: {', '.join(allowed_types)}")