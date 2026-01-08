from typing import Dict, Any
from app.orchestration.agent_manager import AgentManager
from app.agents.tool_agent import ToolAgent
from app.safety.guardrails import validate_tool_input


def run_demo_workflow(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Demonstration workflow showing deterministic agent execution.
    """

    # Simple demo tool
    def echo_tool(payload: Any) -> Any:
        return payload

    # Initialize agent manager
    agent_manager = AgentManager()

    # Register tool-using agent
    tools = {"echo": echo_tool}
    tool_agent = ToolAgent(tools=tools)
    agent_manager.register_agent("tool_agent", tool_agent)

    # Validate input before execution
    validate_tool_input(input_data)

    # Execute workflow
    return agent_manager.run_agent("tool_agent", input_data)
