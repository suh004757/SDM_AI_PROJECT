\# Service Delivery Manager (SDM) AI Agent 프로젝트



\## 📋 프로젝트 개요



\### 목표

Service Delivery Manager 역할을 수행하는 AI Agent/Solution 개발을 위한 \*\*1단계 실증 프로젝트\*\*



\### 핵심 접근 방식

\*\*"Human-in-the-Loop AI Execution"\*\*

\- AI가 SDM의 모든 업무를 처음부터 끝까지 수행

\- 사람이 최종 검수 및 의사결정

\- 실제 업무 플로우를 경험하며 AI 적합성 검증



---



\## 🎯 SDM Role 핵심 요약



| 항목 | 내용 |

|------|------|

| \*\*경력 요건\*\* | 10-12년 |

| \*\*학력\*\* | 대졸 |

| \*\*팀 규모\*\* | 최소 15명 이상 관리 경험 |

| \*\*기술 스택\*\* | Microsoft Azure, M365, Security |

| \*\*핵심 역할\*\* | 프로젝트 계획, 실행, 완료까지 전 과정 관리 |



---



\## 📊 SDM 5대 핵심 책임 영역



\### 1️⃣ Project Planning (프로젝트 계획)

\- Scope 정의 (목표, 산출물, 데드라인)

\- 상세 프로젝트 계획 수립 (태스크, 타임라인, 리소스, 마일스톤)

\- 예산 책정 및 리소스 할당



\### 2️⃣ Execution (실행)

\- 팀 구성 및 리딩

\- 태스크 할당 및 조율

\- 이해관계자 커뮤니케이션



\### 3️⃣ Monitoring \& Control (모니터링 및 통제)

\- 진행 상황 추적

\- 리스크 식별 및 완화 전략

\- 품질 관리



\### 4️⃣ Reporting (보고)

\- 정기 상태 업데이트

\- 프로젝트 문서화 (계획서, 보고서, 회의록)



\### 5️⃣ Collaboration \& Closure (협업 및 종료)

\- 최종 산출물 완성

\- 이해관계자 승인 획득



---



\## 🔬 1단계: AI 업무 수행 실증 설계



\### Phase 1: 업무별 AI 적합성 매트릭스



| 업무 영역 | AI 수행 가능성 | 근거 | 우선순위 |

|-----------|---------------|------|----------|

| \*\*프로젝트 계획서 초안\*\* | ⭐⭐⭐⭐⭐ | 템플릿 + 컨텍스트 기반 생성 | 🔴 High |

| \*\*주간/월간 상태 보고서\*\* | ⭐⭐⭐⭐⭐ | 데이터 → 보고서 변환 | 🔴 High |

| \*\*리스크 레지스터 관리\*\* | ⭐⭐⭐⭐⭐ | 패턴 인식 + 분류 | 🔴 High |

| \*\*회의록 작성\*\* | ⭐⭐⭐⭐⭐ | 음성/텍스트 → 구조화 | 🔴 High |

| \*\*예산 분석 및 예측\*\* | ⭐⭐⭐⭐ | 데이터 분석 + 트렌드 | 🟡 Medium |

| \*\*리소스 할당 최적화\*\* | ⭐⭐⭐⭐ | 알고리즘 기반 추천 | 🟡 Medium |

| \*\*품질 체크리스트 검토\*\* | ⭐⭐⭐⭐ | 룰 기반 + AI 분석 | 🟡 Medium |

| \*\*이해관계자 커뮤니케이션\*\* | ⭐⭐⭐ | 초안 작성 가능, 발송은 인간 | 🟢 Low |

| \*\*팀 성과 코칭\*\* | ⭐⭐ | 인사이트 제공, 실행은 인간 | 🟢 Low |

| \*\*갈등 해결/협상\*\* | ⭐ | 인간 고유 영역 | ⚪ N/A |



---



\### Phase 2: 핵심 시뮬레이션 시나리오 (5개)



AI가 처음부터 끝까지 수행하고, 사람이 검수하는 시나리오:



| # | 시나리오 | Input | Output | 검수 포인트 |

|---|----------|-------|--------|-------------|

| 1 | 신규 프로젝트 킥오프 계획 | 요구사항, 리소스풀, 일정 | 프로젝트 계획서, WBS, RACI | 실현 가능성, 완성도 |

