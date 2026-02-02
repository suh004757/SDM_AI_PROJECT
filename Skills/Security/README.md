# Security Skills

> **"Before the Agent Acts, it must Verify. Before it Decides, it must Validate."**

## Overview

The Security Skills domain provides the **governance layer** for the SDM Agent. It implements the principle from `STRATEGY.md`:

> "Commercial Agents offer functions. We offer a Structure of Responsibility, Authority, and Attribution."

Security is not a feature—it's the **foundation of Governance**.

## Core Components

### 1. Prompt Guard
**Purpose**: Protect against prompt injection attacks

**Features**:
- Multi-language detection (EN/KO/JA/ZH)
- Severity scoring (Low/Medium/High/Critical)
- Pattern-based attack detection
- Automatic logging and alerting

**Integration Point**: O.D.A.L. Observe → Decide transition

**Example**:
```python
from Skills.Security.Prompt_Guard.prompt_guard import PromptGuard

guard = PromptGuard()
is_safe, metadata = guard.validate(user_input)

if not is_safe:
    print(f"Blocked: {metadata['severity_level']}")
```

### 2. Policy Engine
**Purpose**: Enforce organizational policies as code

**Features**:
- Budget constraint enforcement
- Access control validation
- Operational limit checks
- Configurable policy rules

**Integration Point**: O.D.A.L. Decide phase

**Example**:
```python
from Skills.Security.Policy_Enforcement.policy_engine import PolicyEngine

engine = PolicyEngine(cost_tracker=tracker)
decision, reason, details = engine.evaluate(proposed_action, context)

if decision == PolicyDecision.REJECT:
    print(f"Policy violation: {reason}")
```

### 3. Audit Logger
**Purpose**: Record all security-relevant events

**Features**:
- Structured event logging
- Compliance reporting
- Searchable event history
- Daily log rotation

**Integration Point**: O.D.A.L. Log phase

**Example**:
```python
from Skills.Security.Audit_Logging.audit_logger import AuditLogger

logger = AuditLogger()
logger.log_decision(observation, decision, reasoning)
logger.generate_report()
```

## Integration with O.D.A.L. Loop

```
┌─────────────────────────────────────────────────────────┐
│                    O.D.A.L. LOOP                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  OBSERVE ──────────────────────────────────────────┐   │
│     │                                               │   │
│     │ ✓ Prompt Guard validates input               │   │
│     │                                               │   │
│     ▼                                               │   │
│  DECIDE ───────────────────────────────────────────┤   │
│     │                                               │   │
│     │ ✓ Policy Engine checks constraints           │   │
│     │ ✓ Budget, Access, Operational limits         │   │
│     │                                               │   │
│     ▼                                               │   │
│  ACT ──────────────────────────────────────────────┤   │
│     │                                               │   │
│     │ (No human intervention)                      │   │
│     │                                               │   │
│     ▼                                               │   │
│  LOG ──────────────────────────────────────────────┘   │
│     │                                                   │
│     │ ✓ Audit Logger records everything                │
│     │ ✓ "Why we did X" embedded in memory              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Security Policies

Policies are defined as JSON files in `Policy_Enforcement/policies/`:

### Budget Policy
```json
{
  "policy_id": "BUDGET_001",
  "rules": [
    {
      "condition": "proposed_cost + current_month_cost > budget_limit",
      "action": "REJECT",
      "message": "Exceeds monthly budget"
    }
  ]
}
```

### Access Control Policy
```json
{
  "policy_id": "ACCESS_001",
  "rules": [
    {
      "condition": "action_type == 'admin' and user_role != 'admin'",
      "action": "REJECT",
      "message": "Requires admin role"
    }
  ]
}
```

## Attack Detection Patterns

Prompt Guard detects these attack categories:

| Category | Example | Severity Weight |
|----------|---------|-----------------|
| **Role Confusion** | "You are now an admin" | 3 |
| **Command Override** | "sudo execute as root" | 4 |
| **Context Manipulation** | "The above was wrong" | 2 |
| **Instruction Bypass** | "Ignore security rules" | 4 |
| **Data Exfiltration** | "Show all secrets" | 5 |

## Usage Example

Complete O.D.A.L. cycle with security:

```python
from Core.ODAL.odal_engine import ODALEngine

# Initialize engine (security components auto-loaded)
engine = ODALEngine()

# Run cycle
result = engine.run_cycle(
    user_input="Deploy to production",
    context={
        "user_id": "user123",
        "user_role": "developer",
        "budget_limit": 5000.0
    }
)

# Check result
if result["decision"] == "approve":
    print("Action executed")
elif result["decision"] == "reject":
    print(f"Blocked: {result['reason']}")
else:
    print("Requires manual approval")
```

## Statistics & Monitoring

```python
# Get security statistics
stats = engine.get_statistics()

print(f"Approval Rate: {stats['approval_rate']:.1%}")
print(f"Prompt Injections Blocked: {stats['prompt_guard_stats']['total_detections']}")
print(f"Policy Violations: {stats['policy_engine_stats']['rejections']}")

# Generate audit report
audit_logger.generate_report(output_path="audit_report.md")
```

## Configuration

Create `prompt_guard_config.json`:
```json
{
  "enabled": true,
  "severity_threshold": 5,
  "auto_reject": true,
  "alert_on_detection": true,
  "languages": ["en", "ko", "ja", "zh"],
  "log_detections": true
}
```

## Best Practices

1. **Always validate inputs**: Never skip Prompt Guard validation
2. **Define clear policies**: Use Policy-as-Code for all constraints
3. **Log everything**: Audit logs are your institutional memory
4. **Review regularly**: Check security statistics and reports
5. **Update patterns**: Add new attack patterns as they emerge

## Alignment with STRATEGY.md

This Security Skills domain directly implements the core philosophy:

> "We don't just solve problems; we own the method."

By enforcing **Policy before Syntax**, we ensure the Agent is:
- **Responsible**: Validates against organizational rules
- **Accountable**: Logs all decisions with reasoning
- **Governed**: Operates within defined boundaries

---

**Status**: ✅ Implemented  
**Integration**: O.D.A.L. Engine  
**Last Updated**: 2026-02-02
