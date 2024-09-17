# src/controllers/settings_tab_components/expense_method.py

class ExpenseMethod:
    def __init__(self, database_controller):
        self.db_controller = database_controller

    def get_expenses(self):
        return self.db_controller.expense_ops.get_expenses()

    def add_expense(self, expense_name, category_id, due_date, frequency, amount):
        return self.db_controller.expense_ops.add_expense(expense_name, category_id, due_date, frequency, amount)

    def get_expense_frequencies(self):
        return self.db_controller.expense_ops.get_expense_frequencies()

    def update_expense(self, expense_id, expense_name, category_id, due_date, frequency, amount):
        return self.db_controller.expense_ops.update_expense(expense_id, expense_name, category_id, due_date, frequency, amount)

    def delete_expense(self, expense_id):
        return self.db_controller.expense_ops.delete_expense(expense_id)

    def get_expenses_by_category(self, category_id):
        return self.db_controller.expense_ops.get_expenses_by_category(category_id)

    def get_expenses_by_date_range(self, start_date, end_date):
        return self.db_controller.expense_ops.get_expenses_by_date_range(start_date, end_date)