from typing import Dict, Any
from app.orchestration.agent_manager import AgentManager


def run_workflow(
    agent_manager: AgentManager,
    workflow_name: str,
    input_data: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Entry point for executing named workflows.
    """
    # For now, workflows map directly to a single agent.
    return agent_manager.run_agent(workflow_name, input_data)

