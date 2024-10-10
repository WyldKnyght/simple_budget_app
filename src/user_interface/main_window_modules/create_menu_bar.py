# src/user_interface/main_window_modules/create_menu_bar.py
from PyQt6.QtWidgets import QMenuBar

def create_menu_bar(main_window):
    menu_bar = QMenuBar(main_window)
    
    # File Menu
    file_menu = menu_bar.addMenu("File")
    
    reset_action = file_menu.addAction("Reset Database")
    reset_action.triggered.connect(main_window.reset_database)
    
    file_menu.addSeparator()
    
    exit_action = file_menu.addAction("Exit")
    exit_action.triggered.connect(main_window.close)
    
    # Help Menu
    help_menu = menu_bar.addMenu("Help")
    
    about_action = help_menu.addAction("About")
    about_action.triggered.connect(main_window.show_about_dialog)
    
    return menu_bar