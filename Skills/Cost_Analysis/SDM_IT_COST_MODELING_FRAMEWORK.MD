# SDM Cost Modeling Framework: IT Infrastructure Economics

## 📋 Overview

### Purpose
This framework enables the SDM (Service Delivery Manager) to perform comprehensive **cost modeling for IT infrastructure projects**, applying CostNav's economic evaluation philosophy to real-world IT service delivery.

### CostNav Philosophy Applied
> *"Optimizing for task success fundamentally differs from optimizing for economic deployment"*

**Traditional IT Metrics:** Uptime, SLA compliance, ticket resolution
**Economic Reality:** TCO, Break-even, Cost per user, ROI

---

## 🏗️ PART 1: CAPEX PLANNING

### 1.1 Hardware Infrastructure Cost Model

#### Pre-Deployment Costs (Fixed Investment)

| Category | Cost Components | Estimation Method |
|----------|-----------------|-------------------|
| **Compute** | Servers, blades, HCI | Capacity × Unit cost |
| **Storage** | SAN, NAS, backup | TB required × $/TB |
| **Network** | Switches, routers, firewalls | Port count × complexity |
| **Facilities** | Rack space, power, cooling | kW × PUE × rate |
| **Licensing** | OS, virtualization, management | Per-core/per-socket |
| **Implementation** | Professional services, migration | Hours × rate |

#### CAPEX Calculation Template

```
┌─────────────────────────────────────────────────────────────────┐
│                    CAPEX PLANNING WORKSHEET                      │
├─────────────────────────────────────────────────────────────────┤
│ Project: _______________________  Date: _______________          │
│ Prepared by: __________________  Version: _____________          │
├─────────────────────────────────────────────────────────────────┤
│ HARDWARE                                                         │
│ ├─ Servers          : _____ units × $_______ = $_____________   │
│ ├─ Storage          : _____ TB    × $_______ = $_____________   │
│ ├─ Network Equipment: _____ units × $_______ = $_____________   │
│ ├─ End User Devices : _____ units × $_______ = $_____________   │
│ └─ Peripherals      :                        = $_____________   │
│                                    Subtotal  = $_____________   │
├─────────────────────────────────────────────────────────────────┤
│ SOFTWARE & LICENSING                                             │
│ ├─ Operating Systems: _____ licenses × $____ = $_____________   │
│ ├─ Virtualization   : _____ sockets  × $____ = $_____________   │
│ ├─ Database         : _____ cores    × $____ = $_____________   │
│ ├─ Security Tools   :                        = $_____________   │
│ └─ Management Tools :                        = $_____________   │
│                                    Subtotal  = $_____________   │
├─────────────────────────────────────────────────────────────────┤
│ IMPLEMENTATION SERVICES                                          │
│ ├─ Design & Architecture: _____ hours × $____ = $____________   │
│ ├─ Deployment & Config  : _____ hours × $____ = $____________   │
│ ├─ Migration            : _____ hours × $____ = $____________   │
│ ├─ Testing & Validation : _____ hours × $____ = $____________   │
│ └─ Training             : _____ hours × $____ = $____________   │
│                                    Subtotal  = $_____________   │
├─────────────────────────────────────────────────────────────────┤
│ CONTINGENCY (10-20%)                         = $_____________   │
├─────────────────────────────────────────────────────────────────┤
│ TOTAL CAPEX                                  = $_____________   │
└─────────────────────────────────────────────────────────────────┘
```

#### Depreciation Model

| Asset Type | Useful Life | Depreciation Method | Annual Expense |
|------------|-------------|---------------------|----------------|
| Servers | 5 years | Straight-line | CAPEX ÷ 5 |
| Storage | 5 years | Straight-line | CAPEX ÷ 5 |
| Network | 7 years | Straight-line | CAPEX ÷ 7 |
| End User Devices | 3-4 years | Straight-line | CAPEX ÷ 3.5 |
| Software (perpetual) | 3-5 years | Straight-line | CAPEX ÷ 4 |

---

