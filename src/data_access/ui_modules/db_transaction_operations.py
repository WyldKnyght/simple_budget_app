from ..database_manager import DatabaseManager
from configs.db_constants import (
    TABLE_TRANSACTIONS, FIELD_TRANSACTION_ID, FIELD_ACCOUNT_ID, FIELD_DATE,
    FIELD_PAYEE, FIELD_MEMO, FIELD_CATEGORY_ID, FIELD_PAYMENT, FIELD_DEPOSIT,
    FIELD_ACCOUNT_BALANCE, FIELD_NOTE,
    SQL_INSERT_TRANSACTION, SQL_SELECT_TRANSACTION_BY_ID,
    SQL_SELECT_ALL_TRANSACTIONS, SQL_UPDATE_TRANSACTION, SQL_DELETE_TRANSACTION
)

class TransactionOperations:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def create_transaction(self, account_id, date, payee, memo, category_id, payment, deposit, account_balance, note):
        query = SQL_INSERT_TRANSACTION.format(
            table=TABLE_TRANSACTIONS,
            account_id=FIELD_ACCOUNT_ID,
            date=FIELD_DATE,
            payee=FIELD_PAYEE,
            memo=FIELD_MEMO,
            category_id=FIELD_CATEGORY_ID,
            payment=FIELD_PAYMENT,
            deposit=FIELD_DEPOSIT,
            account_balance=FIELD_ACCOUNT_BALANCE,
            note=FIELD_NOTE
        )
        params = (account_id, date, payee, memo, category_id, payment, deposit, account_balance, note)
        cursor = self.db_manager.execute_query(query, params)
        return cursor.lastrowid

    def get_transaction_by_id(self, transaction_id):
        query = SQL_SELECT_TRANSACTION_BY_ID.format(table=TABLE_TRANSACTIONS, id=FIELD_TRANSACTION_ID)
        cursor = self.db_manager.execute_query(query, (transaction_id,))
        return cursor.fetchone()

    def get_all_transactions(self):
        query = SQL_SELECT_ALL_TRANSACTIONS.format(table=TABLE_TRANSACTIONS)
        cursor = self.db_manager.execute_query(query)
        return cursor.fetchall()

    def update_transaction(self, transaction_id, account_id, date, payee, memo, category_id, payment, deposit, account_balance, note):
        query = SQL_UPDATE_TRANSACTION.format(
            table=TABLE_TRANSACTIONS,
            account_id=FIELD_ACCOUNT_ID,
            date=FIELD_DATE,
            payee=FIELD_PAYEE,
            memo=FIELD_MEMO,
            category_id=FIELD_CATEGORY_ID,
            payment=FIELD_PAYMENT,
            deposit=FIELD_DEPOSIT,
            account_balance=FIELD_ACCOUNT_BALANCE,
            note=FIELD_NOTE,
            id=FIELD_TRANSACTION_ID
        )
        params = (account_id, date, payee, memo, category_id, payment, deposit, account_balance, note, transaction_id)
        self.db_manager.execute_query(query, params)

    def delete_transaction(self, transaction_id):
        query = SQL_DELETE_TRANSACTION.format(table=TABLE_TRANSACTIONS, id=FIELD_TRANSACTION_ID)
        self.db_manager.execute_query(query, (transaction_id,))