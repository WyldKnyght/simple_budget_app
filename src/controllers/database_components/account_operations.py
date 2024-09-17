# src/controllers/database_components/account_operations.py

class AccountOperations:
    def __init__(self, db_service):
        self.db_service = db_service

    def add_account(self, account_name, account_number, account_type):
        sql = "INSERT INTO Accounts (account_name, account_number, account_type) VALUES (?, ?, ?)"
        return self.db_service.execute_query(sql, (account_name, account_number, account_type))

    def get_accounts(self):
        return self.db_service.fetch_all_records("SELECT * FROM Accounts")

    def add_account_type(self, account_type):
        sql = "INSERT INTO AccountTypes (type_name) VALUES (?)"
        return self.db_service.execute_query(sql, (account_type,))

    def delete_all_account_types(self):
        sql = "DELETE FROM AccountTypes"
        return self.db_service.execute_query(sql)

    def get_account_types(self):
        return self.db_service.fetch_all_records("SELECT * FROM AccountTypes")