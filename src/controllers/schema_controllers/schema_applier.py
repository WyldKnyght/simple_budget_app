# src/controllers/schema_controllers/schema_applier.py
from typing import Tuple, List, Dict, Any
from utils.custom_logging import logger

class SchemaApplier:
    def __init__(self, db_ops, schema_reader, table_info_extractor, schema_validator):
        self.db_ops = db_ops
        self.schema_reader = schema_reader
        self.table_info_extractor = table_info_extractor
        self.schema_validator = schema_validator

    def apply_schema_changes(self) -> Tuple[bool, str]:
        differences = self.schema_validator.get_table_differences()

        if not any(differences.values()):
            return True, "No changes needed. Database already matches the schema."

        try:
            with self.db_ops.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("PRAGMA foreign_keys = ON;")

                for table in differences['missing_tables']:
                    if create_stmt := self.schema_reader.get_create_table_statement(
                        table
                    ):
                        cursor.execute(create_stmt)
                        logger.info(f"Created missing table: {table}")

                for table, mismatch in differences['column_mismatches'].items():
                    for column in mismatch['missing_columns']:
                        if column_info := next(
                            (col for col in self.get_columns(table) if col['name'] == column),
                            None,
                        ):
                            column_def = f"{column} {column_info['type']}"
                            if column_info['not_null']:
                                column_def += " NOT NULL"
                            if column_info['primary_key']:
                                column_def += " PRIMARY KEY"
                            # Note: We're not adding foreign key constraints here
                            cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column_def}")
                            logger.info(f"Added missing column {column} to table {table}")

            self.db_ops.execute_query("UPDATE schema_version SET version = version + 1")
            logger.info("Schema version incremented")
            return True, "Schema changes applied successfully."
        except Exception as e:
            logger.error(f"Error applying schema changes: {e}")
            return False, f"Failed to apply schema changes: {str(e)}"

    def get_columns(self, table_name: str) -> List[Dict[str, Any]]:
        return self.table_info_extractor.get_columns(table_name)
    
    @staticmethod
    def _enable_foreign_keys(cursor):
        cursor.execute("PRAGMA foreign_keys = ON;")

    @staticmethod
    def _create_missing_tables(differences, cursor, get_create_table_statement):
        for table in differences['missing_tables']:
            if create_stmt := get_create_table_statement(table):
                cursor.execute(create_stmt)
                logger.info(f"Created missing table: {table}")

    @staticmethod
    def _add_missing_columns(differences, cursor, get_columns):
        for table, mismatch in differences['column_mismatches'].items():
            for column in mismatch['missing_columns']:
                if column_info := next((col for col in get_columns(table) if col['name'] == column), None):
                    SchemaApplier._add_column(cursor, table, column, column_info)

    @staticmethod
    def _add_column(cursor, table, column, column_info):
        column_def = SchemaApplier._build_column_definition(column, column_info)
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column_def}")
        logger.info(f"Added missing column {column} to table {table}")

    @staticmethod
    def _build_column_definition(column, column_info):
        column_def = f"{column} {column_info['type']}"
        if column_info.get('not_null'):
            column_def += " NOT NULL"
        if column_info.get('primary_key'):
            column_def += " PRIMARY KEY"
        if column_info.get('foreign_key'):
            fk = column_info['foreign_key']
            column_def += f" REFERENCES {fk['table']}({fk['column']})"
        return column_def

    @staticmethod
    def _increment_schema_version(db_ops):
        db_ops.execute_query("UPDATE schema_version SET version = version + 1")
        logger.info("Schema version incremented")