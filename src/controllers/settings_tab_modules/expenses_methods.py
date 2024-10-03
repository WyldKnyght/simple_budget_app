# src/controllers/settings_tab_modules/expenses_methods.py

class ExpenseMethods:
    def __init__(self, db_controller):
        self.db = db_controller

    def get_expenses(self):
        return self.db.get_expenses()

    def get_expense(self, expense_id):
        return self.db.get_expense(expense_id)

    def add_expense(self, expense_name, category_id, due_date, frequency, amount):
        return self.db.add_expense(expense_name, category_id, due_date, frequency, amount)

    def update_expense(self, expense_id, expense_name, category_id, due_date, frequency, amount):
        return self.db.update_expense(expense_id, expense_name, category_id, due_date, frequency, amount)

    def remove_expense(self, expense_name):
        query = "DELETE FROM Expenses WHERE expense_name = ?"
        self.db_manager.execute_query(query, (expense_name,))

    def get_categories(self):
        return self.db.get_categories()