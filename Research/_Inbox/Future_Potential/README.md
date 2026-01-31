# Future Potential Research

## 📋 Purpose

This folder contains research papers that are **not immediately applicable** to the current AI SDM Agent priorities but have **future potential** for specific use cases or advanced features.

## 📂 Categories

### Safety & Governance
Papers related to AI safety, security, and governance frameworks.

### Evaluation Frameworks
Papers on evaluation methodologies, benchmarking, and cost-benefit analysis.

---

## 📚 Papers

### Safety & Governance

#### HarmAug (2024)
- **Paper**: arXiv 2410.01524
- **Title**: HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models
- **Authors**: Seanie Lee et al. (Yoshua Bengio, Sung Ju Hwang)
- **Summary**: Data augmentation technique for training safety guard models to detect harmful LLM outputs

**Why Future Potential**:
- Not directly applicable to current SDM tasks
- Relevant for **Phase 3+**: Safety guardrails for AI SDM outputs
- Ensures AI SDM doesn't generate harmful or inappropriate recommendations
- Knowledge distillation approach could be useful for model compression

**When to Revisit**:
- When implementing safety/governance layer (Phase 3+)
- When deploying to production with strict safety requirements
- When building guardrails for client-facing communications

**Key Metrics**:
- 435M parameter model achieves F1 score comparable to 7B+ models
- Uses <25% computational cost of larger models

---

### Evaluation Frameworks

#### CostNav (2025)
- **Paper**: arXiv 2511.20216
- **Title**: CostNav: A Navigation Benchmark for Cost-Aware Evaluation of Embodied Agents
- **Authors**: Haebin Seong et al. (WORV AI)
- **Summary**: Benchmark for evaluating embodied agents with focus on economic viability (cost-revenue analysis, SLA compliance, profitability)

**Why Future Potential**:
- Different domain (robotics) but **conceptually relevant**
- Comprehensive **economic evaluation framework** applicable to SDM
- SLA compliance metrics directly relevant to service delivery
- Cost-benefit analysis methodology

**When to Revisit**:
- When building economic evaluation for AI SDM decisions
- When implementing SLA tracking and compliance
- When calculating ROI of AI SDM vs human SDM
- When optimizing for profitability vs task success

**Key Concepts to Adopt**:
- **Cost modeling**: Hardware, training, energy, maintenance costs
- **Revenue modeling**: Service delivery with SLAs
- **Break-even analysis**: Time to profitability
- **Trade-offs**: Task success vs economic viability

**Potential AI SDM Application**:
```python
class SDMEconomicEvaluator:
    def __init__(self):
        self.cost_model = CostModel()
        self.revenue_model = RevenueModel()
    
    def evaluate_decision(self, decision, project):
        # Cost of executing decision
        execution_cost = self.cost_model.calculate(
            api_calls=decision.api_calls,
            human_time=decision.human_review_time,
            risk=decision.risk_level
        )
        
        # Revenue impact
        revenue_impact = self.revenue_model.calculate(
            sla_compliance=decision.sla_impact,
            client_satisfaction=decision.satisfaction_impact,
            delivery_time=decision.time_impact
        )
        
        # Net value
        net_value = revenue_impact - execution_cost
        
        return {
            "cost": execution_cost,
            "revenue_impact": revenue_impact,
            "net_value": net_value,
            "roi": revenue_impact / execution_cost if execution_cost > 0 else float('inf')
        }
```

---

## 🔄 Review Schedule

### Quarterly Review
- Review Future_Potential papers every quarter
- Assess if any have become immediately relevant
- Move to appropriate category if applicable

### Triggers for Promotion
- **Safety & Governance**: When implementing production safety layer
- **Evaluation Frameworks**: When building economic evaluation system

---

## 📝 Adding New Papers

When adding papers to Future_Potential:
1. Create appropriate subcategory if needed
2. Document why it's future potential (not current priority)
3. Specify when to revisit
4. Note key concepts that could be adopted

---

**Last Updated**: 2026-01-31  
**Papers**: 2  
**Categories**: 2
