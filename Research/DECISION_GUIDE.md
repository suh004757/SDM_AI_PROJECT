# Decision Guide: Finding Your Research Topic

이 가이드는 당신의 필요에 맞는 Research 카테고리를 찾도록 도와줍니다.

## 🎯 자신의 필요에 맞는 카테고리 찾기

### Q1: 무엇을 개선하고 싶습니까?

```
┌─ 에이전트의 행동 선택 개선 (액션 추천, API 호출 최적화)
│  └─> A1: Tool Execution Signaled ✅
│      [Agent_Adaptation/A1_Tool_Execution_Signaled/](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md)
│
├─ 보고서 품질, 설명가능성, 자체 개선 능력
│  └─> A2: Agent Output Signaled ✅
│      [Agent_Adaptation/A2_Agent_Output_Signaled/](Agent_Adaptation/A2_Agent_Output_Signaled/README.md)
│
├─ 데이터 검색, 임베딩, 일반 도구 통합
│  └─> T1: Agent-Agnostic Tools ✅
│      [Tool_Adaptation/T1_Agent_Agnostic/](Tool_Adaptation/T1_Agent_Agnostic/README.md)
│
└─ 컨텍스트 메모리, 적응형 검색, 에이전트 피드백 학습 도구
   └─> T2: Agent-Supervised Tools ✅
       [Tool_Adaptation/T2_Agent_Supervised/](Tool_Adaptation/T2_Agent_Supervised/README.md)
```

## 🛠️ 스킬셋 프레임워크별 매핑

**Q2: Skillset Framework의 어느 부분을 강화하고 싶습니까?**

| Framework 섹션 | 학습 포커스 | Research Category |
|---|---|---|
| **2.1 Data Ingestion** | 데이터 수집 및 전처리 | [T1: Agent-Agnostic](Tool_Adaptation/T1_Agent_Agnostic/README.md) |
| **2.5 Context Memory** | 컨텍스트 관리 및 메모리 | [T2: Agent-Supervised](Tool_Adaptation/T2_Agent_Supervised/README.md) |
| **3.1 Rule Engine** | 규칙 및 의사결정 | [A1: Tool Execution](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md) |
| **4.1 Task Control** | 작업 제어 및 스케줄링 | [A1: Tool Execution](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md) |
| **6.1 Auto Reporting** | 자동화된 보고 | [A2: Output Signaled](Agent_Adaptation/A2_Agent_Output_Signaled/README.md) |
| **6.2 Explainability** | 설명가능성 및 투명성 | [A2: Output Signaled](Agent_Adaptation/A2_Agent_Output_Signaled/README.md) |

**→ [Skills Framework](../Skills/Framework/README.md)에서 전체 매핑 확인**

## 💼 비즈니스 목표별

**Q3: 어떤 비즈니스 결과를 원합니까?**

```
🎯 목표: 에이전트 정확도 40% 향상
└─ 연구: [A1: Tool Execution Learning](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md)
   기대 영향: RL 기반 액션 최적화

🎯 목표: 휴먼 리뷰 시간 50% 단축
└─ 연구: [A2: Output Signaled Learning](Agent_Adaptation/A2_Agent_Output_Signaled/README.md)
   기대 영향: 자동 개선 + 자체 평가

🎯 목표: 검색 시간 20% 단축
└─ 연구: [T1: Agent-Agnostic Tools](Tool_Adaptation/T1_Agent_Agnostic/README.md)
   기대 영향: 프리트레인된 도구 활용

🎯 목표: 의사결정 품질 30% 향상
└─ 연구: [T2: Agent-Supervised Tools](Tool_Adaptation/T2_Agent_Supervised/README.md)
   기대 영향: 적응형 검색 + 메모리 시스템
```

## 📚 학습 경로

### 🔴 **초급자 (처음 시작)**
1. [OVERVIEW.md](OVERVIEW.md) 읽기 (전체 그림 이해)
2. [A1 README](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md) 학습
3. Agent-R 논문 읽기

### 🟡 **중급자 (기초 이해)**
1. A1과 A2 모두 마스터
2. T1에서 도구 통합 학습
3. T2에서 적응형 시스템 이해

### 🟢 **고급자 (구현 준비)**
1. 모든 카테고리 정통
2. 구현 예제 코드 검토
3. 자신의 프로젝트에 적용

## 🚦 의사결정 트리

```
시작
  │
  ├─ "에이전트가 어떻게 학습해야 할까?" 
  │  ├─ "도구 실행 결과에서" → A1 ✅
  │  └─ "출력 품질에서" → A2 ✅
  │
  └─ "어떤 도구를 사용할까?"
     ├─ "일반 도구" → T1 ✅
     └─ "에이전트-맞춤형 도구" → T2 ✅
```

## ✅ 카테고리별 체크리스트

### A1: Tool Execution Signaled ✅
- [ ] OVERVIEW 섹션 읽기
- [ ] 카테고리 README 학습
- [ ] 주요 논문 1-2개 읽기 (Agent-R, FTRL)
- [ ] 코드 예제 검토
- [ ] 자신의 케이스에 맞게 조정

### A2: Agent Output Signaled ✅
- [ ] OVERVIEW 섹션 읽기
- [ ] 카테고리 README 학습
- [ ] 주요 논문 1-2개 읽기 (Self-RAG, AutoRefine)
- [ ] 자체 평가 매커니즘 설계

### T1: Agent-Agnostic Tools ✅
- [ ] 사용 가능한 도구 목록 검토
- [ ] 각 도구의 특성 이해
- [ ] 통합 가이드 학습
- [ ] 프로토타입 테스트

### T2: Agent-Supervised Tools ✅
- [ ] 적응형 시스템 원리 이해
- [ ] 피드백 루프 설계
- [ ] 메모리 시스템 검토
- [ ] 파일럿 구현

## 🔗 빠른 링크

| 목적 | 링크 |
|---|---|
| 전체 개요 | [OVERVIEW.md](OVERVIEW.md) |
| A1 심층 학습 | [A1 README](Agent_Adaptation/A1_Tool_Execution_Signaled/README.md) |
| A2 심층 학습 | [A2 README](Agent_Adaptation/A2_Agent_Output_Signaled/README.md) |
| T1 심층 학습 | [T1 README](Tool_Adaptation/T1_Agent_Agnostic/README.md) |
| T2 심층 학습 | [T2 README](Tool_Adaptation/T2_Agent_Supervised/README.md) |
| 새 논문 추가 | [_Inbox/README.md](_Inbox/README.md) |
| Skills 매핑 | [../Skills/Framework/README.md](../Skills/Framework/README.md) |

## 💡 팁

1. **명확한 문제 정의**: 먼저 해결하려는 문제를 명확히 하세요.
2. **Framework 검토**: [Skills Framework](../Skills/Framework/README.md)에서 관련 스킬을 확인하세요.
3. **순차적 학습**: 한 번에 한 카테고리씩 깊이 있게 학습하세요.
4. **실습**: 각 카테고리의 코드 예제를 실행해보세요.
5. **문제 해결**: 기술적 질문은 각 카테고리의 README를 참고하세요.

---

**다음 단계**: 위 항목 중 하나를 선택하고 해당 README로 이동하세요! 🚀
