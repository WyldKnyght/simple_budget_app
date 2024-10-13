# src/controllers/common/entity_controller.py
from typing import Dict, Any, List, Optional
from utils.custom_logging import error_handler

class EntityController:
    def __init__(self, db_ops, table_name: str):
        self.db_ops = db_ops
        self.table_name = table_name
        self.columns = self.db_ops.schema_controller.get_columns(table_name)

    @error_handler
    def add_entity(self, entity_data: Dict[str, Any]) -> int:
        columns = ', '.join(entity_data.keys())
        placeholders = ', '.join(['?' for _ in entity_data])
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        cursor = self.db_ops.execute_query(query, tuple(entity_data.values()))
        return cursor.lastrowid

    @error_handler
    def get_entity(self, entity_id: int) -> Optional[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name} WHERE id = ?"
        result = self.db_ops.fetch_one(query, (entity_id,))
        return dict(zip([col['name'] for col in self.columns], result)) if result else None

    @error_handler
    def get_entities(self) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table_name}"
        results = self.db_ops.fetch_all(query)
        return [dict(zip([col['name'] for col in self.columns], row)) for row in results]

    @error_handler
    def update_entity(self, entity_id: int, entity_data: Dict[str, Any]) -> None:
        set_clause = ', '.join([f"{key} = ?" for key in entity_data])
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE id = ?"
        self.db_ops.execute_query(query, tuple(entity_data.values()) + (entity_id,))

    @error_handler
    def remove_entity(self, entity_id: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.db_ops.execute_query(query, (entity_id,))