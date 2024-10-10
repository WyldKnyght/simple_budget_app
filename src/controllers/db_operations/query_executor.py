# src/controllers/query_executor.py
import sqlite3
from typing import Any, Tuple, List

class QueryExecutor:
    def __init__(self, connection):
        self.connection = connection

    def execute(self, query: str, params: Tuple[Any, ...] = ()) -> sqlite3.Cursor:
        return self.connection.execute_query(query, params)

    def fetch_one(self, query: str, params: Tuple[Any, ...] = ()) -> Tuple[Any, ...]:
        return self.connection.fetch_one(query, params)

    def fetch_all(self, query: str, params: Tuple[Any, ...] = ()) -> List[Tuple[Any, ...]]:
        return self.connection.fetch_all(query, params)