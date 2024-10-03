# src/controllers/database_modules/account_operations.py

class AccountOperations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Account operations
    def add_account(self, account_name, account_number, account_type):
        query = "INSERT INTO Accounts (account_name, account_number, account_type) VALUES (?, ?, ?)"
        self.db_manager.execute_query(query, (account_name, account_number, account_type))

    def get_accounts(self):
        query = "SELECT * FROM Accounts"
        return self.db_manager.fetch_all(query)

    def remove_account(self, account_name):
        query = "DELETE FROM Accounts WHERE account_name = ?"
        self.db_manager.execute_query(query, (account_name,))
