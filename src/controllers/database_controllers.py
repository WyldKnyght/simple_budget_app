# src/controllers/database_controllers.py

import sqlite3
import os
from sqlite3 import Error
from utils.custom_logging import logger
from configs.app_config import DATABASE_DIR, DATABASE_NAME
from .database_components.account_operations import AccountOperations
from .database_components.category_operations import CategoryOperations
from .database_components.transaction_operations import TransactionOperations
from .database_components.expense_operations import ExpenseOperations
from .database_components.table_operations import TableOperations

class DatabaseController:
    def __init__(self, db_file=os.path.join(DATABASE_DIR, DATABASE_NAME)):
        self.db_file = db_file
        self.conn = None
        self.create_connection()
        self.table_ops = TableOperations(self)
        try:
            self.table_ops.initialize_default_data()
        except Exception as e:
            logger.error(f"Error initializing default data: {e}")
        self.account_ops = AccountOperations(self)
        self.category_ops = CategoryOperations(self)
        self.transaction_ops = TransactionOperations(self)
        self.expense_ops = ExpenseOperations(self)

    def create_connection(self):
        if not self.conn:
            try:
                self.conn = sqlite3.connect(self.db_file)
                logger.info(f"Successfully connected to database at {self.db_file}")
            except Error as e:
                logger.error(f"Error connecting to database: {e}")
                self.conn = None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            logger.info("Database connection closed")

    def execute_query(self, sql, params=None):
        self.create_connection()
        try:
            cur = self.conn.cursor()
            if params:
                cur.execute(sql, params)
            else:
                cur.execute(sql)
            self.conn.commit()
            return cur
        except sqlite3.OperationalError as e:
            if "already exists" not in str(e):
                logger.error(f"Error executing query: {e}")
        except Error as e:
            logger.error(f"Error executing query: {e}")
        return None

    def __enter__(self):
        self.create_connection()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

    def __del__(self):
        self.close_connection()

    def fetch_all_records(self, sql, params=None):
        cur = self.execute_query(sql, params)
        records = cur.fetchall() if cur else []
        logger.debug(f"Fetched records: {records}")
        return records

    def check_database(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(*) FROM Categories")
            count = cur.fetchone()[0]
            logger.debug(f"Number of categories in database: {count}")
            cur.execute("SELECT * FROM Categories LIMIT 5")
            sample = cur.fetchall()
            logger.debug(f"Sample categories: {sample}")
        except Exception as e:
            logger.error(f"Error checking database: {e}")