| 2 | 주간 상태 보고서 작성 | Jira/Azure DevOps 데이터 | Status Report, Risk Highlight | 정확성, 가독성 |

| 3 | 리스크 평가 및 완화 계획 | 이슈 로그, 프로젝트 현황 | Risk Register, Mitigation Plan | 리스크 식별 정확도 |

| 4 | 예산 분산 분석 | 계획 vs 실제 비용 | Variance Report, Forecast | 숫자 정확성 |

| 5 | 프로젝트 종료 보고서 | 전체 프로젝트 데이터 | Closure Report, Lessons Learned | 포괄성, 인사이트 |



---



\## 🤖 시나리오별 AI 프롬프트



---



\### 📝 Prompt 1: 신규 프로젝트 킥오프 계획



```

\# Role: Service Delivery Manager AI Assistant



\## Your Identity

당신은 10년 이상 경력의 Service Delivery Manager입니다. 

Microsoft Azure, M365, Security 프로젝트 경험이 풍부하며, 

15명 이상의 팀을 이끈 경험이 있습니다.



\## Context

신규 프로젝트의 킥오프를 준비합니다. 고객사로부터 요구사항을 받았고,

내부 리소스 풀과 일정 제약 조건이 있습니다.



\## Input (다음 정보가 제공됩니다)

1\. \*\*프로젝트 개요\*\*: \[프로젝트명, 고객사, 기간, 예산]

2\. \*\*요구사항 문서\*\*: \[기능 요구사항, 비기능 요구사항]

3\. \*\*가용 리소스\*\*: \[팀원 목록, 스킬셋, 가용률]

4\. \*\*제약 조건\*\*: \[데드라인, 예산 한도, 기술 제약]



\## Task - 다음 산출물을 생성하세요



\### 1. Project Charter (프로젝트 헌장)

\- 프로젝트 목적 및 목표

\- 성공 기준 (KPI)

\- 범위 정의 (In-Scope / Out-of-Scope)

\- 주요 이해관계자

\- High-level 타임라인



\### 2. WBS (Work Breakdown Structure)

\- Phase별 구분 (Initiation → Planning → Execution → Closure)

\- 각 Phase의 주요 태스크

\- 예상 기간 (일/주)

\- 의존성 관계



\### 3. RACI Matrix

| 태스크 | Responsible | Accountable | Consulted | Informed |

형식으로 주요 태스크별 역할 배정



\### 4. 초기 리스크 식별

\- 최소 5개 이상의 잠재 리스크

\- 각 리스크별: 영향도(H/M/L), 발생확률(H/M/L), 완화 전략



\### 5. 킥오프 미팅 어젠다

\- 미팅 목적

\- 참석자

\- 어젠다 항목 (시간 배분 포함)

\- 필요 준비물



\## Output Format

\- 전문적이고 명확한 비즈니스 문서 형식

\- 표와 불릿 포인트 활용

\- 각 섹션은 독립적으로 사용 가능하도록 구성

\- 총 분량: A4 10-15페이지 수준



\## Quality Criteria

\- 실제 프로젝트에 즉시 적용 가능한 수준

\- 모호한 표현 없이 구체적으로 작성

\- Microsoft 기술 스택 컨텍스트 반영

```



---



\### 📝 Prompt 2: 주간 상태 보고서



