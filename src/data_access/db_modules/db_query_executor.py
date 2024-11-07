# src\data_access\db_modules\db_query_executor.py
import sqlite3
from utils.custom_logging import logger, error_handler
from configs.messages_config import DB_QUERY_ERROR
from .db_custom_exceptions import QueryExecutionError

class QueryExecutor:
    def __init__(self, connections):
        self.connections = connections

    @error_handler
    def execute_query(self, query, params=None):
        conn = None
        try:
            conn = self.connections.get_connection()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Error executing query: {e}")
            if conn:
                conn.rollback()
            raise QueryExecutionError(DB_QUERY_ERROR.format(str(e))) from e

    @error_handler
    def execute_non_query(self, query, params=None):
        conn = None
        try:
            conn = self.connections.get_connection()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error executing query: {e}")
            if conn:
                conn.rollback()
            raise QueryExecutionError(DB_QUERY_ERROR.format(str(e))) from e