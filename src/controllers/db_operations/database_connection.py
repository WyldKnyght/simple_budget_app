# src/controllers/db_operations/database_connection.py
import sqlite3
from typing import Tuple, Any, List
from utils.custom_logging import logger
from configs.path_config import SCHEMA_PATH

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def execute_query(self, query, params):
        if self.cursor is None:
            self.connect()
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()

    def _create_tables(self):
        try:
            with open(SCHEMA_PATH, 'r') as schema_file:
                schema = schema_file.read()
            for statement in schema.split(';'):
                if statement.strip():
                    try:
                        self.cursor.execute(statement)
                    except sqlite3.OperationalError as e:
                        if "already exists" not in str(e):
                            raise
            self.connection.commit()
        except (sqlite3.Error, IOError) as e:
            logger.error(f"Error creating tables: {e}")
            raise

    def fetch_one(self, query: str, params: Tuple[Any, ...] = ()) -> Tuple[Any, ...]:
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            logger.error(f"Error fetching one row: {e}")
            raise

    def fetch_all(self, query: str, params: Tuple[Any, ...] = ()) -> List[Tuple[Any, ...]]:
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Error fetching all rows: {e}")
            raise

    def _handle_error(self, message: str, error: Exception):
        self.conn.rollback()
        logger.error(f"{message}{error}")
        raise