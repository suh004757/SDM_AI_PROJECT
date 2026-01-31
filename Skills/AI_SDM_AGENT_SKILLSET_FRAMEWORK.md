# AI SDM Agent 개발을 위한 Skill Set Framework

## 📋 프로젝트 본질 정의

### 한 줄 요약
> **이 프로젝트는 'AI 개발'이 아니라  
> 'SDM이라는 직무를 하나의 운영체제로 재작성하는 작업'입니다.**

### 핵심 철학
❌ "AI 써서 자동화"  
✅ **"조직 역할을 소프트웨어로 재정의"**

**SDM을 "사람"이 아니라 상태 전이 시스템(State Machine)으로 모델링**

---

## 🎯 Meta Skill (프로젝트의 핵심 역량)

이건 기술이 아니라 **레벨 차이**입니다.

### Required Meta Skills

| Meta Skill | Description | Why Critical |
|------------|-------------|--------------|
| **Role Abstraction** | 직무를 시스템 컴포넌트로 분해하는 능력 | SDM 역할을 함수/상태/이벤트로 재정의 |
| **조직·책임 구조 이해** | 기업 내 의사결정 흐름과 권한 체계 파악 | AI가 올바른 escalation path 설정 |
| **Agentic System Design** | 자율 에이전트 시스템 설계 사고 | 단순 자동화를 넘어 자율 판단 시스템 구축 |
| **System Thinking** | 전체 시스템의 상호작용과 피드백 루프 이해 | 부분 최적화가 아닌 전체 최적화 |

---

## 1️⃣ Delivery Domain Modeling (가장 중요)

**❗ SDM을 "사람"이 아니라 상태 전이 시스템(State Machine)으로 모델링하는 능력**

### 1.1 Service Delivery 개념 모델링

#### 핵심 개념 구조화
- **SLA (Service Level Agreement)** 구조화
- **KPI (Key Performance Indicator)** 정의 및 측정
- **SOW (Statement of Work)** 분해 및 추적

#### 서비스 유형 구분
- **Run**: 운영 유지보수 서비스
- **Project**: 프로젝트 기반 서비스
- **Managed Service**: 관리형 서비스

#### 예외 상황 정의
- **Escalation**: 상위 보고 조건 및 절차
- **Breach**: SLA 위반 조건 및 대응
- **Exception**: 정상 프로세스 예외 처리

#### Required Skills
```
□ Service Management 이론 (ITIL, SLA, SOW)
□ 시스템 사고 (System Thinking)
□ 상태 머신 / 이벤트 기반 모델링
□ 비즈니스 프로세스 모델링 (BPMN)
□ 도메인 주도 설계 (Domain-Driven Design)
```

---

### 1.2 Project / Service State Graph 설계

#### 상태 정의
프로젝트/서비스를 다음 상태로 분류:
- **🟢 정상 (Normal)**: 계획대로 진행 중
- **🟡 지연 (Delayed)**: 경미한 지연, 회복 가능
- **🟠 위험 (At Risk)**: 심각한 지연, 개입 필요
- **🔴 위기 (Critical)**: SLA 위반 임박, 즉각 조치

#### 상태 전이 조건 수식화
```python
# Example: State Transition Logic
if (task_delay_days > sla_threshold * 0.8) and (remaining_buffer < 2_days):
    state = "CRITICAL"
elif (task_delay_days > sla_threshold * 0.5):
    state = "AT_RISK"
elif (task_delay_days > 0):
    state = "DELAYED"
else:
    state = "NORMAL"
```

#### 상태 벡터 표현
**"지금 이 프로젝트는 어떤 상태인가?"를 단일 벡터로 표현**

```python
project_state_vector = {
    "schedule_health": 0.75,      # 0.0 (critical) ~ 1.0 (perfect)
    "budget_health": 0.85,
    "quality_health": 0.90,
    "team_health": 0.70,
    "risk_level": 0.40,           # 0.0 (no risk) ~ 1.0 (extreme)
    "overall_status": "DELAYED"   # Derived from above
}
```

#### State Persistence & Recovery
- **상태 복원 전략**: 시스템 재시작 시 상태 복구
- **상태 이력 추적**: 상태 변화 로그 및 분석

#### Multi-Project State Aggregation
- **포트폴리오 뷰**: 10개 프로젝트 동시 관리 시 전체 상태 표현
- **우선순위 자동 계산**: 가장 위험한 프로젝트 식별

#### Required Skills
```
□ State Machine / Finite Automata
□ Graph-based modeling
□ KPI → State abstraction 능력
□ Multi-dimensional scoring systems
□ State persistence patterns
□ Portfolio management theory
```

---

## 2️⃣ Data Ingestion & Integration

**❗ AI가 SDM이 되려면 현실 세계를 실시간으로 읽어야 함**

### 2.1 Enterprise Tool 연동

#### 프로젝트 관리 도구
- **Jira**: Task, Sprint, Backlog, Burndown
- **Azure DevOps**: Work Items, Boards, Pipelines
- **Microsoft Project**: Gantt, Resource Allocation

#### 클라우드 & 인프라 모니터링
- **Azure Cost Management**: 비용 추적 및 예측
- **Azure Monitor**: 성능 및 가용성 메트릭
- **AWS CloudWatch**: 멀티클라우드 환경 지원

#### 협업 도구
- **Microsoft 365 (Teams, Outlook)**: 커뮤니케이션 로그
- **Slack**: 팀 대화 및 알림
- **SharePoint**: 문서 및 지식 관리