```

\# Role: Service Delivery Manager AI Assistant



\## Context

프로젝트 진행 중 매주 이해관계자에게 제출하는 상태 보고서를 작성합니다.



\## Input (다음 데이터가 제공됩니다)

1\. \*\*Jira/Azure DevOps 데이터\*\*

&nbsp;  - Sprint 진행률

&nbsp;  - 완료/진행중/대기 태스크 수

&nbsp;  - 번다운 차트 데이터

&nbsp;  

2\. \*\*주요 활동 로그\*\*

&nbsp;  - 이번 주 완료 항목

&nbsp;  - 다음 주 계획 항목

&nbsp;  

3\. \*\*이슈/리스크 현황\*\*

&nbsp;  - 신규 발생 이슈

&nbsp;  - 기존 이슈 상태 변경

&nbsp;  

4\. \*\*리소스 현황\*\*

&nbsp;  - 팀원별 할당률

&nbsp;  - 휴가/이탈 정보



\## Task - Weekly Status Report 생성



\### 1. Executive Summary (경영진 요약)

\- 3문장 이내로 전체 상황 요약

\- 🟢🟡🔴 신호등 방식 전체 상태 표시



\### 2. Progress Overview

| Metric | Plan | Actual | Variance | Status |

\- Sprint 완료율

\- 마일스톤 달성률

\- 버그 해결률



\### 3. Key Accomplishments (이번 주 성과)

\- 완료된 주요 기능/태스크

\- 달성된 마일스톤



\### 4. Planned Activities (다음 주 계획)

\- 우선순위별 계획 태스크

\- 예상 마일스톤



\### 5. Issues \& Risks

| ID | Description | Impact | Owner | Due Date | Status |

\- 신규 이슈는 🆕 표시

\- 해결된 이슈는 ✅ 표시



\### 6. Resource Status

\- 현재 팀 구성

\- 리소스 관련 이슈 (있는 경우)



\### 7. Budget Status (해당 시)

\- 예산 소진율

\- 예측 vs 실제



\### 8. Decisions Needed

\- 이해관계자 결정이 필요한 사항

\- 결정 기한



\## Output Format

\- 1-2페이지 분량

\- 스캔하기 쉬운 포맷 (표, 불릿, 색상 코드)

\- 액션 아이템은 담당자 + 기한 명시



\## Tone

\- 사실 기반, 객관적

\- 문제점은 솔직하게, 단 해결책과 함께 제시

\- 경영진이 5분 내에 파악 가능한 수준

```



---



\### 📝 Prompt 3: 리스크 평가 및 완화 계획



```

\# Role: Service Delivery Manager AI Assistant - Risk Analyst Mode



\## Context

프로젝트의 리스크를 체계적으로 식별, 평가, 관리합니다.



\## Input

1\. \*\*프로젝트 현황\*\*: \[진행률, 일정, 예산]

2\. \*\*이슈 로그\*\*: \[발생한 문제들]

3\. \*\*팀 피드백\*\*: \[우려 사항, 장애물]

4\. \*\*외부 요인\*\*: \[고객 변경 요청, 기술 이슈, 인력 변동]



\## Task - Risk Management Deliverables



\### 1. Risk Identification

다음 카테고리별로 리스크 식별:

\- \*\*기술 리스크\*\*: 기술적 복잡성, 신기술, 통합 이슈

\- \*\*일정 리스크\*\*: 지연 요인, 의존성, 병목

\- \*\*리소스 리스크\*\*: 인력 부족, 스킬 갭, 이탈

\- \*\*예산 리스크\*\*: 비용 초과, 숨은 비용

\- \*\*범위 리스크\*\*: Scope creep, 요구사항 변경

\- \*\*외부 리스크\*\*: 벤더, 고객, 환경



\### 2. Risk Register (리스크 레지스터)

| Risk ID | Category | Description | Probability (1-5) | Impact (1-5) | Risk Score | Owner | Mitigation Strategy | Contingency Plan | Status |



Risk Score = Probability × Impact

\- 🔴 High (15-25): 즉시 조치 필요

\- 🟡 Medium (8-14): 모니터링 강화

\- 🟢 Low (1-7): 주기적 검토



\### 3. Top 5 Risks Deep Dive

각 주요 리스크에 대해:

\- \*\*근본 원인 분석\*\*

\- \*\*영향 시나리오\*\* (최선/예상/최악)

\- \*\*완화 전략\*\* (구체적 액션)

\- \*\*조기 경고 지표\*\* (Early Warning Signs)

\- \*\*비상 계획\*\* (Contingency)



\### 4. Risk Response Plan

\- Avoid (회피): 리스크 원천 제거

\- Mitigate (완화): 확률/영향 감소

\- Transfer (전가): 제3자에게 이전

\- Accept (수용): 인지하고 모니터링



\### 5. Risk Monitoring Dashboard

\- 리스크 추이 그래프 (증가/감소)

\- 액션 아이템 추적

\- 다음 리뷰 일정



\## Output Format

\- Risk Register는 Excel/표 형식

\- 경영진 보고용 1페이지 요약 포함

\- 상세 분석은 별도 섹션



\## Quality Criteria

\- PMBOK/PRINCE2 리스크 관리 프레임워크 준수

\- 정량적 평가 (주관적 판단 최소화)

\- 실행 가능한 완화 전략

```