### 1.2 Data Center Cost Model

#### Facility Cost Components

| Component | Formula | Industry Benchmark |
|-----------|---------|-------------------|
| **Power Cost** | kW × Hours × Rate × PUE | $0.08-0.15/kWh |
| **Cooling** | Included in PUE | PUE 1.2-1.8 |
| **Rack Space** | # Racks × $/rack/month | $500-2,000/rack |
| **Physical Security** | Fixed + variable | 5-10% of facility |
| **Connectivity** | Bandwidth × $/Mbps | $1-5/Mbps |

#### Power Usage Effectiveness (PUE) Calculation

```
PUE = Total Facility Power / IT Equipment Power

Example:
- IT Load: 100 kW
- Total Facility: 150 kW
- PUE = 1.5

Annual Power Cost = IT Load × 8,760 hrs × Rate × PUE
                  = 100 kW × 8,760 × $0.10 × 1.5
                  = $131,400/year
```

#### Colocation vs On-Premise Decision Matrix

| Factor | On-Premise | Colocation | Weight |
|--------|------------|------------|--------|
| **CAPEX** | High (build facility) | Low (use existing) | 25% |
| **OPEX** | Variable (manage all) | Predictable ($/rack) | 20% |
| **Control** | Full | Shared | 15% |
| **Scalability** | Limited | Flexible | 15% |
| **Security** | Self-managed | Provider-managed | 10% |
| **Compliance** | Self-certified | Provider-certified | 10% |
| **Location** | Fixed | Multiple options | 5% |

---

## ☁️ PART 2: CLOUD PLANNING

### 2.1 Cloud Cost Model Structure

#### Cost Categories (Following CostNav's Pre-Run/Run-Time Model)

**Pre-Migration Costs (One-Time)**
| Item | Description | Typical Range |
|------|-------------|---------------|
| Assessment | Discovery, dependency mapping | $10K-50K |
| Architecture Design | Landing zone, network design | $20K-100K |
| Migration Tools | CloudEndure, Azure Migrate | $0-50K |
| Training | Team certification | $5K-20K/person |
| Professional Services | MSP, SI engagement | $50K-500K |

**Run-Time Costs (Recurring)**
| Category | Components | Billing Model |
|----------|------------|---------------|
| **Compute** | VMs, containers, serverless | Per-hour/per-second |
| **Storage** | Block, object, archive | Per-GB/month |
| **Network** | Egress, VPN, load balancer | Per-GB, per-hour |
| **Database** | RDS, managed services | Per-hour + storage |
| **Security** | WAF, DDoS, key management | Per-request, per-key |
| **Management** | Monitoring, backup, DR | Per-resource |

### 2.2 Azure Cost Estimation Framework

#### Compute Sizing Model

```
┌─────────────────────────────────────────────────────────────────┐
│                 AZURE VM COST CALCULATOR                         │
├─────────────────────────────────────────────────────────────────┤
│ Workload: _______________________                                │
├─────────────────────────────────────────────────────────────────┤
│ REQUIREMENTS                                                     │
│ ├─ vCPUs Required    : _______                                  │
│ ├─ RAM Required (GB) : _______                                  │
│ ├─ Storage (GB)      : _______                                  │
│ ├─ IOPS Required     : _______                                  │
│ └─ Network (Gbps)    : _______                                  │
├─────────────────────────────────────────────────────────────────┤
│ VM SELECTION                                                     │
│ ├─ Series            : D-series / E-series / F-series           │
│ ├─ Size              : Standard_D4s_v5                          │
│ ├─ Region            : East US / West Europe / etc.             │
│ └─ Availability      : Single / Availability Set / Zone         │
├─────────────────────────────────────────────────────────────────┤
│ PRICING OPTIONS                                                  │
│ ├─ Pay-as-you-go     : $_______ /hour × 730 hrs = $______/mo   │
│ ├─ 1-Year Reserved   : $_______ /month (___% savings)           │
│ ├─ 3-Year Reserved   : $_______ /month (___% savings)           │
│ └─ Spot Instance     : $_______ /hour (up to 90% savings)       │
├─────────────────────────────────────────────────────────────────┤
│ ADDITIONAL COSTS                                                 │
│ ├─ OS License (Windows): $_______ /month                        │
│ ├─ Managed Disk        : $_______ /month                        │
│ ├─ Backup              : $_______ /month                        │
│ └─ Monitoring          : $_______ /month                        │
├─────────────────────────────────────────────────────────────────┤
│ TOTAL MONTHLY COST                           = $______________  │
└─────────────────────────────────────────────────────────────────┘
```

