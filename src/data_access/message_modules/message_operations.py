# src/data_access/message_operations.py

class MessageOperations:
    def get_message(self, message_key):
        # This method would typically fetch messages from a database
        # For now, we'll use the error_config as a simple key-value store
        return globals().get(message_key, "Message not found")