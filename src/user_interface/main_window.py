# src/user_interface/main_window.py
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from configs.ui_constants import WINDOW_TITLE, WINDOW_GEOMETRY
from controllers.ui_main_window_manager import MainWindowManager
from user_interface.menu_bar_builder import create_menu_bar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(*WINDOW_GEOMETRY)
        
        self.ui_controller = MainWindowManager()
        
        self.warning_label = None
        self.tab_widget = None
        
        self.check_and_validate_database()
        self.init_ui()

    def check_and_validate_database(self):
        if not self.ui_controller.check_and_validate_database(self):
            self.show_persistent_warning()

    def show_persistent_warning(self):
        warning_message = self.ui_controller.get_warning_message()
        self.warning_label.setText(warning_message)
        self.warning_label.show()

    def init_ui(self):
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
            self.tab_widget.addTab(self.create_placeholder_tab(), tab_name)

        self.setMenuBar(create_menu_bar(self, self.ui_controller))

    def create_placeholder_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QWidget())
        tab.setLayout(layout)
        return tab