# AI SDM Agent Project

> **Governance-First Agentic AI Framework for Enterprise Service Delivery Management**

## 📚 What is This Project?

This project is a **research-based skills framework** and **governance engine** for building **AI SDM (Software Development Management) Agents**.

It serves as a bridge connecting cutting-edge **Agentic AI research** to practical, **governed enterprise implementations**.

Unlike generic AI assistants, this project focuses on **Governance, Responsibility, and Attribution**. We don't just execute tasks; we ensure they are safe, policy-compliant, and audited via the **O.D.A.L. Loop**.

## 🎯 Quick Navigation

### ✨ New Visitor?
→ **[NAVIGATION.md](NAVIGATION.md)** ← Start here!

### 🛡️ Core Philosophy
→ **[STRATEGY.md](STRATEGY.md)** ← **MUST READ: Why we are different**
*Learn about the O.D.A.L. Loop (Observe-Decide-Act-Log) and our "Governance Over Features" strategy.*

### 🚀 Get Started in 5 Minutes
1. Read [NAVIGATION.md](NAVIGATION.md) (2 min)
2. Use [Research/DECISION_GUIDE.md](Research/DECISION_GUIDE.md) (3 min)
3. Explore the [Skills/Security](Skills/Security/README.md) domain

## 📁 Folder Structure

```
SDM_AI_PROJECT/
│
├─ STRATEGY.md                     🚨 Core Philosophy & Governance Strategy
│
├─ Core/                           🔧 Core Infrastructure
│  ├─ ODAL/                         → 🆕 O.D.A.L. State Machine (Governance Engine)
│  └─ LLM/                          → Multi-LLM Integration System
│     ├─ Clients/                   → Claude, OpenAI, Gemini, Local LLM
│     ├─ Utils/                     → Router, Cost Tracker
│     └─ README.md
│
├─ Skills/                         🛠️ Implementation & Framework
│  ├─ Security/                     → 🆕 Prompt Guard, Policy Engine, Audit Logger
│  ├─ Technical_Skills/             → Technical implementation examples
│  ├─ Framework/                    → Skillset hierarchy & Research mapping
│  ├─ Project_Definition/           → Project vision, goals, scope
│  └─ Cost_Analysis/                → Cost models & ROI analysis
│
├─ Research/                       📚 Theory & Papers
│  ├─ DECISION_GUIDE.md             → Find research matching your needs
│  ├─ A1_Tool_Execution_Signaled/   → Agents learning from tool execution
│  ├─ A2_Agent_Output_Signaled/     → Agents learning from output quality
│  ├─ T1_Agent_Agnostic/            → General-purpose tool utilization
│  └─ T2_Agent_Supervised/          → Custom tool development
│
├─ NAVIGATION.md                   🗺️ Main navigation guide
└─ README.md                       👈 You are here
```

## 🔑 Core Concepts

### 1. The O.D.A.L. Loop (Governance Engine)
We operate on a strict **Observe → Decide → Act → Log** cycle:
- **Observe**: Validate inputs with **Prompt Guard** (Anti-Injection).
- **Decide**: Check **Policy Engine** (Budget, Access) before approval.
- **Act**: Execute only if authorized.
- **Log**: Record decision reasoning in **Audit Logger**.

### 2. Multi-LLM Intelligence Layer (Infrastructure)

| Component | Description | Key Features |
|---|---|---|
| **LLM Clients** | Unified interface for multiple providers | Claude 3.5, GPT-4o, Gemini 1.5, Local Models |
| **Router** | Intelligent LLM selection | Cost-based & Capability-based routing |
| **Cost Tracker** | Real-time budget monitoring | Per-provider tracking, alerts, JSON/CSV export |

### 3. Skills Layer: 5 Domains

| Domain | Description | Key Contents |
|---|---|---|
| **Security** | 🆕 **Governance & Safety** | Prompt Guard, Policy Engine, Audit Logger |
| **Project Definition** | Vision & Scope | Goals, Success Metrics, Stakeholders |
| **Framework** | Skillset Hierarchy | 6 Capabilities, Research Mapping |
| **Technical Skills** | Implementation | Code patterns, Cloud skills, Evaluation |
| **Cost Analysis** | ROI & Budgeting | TCO analysis, Resource planning |

