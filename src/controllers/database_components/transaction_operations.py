# src/controllers/database_components/transaction_operations.py
class TransactionOperations:
    def __init__(self, db_controller):
        self.db_controller = db_controller

    def add_transaction(self, account_id, date, payee, memo, category_id, payment, deposit, account_balance):
        sql = """
        INSERT INTO Transactions (account_id, date, payee, memo, category_id, payment, deposit, account_balance)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        return self.db_controller.execute_query(sql, (account_id, date, payee, memo, category_id, payment, deposit, account_balance))

    def get_transactions(self, account_id=None):
        if account_id:
            sql = "SELECT * FROM Transactions WHERE account_id = ?"
            cur = self.db_controller.execute_query(sql, (account_id,))
        else:
            sql = "SELECT * FROM Transactions"
            cur = self.db_controller.execute_query(sql)
        return cur.fetchall() if cur else []