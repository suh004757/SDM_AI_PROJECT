"""
Cost Tracker - Monitor and manage LLM API costs
Tracks usage, provides alerts, and exports cost data
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass, asdict
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class CostEntry:
    """Single cost tracking entry"""
    timestamp: datetime
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cost_usd: float
    task_description: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary with serializable timestamp"""
        data = asdict(self)
        data['timestamp'] = self.timestamp.isoformat()
        return data


class CostTracker:
    """
    Track and manage LLM API costs
    Provides budgeting, alerts, and cost analysis
    """
    
    def __init__(
        self,
        budget_limit: Optional[float] = None,
        alert_threshold: Optional[float] = None,
        export_dir: Optional[str] = None
    ):
        """
        Initialize cost tracker
        
        Args:
            budget_limit: Maximum budget in USD (None = no limit)
            alert_threshold: Alert when cost exceeds this (None = no alerts)
            export_dir: Directory to export cost data (None = don't export)
        """
        self.budget_limit = budget_limit
        self.alert_threshold = alert_threshold
        self.export_dir = Path(export_dir) if export_dir else None
        
        self.entries: List[CostEntry] = []
        self.total_cost = 0.0
        self.total_tokens = 0
        self.provider_costs: Dict[str, float] = {}
        
        if self.export_dir:
            self.export_dir.mkdir(parents=True, exist_ok=True)
    
    def track(
        self,
        provider: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        cost_usd: float,
        task_description: Optional[str] = None
    ) -> None:
        """
        Track a single API call
        
        Args:
            provider: Provider name
            model: Model identifier
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            cost_usd: Cost in USD
            task_description: Optional description of the task
        """
        # Create entry
        entry = CostEntry(
            timestamp=datetime.now(),
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
            cost_usd=cost_usd,
            task_description=task_description
        )
        
        # Add to tracking
        self.entries.append(entry)
        self.total_cost += cost_usd
        self.total_tokens += entry.total_tokens
        
        # Update provider costs
        if provider not in self.provider_costs:
            self.provider_costs[provider] = 0.0
        self.provider_costs[provider] += cost_usd
        
        # Check alerts
        self._check_alerts()
        
        # Log
        logger.info(
            f"Tracked: {provider}/{model} - "
            f"{input_tokens}+{output_tokens} tokens = ${cost_usd:.4f}"
        )
    
    def _check_alerts(self) -> None:
        """Check if cost thresholds are exceeded"""
        # Budget limit alert
        if self.budget_limit and self.total_cost >= self.budget_limit:
            logger.warning(
                f"⚠️ BUDGET LIMIT EXCEEDED: ${self.total_cost:.2f} / ${self.budget_limit:.2f}"
            )
        
        # Alert threshold
        if self.alert_threshold and self.total_cost >= self.alert_threshold:
            logger.warning(
                f"⚠️ Cost alert: ${self.total_cost:.2f} (threshold: ${self.alert_threshold:.2f})"
            )
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get cost summary
        
        Returns:
            Dict with total costs, tokens, and breakdown by provider
        """
        return {
            'total_cost_usd': self.total_cost,
            'total_tokens': self.total_tokens,
            'total_calls': len(self.entries),
            'budget_limit': self.budget_limit,
            'budget_remaining': self.budget_limit - self.total_cost if self.budget_limit else None,
            'provider_breakdown': self.provider_costs.copy(),
            'average_cost_per_call': self.total_cost / len(self.entries) if self.entries else 0,
        }
    
    def get_provider_stats(self, provider: str) -> Dict[str, Any]:
        """
        Get statistics for specific provider
        
        Args:
            provider: Provider name
            
        Returns:
            Dict with provider-specific stats
        """
        provider_entries = [e for e in self.entries if e.provider == provider]
        
        if not provider_entries:
            return {
                'provider': provider,
                'total_cost_usd': 0.0,
                'total_tokens': 0,
                'total_calls': 0,
            }
        
        total_cost = sum(e.cost_usd for e in provider_entries)
        total_tokens = sum(e.total_tokens for e in provider_entries)
        
        return {
            'provider': provider,
            'total_cost_usd': total_cost,
            'total_tokens': total_tokens,
            'total_calls': len(provider_entries),
            'average_cost_per_call': total_cost / len(provider_entries),
            'models_used': list(set(e.model for e in provider_entries)),
        }
    
    def export_to_json(self, filename: Optional[str] = None) -> str:
        """
        Export cost data to JSON file
        
        Args:
            filename: Output filename (None = auto-generate)
            
        Returns:
            Path to exported file
        """
        if not self.export_dir:
            raise ValueError("Export directory not configured")
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"cost_tracking_{timestamp}.json"
        
        filepath = self.export_dir / filename
        
        data = {
            'summary': self.get_summary(),
            'entries': [e.to_dict() for e in self.entries]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Exported cost data to {filepath}")
        return str(filepath)
    
    def export_to_csv(self, filename: Optional[str] = None) -> str:
        """
        Export cost data to CSV file
        
        Args:
            filename: Output filename (None = auto-generate)
            
        Returns:
            Path to exported file
        """
        if not self.export_dir:
            raise ValueError("Export directory not configured")
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"cost_tracking_{timestamp}.csv"
        
        filepath = self.export_dir / filename
        
        # Write CSV
        with open(filepath, 'w', encoding='utf-8') as f:
            # Header
            f.write("Timestamp,Provider,Model,Input Tokens,Output Tokens,Total Tokens,Cost (USD),Task Description\n")
            
            # Entries
            for entry in self.entries:
                f.write(
                    f"{entry.timestamp.isoformat()},"
                    f"{entry.provider},"
                    f"{entry.model},"
                    f"{entry.input_tokens},"
                    f"{entry.output_tokens},"
                    f"{entry.total_tokens},"
                    f"{entry.cost_usd:.6f},"
                    f"\"{entry.task_description or ''}\"\n"
                )
        
        logger.info(f"Exported cost data to {filepath}")
        return str(filepath)
    
    def reset(self) -> None:
        """Reset all tracking data"""
        self.entries.clear()
        self.total_cost = 0.0
        self.total_tokens = 0
        self.provider_costs.clear()
        logger.info("Cost tracker reset")
    
    def print_summary(self) -> None:
        """Print formatted cost summary to console"""
        summary = self.get_summary()
        
        print("\n" + "="*50)
        print("LLM COST SUMMARY")
        print("="*50)
        print(f"Total Cost:        ${summary['total_cost_usd']:.4f}")
        print(f"Total Tokens:      {summary['total_tokens']:,}")
        print(f"Total API Calls:   {summary['total_calls']}")
        print(f"Avg Cost/Call:     ${summary['average_cost_per_call']:.4f}")
        
        if summary['budget_limit']:
            print(f"Budget Limit:      ${summary['budget_limit']:.2f}")
            print(f"Budget Remaining:  ${summary['budget_remaining']:.2f}")
        
        print("\nProvider Breakdown:")
        print("-"*50)
        for provider, cost in summary['provider_breakdown'].items():
            percentage = (cost / summary['total_cost_usd'] * 100) if summary['total_cost_usd'] > 0 else 0
            print(f"  {provider:12s} ${cost:8.4f} ({percentage:5.1f}%)")
        
        print("="*50 + "\n")


# Global cost tracker instance
_tracker_instance = None


def get_tracker(
    budget_limit: Optional[float] = None,
    alert_threshold: Optional[float] = None,
    export_dir: Optional[str] = None
) -> CostTracker:
    """
    Get global cost tracker instance (singleton pattern)
    
    Args:
        budget_limit: Budget limit (only used on first call)
        alert_threshold: Alert threshold (only used on first call)
        export_dir: Export directory (only used on first call)
        
    Returns:
        CostTracker instance
    """
    global _tracker_instance
    if _tracker_instance is None:
        _tracker_instance = CostTracker(
            budget_limit=budget_limit,
            alert_threshold=alert_threshold,
            export_dir=export_dir
        )
    return _tracker_instance