#### Required Skills
```
□ REST API / Webhook 설계
□ OAuth / Service Account 인증
□ Event-driven architecture
□ API rate limiting 및 retry 전략
□ Data synchronization patterns
□ Multi-tenant data isolation
```

---

### 2.2 Telemetry & Signal Engineering

#### Signal 정의
현실 세계의 이벤트를 AI가 이해할 수 있는 **Signal**로 변환:

| Real-world Event | Signal | Threshold |
|------------------|--------|-----------|
| Task 3일 연속 지연 | `task_delay_signal` | `delay_days > 3` |
| SLA 달성률 80% 미만 | `sla_drift_signal` | `achievement < 0.8` |
| 예산 10% 초과 | `cost_variance_signal` | `variance > 0.1` |
| 팀원 3명 동시 휴가 | `resource_shortage_signal` | `available_headcount < threshold` |

#### Human Signal (신규 추가)
- **팀원 피로도**: 연속 근무일, 야근 빈도
- **이탈 징후**: 커밋 빈도 감소, 응답 지연
- **갈등 신호**: 부정적 감정 키워드 탐지 (Teams/Slack)

#### External Dependency Signal (신규 추가)
- **클라이언트 응답 지연**: 승인 요청 후 무응답 기간
- **승인 대기**: 의사결정 병목 탐지
- **벤더 지연**: 외부 의존성 추적

#### Required Skills
```
□ Feature engineering
□ Time-series 데이터 처리
□ Observability 개념 (logs / metrics / traces)
□ Anomaly detection (통계적 이상 탐지)
□ Sentiment analysis (감정 분석)
□ Behavioral analytics
```

---

## 2️⃣.5 Organizational Context & Memory (신규 추가)

**❗ 인간 SDM의 가장 큰 강점: "이 조직/클라이언트를 안다"**

### 2.5.1 Institutional Knowledge Capture

#### 과거 프로젝트 패턴 학습
- **성공 패턴**: 유사 프로젝트에서 효과적이었던 전략
- **실패 패턴**: 반복되는 문제와 원인
- **팀 역학**: 특정 팀 구성의 성과 패턴

#### 클라이언트별 선호도/금기사항
```json
{
  "client_id": "ACME_Corp",
  "preferences": {
    "communication_style": "formal_weekly_reports",
    "escalation_threshold": "low",  // 작은 이슈도 즉시 보고 선호
    "forbidden_keywords": ["delay", "risk"],  // 보고서에서 회피할 단어
    "preferred_meeting_time": "Tuesday 10:00 AM KST"
  },
  "historical_issues": [
    "scope_creep_tendency",
    "late_approval_pattern"
  ]
}
```

#### 팀원별 강점/약점 프로파일
- **기술 스택**: 각 팀원의 전문 분야
- **생산성 패턴**: 시간대별, 요일별 성과
- **협업 스타일**: 선호하는 커뮤니케이션 방식
- **과거 성과**: 이전 프로젝트 기여도

---

### 2.5.2 Long-term Memory Architecture

#### Vector DB for Historical Decisions
```
"2023년 Q2 프로젝트에서 비슷한 리스크 발생 시 어떻게 대응했는가?"
→ Vector similarity search → 과거 의사결정 검색
```

#### Retrieval-Augmented Decision Making
```
현재 상황 → Embedding → 유사 과거 사례 검색 → 
과거 대응 전략 참고 → 현재 상황에 맞게 조정
```

#### Required Skills
```
□ RAG (Retrieval-Augmented Generation)
□ Knowledge graph modeling
□ Organizational learning theory
□ Vector databases (Pinecone, Weaviate, Qdrant)
□ Embedding models (OpenAI, Sentence Transformers)
□ Semantic search
```

---

## 3️⃣ Decision Engine (AI SDM의 두뇌)

**❗ LLM보다 이 레이어가 훨씬 중요**

### 3.1 Rule Engine 설계 (Rule-first)

#### SLA Breach 조건
```python
# Deterministic Rule Example
if (days_until_deadline <= 3) and (completion_rate < 0.9):
    trigger_escalation(level="URGENT", recipient="VP")
    
if (sla_achievement_rate < 0.95) for 2_consecutive_weeks:
    create_improvement_plan()
```

#### Scope Change Acceptance Rules
```python
# Scope Change Decision Logic
def should_accept_scope_change(change_request):
    if change_request.impact_days > remaining_buffer * 0.5:
        return "REJECT", "Insufficient schedule buffer"
    
    if change_request.cost > budget_reserve * 0.3:
        return "ESCALATE", "Requires budget approval"
    
    if change_request.priority == "CRITICAL" and client.tier == "PLATINUM":
        return "ACCEPT", "Strategic client critical request"
    
    return "REVIEW", "Requires manual assessment"
```

#### Auto-Escalation Rules
```python
# Escalation Matrix
escalation_rules = {
    "budget_overrun_10%": {"recipient": "Finance Manager", "sla": "24h"},
    "sla_breach_imminent": {"recipient": "Delivery Director", "sla": "4h"},
    "client_complaint": {"recipient": "Account Manager", "sla": "2h"},
    "security_incident": {"recipient": "CISO", "sla": "immediate"}
}
```

