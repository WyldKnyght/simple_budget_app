# src/controllers/schema_controllers/table_info_extractor.py
import re
from typing import List, Dict, Any

class TableInfoExtractor:
    def __init__(self, schema_reader):
        self.schema_reader = schema_reader

    def get_columns(self, table_name: str) -> List[Dict[str, Any]]:
        create_table_stmt = self.schema_reader.get_create_table_statement(table_name)
        if not create_table_stmt:
            return []

        column_pattern = r'(\w+)\s+(\w+)(?:\s+(\w+))*'
        columns = []
        for match in re.finditer(column_pattern, create_table_stmt):
            column = {
                'name': match.group(1),
                'type': match.group(2),
                'not_null': 'NOT NULL' in match.group(0).upper(),
                'primary_key': 'PRIMARY KEY' in match.group(0).upper()
            }
            columns.append(column)
        return columns

    def get_foreign_keys(self, table_name: str) -> List[Dict[str, str]]:
        create_table_stmt = self.schema_reader.get_create_table_statement(table_name)
        if not create_table_stmt:
            return []

        fk_pattern = r'FOREIGN KEY\s*\((\w+)\)\s*REFERENCES\s*(\w+)\s*\((\w+)\)'
        return [
            {
                'column': match.group(1),
                'referenced_table': match.group(2),
                'referenced_column': match.group(3),
            }
            for match in re.finditer(fk_pattern, create_table_stmt)
        ]