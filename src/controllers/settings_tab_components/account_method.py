# src/controllers/settings_tab_components/account_method.py

class AccountMethod:
    def __init__(self, database_controller):
        self.db_controller = database_controller

    def get_accounts(self):
        return self.db_controller.account_ops.get_accounts()

    def add_account(self, account_name, account_number, account_type):
        return self.db_controller.account_ops.add_account(account_name, account_number, account_type)

    def get_account_types(self):
        return self.db_controller.account_ops.get_account_types()

    def add_account_type(self, account_type):
        return self.db_controller.account_ops.add_account_type(account_type)

    def update_account(self, account_id, account_name, account_number, account_type):
        return self.db_controller.account_ops.update_account(account_id, account_name, account_number, account_type)

    def delete_account(self, account_id):
        return self.db_controller.account_ops.delete_account(account_id)