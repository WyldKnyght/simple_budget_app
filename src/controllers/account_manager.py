# src\controllers\account_manager.py
from services.account_service import AccountService

class AccountManager:
    def __init__(self):
        self.account_service = AccountService()

    def create_account(self, account_name, account_number, account_type):
        """
        Coordinate the creation of a new account.
        """
        return self.account_service.create_account(account_name, account_number, account_type)

    def get_account_by_id(self, account_id):
        """
        Coordinate retrieving an account by its ID.
        """
        return self.account_service.get_account_by_id(account_id)

    def get_all_accounts(self):
        """
        Coordinate retrieving all accounts.
        """
        return self.account_service.get_all_accounts()

    def update_account(self, account_id, account_name, account_number, account_type):
        """
        Coordinate updating an existing account.
        """
        self.account_service.update_account(account_id, account_name, account_number, account_type)

    def delete_account(self, account_id):
        """
        Coordinate deleting an account by its ID.
        """
        self.account_service.delete_account(account_id)