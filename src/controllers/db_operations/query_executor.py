# src/controllers/db_operations/query_executor.py
import sqlite3
from typing import Any, Tuple, List, Optional
from utils.custom_logging import logger

class QueryExecutor:
    def __init__(self, connection: Any):
        self.connection = connection

    def execute(self, query: str, params: Tuple[Any, ...] = ()) -> sqlite3.Cursor:
        try:
            return self.connection.execute_query(query, params)
        except sqlite3.Error as e:
            logger.error(f"Error executing query: {query}. Error: {e}")
            raise

    def fetch_one(self, query: str, params: Tuple[Any, ...] = ()) -> Optional[sqlite3.Row]:
        try:
            cursor = self.execute(query, params)
            return cursor.fetchone()
        except sqlite3.Error as e:
            logger.error(f"Error fetching one row: {query}. Error: {e}")
            raise

    def fetch_all(self, query: str, params: Tuple[Any, ...] = ()) -> List[sqlite3.Row]:
        try:
            cursor = self.execute(query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Error fetching all rows: {query}. Error: {e}")
            raise

    def execute_many(self, query: str, param_list: List[Tuple[Any, ...]]) -> None:
        try:
            with self.connection.get_connection() as conn:
                conn.executemany(query, param_list)
        except sqlite3.Error as e:
            logger.error(f"Error executing many: {query}. Error: {e}")
            raise

    def execute_script(self, script: str) -> None:
        try:
            with self.connection.get_connection() as conn:
                conn.executescript(script)
        except sqlite3.Error as e:
            logger.error(f"Error executing script. Error: {e}")
            raise