# src/database_app.py

import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit
from configs.path_config import DB_PATH  # Importing DB_PATH from config
from data_access.database_manager import DatabaseManager
from data_access.db_modules.db_reset_database import ResetDatabase  # Importing ResetDatabase
from data_access.schema_manager import SchemaOperations  # Importing SchemaOperations
from utils.custom_logging import logger

class DatabaseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager()
        self.reset_db_manager = ResetDatabase(self.db_manager.connections)  # Initialize ResetDatabase
        self.schema_operations = SchemaOperations()  # Initialize SchemaOperations
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Database Manager Test App")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Button to validate schema
        validate_schema_button = QPushButton("Validate Schema")
        validate_schema_button.clicked.connect(self.validate_schema)
        layout.addWidget(validate_schema_button)

        # Button to reset database
        reset_db_button = QPushButton("Reset Database")
        reset_db_button.clicked.connect(self.reset_database)
        layout.addWidget(reset_db_button)

        # Button to display database layout and compare with schema
        compare_layout_button = QPushButton("Compare Database Layout with Schema")
        compare_layout_button.clicked.connect(self.compare_layout_with_schema)
        layout.addWidget(compare_layout_button)

        # Label to display results
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Text area to display detailed output
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        layout.addWidget(self.output_display)

        # Set the central widget and layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def validate_schema(self):
        try:
            is_valid, message = self.db_manager.validation_operations.validate_schema()
            
            if is_valid:
                self.result_label.setText("Schema is valid.")
                logger.info("Schema is valid.")
            else:
                self.result_label.setText(f"Schema validation failed:\n{message}")
                logger.warning(f"Schema validation failed:\n{message}")

            # Fetch and display both current and expected schemas for manual comparison
            current_structure = self.db_manager.validation_operations.get_current_structure()
            expected_structure = self.schema_operations.get_table_definitions()

            if current_structure:
                self.output_display.append("Current Database Structure:\n")
                self.output_display.append(str(current_structure))

            if expected_structure:
                self.output_display.append("\nExpected Structure:\n")
                self.output_display.append(str(expected_structure))

        except Exception as e:
            self.result_label.setText(f"Error during validation: {str(e)}")
            logger.error(f"Error during validation: {str(e)}")

    def reset_database(self):
        try:
            success, message = self.reset_db_manager.reset_database()  # Call reset on ResetDatabase instance
            if success:
                self.result_label.setText("Database reset successfully.")
                logger.info("Database reset successfully.")
            else:
                self.result_label.setText(f"Reset failed: {message}")
                logger.error(f"Reset failed: {message}")
            self.output_display.append(message)  # Display output in text area
        except Exception as e:
            self.result_label.setText(f"Error during reset: {str(e)}")
            logger.error(f"Error during reset: {str(e)}")

    def compare_layout_with_schema(self):
        try:
            current_layout = self.get_database_structure()  # Fetch current database structure
            expected_schema = self.schema_operations.get_schema()  # Fetch expected schema

            if current_layout is None or expected_schema is None:
                raise Exception("Could not retrieve current layout or expected schema.")

            # Display both layouts for comparison
            self.output_display.clear()  # Clear previous output
            self.output_display.append("Current Database Layout:\n")
            for table_name, columns in current_layout.items():
                self.output_display.append(f"Table: {table_name}")
                for column in columns:
                    self.output_display.append(f" - Column: {column['name']} (Type: {column['type']})")
                self.output_display.append("")  # Blank line between tables

            self.output_display.append("\nExpected Schema:\n")
            self.output_display.append(expected_schema)  # Display expected schema
            
            logger.info("Displayed current database layout and expected schema for comparison.")
        
        except Exception as e:
            self.result_label.setText(f"Error comparing layouts: {str(e)}")
            logger.error(f"Error comparing layouts: {str(e)}")

    def get_database_structure(self):
        """Fetches the current structure of the database (tables and their columns)."""
        
        conn = sqlite3.connect(DB_PATH)  # Connect to the database using the path from config
        
        try:
            cursor = conn.cursor()
            
            # Get all table names
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            db_structure = {}
            
            for table in tables:
                table_name = table[0]
                
                # Get column information for each table
                cursor.execute(f"PRAGMA table_info({table_name});")
                columns_info = cursor.fetchall()
                
                columns = [{'name': col[1], 'type': col[2]} for col in columns_info]
                db_structure[table_name] = columns
            
            return db_structure
        
        except Exception as e:
            logger.error(f"Failed to retrieve database structure: {str(e)}")
            return None
        
        finally:
            conn.close()  # Ensure connection is closed after operation

def main():
    app = QApplication(sys.argv)
    window = DatabaseApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()