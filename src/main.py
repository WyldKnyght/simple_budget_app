# src/main.py
import sys
from PyQt6.QtWidgets import QApplication
from user_interface.main_window import MainWindow
from controllers.database_controllers import db_manager

def main():
    app = QApplication(sys.argv)
    
    # Initialize database connection
    db_manager.connect()
    db_manager.create_tables()
    
    window = MainWindow()
    window.show()
    
    exit_code = app.exec()
    
    # Close database connection
    db_manager.close()
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main()