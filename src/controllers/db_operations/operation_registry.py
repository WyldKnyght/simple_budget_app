# src/controllers/operation_registry.py
from typing import Dict, Callable, Optional, List
from utils.custom_logging import logger

class OperationRegistry:
    def __init__(self):
        self.operations: Dict[str, Callable] = {}

    def register(self, name: str, operation: Callable) -> None:
        """Register an operation with the given name."""
        if name in self.operations:
            logger.warning(f"Operation '{name}' is being overwritten.")
        self.operations[name] = operation
        logger.info(f"Operation '{name}' registered successfully.")

    def get(self, name: str) -> Optional[Callable]:
        """Retrieve an operation by its name."""
        operation = self.operations.get(name)
        if operation is None:
            logger.warning(f"Operation '{name}' not found in registry.")
        return operation

    def unregister(self, name: str) -> None:
        """Unregister an operation by its name."""
        if name in self.operations:
            del self.operations[name]
            logger.info(f"Operation '{name}' unregistered successfully.")
        else:
            logger.warning(f"Attempted to unregister non-existent operation '{name}'.")

    def list_operations(self) -> List[str]:
        """List all registered operation names."""
        return list(self.operations.keys())