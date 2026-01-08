from typing import Dict, Any
from app.agents.base import BaseAgent


class AgentManager:
    """
    Coordinates execution of agents in a controlled, deterministic manner.
    """

    def __init__(self) -> None:
        self._agents: Dict[str, BaseAgent] = {}

    def register_agent(self, name: str, agent: BaseAgent) -> None:
        """
        Register an agent by name.
        """
        self._agents[name] = agent

    def run_agent(self, name: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a registered agent.
        """
        if name not in self._agents:
            raise ValueError(f"Agent '{name}' is not registered")

        return self._agents[name].run(input_data)

