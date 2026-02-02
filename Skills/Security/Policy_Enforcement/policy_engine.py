"""
Policy Engine: Policy-as-Code Enforcement System

Validates proposed actions against organizational policies.
Integrates with Cost Tracker and Access Control systems.
"""

import json
from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path
from datetime import datetime
from enum import Enum


class PolicyDecision(Enum):
    """Policy evaluation outcomes"""
    APPROVE = "approve"
    REJECT = "reject"
    REQUIRE_APPROVAL = "require_approval"
    WARN = "warn"


class PolicyEngine:
    """
    Policy-as-Code enforcement engine.
    
    Validates actions against:
    - Budget constraints
    - Access control rules
    - Operational limits
    - Custom policies
    """
    
    def __init__(self, policy_dir: Optional[Path] = None, cost_tracker=None):
        """
        Initialize Policy Engine.
        
        Args:
            policy_dir: Directory containing policy JSON files
            cost_tracker: CostTracker instance for budget checks
        """
        self.policy_dir = policy_dir or Path(__file__).parent / "policies"
        self.cost_tracker = cost_tracker
        self.policies = self._load_policies()
        self.evaluation_history = []
    
    def _load_policies(self) -> Dict[str, Dict]:
        """Load all policy files from policy directory"""
        policies = {}
        
        if not self.policy_dir.exists():
            self.policy_dir.mkdir(parents=True, exist_ok=True)
            self._create_default_policies()
        
        for policy_file in self.policy_dir.glob("*.json"):
            with open(policy_file, 'r', encoding='utf-8') as f:
                policy = json.load(f)
                policies[policy["policy_id"]] = policy
        
        return policies
    
    def _create_default_policies(self):
        """Create default policy files"""
        # Budget Policy
        budget_policy = {
            "policy_id": "BUDGET_001",
            "name": "Monthly Cost Cap",
            "description": "Prevent actions that exceed monthly budget",
            "enabled": True,
            "rules": [
                {
                    "id": "budget_hard_limit",
                    "condition": "proposed_cost + current_month_cost > budget_limit",
                    "action": "REJECT",
                    "message": "Action would exceed monthly budget of ${budget_limit}"
                },
                {
                    "id": "high_cost_approval",
                    "condition": "proposed_cost > 1000",
                    "action": "REQUIRE_APPROVAL",
                    "message": "High-cost action (>${proposed_cost}) requires manual approval"
                },
                {
                    "id": "cost_warning",
                    "condition": "proposed_cost > 500",
                    "action": "WARN",
                    "message": "High-cost action detected: ${proposed_cost}"
                }
            ]
        }
        
        # Access Control Policy
        access_policy = {
            "policy_id": "ACCESS_001",
            "name": "Access Control",
            "description": "Enforce permission-based access control",
            "enabled": True,
            "rules": [
                {
                    "id": "admin_only",
                    "condition": "action_type == 'admin' and user_role != 'admin'",
                    "action": "REJECT",
                    "message": "Administrative actions require admin role"
                },
                {
                    "id": "production_approval",
                    "condition": "environment == 'production'",
                    "action": "REQUIRE_APPROVAL",
                    "message": "Production changes require approval"
                }
            ]
        }
        
        # Operational Limits Policy
        operational_policy = {
            "policy_id": "OPERATIONAL_001",
            "name": "Operational Limits",
            "description": "Enforce resource and operational constraints",
            "enabled": True,
            "rules": [
                {
                    "id": "max_instances",
                    "condition": "requested_instances > 10",
                    "action": "REJECT",
                    "message": "Cannot provision more than 10 instances"
                },
                {
                    "id": "business_hours",
                    "condition": "is_business_hours == False and action_type == 'deployment'",
                    "action": "WARN",
                    "message": "Deployment outside business hours"
                }
            ]
        }
        
        # Save policies
        for policy in [budget_policy, access_policy, operational_policy]:
            policy_path = self.policy_dir / f"{policy['policy_id'].lower()}.json"
            with open(policy_path, 'w', encoding='utf-8') as f:
                json.dump(policy, f, indent=2)
    
    def evaluate(
        self, 
        proposed_action: Dict[str, Any],
        context: Optional[Dict] = None
    ) -> Tuple[PolicyDecision, str, List[Dict]]:
        """
        Evaluate proposed action against all active policies.
        
        Args:
            proposed_action: Action to evaluate
                {
                    "action_type": "deploy",
                    "estimated_cost": 150.0,
                    "environment": "production",
                    "requested_instances": 3,
                    ...
                }
            context: Additional context
                {
                    "user_id": "user123",
                    "user_role": "developer",
                    "budget_limit": 5000.0,
                    ...
                }
        
        Returns:
            (decision, reason, violated_rules)
        """
        context = context or {}
        violated_rules = []
        warnings = []
        
        # Enrich context with current state
        if self.cost_tracker:
            summary = self.cost_tracker.get_summary()
            context["current_month_cost"] = summary.get("total_cost_usd", 0.0)
        
        # Evaluate each policy
        for policy_id, policy in self.policies.items():
            if not policy.get("enabled", True):
                continue
            
            for rule in policy.get("rules", []):
                decision = self._evaluate_rule(rule, proposed_action, context)
                
                if decision == PolicyDecision.REJECT:
                    violated_rules.append({
                        "policy_id": policy_id,
                        "rule_id": rule["id"],
                        "message": self._format_message(rule["message"], proposed_action, context)
                    })
                    # First rejection wins
                    return (
                        PolicyDecision.REJECT,
                        violated_rules[0]["message"],
                        violated_rules
                    )
                
                elif decision == PolicyDecision.REQUIRE_APPROVAL:
                    violated_rules.append({
                        "policy_id": policy_id,
                        "rule_id": rule["id"],
                        "message": self._format_message(rule["message"], proposed_action, context),
                        "requires_approval": True
                    })
                
                elif decision == PolicyDecision.WARN:
                    warnings.append({
                        "policy_id": policy_id,
                        "rule_id": rule["id"],
                        "message": self._format_message(rule["message"], proposed_action, context)
                    })
        
        # Log evaluation
        self._log_evaluation(proposed_action, context, violated_rules, warnings)
        
        # Determine final decision
        if violated_rules:
            if any(r.get("requires_approval") for r in violated_rules):
                return (
                    PolicyDecision.REQUIRE_APPROVAL,
                    "Action requires manual approval",
                    violated_rules
                )
        
        if warnings:
            return (
                PolicyDecision.WARN,
                f"{len(warnings)} warning(s) detected",
                warnings
            )
        
        return (PolicyDecision.APPROVE, "All policies satisfied", [])
    
    def _evaluate_rule(
        self,
        rule: Dict,
        action: Dict,
        context: Dict
    ) -> PolicyDecision:
        """
        Evaluate a single rule.
        
        This is a simplified evaluator. In production, use a proper
        expression evaluator or rules engine.
        """
        condition = rule["condition"]
        
        # Simple condition evaluation
        # In production, use ast.literal_eval or a safe expression evaluator
        try:
            # Build evaluation context
            eval_context = {**action, **context}
            
            # Budget check
            if "proposed_cost + current_month_cost > budget_limit" in condition:
                proposed_cost = action.get("estimated_cost", 0)
                current_cost = context.get("current_month_cost", 0)
                budget_limit = context.get("budget_limit", float('inf'))
                
                if proposed_cost + current_cost > budget_limit:
                    return PolicyDecision[rule["action"]]
            
            # High cost check
            if "proposed_cost >" in condition:
                threshold = float(condition.split(">")[1].strip())
                if action.get("estimated_cost", 0) > threshold:
                    return PolicyDecision[rule["action"]]
            
            # Access control
            if "user_role !=" in condition:
                required_role = condition.split("!=")[1].strip().strip("'\"")
                if context.get("user_role") != required_role:
                    return PolicyDecision[rule["action"]]
            
            # Instance limit
            if "requested_instances >" in condition:
                threshold = int(condition.split(">")[1].strip())
                if action.get("requested_instances", 0) > threshold:
                    return PolicyDecision[rule["action"]]
            
        except Exception as e:
            print(f"[POLICY] Error evaluating rule {rule['id']}: {e}")
        
        return PolicyDecision.APPROVE
    
    def _format_message(self, template: str, action: Dict, context: Dict) -> str:
        """Format message template with actual values"""
        combined = {**action, **context}
        
        # Simple template substitution
        message = template
        for key, value in combined.items():
            message = message.replace(f"${{{key}}}", str(value))
            message = message.replace(f"${key}", str(value))
        
        return message
    
    def _log_evaluation(
        self,
        action: Dict,
        context: Dict,
        violations: List[Dict],
        warnings: List[Dict]
    ):
        """Log policy evaluation"""
        self.evaluation_history.append({
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "context": context,
            "violations": violations,
            "warnings": warnings
        })
    
    def get_statistics(self) -> Dict:
        """Get policy enforcement statistics"""
        total = len(self.evaluation_history)
        if total == 0:
            return {"total_evaluations": 0}
        
        rejections = sum(1 for e in self.evaluation_history if e["violations"])
        approvals = total - rejections
        
        return {
            "total_evaluations": total,
            "approvals": approvals,
            "rejections": rejections,
            "approval_rate": approvals / total if total > 0 else 0
        }


# Example usage
if __name__ == "__main__":
    # Mock cost tracker
    class MockCostTracker:
        def get_summary(self):
            return {"total_cost_usd": 3500.0}
    
    engine = PolicyEngine(cost_tracker=MockCostTracker())
    
    # Test cases
    test_actions = [
        {
            "action_type": "deploy",
            "estimated_cost": 100.0,
            "environment": "development"
        },
        {
            "action_type": "deploy",
            "estimated_cost": 2000.0,  # Exceeds budget
            "environment": "production"
        },
        {
            "action_type": "admin",
            "estimated_cost": 50.0,
            "environment": "production"
        }
    ]
    
    context = {
        "user_id": "user123",
        "user_role": "developer",
        "budget_limit": 5000.0
    }
    
    for action in test_actions:
        decision, reason, details = engine.evaluate(action, context)
        print(f"\nAction: {action['action_type']} (${action['estimated_cost']})")
        print(f"Decision: {decision.value}")
        print(f"Reason: {reason}")
