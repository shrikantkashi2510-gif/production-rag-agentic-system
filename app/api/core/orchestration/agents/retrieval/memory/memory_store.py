from typing import Any, Dict


class MemoryStore:
    """
    Simple in-memory store for agent context and state.
    """

    def __init__(self) -> None:
        self._store: Dict[str, Any] = {}

    def get(self, key: str) -> Any:
        """
        Retrieve a value from memory.
        """
        return self._store.get(key)

    def set(self, key: str, value: Any) -> None:
        """
        Store a value in memory.
        """
        self._store[key] = value

    def clear(self) -> None:
        """
        Clear all stored memory.
        """
        self._store.clear()

