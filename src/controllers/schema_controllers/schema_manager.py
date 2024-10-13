# src/controllers/schema_controllers/schema_manager.py
from typing import List, Dict, Optional, Any, Tuple
from .schema_reader import SchemaReader
from .table_info_extractor import TableInfoExtractor
from .schema_validator import SchemaValidator
from .schema_applier import SchemaApplier
from .database_backup import DatabaseBackup

class SchemaManager:
    def __init__(self, db_ops: Any):
        self.db_ops = db_ops
        self.schema_reader = SchemaReader(self.db_ops)
        self.table_info_extractor = TableInfoExtractor(self.schema_reader)
        self.schema_validator = SchemaValidator(self.db_ops, self.schema_reader, self.table_info_extractor)
        self.schema_applier = SchemaApplier(self.db_ops, self.schema_reader, self.table_info_extractor, self.schema_validator)
        self.database_backup = DatabaseBackup(self.db_ops)

    def get_table_names(self) -> List[str]:
        return self.schema_reader.get_table_names()

    def get_table_name_by_prefix(self, prefix: str) -> Optional[str]:
        return self.schema_reader.get_table_name_by_prefix(prefix)

    def get_columns(self, table_name: str) -> List[Dict[str, Any]]:
        return self.table_info_extractor.get_columns(table_name)

    def get_foreign_keys(self, table_name: str) -> List[Dict[str, str]]:
        return self.table_info_extractor.get_foreign_keys(table_name)

    def validate_schema(self) -> bool:
        return self.schema_validator.validate_schema()

    def apply_schema_changes(self) -> Tuple[bool, str]:
        return self.schema_applier.apply_schema_changes()

    def backup_database(self, backup_path: str) -> Tuple[bool, str]:
        return self.database_backup.backup_database(self.db_ops, backup_path)

    def get_schema_version(self) -> Optional[str]:
        return self.schema_reader.get_schema_version()

    def ensure_indexes(self, table_name: str, indexes: List[str]) -> None:
        self.schema_reader.ensure_indexes(table_name, indexes)