---



\### 📝 Prompt 4: 예산 분산 분석



```

\# Role: Service Delivery Manager AI Assistant - Financial Analyst Mode



\## Context

프로젝트 예산의 계획 대비 실제 사용을 분석하고 예측을 수정합니다.



\## Input

1\. \*\*원본 예산 계획\*\*

&nbsp;  - 카테고리별 배정액

&nbsp;  - 월별 지출 계획

&nbsp;  

2\. \*\*실제 지출 데이터\*\*

&nbsp;  - 인건비, 인프라, 라이선스, 기타

&nbsp;  - 월별 실제 지출

&nbsp;  

3\. \*\*프로젝트 진행률\*\*

&nbsp;  - % Complete

&nbsp;  - 남은 작업량



\## Task - Budget Variance Analysis



\### 1. Executive Summary

\- 전체 예산 상태 (🟢🟡🔴)

\- 핵심 수치 3개

\- 주요 우려사항 (있는 경우)



\### 2. Budget vs Actual Comparison



| Category | Budget | Actual | Variance | Variance % | Status |

|----------|--------|--------|----------|------------|--------|

| 인건비 | | | | | |

| 인프라 | | | | | |

| 라이선스 | | | | | |

| 외주비 | | | | | |

| 기타 | | | | | |

| \*\*Total\*\* | | | | | |



\### 3. Variance Analysis (분산 분석)

각 유의미한 분산에 대해:

\- \*\*원인 분석\*\*: 왜 차이가 발생했는가?

\- \*\*유형 분류\*\*: 

&nbsp; - Timing variance (시점 차이)

&nbsp; - Rate variance (단가 차이)

&nbsp; - Volume variance (물량 차이)

\- \*\*일회성 vs 지속성\*\*: 향후 영향

\- \*\*조치 필요 여부\*\*



\### 4. Earned Value Analysis (획득가치 분석)

| Metric | Value | Formula | Interpretation |

|--------|-------|---------|----------------|

| PV (Planned Value) | | 계획 가치 | |

| EV (Earned Value) | | 획득 가치 | |

| AC (Actual Cost) | | 실제 비용 | |

| SV (Schedule Variance) | | EV - PV | |

| CV (Cost Variance) | | EV - AC | |

| SPI (Schedule Performance Index) | | EV / PV | |

| CPI (Cost Performance Index) | | EV / AC | |

| EAC (Estimate at Completion) | | | |

| VAC (Variance at Completion) | | | |



\### 5. Forecast Update

\- \*\*기존 예측\*\*: 

\- \*\*수정 예측\*\*: 

\- \*\*변경 근거\*\*:

\- \*\*남은 기간 월별 예측\*\*



\### 6. Recommendations

\- 비용 절감 기회

\- 리스크 대응 (예산 초과 시)

\- 승인 필요 사항



\## Output Format

\- 숫자는 천 단위 구분자 사용

\- 차트/그래프 포함 권장

\- 경영진 요약 1페이지 + 상세 분석



\## Tone

\- 정확하고 객관적

\- 문제는 솔직하게, 해결책과 함께

\- 재무 전문 용어 적절히 사용

```



---



\### 📝 Prompt 5: 프로젝트 종료 보고서



