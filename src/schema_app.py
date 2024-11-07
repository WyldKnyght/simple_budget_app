# src/schema_app.py

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit
from data_access.schema_manager import SchemaManager
from utils.custom_logging import logger

class SchemaApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.schema_manager = SchemaManager()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Schema Manager Test App")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Button to load schema
        load_schema_button = QPushButton("Load Schema")
        load_schema_button.clicked.connect(self.load_schema)
        layout.addWidget(load_schema_button)

        # Button to get table names
        get_table_names_button = QPushButton("Get Table Names")
        get_table_names_button.clicked.connect(self.get_table_names)
        layout.addWidget(get_table_names_button)

        # Button to get columns for a specific table
        self.table_name_input = QPushButton("Get Columns for 'Accounts' Table")
        self.table_name_input.clicked.connect(self.get_table_columns)
        layout.addWidget(self.table_name_input)

        # Label to display results
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Text area to display schema content
        self.schema_display = QTextEdit()
        self.schema_display.setReadOnly(True)
        layout.addWidget(self.schema_display)

        # Set the central widget and layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_schema(self):
        if schema := self.schema_manager.load_schema():
            self.schema_display.setPlainText(schema)  # Displaying the schema content
            logger.info("Schema loaded successfully.")
            self.result_label.setText("Schema loaded successfully.")
        else:
            logger.error("Failed to load schema.")
            self.result_label.setText("Failed to load schema.")

    def get_table_names(self):
        if table_names := self.schema_manager.get_table_names():
            self.result_label.setText(f"Table Names: {', '.join(table_names)}")
            logger.info(f"Table Names: {', '.join(table_names)}")
        else:
            self.result_label.setText("No tables found.")
            logger.warning("No tables found.")

    def get_table_columns(self):
        if columns := self.schema_manager.get_table_columns('Accounts'):
            self.result_label.setText(f"Columns in 'Accounts': {', '.join(columns)}")
            logger.info(f"Columns in 'Accounts': {', '.join(columns)}")
        else:
            self.result_label.setText("No columns found for 'Accounts'.")
            logger.warning("No columns found for 'Accounts'.")

def main():
    app = QApplication(sys.argv)
    window = SchemaApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()