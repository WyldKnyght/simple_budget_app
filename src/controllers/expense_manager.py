from .services.expense_service import ExpenseService

class ExpenseManager:
    def __init__(self):
        self.expense_service = ExpenseService()

    def create_expense(self, expense_name, category_id, due_date, frequency, amount):
        """
        Coordinate the creation of a new expense.
        """
        return self.expense_service.create_expense(expense_name, category_id, due_date, frequency, amount)

    def get_expense_by_id(self, expense_id):
        """
        Coordinate retrieving an expense by its ID.
        """
        return self.expense_service.get_expense_by_id(expense_id)

    def get_all_expenses(self):
        """
        Coordinate retrieving all expenses.
        """
        return self.expense_service.get_all_expenses()

    def update_expense(self, expense_id, expense_name, category_id, due_date, frequency, amount):
        """
        Coordinate updating an existing expense.
        """
        self.expense_service.update_expense(expense_id, expense_name, category_id, due_date, frequency, amount)

    def delete_expense(self, expense_id):
        """
        Coordinate deleting an expense by its ID.
        """
        self.expense_service.delete_expense(expense_id)