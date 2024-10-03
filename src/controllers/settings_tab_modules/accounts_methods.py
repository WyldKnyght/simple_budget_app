# src/controllers/settings_tab_modules/accounts_methods.py

class AccountMethods:
    def __init__(self, db_controller):
        self.db = db_controller

    def get_accounts(self):
        return self.db.get_accounts()

    def add_account(self, account_name, account_number, account_type):
        return self.db.add_account(account_name, account_number, account_type)

    def remove_account(self, account_id):
        return self.db.remove_account(account_id)

class CategoryMethods:
    def __init__(self, db_controller):
        self.db = db_controller

    def get_categories(self):
        return self.db.get_categories()

    def add_category(self, category_name, parent_id=None):
        return self.db.add_category(category_name, parent_id)

    def update_category(self, category_id, category_name, parent_id=None):
        return self.db.update_category(category_id, category_name, parent_id)

    def remove_category(self, category_id):
        return self.db.remove_category(category_id)

    def get_category_tree(self):
        categories = self.get_categories()
        return self._build_category_tree(categories)

    def _build_category_tree(self, categories, parent_id=None):
        tree = []
        for cat in categories:
            if cat[2] == parent_id:
                subcategories = self._build_category_tree(categories, cat[0])
                tree.append({
                    'id': cat[0],
                    'name': cat[1],
                    'subcategories': subcategories
                })
        return tree