#### Required Skills
```
□ Rule-based system 설계
□ Decision Tree / Policy Engine
□ Deterministic logic 설계
□ Business rules management (Drools, Easy Rules)
□ Conflict resolution strategies
```

---

### 3.2 Heuristic SDM Playbook 구현

**"보통 SDM은 이 상황에서 뭘 하는가?"**

#### 암묵지 → 명시적 규칙화

##### 3.2.1 Playbook Extraction Methodology (신규 추가)

**SDM 인터뷰 프로토콜**
```
질문 예시:
1. "프로젝트가 지연될 조짐이 보일 때 가장 먼저 하는 일은?"
2. "클라이언트가 갑자기 요구사항을 변경하면 어떻게 대응하나요?"
3. "팀원이 번아웃 징후를 보이면?"
4. "예산이 10% 초과될 것 같으면?"
```

**의사결정 트리 역공학**
```
상황: 프로젝트 지연 3일
├─ 원인이 기술적 문제?
│  ├─ Yes → 기술 리드와 1:1 미팅 → 해결책 도출
│  └─ No → 다음 분기
├─ 원인이 리소스 부족?
│  ├─ Yes → 추가 인력 요청 또는 범위 조정
│  └─ No → 다음 분기
└─ 원인이 외부 의존성?
   └─ Yes → 클라이언트/벤더 escalation
```

**Edge Case 카탈로그 작성법**
```markdown
## Edge Case: 핵심 개발자 갑작스런 퇴사

### 발생 빈도: 연 1-2회
### 영향도: Critical
### 대응 Playbook:
1. 즉시 지식 이전 세션 스케줄 (퇴사 전)
2. 코드 리뷰 및 문서화 강화
3. 백업 인력 즉시 투입
4. 클라이언트에 투명하게 커뮤니케이션
5. 일정 재조정 협의
```

#### Heuristic Examples

**Heuristic 1: "조용한 팀원" 패턴**
```
IF team_member.slack_messages < avg * 0.3 FOR 3_days:
    THEN schedule_1on1_checkin()
    # 경험상 조용해지는 건 문제의 신호
```

**Heuristic 2: "금요일 배포 금지"**
```
IF deployment_day == "Friday" AND project.risk_level > "LOW":
    THEN suggest_reschedule_to_monday()
    # 주말 장애 대응 리스크
```

**Heuristic 3: "첫 마일스톤 지연 = 전체 지연"**
```
IF first_milestone.delay_days > 0:
    THEN increase_monitoring_frequency()
    AND revise_overall_timeline(factor=1.2)
    # 초기 지연은 전체 프로젝트 지연으로 이어지는 경향
```

#### Required Skills
```
□ SDM 실무 이해 (최소 5년 경력 수준)
□ Heuristic modeling
□ Edge-case 정리 능력
□ Qualitative research (인터뷰, 관찰)
□ Decision mining
□ Tacit knowledge elicitation (암묵지 추출)
□ Pattern recognition in organizational behavior
```

---

### 3.3 LLM Reasoning Layer (보조)

**LLM은 주연이 아니라 조연**

#### 복합 상황 요약
```
Input: 50개 Jira 티켓, 20개 Slack 대화, 5개 이메일 스레드
Output: "이번 주 핵심 이슈는 DB 마이그레이션 지연입니다. 
        원인은 테스트 환경 불안정이며, 
        DevOps 팀과 조율이 필요합니다."
```

#### 설명 생성 (Explainability)
```
Decision: "프로젝트 일정 2주 연장 권고"
LLM Explanation: 
"현재 완료율 65%이지만 남은 작업의 복잡도가 높습니다.
 과거 유사 프로젝트(Project Alpha)에서 마지막 30%에 
 전체 시간의 50%가 소요된 패턴이 있습니다.
 따라서 2주 버퍼 추가를 권장합니다."
```

#### 리포트 문장 생성
```python
# Template-based + LLM polish
template = "이번 주 {completed_tasks}개 작업 완료, {pending_tasks}개 진행 중"
llm_polished = "이번 주 12개 작업을 성공적으로 완료했으며, 
                8개 작업이 계획대로 진행 중입니다. 
                전반적으로 일정 준수 중입니다."
```

#### Required Skills
```
□ Prompt Engineering
□ Tool-using LLM 설계 (Function Calling)
□ Hallucination 제어 전략
□ RAG (Retrieval-Augmented Generation)
□ LLM output validation
□ Cost optimization (token usage)
```

---

## 4️⃣ Action Execution Layer

**❗ AI가 "말만 하는 관리자"면 실패**

### 4.1 Task Control

#### Task 생성 / 재할당
```python
# Example: Automated Task Creation
def create_task_from_risk(risk):
    task = {
        "title": f"Mitigate Risk: {risk.description}",
        "assignee": risk.owner,
        "priority": risk.severity,
        "due_date": calculate_due_date(risk.impact),
        "description": generate_mitigation_plan(risk)
    }
    jira_api.create_issue(task)
    notify_assignee(task)
```

#### Priority 변경
```python
# Auto-prioritization based on state
if project.state == "CRITICAL":
    for task in project.tasks:
        if task.blocks_milestone:
            task.priority = "P0"
            jira_api.update_priority(task.id, "Highest")
```

#### Deadline 조정
```python
# Intelligent deadline adjustment
if task.estimated_remaining > (task.deadline - today):
    new_deadline = today + task.estimated_remaining + buffer
    request_deadline_extension(task, new_deadline, reason="Realistic re-estimation")
```

