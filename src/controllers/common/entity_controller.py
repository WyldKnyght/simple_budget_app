# src/controllers/common/entity_controller.py
from typing import Dict, Any, List
from utils.custom_logging import logger
from configs.path_config import SCHEMA_PATH

class EntityController:
    def __init__(self, db_ops, table_name):
        self.db_ops = db_ops
        self.table_name = table_name
        self.columns = self._get_columns_from_schema()

    def _get_columns_from_schema(self) -> List[Dict[str, Any]]:
        with open(SCHEMA_PATH, 'r') as schema_file:
            schema = schema_file.read()
        start = schema.find(f"CREATE TABLE {self.table_name}")
        end = schema.find(")", start)
        create_table_stmt = schema[start:end+1]
        
        columns = []
        for line in create_table_stmt.split('\n')[1:]:
            line = line.strip()
            if line and not line.startswith(('PRIMARY', 'FOREIGN')):
                parts = line.split()
                if len(parts) >= 2:
                    column = {
                        'name': parts[0],
                        'type': parts[1],
                        'not_null': 'NOT NULL' in line.upper()
                    }
                    columns.append(column)
        return columns

    def add_entity(self, entity_data: Dict[str, Any]) -> int:
        columns = ', '.join(entity_data.keys())
        placeholders = ', '.join(['?' for _ in entity_data])
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        
        try:
            cursor = self.db_ops.execute_query(query, tuple(entity_data.values()))
            return cursor.lastrowid
        except Exception as e:
            logger.error(f"Error adding entity to {self.table_name}: {e}")
            raise

    def get_entities(self) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name}"
        try:
            results = self.db_ops.fetch_all(query)
            return [dict(zip([col['name'] for col in self.columns], row)) for row in results]
        except Exception as e:
            logger.error(f"Error fetching entities from {self.table_name}: {e}")
            return []

    def update_entity(self, entity_id: int, entity_data: Dict[str, Any]) -> None:
        set_clause = ', '.join([f"{key} = ?" for key in entity_data])
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE id = ?"
        
        try:
            self.db_ops.execute_query(query, tuple(entity_data.values()) + (entity_id,))
        except Exception as e:
            logger.error(f"Error updating entity in {self.table_name}: {e}")
            raise

    def remove_entity(self, entity_id: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        try:
            self.db_ops.execute_query(query, (entity_id,))
        except Exception as e:
            logger.error(f"Error removing entity from {self.table_name}: {e}")
            raise