# AI Agent 분류 프롬프트

## 📋 Task

`_Inbox` 폴더의 리서치 자료를 분석하고 적절한 카테고리로 분류하세요.

## 🎯 분류 카테고리

### A1: Tool Execution Signaled
- **정의**: Agent가 도구 실행 결과로부터 학습
- **신호 소스**: API 응답, 성공/실패 피드백, 실행 결과
- **학습 방법**: Reinforcement Learning, Supervised Fine-tuning, DPO
- **키워드**: RL, tool execution, API feedback, action selection, reward model, policy learning

### A2: Agent Output Signaled
- **정의**: Agent가 자신의 출력 품질로부터 학습
- **신호 소스**: 인간 피드백, 자기 평가, 결과 메트릭
- **학습 방법**: Self-refinement, Preference learning, Iterative improvement
- **키워드**: self-refinement, output quality, human feedback, preference learning, self-evaluation, DPO

### T1: Agent-Agnostic
- **정의**: Agent와 독립적으로 작동하는 범용 도구
- **특징**: 사전학습, 플러그앤플레이, 범용 목적
- **예시**: CLIP, SAM, Whisper, 임베딩 모델
- **키워드**: pre-trained, embedding, general-purpose, plug-and-play, foundation model

### T2: Agent-Supervised
- **정의**: Agent 피드백으로 개선되는 도구
- **학습**: Agent 사용 패턴으로부터 적응
- **예시**: Adaptive retrieval, Memory systems, Custom adapters
- **키워드**: adaptive retrieval, memory system, tool adaptation, agent feedback, fine-tuning

## 🔍 분류 프로세스

### Step 1: 파일 읽기
```python
# Inbox의 모든 파일 스캔
files = scan_inbox_folder()
for file in files:
    content = read_file(file)
    classify_and_move(file, content)
```

### Step 2: 내용 분석
다음을 확인:
1. **제목/초록**: 주요 주제 파악
2. **키워드**: 위 카테고리 키워드 매칭
3. **방법론**: 학습 방법 (RL, Self-refinement, Pre-training, Adaptation)
4. **신호 소스**: 무엇으로부터 학습하는가?

### Step 3: 분류 결정
```python
def classify_research(content):
    # 키워드 매칭
    keywords = extract_keywords(content)
    
    # 점수 계산
    scores = {
        "A1": calculate_score(keywords, A1_KEYWORDS),
        "A2": calculate_score(keywords, A2_KEYWORDS),
        "T1": calculate_score(keywords, T1_KEYWORDS),
        "T2": calculate_score(keywords, T2_KEYWORDS)
    }
    
    # 최고 점수 카테고리 선택
    primary_category = max(scores, key=scores.get)
    
    # 2차 카테고리 (점수가 임계값 이상)
    secondary_categories = [
        cat for cat, score in scores.items() 
        if score > THRESHOLD and cat != primary_category
    ]
    
    return primary_category, secondary_categories
```

### Step 4: 파일 이동 및 문서화
```python
def move_and_document(file, primary_cat, secondary_cats):
    # 1. 파일을 주 카테고리로 이동
    new_path = f"Research/{primary_cat}/{file.name}"
    move_file(file, new_path)
    
    # 2. 주 카테고리 README 업데이트
    update_category_readme(primary_cat, file, "full")
    
    # 3. 부 카테고리에 링크 추가
    for cat in secondary_cats:
        update_category_readme(cat, file, "link")
    
    # 4. 분류 로그 기록
    log_classification(file, primary_cat, secondary_cats)
```

## 📝 README 업데이트 템플릿

### 새 논문 추가 시
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
