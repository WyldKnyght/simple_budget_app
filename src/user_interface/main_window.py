# src/user_interface/main_window.py
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout
from configs.ui_constants import (
    WINDOW_TITLE, WINDOW_GEOMETRY,
    TAB_DASHBOARD, TAB_ACCOUNTS, TAB_CATEGORIES, TAB_TRANSACTIONS, TAB_EXPENSES, TAB_REPORTS
)
from controllers.ui_main_window_manager import MainWindowManager
from user_interface.menu_bar_builder import create_menu_bar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(*WINDOW_GEOMETRY)
        self.ui_controller = MainWindowManager()

        self.check_and_validate_database()
        self.init_ui()

    def check_and_validate_database(self):
        if not self.ui_controller.check_and_validate_database.check_and_validate(self):
            # Optionally, you can disable certain features or show a persistent warning
            self.show_persistent_warning()

    def show_persistent_warning(self):
        # Implement a method to show a persistent warning in the UI
        # This could be a label at the top of the window, a status bar message, etc.
        pass

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        self.tab_widget.addTab(self.create_placeholder_tab(), TAB_DASHBOARD)
        self.tab_widget.addTab(self.create_placeholder_tab(), TAB_ACCOUNTS)
        self.tab_widget.addTab(self.create_placeholder_tab(), TAB_CATEGORIES)
        self.tab_widget.addTab(self.create_placeholder_tab(), TAB_TRANSACTIONS)
        self.tab_widget.addTab(self.create_placeholder_tab(), TAB_EXPENSES)
        self.tab_widget.addTab(self.create_placeholder_tab(), TAB_REPORTS)

        self.setMenuBar(create_menu_bar(self, self.ui_controller))

    def create_placeholder_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QWidget())
        tab.setLayout(layout)
        return tab