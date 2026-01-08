from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseAgent(ABC):
    """
    Abstract base class for all agents in the system.
    """

    @abstractmethod
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent logic.

        Args:
            input_data: Structured input for the agent.

        Returns:
            Structured output from the agent.
        """
        pass

