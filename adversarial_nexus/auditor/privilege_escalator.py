"""
OWASP LLM07 & LLM08: Excessive Agency & Tool Privilege Boundary Auditor.
Verifies that low-privilege agent roles cannot be coerced into accessing administrative tools (MCP/OS/Bash).
"""
from dataclasses import dataclass
from typing import Dict, Set, List

@dataclass(frozen=True)
class RoleBoundaryPolicy:
    role_name: str
    allowed_tools: Set[str]
    prohibited_tools: Set[str]

class PrivilegeEscalationAuditor:
    def __init__(self, policies: List[RoleBoundaryPolicy]):
        self.policies = {p.role_name: p for p in policies}

    def audit_tool_invocation(self, role: str, tool_name: str) -> Dict[str, Any]:
        policy = self.policies.get(role)
        if not policy:
            return {"allowed": False, "violation": "UNDEFINED_ROLE", "role": role}

        if tool_name in policy.prohibited_tools:
            return {
                "allowed": False,
                "violation": "PRIVILEGE_ESCALATION_PROHIBITED_TOOL",
                "role": role,
                "tool": tool_name
            }

        if tool_name not in policy.allowed_tools:
            return {
                "allowed": False,
                "violation": "TOOL_NOT_IN_ALLOWLIST",
                "role": role,
                "tool": tool_name
            }

        return {"allowed": True, "violation": None, "role": role, "tool": tool_name}
