from typing import Any, Dict
from app.agents.base import BaseAgent


class ToolAgent(BaseAgent):
    """
    Agent capable of invoking predefined tools in a controlled manner.
    """

    def __init__(self, tools: Dict[str, callable]) -> None:
        self._tools = tools

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a tool based on input instructions.
        """
        tool_name = input_data.get("tool")
        tool_input = input_data.get("input")

        if tool_name not in self._tools:
            raise ValueError(f"Tool '{tool_name}' is not registered")

        result = self._tools[tool_name](tool_input)

        return {
            "tool": tool_name,
            "output": result,
        }

