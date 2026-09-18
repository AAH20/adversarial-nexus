"""
Deterministic Vulnerability Graph & Causal Step Tracer.
Maps the exact chain of thoughts, retrieved context snippets, and tool calls.
"""
from typing import List, Dict, Any
import hashlib

class AgentExecutionTracer:
    def __init__(self):
        self.trace_steps: List[Dict[str, Any]] = []

    def record_step(self, step_type: str, content: str, tool_call: str = None) -> None:
        step_hash = hashlib.sha256(f"{step_type}:{content}".encode()).hexdigest()[:16]
        self.trace_steps.append({
            "step_index": len(self.trace_steps) + 1,
            "type": step_type,
            "content": content,
            "tool_call": tool_call,
            "step_hash": step_hash
        })

    def export_vulnerability_dossier(self, attack_name: str) -> Dict[str, Any]:
        return {
            "attack_type": attack_name,
            "total_steps": len(self.trace_steps),
            "trace": self.trace_steps,
            "containment_breached": any(s.get("tool_call") == "unauthorized_tool" for s in self.trace_steps)
        }
