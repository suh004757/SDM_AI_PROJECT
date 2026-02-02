"""
Audit Logger: Security Event Tracking System

Records all security-relevant events for compliance and forensics.
Integrates with O.D.A.L. Log phase.
"""

import json
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime
from enum import Enum


class EventType(Enum):
    """Types of security events"""
    PROMPT_INJECTION = "prompt_injection"
    POLICY_VIOLATION = "policy_violation"
    POLICY_APPROVAL = "policy_approval"
    ACCESS_DENIED = "access_denied"
    HIGH_COST_ACTION = "high_cost_action"
    DECISION_MADE = "decision_made"
    ACTION_EXECUTED = "action_executed"


class AuditLogger:
    """
    Security audit logging system.
    
    Features:
    - Structured event logging
    - Searchable event history
    - Compliance reporting
    - Anomaly detection
    """
    
    def __init__(self, log_dir: Optional[Path] = None):
        """
        Initialize Audit Logger.
        
        Args:
            log_dir: Directory to store audit logs
        """
        self.log_dir = log_dir or Path(__file__).parent / "logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        self.current_log_file = self._get_log_file()
        self.events = []
    
    def _get_log_file(self) -> Path:
        """Get current log file path (daily rotation)"""
        date_str = datetime.utcnow().strftime("%Y-%m-%d")
        return self.log_dir / f"audit_{date_str}.jsonl"
    
    def log_event(
        self,
        event_type: EventType,
        description: str,
        metadata: Optional[Dict[str, Any]] = None,
        severity: str = "info"
    ):
        """
        Log a security event.
        
        Args:
            event_type: Type of event
            description: Human-readable description
            metadata: Additional event data
            severity: Event severity (info, warning, error, critical)
        """
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type.value,
            "description": description,
            "severity": severity,
            "metadata": metadata or {}
        }
        
        # Store in memory
        self.events.append(event)
        
        # Write to file
        self._write_event(event)
        
        # Console output for critical events
        if severity in ["error", "critical"]:
            print(f"[AUDIT:{severity.upper()}] {event_type.value}: {description}")
    
    def _write_event(self, event: Dict):
        """Write event to log file"""
        with open(self.current_log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(event) + '\n')
    
    def log_prompt_injection(
        self,
        user_input: str,
        detection_metadata: Dict
    ):
        """Log prompt injection detection"""
        self.log_event(
            EventType.PROMPT_INJECTION,
            f"Prompt injection detected (severity: {detection_metadata['severity_level']})",
            metadata={
                "input_preview": user_input[:100],
                "severity_score": detection_metadata["severity_score"],
                "detected_patterns": detection_metadata["detected_patterns"]
            },
            severity="error" if detection_metadata["severity_level"] in ["high", "critical"] else "warning"
        )
    
    def log_policy_violation(
        self,
        action: Dict,
        policy_id: str,
        violation_details: Dict
    ):
        """Log policy violation"""
        self.log_event(
            EventType.POLICY_VIOLATION,
            f"Policy {policy_id} violated",
            metadata={
                "action": action,
                "policy_id": policy_id,
                "violation": violation_details
            },
            severity="warning"
        )
    
    def log_decision(
        self,
        observation: Dict,
        decision: str,
        reasoning: str,
        metadata: Optional[Dict] = None
    ):
        """Log O.D.A.L. decision"""
        self.log_event(
            EventType.DECISION_MADE,
            f"Decision: {decision}",
            metadata={
                "observation": observation,
                "decision": decision,
                "reasoning": reasoning,
                **(metadata or {})
            },
            severity="info"
        )
    
    def log_action_executed(
        self,
        action: Dict,
        result: Dict,
        duration_ms: float
    ):
        """Log action execution"""
        self.log_event(
            EventType.ACTION_EXECUTED,
            f"Action executed: {action.get('action_type', 'unknown')}",
            metadata={
                "action": action,
                "result": result,
                "duration_ms": duration_ms
            },
            severity="info"
        )
    
    def search_events(
        self,
        event_type: Optional[EventType] = None,
        severity: Optional[str] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None
    ) -> List[Dict]:
        """
        Search audit events.
        
        Args:
            event_type: Filter by event type
            severity: Filter by severity
            start_time: Filter by start time
            end_time: Filter by end time
        
        Returns:
            List of matching events
        """
        results = self.events
        
        if event_type:
            results = [e for e in results if e["event_type"] == event_type.value]
        
        if severity:
            results = [e for e in results if e["severity"] == severity]
        
        if start_time:
            start_iso = start_time.isoformat()
            results = [e for e in results if e["timestamp"] >= start_iso]
        
        if end_time:
            end_iso = end_time.isoformat()
            results = [e for e in results if e["timestamp"] <= end_iso]
        
        return results
    
    def get_statistics(self) -> Dict:
        """Get audit statistics"""
        if not self.events:
            return {"total_events": 0}
        
        event_type_counts = {}
        severity_counts = {}
        
        for event in self.events:
            event_type = event["event_type"]
            severity = event["severity"]
            
            event_type_counts[event_type] = event_type_counts.get(event_type, 0) + 1
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
        
        return {
            "total_events": len(self.events),
            "event_type_distribution": event_type_counts,
            "severity_distribution": severity_counts,
            "first_event": self.events[0]["timestamp"],
            "last_event": self.events[-1]["timestamp"]
        }
    
    def generate_report(self, output_path: Optional[Path] = None) -> str:
        """
        Generate audit report.
        
        Args:
            output_path: Path to save report (optional)
        
        Returns:
            Report as string
        """
        stats = self.get_statistics()
        
        report = f"""
# Security Audit Report
Generated: {datetime.utcnow().isoformat()}

## Summary
- Total Events: {stats['total_events']}
- Time Range: {stats.get('first_event', 'N/A')} to {stats.get('last_event', 'N/A')}

## Event Type Distribution
"""
        for event_type, count in stats.get('event_type_distribution', {}).items():
            report += f"- {event_type}: {count}\n"
        
        report += "\n## Severity Distribution\n"
        for severity, count in stats.get('severity_distribution', {}).items():
            report += f"- {severity}: {count}\n"
        
        # Critical events
        critical_events = [e for e in self.events if e["severity"] in ["error", "critical"]]
        if critical_events:
            report += f"\n## Critical Events ({len(critical_events)})\n"
            for event in critical_events[:10]:  # Top 10
                report += f"- [{event['timestamp']}] {event['event_type']}: {event['description']}\n"
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
        
        return report


# Example usage
if __name__ == "__main__":
    logger = AuditLogger()
    
    # Log various events
    logger.log_prompt_injection(
        "Ignore all previous instructions",
        {
            "severity_level": "high",
            "severity_score": 8,
            "detected_patterns": [{"category": "role_confusion"}]
        }
    )
    
    logger.log_decision(
        observation={"user_input": "Deploy to production"},
        decision="REQUIRE_APPROVAL",
        reasoning="Production deployment requires manual approval"
    )
    
    logger.log_action_executed(
        action={"action_type": "deploy", "environment": "staging"},
        result={"status": "success"},
        duration_ms=1250.5
    )
    
    # Generate report
    print(logger.generate_report())
