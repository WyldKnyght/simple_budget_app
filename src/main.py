# src/main.py
import sys
from PyQt6.QtWidgets import QApplication
from utils.custom_logging import setup_logging, logger
from views.main_window import MainWindow

def main():
    setup_logging()
    logger.info("Initializing application...")

    app = QApplication(sys.argv)

    try:
        main_window = MainWindow()
        main_window.show()

        logger.info("Application initialized successfully.")
        sys.exit(app.exec())
    except Exception as e:
        logger.error(f"An error occurred during application initialization: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()