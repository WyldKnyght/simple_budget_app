# src/controllers/db_operations/database_connection.py
import sqlite3
from contextlib import contextmanager
from typing import Tuple, Any, List, Optional
from utils.custom_logging import logger
from configs.path_config import SCHEMA_PATH

class DatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)
            self.connection.row_factory = sqlite3.Row

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    @contextmanager
    def get_connection(self):
        if self.connection is None:
            self.connect()
        try:
            yield self.connection
        finally:
            pass  # Don't close the connection here

    def execute_query(self, query: str, params: tuple = ()):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor

    def _create_tables(self, conn: sqlite3.Connection):
        try:
            with open(SCHEMA_PATH, 'r') as schema_file:
                schema = schema_file.read()

            # Split the schema into individual CREATE TABLE statements
            create_statements = [stmt.strip() for stmt in schema.split(';') if stmt.strip()]

            for statement in create_statements:
                # Extract table name from the CREATE TABLE statement
                table_name = statement.split('CREATE TABLE')[1].split('(')[0].strip()

                # Check if the table already exists
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                    (table_name,),
                )
                if cursor.fetchone() is None:
                    # Table doesn't exist, so create it
                    conn.execute(statement)
                    logger.info(f"Created table: {table_name}")
                else:
                    logger.info(f"Table {table_name} already exists, skipping creation")

            conn.commit()
        except (sqlite3.Error, IOError) as e:
            logger.error(f"Error creating tables: {e}")
            raise

    def fetch_one(self, query: str, params: Tuple[Any, ...] = ()) -> Optional[sqlite3.Row]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()

    def fetch_all(self, query: str, params: Tuple[Any, ...] = ()) -> List[sqlite3.Row]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def execute_script(self, script: str):
        with self.get_connection() as conn:
            conn.executescript(script)

    def get_table_names(self) -> List[str]:
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        return [row['name'] for row in self.fetch_all(query)]