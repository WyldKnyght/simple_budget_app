# src/controllers/db_operations/database_initializer.py

from .database_manager import DatabaseManager
from ..settings_tab_controllers.accounts_controller import AccountsController
from ..settings_tab_controllers.categories_controller import CategoriesController
from ..settings_tab_controllers.expenses_controller import ExpensesController
from services.database_reset_service import DatabaseResetService
from utils.schema_utils import get_table_name_by_prefix

class DatabaseInitializer:
    @staticmethod
    def initialize_database(db_manager: DatabaseManager):
        accounts_table = get_table_name_by_prefix("account")
        categories_table = get_table_name_by_prefix("categor")
        expenses_table = get_table_name_by_prefix("expense")

        db_manager.register_operation('accounts', AccountsController(db_manager, accounts_table))
        db_manager.register_operation('categories', CategoriesController(db_manager, categories_table))
        db_manager.register_operation('expenses', ExpensesController(db_manager, expenses_table))

    @staticmethod
    def reset_database(db_manager: DatabaseManager):
        reset_db = DatabaseResetService(db_manager)
        reset_db.reset_database()