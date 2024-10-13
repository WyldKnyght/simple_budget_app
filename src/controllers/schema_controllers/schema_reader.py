# src/controllers/schema_controllers/schema_reader.py
import re
from typing import List, Optional
from configs.path_config import SCHEMA_PATH
from utils.custom_logging import logger

class SchemaReader:
    def __init__(self):
        self.schema = self._read_schema()

    def _read_schema(self) -> str:
        try:
            with open(SCHEMA_PATH, 'r') as schema_file:
                return schema_file.read()
        except IOError as e:
            logger.error(f"Error reading schema file: {e}")
            return ""

    def get_table_names(self) -> List[str]:
        return re.findall(r'CREATE TABLE (\w+)', self.schema)

    def get_table_name_by_prefix(self, prefix: str) -> Optional[str]:
        table_names = self.get_table_names()
        return next((name for name in table_names if name.lower().startswith(prefix.lower())), None)

    def get_create_table_statement(self, table_name: str) -> Optional[str]:
        pattern = rf'CREATE TABLE {table_name}\s*\((.*?)\);'
        match = re.search(pattern, self.schema, re.DOTALL)
        return f"CREATE TABLE {table_name} ({match[1]});" if match else None

    def get_schema_version(self) -> Optional[str]:
        try:
            result = self.db_ops.fetch_one("SELECT version FROM schema_version ORDER BY id DESC LIMIT 1")
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Error retrieving schema version: {e}")
            return None

    def ensure_indexes(self, table_name: str, indexes: List[str]) -> None:
        for column in indexes:
            query = f"CREATE INDEX IF NOT EXISTS idx_{table_name}_{column} ON {table_name} ({column})"
            try:
                self.db_ops.execute_query(query)
                logger.info(f"Index created or already exists for {column} on {table_name}")
            except Exception as e:
                logger.error(f"Error creating index on {column} for table {table_name}: {e}")