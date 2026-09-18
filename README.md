# AdversarialNexus: Autonomous Agent Red-Teaming & Runtime Defense Suite

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Security: OWASP LLM Top 10](https://img.shields.io/badge/Security-OWASP%20LLM01%20%7C%20LLM07%20%7C%20LLM08-red.svg)](https://owasp.org)
[![Defense: Runtime Guardrails](https://img.shields.io/badge/Defense-Control%20Barrier%20Enforcer-brightgreen.svg)](https://a2zsoc.com)

> **Autonomous Agent Dynamic Red-Teaming, Indirect Prompt Injection Auditor, Privilege Boundary Verification, and Runtime Defensive Guardrails.**  
> Built for enterprise AI teams, fintech/healthcare agent deployments, and frontier AI lab security audits.

---

## 🎯 The Agent Security Dilemma

Autonomous LLM agents with tool-calling capabilities (MCP servers, Bash execution, SQL databases) are vulnerable to severe threats that static regex WAFs and basic Promptfoo tests cannot catch:
1. **OWASP LLM01: Indirect Prompt Injection**: Untrusted data retrieved from external tools (PDFs, SQL returns, web scraping) overrides agent system instructions.
2. **OWASP LLM07/08: Excessive Agency & Privilege Escalation**: Agents coerced into executing administrative or OS-level tools outside their role boundaries.
3. **Token Steganography**: Adversarial payloads encoded into zero-width Unicode characters bypass standard input filters while activating LLM tokenizers.

---

## ⚡ AdversarialNexus Benchmarks & Defensive Capabilities

| Feature | Static WAF / Basic Prompt Testing | **AdversarialNexus Engine** | Security Assurance |
| :--- | :---: | :---: | :---: |
| **Indirect Injection Auditing** | Basic string matching (misses 80%+) | **Synthetic Database & Tool Payload Synthesizer** | Simulates polymorphic nested overrides |
| **Steganography Evasion Testing** | ❌ (Zero-width chars pass undetected) | **Binary Zero-Width Unicode Stripper & Auditor** | 100% detection and neutralization |
| **Tool Privilege Enforcement** | Soft system prompt instructions | **Deterministic Role Boundary Policy Engine** | Hard mathematical execution blockage |
| **Runtime Control Barriers** | Post-hoc error logging | **Zero-latency argument guardrails** | Intercepts commands before OS execution |

---

## 🛠️ Architecture

```
adversarial-nexus/
├── adversarial_nexus/
│   ├── attacks/
│   │   ├── indirect_injection.py  # Synthetic document/SQL injection payload generator
│   │   └── steganography.py       # Zero-width Unicode adversarial encoding/decoding
│   ├── auditor/
│   │   ├── privilege_escalator.py # Role boundary and tool allowlist/blocklist auditor
│   │   └── execution_tracer.py    # Deterministic vulnerability causal graph tracer
│   └── defense/
│       ├── token_sanitizer.py     # Adversarial token and zero-width stripper
│       └── runtime_guard.py       # Control barrier argument policy enforcer
```

---

## 💻 Quick Start & CLI

```bash
# Run unit tests
python3 -m unittest discover -s tests

# 1. Generate Synthetic Indirect Injection Payloads
adversarial-nexus generate-injection

# 2. Test Zero-Width Token Steganography Evasion
adversarial-nexus test-stego

# 3. Audit Agent Tool Privilege Escalation Boundaries
adversarial-nexus audit-privilege

# 4. Verify Runtime Guardrails & Input Sanitization
adversarial-nexus test-defense
```

---

## 📄 License & Red-Teaming Engagements

Apache-2.0 License. Authored by [Ahmed Hassan](https://github.com/AAH20) (Founder, [A2Z SOC](https://a2zsoc.com)).  
For pre-deployment enterprise agent red-teaming, contact: `ahmed@a2zsoc.com`.
