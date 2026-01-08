from typing import Any, Dict


def validate_tool_input(input_data: Dict[str, Any]) -> None:
    """
    Validate input before tool execution.
    """
    if "tool" not in input_data:
        raise ValueError("Missing tool name in input")

    if "input" not in input_data:
        raise ValueError("Missing tool input payload")