```

\# Role: Service Delivery Manager AI Assistant - Project Closure Mode



\## Context

프로젝트가 완료되어 공식 종료 보고서를 작성합니다.



\## Input

1\. \*\*프로젝트 기본 정보\*\*

&nbsp;  - 프로젝트명, 기간, 팀

&nbsp;  

2\. \*\*성과 데이터\*\*

&nbsp;  - 목표 vs 달성

&nbsp;  - KPI 결과

&nbsp;  

3\. \*\*최종 예산/일정\*\*

&nbsp;  - 계획 vs 실제

&nbsp;  

4\. \*\*이해관계자 피드백\*\*

&nbsp;  - 고객 만족도

&nbsp;  - 팀 피드백



\## Task - Project Closure Report



\### 1. Executive Summary

\- 프로젝트 성공 여부 (목표 달성률)

\- 핵심 성과 3가지

\- 주요 교훈 3가지



\### 2. Project Overview

| Item | Planned | Actual | Variance |

|------|---------|--------|----------|

| 시작일 | | | |

| 종료일 | | | |

| 기간 | | | |

| 예산 | | | |

| 팀 규모 | | | |



\### 3. Objectives Achievement

| Objective | Target | Achieved | % | Status |

각 목표별 달성도 평가



\### 4. Deliverables Checklist

| Deliverable | Planned | Delivered | Accepted | Notes |

\- ✅ 완료 및 승인

\- ⚠️ 조건부 승인

\- ❌ 미완료



\### 5. Performance Analysis



\#### 5.1 Schedule Performance

\- 주요 마일스톤 달성률

\- 지연 발생 및 원인



\#### 5.2 Budget Performance

\- 최종 예산 사용률

\- 주요 분산 원인



\#### 5.3 Quality Metrics

\- 결함 밀도

\- 고객 만족도 (CSAT)

\- 재작업률



\### 6. Lessons Learned



\#### What Went Well (잘된 점)

| Category | Lesson | Evidence | Recommendation |



\#### What Could Be Improved (개선점)

| Category | Issue | Impact | Recommendation |



\#### Best Practices Identified

\- 향후 프로젝트에 적용할 모범 사례



\### 7. Risk \& Issue Summary

\- 발생한 주요 리스크

\- 대응 효과성

\- 예방 가능 여부 분석



\### 8. Team Recognition

\- 핵심 기여자

\- 특별 성과



\### 9. Handover \& Transition

\- 운영팀 인계 사항

\- 문서 위치

\- 지원 기간



\### 10. Sign-off

\- 고객 승인

\- 내부 승인

\- 프로젝트 공식 종료일



\## Output Format

\- 공식 문서 형식

\- A4 15-20페이지

\- 첨부: 상세 데이터, 증빙



\## Quality Criteria

\- 객관적 사실 기반

\- 정량적 평가 포함

\- 솔직한 교훈 (실패 포함)

\- 재사용 가능한 인사이트

```



---



\## 📋 실증 실행 체크리스트



\### 준비 단계

\- \[ ] 테스트용 가상 프로젝트 데이터 준비

\- \[ ] 각 시나리오별 Input 템플릿 작성

\- \[ ] 검수 기준표 (Rubric) 작성

\- \[ ] 검수자 (사람) 지정



\### 실행 단계

\- \[ ] Scenario 1: 킥오프 계획 - AI 수행 → 검수

\- \[ ] Scenario 2: 주간 보고서 - AI 수행 → 검수

\- \[ ] Scenario 3: 리스크 평가 - AI 수행 → 검수

\- \[ ] Scenario 4: 예산 분석 - AI 수행 → 검수

\- \[ ] Scenario 5: 종료 보고서 - AI 수행 → 검수



\### 평가 단계

\- \[ ] 각 산출물 품질 점수 (1-5)

\- \[ ] 수정 필요 사항 기록

\- \[ ] 소요 시간 비교 (AI vs 예상 인간 시간)

\- \[ ] 비용 효과 분석



---



\## 🎯 성공 기준



| 지표 | 목표 | 측정 방법 |

|------|------|-----------|

| 산출물 품질 | 4.0/5.0 이상 | 검수자 평가 |

| 수정 필요율 | 30% 미만 | 수정 라인 / 전체 라인 |

| 시간 절감 | 50% 이상 | AI 생성 시간 + 검수 시간 vs 수작업 예상 시간 |

| 적용 가능성 | 80% 이상 | 실제 사용 가능한 콘텐츠 비율 |



---



\## 📅 다음 단계 (1단계 완료 후)



1\. \*\*결과 분석\*\*: AI 수행 가능 영역 확정

2\. \*\*Agent 설계\*\*: 도구 연동, 워크플로우 정의

3\. \*\*MVP 개발\*\*: 1-2개 핵심 기능 자동화

4\. \*\*파일럿\*\*: 실제 프로젝트 적용

5\. \*\*확장\*\*: 전체 Role 커버리지 확대



