# src/controllers/database_components/expense_operations.py

class ExpenseOperations:
    def __init__(self, db_service):
        self.db_service = db_service

    def add_expense(self, expense_name, category_id, due_date, frequency, amount):
        sql = """
        INSERT INTO Expenses (expense_name, category_id, due_date, frequency, amount)
        VALUES (?, ?, ?, ?, ?)
        """
        return self.db_service.execute_query(sql, (expense_name, category_id, due_date, frequency, amount))

    def get_expenses(self):
        return self.db_service.fetch_all_records("SELECT * FROM Expenses")

    def update_expense(self, expense_id, expense_name, category_id, due_date, frequency, amount):
        sql = """
        UPDATE Expenses
        SET expense_name = ?, category_id = ?, due_date = ?, frequency = ?, amount = ?
        WHERE id = ?
        """
        return self.db_service.execute_query(sql, (expense_name, category_id, due_date, frequency, amount, expense_id))

    def delete_expense(self, expense_id):
        sql = "DELETE FROM Expenses WHERE id = ?"
        return self.db_service.execute_query(sql, (expense_id,))

    def get_expenses_by_category(self, category_id):
        sql = "SELECT * FROM Expenses WHERE category_id = ?"
        return self.db_service.fetch_all_records(sql, (category_id,))

    def get_expenses_by_date_range(self, start_date, end_date):
        sql = "SELECT * FROM Expenses WHERE due_date BETWEEN ? AND ?"
        return self.db_service.fetch_all_records(sql, (start_date, end_date))

    # New methods for expense frequencies
    def add_expense_frequency(self, frequency):
        sql = "INSERT INTO ExpenseFrequencies (frequency_name) VALUES (?)"
        return self.db_service.execute_query(sql, (frequency,))

    def get_expense_frequencies(self):
        return self.db_service.fetch_all_records("SELECT * FROM ExpenseFrequencies")

    def delete_all_expense_frequencies(self):
        sql = "DELETE FROM ExpenseFrequencies"
        return self.db_service.execute_query(sql)

    def delete_expense_frequency(self, frequency_id):
        sql = "DELETE FROM ExpenseFrequencies WHERE id = ?"
        return self.db_service.execute_query(sql, (frequency_id,))

    def update_expense_frequency(self, frequency_id, new_frequency_name):
        sql = "UPDATE ExpenseFrequencies SET frequency_name = ? WHERE id = ?"
        return self.db_service.execute_query(sql, (new_frequency_name, frequency_id))