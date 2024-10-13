# src/user_interface/settings_tab_modules/categories_tab.py
from PyQt6.QtWidgets import QVBoxLayout, QTreeView, QPushButton, QHBoxLayout
from ..common.base_tab import BaseTab
from .categories_tab_modules.categories_manager import CategoriesManager
from controllers.settings_tab_controllers.categories_controller import CategoriesController
from configs.constants import (CATEGORY_TAB_TITLE, ADD_CATEGORY_BUTTON_TEXT,
                               EDIT_CATEGORY_BUTTON_TEXT, DELETE_CATEGORY_BUTTON_TEXT)
from utils.custom_logging import logger

class CategoriesTab(BaseTab):
    def __init__(self, db_manager, settings_tab_controller):
        super().__init__(db_manager, CategoriesController)
        self.settings_tab_controller = settings_tab_controller
        self.categories_manager = CategoriesManager(self, self.controller)
        self.init_ui()

    def init_ui(self):
        try:
            layout = QVBoxLayout()

            self.tree_view = QTreeView()
            self.tree_view.setEditTriggers(QTreeView.EditTrigger.NoEditTriggers)
            layout.addWidget(self.tree_view)

            button_layout = QHBoxLayout()
            self.add_button = QPushButton(ADD_CATEGORY_BUTTON_TEXT)
            self.edit_button = QPushButton(EDIT_CATEGORY_BUTTON_TEXT)
            self.delete_button = QPushButton(DELETE_CATEGORY_BUTTON_TEXT)
            button_layout.addWidget(self.add_button)
            button_layout.addWidget(self.edit_button)
            button_layout.addWidget(self.delete_button)
            layout.addLayout(button_layout)

            self.setLayout(layout)

            self.add_button.clicked.connect(self.categories_manager.add_category)
            self.edit_button.clicked.connect(self.categories_manager.edit_category)
            self.delete_button.clicked.connect(self.categories_manager.delete_category)

            self.setWindowTitle(CATEGORY_TAB_TITLE)
            self.load_categories()
        except Exception as e:
            logger.error(f"Error in CategoriesTab init_ui: {e}")

    def load_categories(self):
        try:
            self.categories_manager.load_categories(self.tree_view)
        except Exception as e:
            logger.error(f"Error loading categories: {e}")

    def refresh(self):
        self.load_categories()