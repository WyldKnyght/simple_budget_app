# src\data_access\db_query_executor.py
import sqlite3
from utils.custom_logging import logger
from .db_connections import DatabaseConnections
from .db_custom_exceptions import QueryExecutionError

class QueryExecutor:
    def __init__(self):
        self.connections = DatabaseConnections()

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
            return cursor
        except sqlite3.Error as e:
            logger.error(f"Error executing query: {e}")
            if conn:
                conn.rollback()
            raise QueryExecutionError(f"Failed to execute query: {e}") from e
        finally:
            if conn:
                conn.close()