#### Required Skills
```
□ API-based command execution
□ Idempotent action 설계 (중복 실행 방지)
□ Rollback 전략 (실행 취소 메커니즘)
□ Transaction management
□ Audit logging
```

---

### 4.2 Communication Automation

#### Stakeholder 보고 메일
```python
# Auto-generated Weekly Report Email
email = {
    "to": stakeholders,
    "subject": f"[Weekly] {project.name} Status - Week {week_number}",
    "body": generate_status_report(project),
    "attachments": [burndown_chart, risk_register],
    "tone": "professional",  # NOT casual
    "send_time": "Friday 17:00"  # Consistent timing
}
```

#### Tone Calibration by Stakeholder (신규 추가)
```python
# Different tone for different audiences
if recipient.role == "C-Level":
    tone = "executive_summary"  # High-level, strategic
    length = "3_bullet_points"
elif recipient.role == "Technical_Lead":
    tone = "detailed_technical"  # In-depth, specific
    length = "full_report"
elif recipient.role == "Client":
    tone = "reassuring_professional"  # Confident, transparent
    length = "balanced"
```

#### Cultural Adaptation (신규 추가)
```python
# Global project considerations
if client.region == "APAC":
    communication_style = "formal_hierarchical"
    avoid_direct_criticism = True
elif client.region == "US":
    communication_style = "direct_actionable"
    emphasize_solutions = True
```

#### SLA Breach 통보
```python
# Immediate escalation on SLA breach
if sla_breach_detected:
    send_alert(
        recipients=[account_manager, delivery_director],
        severity="HIGH",
        message=f"SLA breach detected: {breach_details}",
        required_action="Immediate mitigation plan needed",
        response_sla="2 hours"
    )
```

#### Escalation 알림
```python
# Escalation with context
escalation_email = {
    "to": escalation_matrix[issue.severity],
    "subject": f"🚨 ESCALATION: {issue.title}",
    "body": f"""
    Issue: {issue.description}
    Impact: {issue.impact}
    Actions Taken: {issue.mitigation_attempts}
    Reason for Escalation: {issue.escalation_reason}
    Recommended Next Steps: {issue.recommendations}
    """,
    "cc": [sdm, project_manager],
    "priority": "HIGH"
}
```

#### Required Skills
```
□ System-generated communication 설계
□ Tone consistency (Non-emotional, professional)
□ Audit-safe 메시지 포맷 (법적 검토 가능)
□ Email template engineering
□ Multi-language support
□ Accessibility compliance (WCAG)
```

---

## 5️⃣ Risk Prediction & Early Warning

**❗ 인간 SDM을 넘어서는 영역**

### 5.1 Risk Pattern Detection

#### 반복 지연 패턴
```python
# Detect recurring delay patterns
if task.delay_count >= 3:
    pattern = analyze_delay_pattern(task.history)
    # Pattern: "매주 월요일 지연" → 주말 작업 미완료
    # Pattern: "특정 개발자 담당 시 지연" → 스킬 갭 또는 과부하
    
    root_cause = identify_root_cause(pattern)
    recommend_intervention(root_cause)
```

#### 특정 리소스 병목
```python
# Bottleneck detection
resource_utilization = calculate_utilization(team)
if resource_utilization["DevOps_Engineer"] > 0.95:
    alert("DevOps Engineer is bottleneck")
    suggest_alternatives([
        "Hire additional DevOps resource",
        "Automate deployment pipeline",
        "Redistribute tasks to other team members"
    ])
```

#### 인력 과부하 신호
```python
# Burnout risk detection
for member in team:
    if (member.overtime_hours > 20/week) AND (member.vacation_days_used == 0):
        burnout_risk_score = calculate_burnout_risk(member)
        if burnout_risk_score > 0.7:
            recommend_intervention(member, "mandatory_time_off")
```

#### Required Skills
```
□ Statistical analysis (회귀, 상관관계)
□ Simple ML (classification / anomaly detection)
□ Pattern recognition
□ Time-series forecasting
□ Clustering algorithms
```

---

### 5.2 Probabilistic Forecasting

#### "2주 내 SLA breach 확률"
```python
# Monte Carlo simulation
def forecast_sla_breach_probability(project, horizon_days=14):
    simulations = []
    for _ in range(10000):
        simulated_completion = simulate_project_completion(
            current_state=project.state,
            remaining_tasks=project.tasks,
            team_velocity=project.velocity,
            risk_events=sample_risk_events()
        )
        simulations.append(simulated_completion)
    
    breach_probability = sum(1 for s in simulations if s > project.sla_deadline) / len(simulations)
    return breach_probability

# Output: "67% probability of SLA breach in next 14 days"
```

#### "현재 인력 구조 유지 시 실패 확률"
```python
# Scenario analysis
scenarios = {
    "current_team": simulate_outcome(team=current_team),
    "add_1_senior": simulate_outcome(team=current_team + senior_dev),
    "add_2_junior": simulate_outcome(team=current_team + [junior_dev, junior_dev]),
}

for scenario, outcome in scenarios.items():
    print(f"{scenario}: Success probability = {outcome.success_rate}")

# Output:
# current_team: Success probability = 45%
# add_1_senior: Success probability = 78%
# add_2_junior: Success probability = 52%
```

#### Required Skills
```
□ Probability modeling
□ Monte Carlo / Scenario simulation
□ Risk scoring framework
□ Bayesian inference
□ Sensitivity analysis
□ Confidence interval calculation
```

