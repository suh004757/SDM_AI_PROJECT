# AI Agent Classification Prompt

## 📋 Task

Analyze research materials in the `_Inbox` folder and classify them into appropriate categories.

## 🎯 Classification Categories

### A1: Tool Execution Signaled
- **Definition**: Agent learns from tool execution results
- **Signal Source**: API responses, success/failure feedback, execution results
- **Learning Methods**: Reinforcement Learning, Supervised Fine-tuning, DPO
- **Keywords**: RL, tool execution, API feedback, action selection, reward model, policy learning

### A2: Agent Output Signaled
- **Definition**: Agent learns from its own output quality
- **Signal Source**: Human feedback, self-evaluation, outcome metrics
- **Learning Methods**: Self-refinement, Preference learning, Iterative improvement
- **Keywords**: self-refinement, output quality, human feedback, preference learning, self-evaluation, DPO

### T1: Agent-Agnostic
- **Definition**: General-purpose tools that work independently of agents
- **Characteristics**: Pre-trained, plug-and-play, general-purpose
- **Examples**: CLIP, SAM, Whisper, embedding models
- **Keywords**: pre-trained, embedding, general-purpose, plug-and-play, foundation model

### T2: Agent-Supervised
- **Definition**: Tools that improve based on agent feedback
- **Learning**: Adapts from agent usage patterns
- **Examples**: Adaptive retrieval, Memory systems, Custom adapters
- **Keywords**: adaptive retrieval, memory system, tool adaptation, agent feedback, fine-tuning

## 🔍 Classification Process

### Step 1: Read Files
```python
# Scan all files in Inbox
files = scan_inbox_folder()
for file in files:
    content = read_file(file)
    classify_and_move(file, content)
```

### Step 2: Analyze Content
Check the following:
1. **Title/Abstract**: Identify main topic
2. **Keywords**: Match with category keywords above
3. **Methodology**: Learning method (RL, Self-refinement, Pre-training, Adaptation)
4. **Signal Source**: What does it learn from?

### Step 3: Classification Decision
```python
def classify_research(content):
    # Keyword matching
    keywords = extract_keywords(content)
    
    # Calculate scores
    scores = {
        "A1": calculate_score(keywords, A1_KEYWORDS),
        "A2": calculate_score(keywords, A2_KEYWORDS),
        "T1": calculate_score(keywords, T1_KEYWORDS),
        "T2": calculate_score(keywords, T2_KEYWORDS)
    }
    
    # Select category with highest score
    primary_category = max(scores, key=scores.get)
    
    # Secondary categories (score above threshold)
    secondary_categories = [
        cat for cat, score in scores.items() 
        if score > THRESHOLD and cat != primary_category
    ]
    
    return primary_category, secondary_categories
```

### Step 4: Move Files and Document
```python
def move_and_document(file, primary_cat, secondary_cats):
    # 1. Move file to primary category
    new_path = f"Research/{primary_cat}/{file.name}"
    move_file(file, new_path)
    
    # 2. Update primary category README
    update_category_readme(primary_cat, file, "full")
    
    # 3. Add links to secondary categories
    for cat in secondary_cats:
        update_category_readme(cat, file, "link")
    
    # 4. Log classification
    log_classification(file, primary_cat, secondary_cats)
```

## 📝 README Update Template

### Adding New Paper
```markdown
#### [N+1]. [Paper Title] ([Author/Org], [Year])
- **Paper**: [URL]
- **Code**: [URL if available]
- **Summary**: [1-2 sentence summary]
- **Key Contribution**: [Main innovation]
- **AI SDM Application**: [How to apply to AI SDM Agent]

**Why Relevant**:
- [Reason 1]
- [Reason 2]
```

### 링크만 추가 시 (부 카테고리)
```markdown
**Related**: See also [Paper Title] in [Primary Category]
```

## 🚨 예외 처리

### 분류 불가능한 경우
- `_Inbox/Unclassified/` 폴더로 이동
- 수동 검토 필요 플래그 추가

### 여러 카테고리에 동등하게 해당
- 가장 AI SDM Agent에 직접적으로 적용 가능한 카테고리 선택
- 우선순위: A1 > A2 > T2 > T1

### 새로운 카테고리 필요
- `_Inbox/New_Category_Proposals/` 폴더에 제안서 작성
- 기존 카테고리 확장 가능성 먼저 검토

## 📊 분류 로그 형식

```markdown
# Classification Log

## [Date]

### [Filename]
- **Primary Category**: A1_Tool_Execution_Signaled
- **Secondary Categories**: A2_Agent_Output_Signaled
- **Confidence**: 0.85
- **Key Matched Keywords**: RL, tool execution, reward model
- **AI SDM Relevance**: High - Directly applicable to task assignment learning
- **Action Taken**: Moved to A1, added link in A2
```

## 🎯 분류 품질 체크리스트

분류 전 확인:
- [ ] 논문 제목과 초록을 읽었는가?
- [ ] 주요 방법론을 파악했는가?
- [ ] AI SDM Agent 적용 가능성을 평가했는가?
- [ ] 카테고리 정의와 일치하는가?
- [ ] 기존 카테고리 논문들과 유사성을 확인했는가?

분류 후 확인:
- [ ] README가 올바르게 업데이트되었는가?
- [ ] 파일이 올바른 위치로 이동했는가?
- [ ] 분류 로그가 기록되었는가?
- [ ] 부 카테고리 링크가 추가되었는가?

---

**사용 방법**: 
이 프롬프트를 AI Agent에게 제공하고 `_Inbox` 폴더를 스캔하도록 지시하세요.