#### Storage Cost Tiers

| Tier | Use Case | Cost (per GB/month) | Access Cost |
|------|----------|---------------------|-------------|
| **Premium SSD** | Production DB | $0.15-0.20 | Included |
| **Standard SSD** | General workloads | $0.05-0.08 | Included |
| **Standard HDD** | Backup, archive | $0.02-0.04 | Included |
| **Blob Hot** | Frequent access | $0.018-0.02 | $0.004/10K ops |
| **Blob Cool** | Infrequent (30+ days) | $0.01 | $0.01/10K ops |
| **Blob Archive** | Rare access (180+ days) | $0.002 | $0.02/10K + retrieval |

#### Network Egress Cost Model

```
Egress Pricing (Azure Example):
┌────────────────────┬──────────────┐
│ Monthly Egress     │ Cost per GB  │
├────────────────────┼──────────────┤
│ First 100 GB       │ Free         │
│ 100 GB - 10 TB     │ $0.087       │
│ 10 TB - 50 TB      │ $0.083       │
│ 50 TB - 150 TB     │ $0.070       │
│ 150 TB - 500 TB    │ $0.050       │
└────────────────────┴──────────────┘

Monthly Egress Cost = Σ (GB in tier × rate)
```

### 2.3 Cloud vs On-Premise TCO Comparison

#### 5-Year TCO Model

```
┌─────────────────────────────────────────────────────────────────┐
│              5-YEAR TCO COMPARISON MODEL                         │
├─────────────────────────────────────────────────────────────────┤
│                          │ ON-PREMISE    │ CLOUD          │
├──────────────────────────┼───────────────┼────────────────┤
│ YEAR 0 (Initial)         │               │                │
│ ├─ Hardware CAPEX        │ $____________ │ $0             │
│ ├─ Software Licenses     │ $____________ │ $____________  │
│ ├─ Implementation        │ $____________ │ $____________  │
│ └─ Migration             │ $0            │ $____________  │
│                          │               │                │
│ YEAR 1-5 (Annual)        │               │                │
│ ├─ Compute               │ $0 (owned)    │ $____________  │
│ ├─ Storage               │ $____________ │ $____________  │
│ ├─ Network               │ $____________ │ $____________  │
│ ├─ Power & Cooling       │ $____________ │ $0 (included)  │
│ ├─ Facility/Rack         │ $____________ │ $0 (included)  │
│ ├─ Maintenance/Support   │ $____________ │ $0 (included)  │
│ ├─ Admin Labor           │ $____________ │ $____________  │
│ └─ Software Subscription │ $____________ │ $____________  │
│                          │               │                │
│ YEAR 5 (Refresh)         │               │                │
│ └─ Hardware Refresh      │ $____________ │ $0             │
├──────────────────────────┼───────────────┼────────────────┤
│ 5-YEAR TOTAL TCO         │ $____________ │ $____________  │
│ Average Annual Cost      │ $____________ │ $____________  │
│ Cost per User/Month      │ $____________ │ $____________  │
└──────────────────────────┴───────────────┴────────────────┘
```

### 2.4 Cloud Cost Optimization Strategies

#### Reserved Instance Planning

| Workload Type | Recommended Commitment | Savings Potential |
|---------------|------------------------|-------------------|
| **Steady-state production** | 3-year reserved | 60-72% |
| **Predictable with growth** | 1-year reserved | 30-40% |
| **Variable/seasonal** | Savings Plans | 20-30% |
| **Dev/Test** | Spot/Preemptible | 60-90% |
| **Burst workloads** | Pay-as-you-go | 0% (flexibility) |