---

## 6️⃣ Reporting & Explainability

**❗ AI SDM은 설명 가능한 관리자여야 함**

### 6.1 Auto Reporting

#### Weekly / Monthly Status
```python
# Automated report generation
weekly_report = {
    "executive_summary": generate_summary(project, audience="executives"),
    "progress_metrics": calculate_kpis(project),
    "accomplishments": extract_completed_milestones(project),
    "upcoming_milestones": forecast_next_milestones(project),
    "risks_and_issues": prioritize_risks(project.risks),
    "budget_status": analyze_budget_variance(project),
    "decisions_needed": identify_pending_decisions(project)
}

distribute_report(weekly_report, stakeholders, format="PDF")
```

#### KPI / SLA 요약
```python
# KPI Dashboard
kpi_summary = {
    "SLA_Achievement": "94.5%",  # Target: 95%
    "On_Time_Delivery": "87%",   # Target: 90%
    "Budget_Variance": "+3.2%",  # Target: ±5%
    "Quality_Score": "4.2/5.0",  # Target: 4.0
    "Team_Satisfaction": "3.8/5.0"  # Target: 4.0
}

# Visual representation
generate_dashboard(kpi_summary, format="PowerBI")
```

#### Risk Outlook
```python
# Forward-looking risk analysis
risk_outlook = {
    "next_30_days": {
        "high_risks": 2,
        "medium_risks": 5,
        "low_risks": 8,
        "top_concern": "Database migration complexity"
    },
    "mitigation_status": {
        "on_track": 10,
        "delayed": 3,
        "not_started": 2
    },
    "recommended_actions": [
        "Allocate additional DBA resource for migration",
        "Schedule risk review meeting with client",
        "Update contingency plan for Scenario B"
    ]
}
```

#### Required Skills
```
□ Data-to-text generation (NLG)
□ Structured reporting
□ Executive summary 작성 능력
□ Data visualization (charts, dashboards)
□ Business intelligence tools (Power BI, Tableau)
```

---

### 6.2 Decision Traceability

**왜 이 결정을 내렸는가? 어떤 규칙이 적용되었는가?**

#### Decision Logging
```python
# Every decision must be logged
decision_log = {
    "decision_id": "DEC-2026-001",
    "timestamp": "2026-01-31T14:30:00Z",
    "decision": "Extend project deadline by 2 weeks",
    "trigger": "SLA breach probability exceeded 70%",
    "rules_applied": [
        "RULE-047: Auto-extend if breach probability > 65%",
        "RULE-103: Require client approval for extension > 1 week"
    ],
    "data_inputs": {
        "current_completion": "68%",
        "remaining_tasks": 47,
        "team_velocity": "3.2 tasks/day",
        "forecasted_completion": "2026-02-18",
        "original_deadline": "2026-02-05"
    },
    "alternatives_considered": [
        "Add 2 additional developers (rejected: budget constraint)",
        "Reduce scope (rejected: client priority)",
        "Extend deadline (selected)"
    ],
    "human_override": None,  # No human intervention
    "outcome": "Client approved extension on 2026-02-01"
}
```

#### Explainable AI (XAI)
```python
# Generate human-readable explanation
explanation = f"""
Decision: {decision_log['decision']}

Why this decision was made:
1. Current project completion is {decision_log['data_inputs']['current_completion']}
2. Based on team velocity of {decision_log['data_inputs']['team_velocity']}, 
   forecasted completion is {decision_log['data_inputs']['forecasted_completion']}
3. This exceeds original deadline by 13 days
4. Monte Carlo simulation shows 72% probability of SLA breach
5. Rule RULE-047 automatically triggers deadline extension recommendation
6. Alternative options (adding resources, reducing scope) were evaluated but rejected

This decision aligns with:
- Risk mitigation strategy (avoid SLA breach)
- Client relationship (transparent communication)
- Budget constraints (no additional hiring)
"""
```

#### Audit Trail
```python
# Complete audit trail for compliance
audit_trail = {
    "decision_chain": [
        "Signal detected: task_delay_signal",
        "Rule triggered: RULE-047",
        "Data retrieved: project metrics from Jira",
        "Simulation executed: Monte Carlo 10,000 iterations",
        "Alternatives evaluated: 3 options",
        "Recommendation generated: Extend deadline",
        "Approval requested: Client stakeholder",
        "Decision executed: Jira deadline updated",
        "Notification sent: All stakeholders"
    ],
    "human_touchpoints": [
        "Client approval: 2026-02-01 09:15 AM",
        "SDM review: 2026-02-01 10:30 AM"
    ],
    "reversibility": "Can be rolled back within 48 hours"
}
```

#### Required Skills
```
□ Decision logging
□ Explainable AI (XAI) 개념
□ Audit trail 설계
□ Provenance tracking
□ Compliance frameworks (SOX, GDPR)
□ Forensic analysis capability
```

---

## 7️⃣ Governance, Safety, Failure Control

**❗ 100% AI일수록 통제 설계가 더 중요**

### 7.1 Guardrail & Boundary 설정

