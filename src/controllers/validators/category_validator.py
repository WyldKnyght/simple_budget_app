# src/controllers/validators/category_validator.py

from utils.custom_logging import logger
from typing import Dict, Any, List

class CategoryValidator:
    def __init__(self, schema_columns: List[Dict[str, Any]]):
        self.schema_columns = schema_columns
        self.column_info = {col['name']: col for col in schema_columns}

    def validate_category_data(self, category_data: Dict[str, Any]) -> None:
        for column_name, column_info in self.column_info.items():
            if column_name != 'id':
                if column_name not in category_data and column_info.get('not_null', False):
                    raise ValueError(f"Missing required field: {column_name}")
                if column_name in category_data:
                    self.validate_field(column_name, category_data[column_name])

    def validate_field(self, column_name: str, value: Any) -> None:
        column_info = self.column_info[column_name]

        if value is None and column_info.get('not_null', False):
            raise ValueError(f"{column_name} cannot be None")

        if value is not None:
            if validator_method := getattr(self, f"_validate_{column_name}", None):
                validator_method(value, column_info)
            else:
                self._validate_default(column_name, value, column_info)

    def _validate_category_name(self, value: str, column_info: Dict[str, Any]) -> None:
        if not isinstance(value, str):
            raise ValueError("Category name must be a string")
        if not value.strip():
            raise ValueError("Category name cannot be empty or just whitespace")
        max_length = column_info.get('length')
        if max_length and len(value) > max_length:
            raise ValueError(f"Category name must have a maximum length of {max_length} characters")

    def _validate_parent_id(self, value: Any, column_info: Dict[str, Any]) -> None:
        if value is not None and (not isinstance(value, int) or value <= 0):
            raise ValueError("Parent ID must be a positive integer or None")

    def _validate_default(self, column_name: str, value: Any, column_info: Dict[str, Any]) -> None:
        column_type = column_info['type']
        if column_type == 'TEXT':
            if not isinstance(value, str):
                raise ValueError(f"{column_name} must be a string")
            max_length = column_info.get('length')
            if max_length and len(value) > max_length:
                raise ValueError(f"{column_name} must have a maximum length of {max_length} characters")
        elif column_type == 'INTEGER':
            if not isinstance(value, int):
                raise ValueError(f"{column_name} must be an integer")
        elif column_type == 'REAL':
            if not isinstance(value, (int, float)):
                raise ValueError(f"{column_name} must be a number")

    def validate_category_id(self, category_id: int) -> None:
        if not isinstance(category_id, int) or category_id <= 0:
            raise ValueError("Category ID must be a positive integer")

logger.info("CategoryValidator initialized")