### 4. Research Layer: 4 Categories

| Category | Description | Key Technologies |
|---|---|---|
| **A1: Tool Execution Signaled** | Agents learning from tool execution results | Reinforcement Learning, DPO |
| **A2: Agent Output Signaled** | Agents learning from output quality | Self-Refinement, Preference Learning |
| **T1: Agent-Agnostic Tools** | General-purpose pre-trained tools | CLIP, Whisper, Embeddings |
| **T2: Agent-Supervised Tools** | Tools evolving with agent feedback | Adaptive Retrieval, Memory Systems |

## 🗺️ Navigation Paths

### 👤 "I want to build a Secure Agent"
```
Skills/Security/README.md 
    ↓
Core/ODAL/Examples/odal_demo.py
    ↓
STRATEGY.md (Understanding the philosophy)
```

### 👤 "I want to integrate LLMs"
```
Core/LLM/README.md
    ↓
Core/LLM/Examples/examples.py
```

### 👤 "I want to understand the framework"
```
NAVIGATION.md 
    ↓
Skills/README.md 
    ↓
Research/OVERVIEW.md 
```

## 📊 Project Status

| Area | Completion | Status |
|---|---|---|
| **Governance Engine (O.D.A.L.)** | 100% ✅ | **Complete & Verified** |
| **Security Skills** | 100% ✅ | **Complete (Prompt Guard, Policy, Audit)** |
| **Multi-LLM Integration** | 100% ✅ | **Complete (Routes, Cost Tracking)** |
| Research Documentation | 95% ✅ | Complete (Continuous updates) |
| Skills Framework | 100% ✅ | Complete |
| Navigation Structure | 100% ✅ | Complete |
| Technical Implementation | 70% 🔄 | In Progress |
| Cost Modeling | 75% ⚠️ | Needs validation |

## 🆕 Recent Improvements

✨ **Latest Updates (v1.3):**
- 🛡️ **Security Skills Domain**: Added Prompt Guard (Multi-language), Policy Engine, and Audit Logger.
- ⚙️ **O.D.A.L. Core Engine**: Implemented the state machine that enforces "Policy before Syntax".
- 🤖 **Multi-LLM Integration**: Unified client system for Claude, OpenAI, Gemini, and Local LLMs.
- 📝 **Governance Strategy**: Codified the responsibility structure in STRATEGY.md.

## 🚀 Getting Started

### Step 1: Understand Governance (5 min)
```bash
→ Read STRATEGY.md
```

### Step 2: See it in Action (10 min)
```bash
→ Run Core/ODAL/Examples/odal_demo.py
→ Run Core/LLM/Examples/examples.py
```

### Step 3: Explore Skills (varies)
```bash
→ Read Skills/Security/README.md
→ Read Skills/Framework/README.md
```

## 💡 Key Features

🛡️ **Governance-First Architecture**
- Inputs validated for Prompt Injection (EN/KO/JA/ZH)
- Actions validated against Budget & Access Policies
- All decisions audit-logged

🤖 **Multi-LLM Intelligence**
- Unified interface for 4 LLM providers
- Intelligent routing based on cost & capability
- Fallback mechanisms for reliability

📚 **Research-Backed**
- Built on top of "Adaptation of Agentic AI" research
- Bidirectional mapping between theory and practice

## 📋 Version History

| Version | Date | Changes |
|---|---|---|
| **1.3** | **2026-02-02** | 🆕 **Security Skills & O.D.A.L. Governance Engine** |
| 1.2 | 2026-02-01 | 🆕 Multi-LLM Integration System |
| 1.1 | 2026-01-31 | 🆕 Navigation, Skills hierarchy, Decision Guide |
| 1.0 | 2026-01-31 | Initial structure |

## 📝 License & Attribution

**Original Repository**: [Awesome-Adaptation-of-Agentic-AI](https://github.com/suh004757/Awesome-Adaptation-of-Agentic-AI)

All papers and resources follow their original licenses.

---

**Status**: 🟢 Active & Governed  
**Last Updated**: 2026-02-02  
**Maintainer**: AI SDM Project Team
