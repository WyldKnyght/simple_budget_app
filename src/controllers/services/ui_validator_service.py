class UIValidatorService:
    def __init__(self, validation_manager, message_manager):
        self.validation_manager = validation_manager
        self.message_manager = message_manager

    def check_and_validate_database(self, parent):
        return self.validation_manager.check_and_validate_database(parent)

    def get_warning_message(self):
        return self.message_manager.get_message('DB_VALIDATION_WARNING')