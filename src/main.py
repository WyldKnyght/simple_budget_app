# src/main.py

import sys
from PyQt6.QtWidgets import QApplication
from user_interface.main_window import MainWindow
from controllers.database_manager import DatabaseManager

def main():
    app = QApplication(sys.argv)
    db_manager = DatabaseManager()
    window = MainWindow(db_manager)
    window.show()
    exit_code = app.exec()
    db_manager.close()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()