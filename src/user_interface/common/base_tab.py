# src/user_interface/common/base_tab.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout

class BaseTab(QWidget):
    def __init__(self, db_manager, controller_class=None):
        super().__init__()
        self.db_manager = db_manager
        if controller_class is not None:
            self.controller = controller_class(db_manager)

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

    def refresh(self):
        self.controller.load_data()