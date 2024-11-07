# src/controllers/services/help_service.py

import webbrowser
from pathlib import Path
from utils.custom_logging import logger
from configs.path_config import DOCUMENTS_PATH

class HelpService:
    def __init__(self):
        self.docs_path = Path(DOCUMENTS_PATH)

    def open_help_topic(self, topic):
        logger.info(f"Opening help topic: {topic}")
        file_path = self.docs_path / f"{topic}.md"
        if file_path.exists():
            webbrowser.open(str(file_path))
            return True
        else:
            logger.error(f"Help file not found: {file_path}")
            return False

    def get_available_topics(self):
        return [file.stem for file in self.docs_path.glob('*.md')]