#### 권한 제한
```python
# AI SDM permission boundaries
ai_permissions = {
    "can_do_autonomously": [
        "Create tasks",
        "Update task priorities",
        "Send status reports",
        "Generate risk alerts",
        "Adjust minor deadlines (<3 days)"
    ],
    "requires_human_approval": [
        "Budget changes >5%",
        "Deadline extensions >1 week",
        "Team member reassignment",
        "Scope changes",
        "Client communication (critical issues)"
    ],
    "strictly_forbidden": [
        "Fire team members",
        "Sign contracts",
        "Commit to SLA without approval",
        "Share confidential data externally"
    ]
}
```

#### 비용 상한
```python
# Cost guardrails
cost_limits = {
    "single_action_limit": 1000,  # USD
    "daily_limit": 5000,
    "monthly_limit": 50000,
    "requires_approval_above": 500
}

def execute_action_with_cost(action, estimated_cost):
    if estimated_cost > cost_limits["single_action_limit"]:
        return "REJECTED", "Exceeds single action limit"
    
    if estimated_cost > cost_limits["requires_approval_above"]:
        return "PENDING_APPROVAL", request_human_approval(action, estimated_cost)
    
    return "APPROVED", execute(action)
```

#### 자동 중단 조건
```python
# Kill-switch conditions
kill_switch_triggers = {
    "consecutive_failures": 5,  # Stop after 5 failed actions
    "error_rate": 0.3,  # Stop if 30% of actions fail
    "human_override_rate": 0.5,  # Stop if 50% of decisions are overridden
    "sla_breach_caused": 1,  # Stop if AI causes SLA breach
    "security_incident": 1  # Immediate stop on security issue
}

if check_kill_switch(ai_agent):
    ai_agent.pause()
    alert_human_operator("AI SDM paused due to kill-switch trigger")
    require_manual_restart()
```

#### Required Skills
```
□ Safety-by-design
□ Policy enforcement
□ Kill-switch 설계
□ Circuit breaker patterns
□ Rate limiting
□ Permission management (RBAC)
```

---

### 7.2 Failure Mode 설계

**AI 판단 오류 시, 데이터 누락 시, 외부 시스템 장애 시**

#### AI 판단 오류 시
```python
# Confidence-based escalation
def make_decision(context):
    decision, confidence = ai_model.predict(context)
    
    if confidence < 0.7:
        return escalate_to_human(context, reason="Low confidence")
    
    if decision in high_risk_decisions:
        return request_human_review(decision, context)
    
    return execute_decision(decision)
```

#### 데이터 누락 시
```python
# Graceful degradation
def get_project_status(project_id):
    try:
        jira_data = fetch_jira_data(project_id)
    except APIError:
        jira_data = use_cached_data(project_id, max_age="24h")
        log_warning("Using cached Jira data due to API failure")
    
    if jira_data is None:
        return fallback_to_manual_input(project_id)
    
    return analyze_status(jira_data)
```

#### 외부 시스템 장애 시
```python
# Fallback strategies
external_systems = {
    "jira": {
        "primary": "https://company.atlassian.net",
        "fallback": "local_cache",
        "max_cache_age": "6h"
    },
    "azure_cost": {
        "primary": "Azure Cost Management API",
        "fallback": "last_known_values",
        "alert_on_fallback": True
    }
}

def fetch_data_with_fallback(system_name):
    system = external_systems[system_name]
    try:
        return fetch_from_primary(system["primary"])
    except Exception as e:
        log_error(f"{system_name} primary failed: {e}")
        if system["alert_on_fallback"]:
            alert_ops_team(system_name)
        return fetch_from_fallback(system["fallback"])
```

#### Required Skills
```
□ Fault-tolerant system design
□ Fallback 전략
□ Chaos thinking (Chaos Engineering)
□ Graceful degradation
□ Circuit breaker patterns
□ Retry with exponential backoff
```

---

### 7.3 Human-in-the-Loop Escalation (신규 추가)

**어떤 결정은 반드시 사람에게 올려야 하는가?**

#### Confidence Threshold 설계
```python
# Escalation based on confidence
escalation_policy = {
    "confidence < 0.5": "MANDATORY_HUMAN_REVIEW",
    "confidence 0.5-0.7": "OPTIONAL_HUMAN_REVIEW",
    "confidence 0.7-0.9": "HUMAN_NOTIFICATION",
    "confidence > 0.9": "AUTONOMOUS_EXECUTION"
}

def decide_with_escalation(decision_context):
    decision, confidence = ai_decide(decision_context)
    policy = escalation_policy[get_confidence_range(confidence)]
    
    if policy == "MANDATORY_HUMAN_REVIEW":
        return await_human_decision(decision_context)
    elif policy == "OPTIONAL_HUMAN_REVIEW":
        return suggest_to_human_with_timeout(decision, timeout="4h")
    elif policy == "HUMAN_NOTIFICATION":
        notify_human(decision)
        return execute(decision)
    else:
        return execute(decision)
```

#### Override Mechanism
```python
# Human can override AI decisions
decision_record = {
    "ai_recommendation": "Extend deadline by 2 weeks",
    "human_override": "Extend by 1 week only",
    "override_reason": "Client relationship consideration",
    "learning_signal": True  # Use this to improve AI
}

# AI learns from overrides
if decision_record["learning_signal"]:
    update_model_with_feedback(
        context=decision_record["context"],
        ai_decision=decision_record["ai_recommendation"],
        correct_decision=decision_record["human_override"],
        reason=decision_record["override_reason"]
    )
```