#### Right-Sizing Analysis

```
Right-Sizing Recommendation Matrix:

Current Utilization → Recommendation
┌─────────────────────┬────────────────────────────────────┐
│ CPU < 10%           │ Downsize 2 tiers or containerize   │
│ CPU 10-30%          │ Downsize 1 tier                    │
│ CPU 30-70%          │ Right-sized ✓                      │
│ CPU 70-90%          │ Monitor for upgrade need           │
│ CPU > 90%           │ Upsize or scale out                │
└─────────────────────┴────────────────────────────────────┘

Savings Example:
- Current: D8s_v5 @ $280/month, 25% CPU utilization
- Recommended: D4s_v5 @ $140/month
- Annual Savings: $1,680 per VM
```

---

## 📊 PART 3: OPERATIONAL COST TRACKING

### 3.1 Run-Rate Cost Model

#### Monthly IT Operations Cost Structure

| Category | Fixed | Variable | Metric |
|----------|-------|----------|--------|
| **Infrastructure** | Base capacity | Burst/overage | Per resource |
| **Licensing** | Enterprise agreements | Per-user adds | Per seat |
| **Support** | Managed services | T&M incidents | Per ticket |
| **Labor** | FTE salaries | Contractors | Per hour |
| **Tools** | Platform licenses | Usage-based | Per unit |

#### Cost per User Calculation

```
Monthly Cost per User = (Total IT OPEX) / (Active Users)

Components:
├─ Infrastructure: $_______ / _____ users = $_____ /user
├─ Software/SaaS : $_______ / _____ users = $_____ /user
├─ Support       : $_______ / _____ users = $_____ /user
├─ Security      : $_______ / _____ users = $_____ /user
└─ Management    : $_______ / _____ users = $_____ /user
                                    TOTAL = $_____ /user/month
```

### 3.2 Project Cost Tracking (CostNav-Inspired)

#### Earned Value Metrics for IT Projects

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **PV** (Planned Value) | Budgeted cost of scheduled work | What should be spent |
| **EV** (Earned Value) | Budgeted cost of completed work | Value delivered |
| **AC** (Actual Cost) | Actual cost incurred | What was spent |
| **SV** (Schedule Variance) | EV - PV | Ahead (+) or behind (-) |
| **CV** (Cost Variance) | EV - AC | Under (+) or over (-) budget |
| **SPI** | EV / PV | >1 = ahead, <1 = behind |
| **CPI** | EV / AC | >1 = under budget, <1 = over |
| **EAC** | BAC / CPI | Estimate at completion |
| **VAC** | BAC - EAC | Variance at completion |

#### IT Project Cost Tracking Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│           PROJECT COST PERFORMANCE DASHBOARD                     │
├─────────────────────────────────────────────────────────────────┤
│ Project: Azure Migration Phase 2    │ Report Date: ___________  │
│ PM: _____________________           │ Status: 🟢 🟡 🔴           │
├─────────────────────────────────────────────────────────────────┤
│ BUDGET SUMMARY                                                   │
│ ├─ Budget at Completion (BAC)      : $500,000                   │
│ ├─ Planned Value (PV)              : $300,000  (60% planned)    │
│ ├─ Earned Value (EV)               : $275,000  (55% complete)   │
│ └─ Actual Cost (AC)                : $290,000  (spent to date)  │
├─────────────────────────────────────────────────────────────────┤
│ PERFORMANCE INDICES                                              │
│ ├─ Schedule Variance (SV)          : -$25,000  ⚠️ Behind        │
│ ├─ Cost Variance (CV)              : -$15,000  ⚠️ Over budget   │
│ ├─ Schedule Performance Index (SPI): 0.92      ⚠️ 8% behind     │
│ └─ Cost Performance Index (CPI)    : 0.95      ⚠️ 5% over       │
├─────────────────────────────────────────────────────────────────┤
│ FORECAST                                                         │
│ ├─ Estimate at Completion (EAC)    : $526,316                   │
│ ├─ Variance at Completion (VAC)    : -$26,316  🔴 Over budget   │
│ └─ To Complete Performance (TCPI)  : 1.07      (need 7% improve)│
├─────────────────────────────────────────────────────────────────┤
│ COST BREAKDOWN BY CATEGORY                                       │
│ ├─ Cloud Resources    : $180,000 / $200,000  (90%)  🟢          │
│ ├─ Professional Svcs  : $85,000  / $75,000   (113%) 🔴          │
│ ├─ Internal Labor     : $20,000  / $20,000   (100%) 🟢          │
│ └─ Contingency Used   : $5,000   / $25,000   (20%)  🟢          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💹 PART 4: BREAK-EVEN & ROI ANALYSIS

