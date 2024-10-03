# src/user_interface/main_window.py
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QMenuBar, QMenu, QMessageBox
from PyQt6.QtGui import QAction
from .transactions_tab import TransactionsTab
from .settings_tab import SettingsTab
from controllers.database_controllers import db_manager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Family Expense and Income Tracker")
        self.setGeometry(100, 100, 800, 600)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.transactions_tab = TransactionsTab()
        self.settings_tab = SettingsTab()

        self.tab_widget.addTab(self.transactions_tab, "Transactions")
        self.tab_widget.addTab(self.settings_tab, "Settings")

        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        reset_action = QAction("Reset Database", self)
        reset_action.triggered.connect(self.reset_database)
        file_menu.addAction(reset_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def reset_database(self):
        reply = QMessageBox.question(self, 'Reset Database', 
                                     "Are you sure you want to reset the database? This will delete all current data.",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            db_manager.close()
            db_manager.reset_database(self)
            db_manager.connect()
            self.refresh_all_tabs()
            QMessageBox.information(self, "Database Reset", "The database has been reset successfully.")

    def refresh_all_tabs(self):
        self.transactions_tab.load_transactions()
        self.settings_tab.accounts_tab.load_accounts()
        self.settings_tab.categories_tab.load_categories()
        self.settings_tab.expenses_tab.load_expenses()