#### Escalation Protocol Design
```python
# Clear escalation paths
escalation_matrix = {
    "budget_decision": {
        "threshold": 5000,  # USD
        "escalate_to": "Finance Manager",
        "sla": "24h",
        "fallback": "CFO"
    },
    "scope_change": {
        "threshold": "any",
        "escalate_to": "Product Owner",
        "sla": "48h",
        "fallback": "Delivery Director"
    },
    "team_conflict": {
        "threshold": "severity > MEDIUM",
        "escalate_to": "HR Manager",
        "sla": "4h",
        "fallback": "VP Engineering"
    }
}
```

#### Required Skills
```
□ Human-AI collaboration design
□ Escalation protocol design
□ Trust calibration
□ Active learning systems
□ Feedback loop design
```

---

## 8️⃣ 구현 우선순위 및 로드맵

### Phase 1: Foundation (3-6개월)
**목표: 결정론적 시스템 구축**

| Priority | Skill Area | Deliverable |
|----------|-----------|-------------|
| 🔴 P0 | **1.1 Domain Modeling** | State Machine 설계 완료 |
| 🔴 P0 | **3.1 Rule Engine** | 핵심 비즈니스 규칙 100개 구현 |
| 🔴 P0 | **2.1 Data Ingestion** | Jira 연동 완료 |
| 🟡 P1 | **1.2 State Graph** | 프로젝트 상태 벡터 정의 |
| 🟡 P1 | **6.2 Decision Logging** | 모든 결정 추적 시스템 |

**Success Criteria:**
- AI가 80% 이상의 상황에서 올바른 규칙 적용
- 모든 의사결정이 추적 가능
- Jira 데이터 실시간 동기화

---

### Phase 2: Intelligence (3-6개월)
**목표: 패턴 인식 및 예측 능력**

| Priority | Skill Area | Deliverable |
|----------|-----------|-------------|
| 🔴 P0 | **3.2 Heuristic Playbook** | SDM 암묵지 50개 규칙화 |
| 🔴 P0 | **5.1 Risk Pattern Detection** | 반복 패턴 자동 탐지 |
| 🟡 P1 | **2.2 Signal Engineering** | 20개 핵심 Signal 정의 |
| 🟡 P1 | **2.5 Context Memory** | 과거 프로젝트 학습 시스템 |
| 🟢 P2 | **5.2 Probabilistic Forecasting** | Monte Carlo 시뮬레이션 |

**Success Criteria:**
- 리스크 조기 탐지율 70% 이상
- 과거 프로젝트 패턴 활용 가능
- 예측 정확도 ±10% 이내

---

### Phase 3: Autonomy (6-12개월)
**목표: 자율 실행 및 커뮤니케이션**

| Priority | Skill Area | Deliverable |
|----------|-----------|-------------|
| 🔴 P0 | **4.1 Task Control** | 자동 Task 생성/할당 |
| 🔴 P0 | **4.2 Communication** | 자동 보고서 생성 |
| 🟡 P1 | **3.3 LLM Reasoning** | 복합 상황 요약 |
| 🟡 P1 | **6.1 Auto Reporting** | Weekly/Monthly 자동화 |
| 🟢 P2 | **7.3 HITL Escalation** | 사람-AI 협업 프로토콜 |

**Success Criteria:**
- 80% 업무 자동 처리
- 보고서 품질 인간 수준
- Escalation 정확도 95% 이상

---

### Phase 4: Scale & Governance (지속)
**목표: 안정성 및 확장성**

| Priority | Skill Area | Deliverable |
|----------|-----------|-------------|
| 🔴 P0 | **7.1 Guardrails** | 안전 장치 완비 |
| 🔴 P0 | **7.2 Failure Mode** | 장애 대응 시스템 |
| 🟡 P1 | **Multi-project** | 10개 프로젝트 동시 관리 |
| 🟢 P2 | **5.2 Advanced Forecasting** | 시나리오 분석 고도화 |

**Success Criteria:**
- Zero critical failures
- 10개 프로젝트 동시 관리 가능
- Human override rate < 10%

---

## 9️⃣ 기술 스택 권장사항

### Core Technologies

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Rule Engine** | Drools / Easy Rules | 복잡한 비즈니스 규칙 관리 |
| **State Machine** | XState / Spring State Machine | 상태 전이 로직 명확화 |
| **Data Integration** | Apache Kafka / Azure Event Hub | 실시간 이벤트 처리 |
| **Time-series DB** | InfluxDB / TimescaleDB | 메트릭 및 Signal 저장 |
| **Vector DB** | Pinecone / Weaviate | 과거 의사결정 검색 |
| **LLM** | GPT-4 / Claude 3.5 | 복합 상황 요약 및 설명 생성 |
| **Workflow Engine** | Temporal / Apache Airflow | 복잡한 워크플로우 오케스트레이션 |
| **Monitoring** | Prometheus + Grafana | AI 시스템 자체 모니터링 |

---

## 🎓 학습 경로 및 자격증

### Recommended Learning Path

#### Year 1: Foundations
```
□ Service Management (ITIL Foundation)
□ Project Management (PMP or PRINCE2)
□ System Design (Designing Data-Intensive Applications)
□ State Machines (Formal Methods)
□ Python/Java for Rule Engines
```

#### Year 2: AI & Data
```
□ Machine Learning Basics (Coursera ML)
□ Time-series Analysis
□ LLM Engineering (Prompt Engineering, RAG)
□ Vector Databases
□ Event-driven Architecture
```

