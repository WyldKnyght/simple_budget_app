# src/controllers/schema_controllers/schema_validator.py
from typing import Dict, Any
from utils.custom_logging import logger

class SchemaValidator:
    def __init__(self, db_ops, schema_reader, table_info_extractor):
        self.db_ops = db_ops
        self.schema_reader = schema_reader
        self.table_info_extractor = table_info_extractor

    def get_table_differences(self) -> Dict[str, Any]:
        schema_tables = set(self.schema_reader.get_table_names())
        db_tables = set(self.db_ops.get_table_names())

        differences = {
            'column_mismatches': {},
            'missing_tables': list(schema_tables - db_tables),
            'extra_tables': list(db_tables - schema_tables),
        }
        for table in schema_tables.intersection(db_tables):
            schema_columns = {col['name'] for col in self.table_info_extractor.get_columns(table)}
            db_columns = {
                col[1]
                for col in self.db_ops.execute_query(
                    f"PRAGMA table_info({table})"
                ).fetchall()
            }

            if schema_columns != db_columns:
                differences['column_mismatches'][table] = {
                    'missing_columns': list(schema_columns - db_columns),
                    'extra_columns': list(db_columns - schema_columns)
                }

        return differences

    def validate_schema(self) -> bool:
        schema_tables = set(self.schema_reader.get_table_names())
        db_tables = set(self.db_ops.get_table_names())

        if schema_tables != db_tables:
            logger.error(f"Schema mismatch. Schema tables: {schema_tables}, DB tables: {db_tables}")
            return False

        for table in schema_tables:
            schema_columns = {col['name'] for col in self.table_info_extractor.get_columns(table)}
            db_columns = {
                col[1]
                for col in self.db_ops.execute_query(
                    f"PRAGMA table_info({table})"
                ).fetchall()
            }

            if schema_columns != db_columns:
                logger.error(f"Column mismatch for table {table}. Schema: {schema_columns}, DB: {db_columns}")
                return False

        logger.info("Schema validation successful")
        return True
