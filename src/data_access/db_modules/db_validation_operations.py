# src/data_access/db_modules/db_validation_operations.py

import os
from utils.custom_logging import error_handler, logger

class ValidationOperations:
    def __init__(self, database_manager):
        self.database_manager = database_manager
        self._current_structure = None
        self._expected_structure = None

    @error_handler
    def validate_schema(self):
        logger.info("Validating database schema")
        if not self.database_exists():
            logger.warning("Database does not exist.")
            return False, "Database does not exist."
        
        current_structure = self.get_current_structure()  # Changed from get_current_schema
        expected_structure = self.get_expected_structure()
        
        if current_structure is None:
            logger.error("Failed to retrieve current structure")
            return False, "Failed to retrieve current structure."
        if expected_structure is None:
            logger.error("Failed to retrieve expected structure")
            return False, "Failed to retrieve expected structure."
        
        differences = self.compare_structures(current_structure, expected_structure)
        
        if differences != "No differences found.":
            logger.warning("Schema validation failed. Current structure does not match expected structure.")
            return False, differences
        
        return True, "Schema is valid."

    @error_handler
    def database_exists(self):
        logger.info("Checking if database exists")
        exists = os.path.exists(self.database_manager.db_path)
        if not exists:
            logger.info(f"Database file not found at {self.database_manager.db_path}")
        return exists

    @error_handler
    def get_current_structure(self):
        logger.info("Getting current database structure")
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';"
        results = self.database_manager.execute_query(query)
        
        current_structure = {}
        
        for result in results:
            table_name = result[0]
            # Get column information for each table
            column_query = f"PRAGMA table_info({table_name});"
            columns_info = self.database_manager.execute_query(column_query)
            columns = [{'name': col[1], 'type': col[2]} for col in columns_info]
            
            current_structure[table_name] = columns
        
        return current_structure

    @error_handler
    def get_expected_structure(self):
        logger.info("Getting expected database structure")
        if self._expected_structure is None:
            # Ensure this method returns a structured format of expected tables/columns
            self._expected_structure = self.database_manager.schema_manager.get_table_definitions()
        
        if self._expected_structure is None:
            logger.error("Failed to load expected structure")
        
        return self._expected_structure

    @error_handler
    def compare_structures(self, current_structure, expected_structure):
        differences = []

        # Check for missing or extra tables
        current_tables = set(current_structure.keys())
        expected_tables = set(expected_structure.keys())

        missing_in_expected = current_tables - expected_tables - {'sqlite_sequence'}  # Ignore sqlite_sequence
        missing_in_current = expected_tables - current_tables
        
        if missing_in_expected:
            differences.append(f"Extra tables in current structure: {', '.join(missing_in_expected)}")
        
        if missing_in_current:
            differences.append(f"Missing tables in current structure: {', '.join(missing_in_current)}")

        # Check for column discrepancies in each table
        for table in current_tables.intersection(expected_tables):
            current_columns = {col['name']: col['type'] for col in current_structure[table]}
            expected_columns = {col['name']: col['type'] for col in expected_structure[table]}
            
            for col_name in set(current_columns.keys()).union(expected_columns.keys()):
                curr_type = current_columns.get(col_name, 'Missing')
                exp_type = expected_columns.get(col_name, 'Missing')
                if curr_type != exp_type:
                    differences.append(f"Column mismatch in table '{table}': Column '{col_name}': Current Type: {curr_type}, Expected Type: {exp_type}")

        return "\n".join(differences) if differences else "No differences found."

    @error_handler
    def refresh_schema_cache(self):
        logger.info("Refreshing schema cache")
        self._current_structure = None
        self._expected_structure = None
        logger.info("Schema cache cleared")