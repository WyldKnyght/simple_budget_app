# src/controllers/database_controllers.py
import sqlite3
import os
from configs.path_config import EnvSettings
from configs.default_settings import DEFAULT_ACCOUNT_TYPES, DEFAULT_CATEGORIES
from utils.custom_logging import logger
from .database_modules.account_operations import AccountOperations
from .database_modules.expense_operations import ExpenseOperations
from .database_modules.category_operations import CategoryOperations
from user_interface.common.show_progress_dialog import show_progress_dialog

class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.account_ops = None
        self.expense_ops = None
        self.category_ops = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(EnvSettings.DB_PATH)
            self.cursor = self.conn.cursor()
            self.account_ops = AccountOperations(self)
            self.expense_ops = ExpenseOperations(self)
            self.category_ops = CategoryOperations(self)
            logger.info(f"Connected to database: {EnvSettings.DB_PATH}")
        except sqlite3.Error as e:
            logger.error(f"Error connecting to database: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")

    def create_tables(self):
        try:
            with open(EnvSettings.SCHEMA_PATH, 'r') as schema_file:
                schema = schema_file.read()
                self.cursor.executescript(schema)
            self.conn.commit()
            logger.info("Database tables created successfully")
        except sqlite3.OperationalError as e:
            if "table Accounts already exists" in str(e):
                logger.info("Tables already exist, skipping creation")
            else:
                logger.error(f"Error creating tables: {e}")
        except sqlite3.Error as e:
            logger.error(f"Error creating tables: {e}")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error executing query: {e}")
            self.conn.rollback()

    def fetch_all(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Error fetching data: {e}")
            return []

    def reset_database(self, parent_widget=None):
        self.close()
        if os.path.exists(EnvSettings.DB_PATH):
            os.remove(EnvSettings.DB_PATH)
        self.connect()
        self.create_tables()

        total_steps = (len(DEFAULT_ACCOUNT_TYPES) + 
                       self._count_categories(DEFAULT_CATEGORIES))
        
        progress = show_progress_dialog(parent_widget, "Resetting Database", 
                                        "Initializing default data...", total_steps)
        
        try:
            self._initialize_default_data(progress)
        finally:
            progress.close()

    def _initialize_default_data(self, progress):
        step = 0
        # Add default account types
        for account_type in DEFAULT_ACCOUNT_TYPES:
            self.account_ops.add_account(account_type, "0000", account_type)
            step += 1
            progress.setValue(step)
            if progress.wasCanceled():
                return

        # Add default categories
        self._add_categories(DEFAULT_CATEGORIES, None, progress, step)

    def _add_categories(self, categories, parent_id=None, progress=None, step=0):
        for category in categories:
            if isinstance(category, dict):
                new_id = self.category_ops.add_category(category['name'], parent_id)
                step += 1
                if progress:
                    progress.setValue(step)
                    if progress.wasCanceled():
                        return step
                if 'subcategories' in category:
                    step = self._add_categories(category['subcategories'], new_id, progress, step)
            elif isinstance(category, str):
                self.category_ops.add_category(category, parent_id)
                step += 1
                if progress:
                    progress.setValue(step)
                    if progress.wasCanceled():
                        return step
            else:
                logger.warning(f"Unexpected category type: {type(category)}")
        return step

    def _count_categories(self, categories):
        count = 0
        for category in categories:
            if isinstance(category, dict):
                count += 1
                if 'subcategories' in category:
                    count += self._count_categories(category['subcategories'])
            elif isinstance(category, str):
                count += 1
        return count

    def get_transactions(self):
        query = """
        SELECT t.id, a.account_name, t.date, t.payee, c.category_name, t.payment, t.deposit
        FROM Transactions t
        JOIN Accounts a ON t.account_id = a.id
        JOIN Categories c ON t.category_id = c.id
        ORDER BY t.date DESC
        """
        return self.fetch_all(query)

# Create a global instance of DatabaseManager
db_manager = DatabaseManager()