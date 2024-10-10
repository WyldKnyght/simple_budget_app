# src/controllers/validators/account_validator.py

from utils.custom_logging import logger
from typing import Dict, Any, List

class AccountValidator:
    def __init__(self, schema_columns: List[Dict[str, Any]]):
        self.schema_columns = schema_columns
        logger.debug(f"Schema columns: {schema_columns}")
        logger.debug(f"Type of schema_columns: {type(schema_columns)}")
        self.column_info = {col['name']: col for col in schema_columns}

    def validate_account_data(self, account_data: Dict[str, Any]) -> None:
        for column_name, column_info in self.column_info.items():
            if column_name != 'id':
                if column_name not in account_data and column_info.get('not_null', False):
                    raise ValueError(f"Missing required field: {column_name}")
                if column_name in account_data:
                    self.validate_field(column_name, account_data[column_name])

    def validate_field(self, column_name: str, value: Any) -> None:
        column_info = self.column_info[column_name]

        if value is None and column_info.get('not_null', False):
            raise ValueError(f"{column_name} cannot be None")

        if value is not None:
            if validator_method := getattr(self, f"_validate_{column_name}", None):
                validator_method(value, column_info)
            else:
                self._validate_default(column_name, value, column_info)

    def _validate_account_name(self, value: str, column_info: Dict[str, Any]) -> None:
        if not isinstance(value, str):
            raise ValueError("Account name must be a string")
        max_length = column_info.get('length')
        if max_length and len(value) > max_length:
            raise ValueError(f"Account name must have a maximum length of {max_length} characters")
        if not value.strip():
            raise ValueError("Account name cannot be empty or just whitespace")

    def _validate_account_number(self, value: str, column_info: Dict[str, Any]) -> None:
        if not isinstance(value, str):
            raise ValueError("Account number must be a string")
        if not value.strip():
            raise ValueError("Account number cannot be empty or just whitespace")
        if not value.isalnum():
            raise ValueError("Account number must be alphanumeric")

    def _validate_account_type(self, value: str, column_info: Dict[str, Any]) -> None:
        if not isinstance(value, str):
            raise ValueError("Account type must be a string")
        # Here we would ideally check against valid types from the schema,
        # but SQLite doesn't support ENUM. In a real-world scenario, you might
        # want to define valid types in the schema comment or use a separate table.
        # For now, we'll just check if it's a non-empty string.
        if not value.strip():
            raise ValueError("Account type cannot be empty or just whitespace")

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

    def validate_account_id(self, account_id: int) -> None:
        if not isinstance(account_id, int) or account_id <= 0:
            raise ValueError("Account ID must be a positive integer")

logger.info("AccountValidator initialized")