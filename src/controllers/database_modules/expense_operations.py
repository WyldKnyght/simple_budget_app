# src/controllers/database_modules/expense_operations.py

class ExpenseOperations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_expense(self, expense_name, category_id, due_date, frequency, amount):
        query = "INSERT INTO Expenses (expense_name, category_id, due_date, frequency, amount) VALUES (?, ?, ?, ?, ?)"
        self.db_manager.execute_query(query, (expense_name, category_id, due_date, frequency, amount))

    def get_expenses(self):
        query = """
        SELECT e.id, e.expense_name, c.category_name, e.due_date, e.frequency, e.amount
        FROM Expenses e
        JOIN Categories c ON e.category_id = c.id
        """
        return self.db_manager.fetch_all(query)

    def get_expense(self, expense_id):
        query = """
        SELECT e.id, e.expense_name, c.category_name, e.due_date, e.frequency, e.amount
        FROM Expenses e
        JOIN Categories c ON e.category_id = c.id
        WHERE e.id = ?
        """
        return self.db_manager.fetch_all(query, (expense_id,))[0]

    def update_expense(self, expense_id, expense_name, category_id, due_date, frequency, amount):
        query = """
        UPDATE Expenses
        SET expense_name = ?, category_id = ?, due_date = ?, frequency = ?, amount = ?
        WHERE id = ?
        """
        self.db_manager.execute_query(query, (expense_name, category_id, due_date, frequency, amount, expense_id))

    def remove_expense(self, expense_id):
        query = "DELETE FROM Expenses WHERE id = ?"
        self.db_manager.execute_query(query, (expense_id,))