# src/views/main_window.py
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from .budget_tab import BudgetTab
from .transactions_tab import TransactionsTab
from .reports_tab import ReportsTab
from .settings_tab import SettingsTab
from utils.custom_logging import logger
from configs.ui_config import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT
from controllers.settings_tab_controller import SettingsTabController
from controllers.database_controllers import DatabaseController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.status_bar = self.statusBar()
        
        self.db_controller = DatabaseController()
        self.db_controller.check_database()

        self.settings_controller = SettingsTabController(self.db_controller)
        logger.debug("Category tree after initialization:")
        categories = self.settings_controller.category.get_categories()
        logger.debug(f"Total categories: {len(categories)}")
        self.settings_controller.print_category_tree()

        # Call init_ui() to set up the UI components
        self.init_ui()
        logger.info("Main window initialized")

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.tab_widget = QTabWidget()
        self.create_tabs()
        layout.addWidget(self.tab_widget)
        central_widget.setLayout(layout)

        logger.info(f"UI components initialized. Number of tabs: {self.tab_widget.count()}")

    def create_tabs(self):
        self.tab_widget.addTab(self.create_dashboard_tab(), "Dashboard")
        self.tab_widget.addTab(BudgetTab(self.db_controller), "Budget")
        self.tab_widget.addTab(TransactionsTab(self.db_controller), "Transactions")
        self.tab_widget.addTab(ReportsTab(self.db_controller), "Reports")
        self.tab_widget.addTab(SettingsTab(self.settings_controller), "Settings")
        logger.info(f"Tabs created. Total tabs: {self.tab_widget.count()}")

    def closeEvent(self, event):
        self.db_controller.close_connection()
        super().closeEvent(event)

    def create_dashboard_tab(self):
        dashboard_tab = QWidget()
        dashboard_layout = QVBoxLayout()
        dashboard_layout.addWidget(QLabel("Dashboard - To be implemented"))
        dashboard_tab.setLayout(dashboard_layout)
        logger.info("Dashboard tab created")
        return dashboard_tab