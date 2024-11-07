# src/user_interface/ui_main_window.py

from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from configs.ui_constants import WINDOW_TITLE, WINDOW_GEOMETRY
from controllers.main_window_manager import MainWindowManager
from user_interface.main_window_modules.menu_bar_builder import create_menu_bar
from utils.custom_logging import logger

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(*WINDOW_GEOMETRY)
        
        self.ui_controller = MainWindowManager()
        
        self.warning_label = None
        self.tab_widget = None
        
        if self.initialize_database():
            self.init_ui()
        else:
            self.close()

    def initialize_database(self):
        logger.info("Initializing database")
        success = self.ui_controller.initialize_database(self)
        if not success:
            logger.error("Database initialization failed")
            self.close()
        return success

    def check_and_validate_database(self):
        logger.info("Checking and validating database")
        is_valid = self.ui_controller.validate_database()
        if not is_valid:
            logger.warning("Database validation failed")
            self.show_persistent_warning("Database schema is invalid. Please reset the database.")
        return is_valid

    def show_persistent_warning(self, message):
        if self.warning_label:
            self.warning_label.setText(message)
            self.warning_label.show()
        else:
            logger.error("Warning label not initialized")

    def show_error_message(self, title, message):
        self.ui_controller.show_error_message(self, title, message)

    def init_ui(self):
        logger.info("Initializing UI")
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.warning_label = QLabel()
        self.warning_label.setStyleSheet(self.ui_controller.get_warning_label_style())
        self.warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warning_label.hide()
        main_layout.addWidget(self.warning_label)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        for tab_name in self.ui_controller.get_tab_structure():
            tab = self.ui_controller.create_placeholder_tab(tab_name)
            self.tab_widget.addTab(tab, tab_name)

        self.setMenuBar(create_menu_bar(self, self.ui_controller))

        # Check and validate database after UI is initialized
        self.check_and_validate_database()