### 4.1 IT Investment Break-Even Model

#### Formula
```
Break-Even Point = Total Investment / (Annual Savings or Revenue)

Example: Cloud Migration
- Total Investment: $200,000 (migration + Year 1 cloud)
- Annual On-Prem Cost (avoided): $180,000
- Annual Cloud Cost: $120,000
- Net Annual Savings: $60,000

Break-Even = $200,000 / $60,000 = 3.33 years
```

### 4.2 ROI Calculation Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                    IT PROJECT ROI CALCULATOR                     │
├─────────────────────────────────────────────────────────────────┤
│ INVESTMENT (Costs)                                               │
│ ├─ Initial CAPEX                   : $______________            │
│ ├─ Implementation Services         : $______________            │
│ ├─ Migration/Transition            : $______________            │
│ ├─ Training                        : $______________            │
│ └─ Year 1-3 Operating Costs        : $______________            │
│                         Total Investment: $______________        │
├─────────────────────────────────────────────────────────────────┤
│ RETURNS (Benefits)                                               │
│ ├─ Cost Avoidance (old system)     : $______________            │
│ ├─ Productivity Gains              : $______________            │
│ ├─ Revenue Enablement              : $______________            │
│ ├─ Risk Reduction (quantified)     : $______________            │
│ └─ Other Tangible Benefits         : $______________            │
│                           Total Returns: $______________         │
├─────────────────────────────────────────────────────────────────┤
│ ROI METRICS                                                      │
│ ├─ Net Present Value (NPV)         : $______________            │
│ ├─ ROI % = (Returns-Investment)/Investment × 100                │
│ │          = ____________%                                       │
│ ├─ Payback Period                  : _____________ months       │
│ └─ Internal Rate of Return (IRR)   : _____________%             │
└─────────────────────────────────────────────────────────────────┘
```

### 4.3 Sensitivity Analysis

| Variable | Base Case | -20% | +20% | Impact on ROI |
|----------|-----------|------|------|---------------|
| Cloud costs | $120K/yr | $96K | $144K | High |
| Migration cost | $100K | $80K | $120K | Medium |
| Savings realized | $180K/yr | $144K | $216K | High |
| Timeline | 12 months | 10 mo | 14 mo | Medium |
| Headcount reduction | 2 FTEs | 1.6 | 2.4 | High |

---

## 📋 PART 5: SDM COST MODELING PROMPTS

### Prompt: CAPEX Planning

```
# Role: Service Delivery Manager - CAPEX Planning Mode

## Context
You are creating a CAPEX plan for an IT infrastructure project.

