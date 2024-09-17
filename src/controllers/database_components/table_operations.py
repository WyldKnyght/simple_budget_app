# src/controllers/database_components/table_operations.py

from sqlite3 import Error
from utils.custom_logging import logger
from configs.settings_config import DEFAULT_CATEGORIES
from configs.app_config import SCHEMA_FILE_PATH

class TableOperations:
    def __init__(self, db_controller):
        self.db_controller = db_controller

    def create_tables(self):
        try:
            with open(SCHEMA_FILE_PATH, 'r') as f:
                schema_sql = f.read()
            
            # Execute SQL commands one by one
            for statement in schema_sql.split(';'):
                statement = statement.strip()
                if statement:
                    self.db_controller.execute_query(statement)
                    
            logger.info("Tables created successfully.")
        except FileNotFoundError:
            logger.error(f"Schema file not found at {SCHEMA_FILE_PATH}")
        except Error as e:
            logger.error(f"Error while creating tables: {e}")
        except Exception as e:
            logger.error(f"Unexpected error while creating tables: {e}")

    def initialize_default_data(self):
        if not self.table_exists('Categories'):
            # Insert parent categories
            for category in DEFAULT_CATEGORIES:
                parent_id = None if category['name'] == 'Income' else 1
                self.db_controller.execute_query("""
                    INSERT OR IGNORE INTO Categories (parent_id, name, subcategories)
                    VALUES (?, ?, ?)
                """, (parent_id, category['name'], '[]'))

            # Insert subcategories
            for category in DEFAULT_CATEGORIES:
                if category.get('subcategories'):
                    for subcategory in category['subcategories']:
                        self.db_controller.execute_query("""
                            INSERT OR IGNORE INTO Categories (parent_id, name, subcategories)
                            VALUES (?, ?, ?)
                        """, (category['name'], subcategory['name'], '[]'))

            logger.info("Default categories added.")
        else:
            logger.info("Categories table already populated.")

    def table_exists(self, table_name):
        query = """SELECT name FROM sqlite_master WHERE type='table' AND name=?"""
        result = self.db_controller.fetch_all_records(query, (table_name,))
        return len(result) > 0

    def create_table_if_not_exists(self, table_name, create_statement):
        if not self.table_exists(table_name):
            self.db_controller.execute_query(create_statement)
            logger.info(f"Created table: {table_name}")
        else:
            logger.info(f"Table {table_name} already exists.")