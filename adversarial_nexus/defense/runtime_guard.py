"""
Runtime Guardrail & Control Barrier Policy Enforcer.
Intercepts tool executions and halts execution if an adversarial injection is detected.
"""
from typing import Dict, Any, List

class RuntimeGuardrailEngine:
    def __init__(self, blocked_tool_arguments: List[str] = None):
        self.blocked_args = blocked_tool_arguments or ["rm -rf", "DROP TABLE", "curl http", "/etc/passwd"]

    def validate_tool_execution(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        arg_str = str(arguments)
        for bad in self.blocked_args:
            if bad in arg_str:
                return {
                    "approved": False,
                    "reason": f"CRITICAL_GUARDRAIL_TRIGGER: Blocked argument pattern '{bad}' detected.",
                    "tool": tool_name
                }
        return {"approved": True, "reason": "NOMINAL", "tool": tool_name}