## Input Required
1. **Project Scope**: [Description of what's being procured/built]
2. **Business Requirements**: [Capacity, performance, availability needs]
3. **Timeline**: [Implementation schedule]
4. **Constraints**: [Budget ceiling, vendor preferences, compliance]

## Task - Generate CAPEX Plan

### 1. Hardware Bill of Materials
- Itemized list with quantities, specs, unit costs
- Vendor quotes comparison (minimum 2 vendors)
- Recommended configuration with justification

### 2. Software & Licensing
- License type analysis (perpetual vs subscription)
- True-up/compliance considerations
- 3-year cost projection

### 3. Implementation Costs
- Professional services estimate
- Internal labor allocation
- Timeline with resource loading

### 4. Financial Summary
- Total CAPEX by category
- Depreciation schedule
- Cash flow timeline

### 5. Risk & Contingency
- Cost risks identified
- Contingency recommendation (% and rationale)

## Output Format
- Executive summary (1 page)
- Detailed breakdown (tables)
- Appendix with quotes/assumptions
```

### Prompt: Cloud Cost Estimation

```
# Role: Service Delivery Manager - Cloud Economics Mode

## Context
You are estimating cloud costs for a workload migration or new deployment.

## Input Required
1. **Workload Profile**: [VMs, storage, network requirements]
2. **Usage Pattern**: [24/7, business hours, burst]
3. **Data Requirements**: [Volume, retention, access patterns]
4. **Compliance Needs**: [Region, certifications]

## Task - Generate Cloud Cost Estimate

### 1. Resource Sizing
- Compute instances (size, quantity, region)
- Storage (type, capacity, IOPS)
- Network (bandwidth, egress estimate)
- Supporting services (backup, monitoring, security)

### 2. Pricing Analysis
- Pay-as-you-go baseline
- Reserved instance options (1yr, 3yr)
- Savings plan applicability
- Spot instance opportunity

### 3. Cost Optimization
- Right-sizing recommendations
- Auto-scaling configuration
- Storage tiering strategy
- Reserved capacity planning

### 4. 3-Year TCO
- Year 1 (including migration)
- Year 2-3 run rate
- Comparison with alternatives

### 5. Cost Governance
- Budget alerts setup
- Tagging strategy
- Cost allocation model

## Output Format
- Monthly cost summary
- Detailed line items
- Optimization roadmap
```

### Prompt: TCO Comparison

```
# Role: Service Delivery Manager - TCO Analysis Mode

## Context
You are comparing total cost of ownership between infrastructure options.

## Input Required
1. **Options to Compare**: [On-prem vs Cloud, Vendor A vs B, etc.]
2. **Evaluation Period**: [3-year, 5-year]
3. **Workload Details**: [Specs, growth rate]
4. **Cost Factors**: [Labor rates, power costs, facility costs]

## Task - Generate TCO Comparison

### 1. Cost Inventory
For each option:
- Initial investment (CAPEX)
- Recurring costs (OPEX)
- Hidden costs (training, integration, opportunity cost)
- End-of-life costs (decommission, data migration)

### 2. Normalization
- Common assumptions documented
- Equivalent service levels
- Risk-adjusted costs

### 3. Financial Analysis
- NPV comparison
- Break-even analysis
- Sensitivity to key variables

### 4. Non-Financial Factors
- Scalability
- Time to deploy
- Operational complexity
- Strategic alignment

### 5. Recommendation
- Preferred option with rationale
- Decision criteria weighting
- Risk mitigation for chosen path

## Output Format
- Side-by-side comparison table
- Financial summary
- Recommendation memo
```

---

## 📈 Key Metrics Dashboard (CostNav-Inspired)

### Economic Viability Indicators

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| **Cost per User** | Total IT OPEX / Users | < $150/mo | 🟢🟡🔴 |
| **Cloud Unit Cost** | Cloud spend / Workload units | Decreasing | 🟢🟡🔴 |
| **CPI (Cost Performance)** | EV / AC | > 0.95 | 🟢🟡🔴 |
| **Utilization Rate** | Used capacity / Provisioned | > 60% | 🟢🟡🔴 |
| **Reserved Coverage** | Reserved / Total compute | > 70% | 🟢🟡🔴 |
| **Break-Even Progress** | Cumulative savings / Investment | Track to 100% | 🟢🟡🔴 |
| **ROI Realization** | Actual benefits / Projected | > 80% | 🟢🟡🔴 |

---

*This framework transforms IT infrastructure decisions from "What do we need?" to "What delivers the best economic outcome?" — applying CostNav's philosophy to enterprise IT economics.*
