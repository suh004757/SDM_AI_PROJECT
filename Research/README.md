# AI SDM Agent Research Repository

## 📂 Directory Structure

```
Research/
├── README.md                          # This file - Repository overview
├── OVERVIEW.md                        # Comprehensive analysis and roadmap
│
├── _Inbox/                            # 📥 NEW RESEARCH GOES HERE
│   ├── README.md                      # Inbox usage guide
│   └── classification_prompt.md       # AI classification instructions
│
├── Agent_Adaptation/                  # How agents learn
│   ├── A1_Tool_Execution_Signaled/
│   │   └── README.md                  # RL from tool execution results
│   └── A2_Agent_Output_Signaled/
│       └── README.md                  # Learning from output quality
│
└── Tool_Adaptation/                   # How tools evolve
    ├── T1_Agent_Agnostic/
    │   └── README.md                  # Pre-trained general tools
    └── T2_Agent_Supervised/
        └── README.md                  # Tools that adapt to agent needs
```

## 🎯 Quick Navigation

### By Priority
- 🔴 **Start Here**: [A1: Tool Execution Signaled](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md)
- 🔴 **Then Read**: [A2: Agent Output Signaled](Agent_Adaptation/A2_Agent_Output_Signaled/README.md)
- 🟡 **After That**: [T2: Agent-Supervised](Tool_Adaptation/T2_Agent_Supervised/README.md)
- 🟢 **Quick Wins**: [T1: Agent-Agnostic](Tool_Adaptation/T1_Agent_Agnostic/README.md)

### By Use Case
- **Improve Action Selection**: → [A1](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md)
- **Better Reports**: → [A2](Agent_Adaptation/A2_Agent_Output_Signaled/README.md)
- **Smarter Context Retrieval**: → [T2](Tool_Adaptation/T2_Agent_Supervised/README.md)
- **Add Standard Tools**: → [T1](Tool_Adaptation/T1_Agent_Agnostic/README.md)

### By AI SDM Skill Set Section
| Skill Set Section | Research Category | Document |
|-------------------|-------------------|----------|
| 3.1 Rule Engine | A1: Tool Execution | [Link](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md) |
| 4.1 Task Control | A1: Tool Execution | [Link](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md) |
| 6.1 Auto Reporting | A2: Output Signaled | [Link](Agent_Adaptation/A2_Agent_Output_Signaled/README.md) |
| 6.2 Explainability | A2: Output Signaled | [Link](Agent_Adaptation/A2_Agent_Output_Signaled/README.md) |
| 2.5 Context Memory | T2: Agent-Supervised | [Link](Tool_Adaptation/T2_Agent_Supervised/README.md) |
| 2.1 Data Ingestion | T1: Agent-Agnostic | [Link](Tool_Adaptation/T1_Agent_Agnostic/README.md) |

## 📚 What's in Each Category

### A1: Tool Execution Signaled
**Focus**: Learn from API call results  
**Top Papers**: Agent-R, FTRL, DeepSeek-Prover-V2  
**Implementation**: RL loop for action selection  
**Impact**: 40% better action selection

### A2: Agent Output Signaled
**Focus**: Learn from output quality feedback  
**Top Papers**: Self-RAG, Agent-Lightning, AutoRefine  
**Implementation**: Self-refinement + preference learning  
**Impact**: 50% less human review time

### T1: Agent-Agnostic
**Focus**: Use pre-trained general tools  
**Top Tools**: E5 embeddings, Whisper, CLIP  
**Implementation**: Plug-and-play integration  
**Impact**: 20% time saved on search

### T2: Agent-Supervised
**Focus**: Tools that adapt to agent usage  
**Top Papers**: AAR, LLM-Retriever, Memento  
**Implementation**: Adaptive retrieval + memory  
**Impact**: 30% better decision quality

## 📥 Adding New Research

### Quick Add (Recommended)
1. **Drop files in `_Inbox/`**: PDF 논문, 마크다운 노트, 링크 등
2. **AI Agent 실행**: Agent가 자동으로 분류하여 적절한 카테고리로 이동
3. **확인**: 분류 로그에서 결과 확인

### Manual Classification
1. 논문을 읽고 주요 내용 파악
2. [분류 가이드](_Inbox/classification_prompt.md) 참고
3. 적절한 카테고리 README에 직접 추가

### Classification Criteria
- **A1**: 도구 실행 결과로 학습 (RL, API feedback)
- **A2**: 출력 품질로 학습 (Self-refinement, Human feedback)
- **T1**: 범용 사전학습 모델 (CLIP, Whisper, Embeddings)
- **T2**: Agent 피드백으로 개선되는 도구 (Adaptive retrieval, Memory)

---

## 🚀 Getting Started

### Week 1: Foundation
1. Read [OVERVIEW.md](OVERVIEW.md) for comprehensive analysis
2. Study [A1 README](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md)
3. Read Agent-R paper

### Week 2-4: First Implementation
1. Implement tool execution logging
2. Build simple RL loop for one action type
3. Measure baseline vs learned policy

### Month 2-3: Expand
1. Add output quality learning (A2)
2. Integrate pre-trained tools (T1)
3. Start adaptive retrieval (T2)

## 📊 Research Status

| Category | Papers | Implementations | Status |
|----------|--------|----------------|--------|
| A1: Tool Execution | 15+ | 5+ | 🔴 Not Started |
| A2: Output Signaled | 20+ | 5+ | 🔴 Not Started |
| T1: Agent-Agnostic | 10+ | 3+ | 🔴 Not Started |
| T2: Agent-Supervised | 15+ | 5+ | 🔴 Not Started |

## 🎓 Learning Resources

### Essential Papers (Read First)
1. **Agent-R** (ByteDance, 2025) - Comprehensive agent learning framework
2. **FTRL** (ByteDance, 2025) - Practical RL for tool use
3. **Self-RAG** (2023) - Self-reflective generation

### Implementation Guides
- Each category README has detailed implementation sections
- Code examples in Python
- Evaluation metrics and tracking templates

### External Resources
- Original repository: [Awesome-Adaptation-of-Agentic-AI](https://github.com/suh004757/Awesome-Adaptation-of-Agentic-AI)
- All papers linked in category READMEs
- Code repositories for each method

## 🔄 Maintenance

### Adding New Research
1. Identify appropriate category (A1/A2/T1/T2)
2. Add to category README
3. Include: paper link, code link, summary, AI SDM application
4. Update status tracking

### Updating Status
- Mark papers as "Read" when completed
- Track implementations tested
- Update metrics as you progress

## 📝 Contributing Guidelines

When adding research:
- **Relevance**: Must be applicable to AI SDM Agent
- **Quality**: Peer-reviewed or from reputable source
- **Practicality**: Include implementation notes
- **Impact**: Estimate expected impact on AI SDM

## 🎯 Success Metrics

### Research Phase
- [ ] All high-priority papers read (10 papers)
- [ ] Implementation guides completed (4 categories)
- [ ] Pilot project selected

### Implementation Phase
- [ ] A1: 40% improvement in action selection
- [ ] A2: 50% reduction in human review time
- [ ] T1: 20% time saved on search
- [ ] T2: 30% better decision quality

### Production Phase
- [ ] All categories deployed
- [ ] Continuous learning active
- [ ] ROI measured and documented

---

**Version**: 1.0  
**Created**: 2026-01-31  
**Last Updated**: 2026-01-31  
**Maintained by**: AI SDM Project Team  
**Source**: Agentic AI research community
