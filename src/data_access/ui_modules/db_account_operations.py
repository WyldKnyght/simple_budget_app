# src\data_access\db_account_operations.py
from ..database_manager import DatabaseManager
from configs.db_constants import (
    TABLE_ACCOUNTS, FIELD_ACCOUNT_ID, FIELD_ACCOUNT_NAME, 
    FIELD_ACCOUNT_NUMBER, FIELD_ACCOUNT_TYPE,
    SQL_INSERT_ACCOUNT, SQL_SELECT_ACCOUNT_BY_ID, SQL_SELECT_ALL_ACCOUNTS,
    SQL_UPDATE_ACCOUNT, SQL_DELETE_ACCOUNT
)

class AccountOperations:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def create_account(self, account_name, account_number, account_type):
        query = SQL_INSERT_ACCOUNT.format(
            table=TABLE_ACCOUNTS,
            name=FIELD_ACCOUNT_NAME,
            number=FIELD_ACCOUNT_NUMBER,
            type=FIELD_ACCOUNT_TYPE
        )
        params = (account_name, account_number, account_type)
        cursor = self.db_manager.execute_query(query, params)
        return cursor.lastrowid

    def get_account_by_id(self, account_id):
        query = SQL_SELECT_ACCOUNT_BY_ID.format(table=TABLE_ACCOUNTS, id=FIELD_ACCOUNT_ID)
        cursor = self.db_manager.execute_query(query, (account_id,))
        return cursor.fetchone()

    def get_all_accounts(self):
        query = SQL_SELECT_ALL_ACCOUNTS.format(table=TABLE_ACCOUNTS)
        cursor = self.db_manager.execute_query(query)
        return cursor.fetchall()

    def update_account(self, account_id, account_name, account_number, account_type):
        query = SQL_UPDATE_ACCOUNT.format(
            table=TABLE_ACCOUNTS,
            name=FIELD_ACCOUNT_NAME,
            number=FIELD_ACCOUNT_NUMBER,
            type=FIELD_ACCOUNT_TYPE,
            id=FIELD_ACCOUNT_ID
        )
        params = (account_name, account_number, account_type, account_id)
        self.db_manager.execute_query(query, params)

    def delete_account(self, account_id):
        query = SQL_DELETE_ACCOUNT.format(table=TABLE_ACCOUNTS, id=FIELD_ACCOUNT_ID)
        self.db_manager.execute_query(query, (account_id,))