#### Year 3: Advanced Topics
```
□ Explainable AI (XAI)
□ Human-AI Collaboration
□ Chaos Engineering
□ Organizational Behavior
□ Tacit Knowledge Elicitation
```

### Certifications

| Certification | Relevance | Priority |
|--------------|-----------|----------|
| **ITIL 4 Foundation** | Service Management 기초 | 🔴 High |
| **PMP / PRINCE2** | 프로젝트 관리 프레임워크 | 🔴 High |
| **AWS/Azure Solutions Architect** | 클라우드 인프라 이해 | 🟡 Medium |
| **Certified Scrum Master** | Agile 방법론 | 🟡 Medium |
| **Machine Learning Engineer** | ML 시스템 구축 | 🟢 Low |

---

## 📊 성공 지표 (Success Metrics)

### AI SDM Agent 성과 측정

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Decision Accuracy** | >90% | Human agreement rate |
| **Risk Detection Rate** | >70% | Early warning success |
| **Automation Rate** | >80% | Tasks handled autonomously |
| **Response Time** | <5 min | Time to detect and respond |
| **SLA Achievement** | >95% | Projects meeting SLA |
| **Cost Efficiency** | -30% | vs. human SDM cost |
| **Stakeholder Satisfaction** | >4.0/5.0 | Survey score |
| **Human Override Rate** | <10% | AI decisions overridden |

---

## 🚀 Quick Start Guide

### Step 1: 현재 상태 평가
```markdown
1. 기존 SDM 프로세스 문서화
2. 가장 반복적인 업무 5개 식별
3. 데이터 소스 접근성 확인 (Jira, Azure, etc.)
4. 핵심 비즈니스 규칙 10개 추출
```

### Step 2: Pilot Project 선정
```markdown
- 복잡도: Medium (너무 쉽지도, 어렵지도 않게)
- 기간: 3-6개월
- 팀 규모: 10-15명
- 데이터 가용성: High (Jira/Azure 완전 연동)
- 리스크: Low (실패해도 영향 제한적)
```

### Step 3: MVP 구축 (4주)
```markdown
Week 1: State Machine 설계
Week 2: Jira 연동 + 기본 Rule Engine
Week 3: 자동 상태 보고서 생성
Week 4: 테스트 및 피드백
```

### Step 4: 반복 개선
```markdown
- 매주 Human override 분석
- 매월 새로운 규칙 10개 추가
- 분기별 성과 측정 및 조정
```

---

## 📚 참고 자료

### Books
- **"The Phoenix Project"** - DevOps 및 서비스 관리
- **"Designing Data-Intensive Applications"** - 시스템 설계
- **"Thinking in Systems"** - 시스템 사고
- **"The Tacit Dimension"** - 암묵지 이론

### Papers
- **"Human-AI Collaboration in Decision-Making"** (ACM)
- **"Explainable AI for Business Process Management"** (IEEE)
- **"State Machine Replication in Distributed Systems"** (SOSP)

### Online Resources
- **ITIL 4 Official Site**: https://www.axelos.com/certifications/itil-service-management
- **PMI (Project Management Institute)**: https://www.pmi.org/
- **Temporal.io Documentation**: https://docs.temporal.io/

---

## ✅ Skill Assessment Checklist

### Self-Assessment (Rate 1-5)

#### Domain Modeling
- [ ] SLA/KPI/SOW 구조화 능력: ___/5
- [ ] State Machine 설계: ___/5
- [ ] 상태 전이 조건 수식화: ___/5

#### Data Integration
- [ ] REST API 연동: ___/5
- [ ] Event-driven architecture: ___/5
- [ ] Signal engineering: ___/5

#### Decision Engine
- [ ] Rule-based system 설계: ___/5
- [ ] Heuristic modeling: ___/5
- [ ] LLM prompt engineering: ___/5

#### Action Execution
- [ ] API-based automation: ___/5
- [ ] Idempotent design: ___/5
- [ ] Communication automation: ___/5

#### Risk & Forecasting
- [ ] Pattern detection: ___/5
- [ ] Statistical analysis: ___/5
- [ ] Monte Carlo simulation: ___/5

#### Governance
- [ ] Safety-by-design: ___/5
- [ ] Failure mode analysis: ___/5
- [ ] HITL protocol design: ___/5

**Total Score: ___/90**

**Interpretation:**
- 75-90: Ready to lead AI SDM project
- 60-74: Need focused skill development
- <60: Foundational learning required

---

## 🎯 최종 요약

### 이 Skill Set의 핵심 차별점

1. **Rule-first, LLM-last**: 결정론적 시스템이 기반
2. **State Machine Thinking**: SDM을 상태 전이 시스템으로 모델링
3. **Organizational Context**: 과거 프로젝트 학습 및 조직 맥락 이해
4. **Human Signal**: 사람의 피로도, 이탈 징후까지 탐지
5. **Explainability**: 모든 결정이 추적 가능하고 설명 가능
6. **Safety-first**: Guardrail과 Kill-switch로 안전성 확보
7. **HITL Protocol**: 사람-AI 협업 프로토콜 명확화

### 성공의 핵심

> **"기술이 아니라 도메인 이해가 80%입니다.  
> SDM이 무엇을 하는지, 왜 하는지, 어떻게 판단하는지를  
> 시스템으로 재작성하는 것이 본질입니다."**

---

**Version**: 1.0  
**Last Updated**: 2026-01-31  
**Maintained by**: AI SDM Project Team
