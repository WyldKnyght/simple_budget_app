# src/controllers/operation_registry.py
class OperationRegistry:
    def __init__(self):
        self.operations = {}

    def register(self, name: str, operation: callable):
        self.operations[name] = operation

    def get(self, name: str) -> callable:
        return self.operations.get(name)