# T2: Agent-Supervised Tool Adaptation

## 📋 Category Overview

**Definition**: Tools that adapt and improve based on agent feedback  
**Learning Paradigm**: Tools learn from how agents use them  
**Examples**: Adaptive retrieval models, custom memory systems, specialized adapters

## 🎯 Relevance to AI SDM Agent

### Direct Applications
- **Adaptive Retrieval**: Retrieval system learns what information is actually useful
- **Memory Systems**: Memory adapts to agent's information needs
- **Custom Adapters**: Tools fine-tuned for SDM-specific tasks

### Why Agent-Supervised Adaptation
1. **Domain Specialization**: Tools become SDM-specific over time
2. **Continuous Improvement**: Quality improves with usage
3. **Personalization**: Adapts to specific organization/team
4. **Competitive Advantage**: Custom tools are hard to replicate

## 📚 Key Research Papers

### 🔴 High Priority (Must Read)

#### 1. AAR: Augmentation-Adapted Retriever (2023)
- **Paper**: https://arxiv.org/abs/2305.17331
- **Code**: https://github.com/OpenMatch/Augmentation-Adapted-Retriever
- **Summary**: Retrieval model adapts based on which results agent actually uses
- **Key Contribution**: Implicit feedback from agent usage
- **AI SDM Application**: Learn which past projects are most relevant

**Implementation Concept**:
```python
class AdaptiveRetriever:
    def __init__(self):
        self.retriever = DenseRetriever()
        self.usage_tracker = UsageTracker()
    
    def retrieve_and_track(self, query, context):
        # Retrieve candidates
        candidates = self.retriever.search(query, top_k=10)
        
        # Agent uses some of them
        used_docs = agent_decision_making(candidates, context)
        
        # Track which were actually useful
        self.usage_tracker.record(
            query=query,
            retrieved=candidates,
            used=used_docs
        )
        
        # Periodically update retriever
        if self.usage_tracker.should_update():
            self.fine_tune_retriever()
        
        return used_docs
    
    def fine_tune_retriever(self):
        # Positive examples: (query, used_doc)
        positive_pairs = self.usage_tracker.get_positive_pairs()
        
        # Negative examples: (query, retrieved_but_not_used)
        negative_pairs = self.usage_tracker.get_negative_pairs()
        
        # Contrastive learning
        self.retriever.fine_tune(positive_pairs, negative_pairs)
```

---

#### 2. LLM-Retriever (Microsoft, 2023)
- **Paper**: https://arxiv.org/abs/2307.07164
- **Code**: https://github.com/microsoft/LMOps/tree/main/llm_retriever
- **Summary**: Retrieval model supervised by LLM agent
- **Key Contribution**: LLM provides explicit feedback on retrieval quality
- **AI SDM Application**: Agent evaluates whether retrieved context helped decision

**Implementation Concept**:
```python
class LLMSupervisedRetriever:
    def __init__(self):
        self.retriever = DenseRetriever()
        self.llm_agent = LLMAgent()
    
    def retrieve_with_feedback(self, query, context):
        # Retrieve
        docs = self.retriever.search(query, top_k=5)
        
        # Agent makes decision with retrieved docs
        decision = self.llm_agent.decide(context, retrieved_docs=docs)
        
        # Agent evaluates retrieval quality
        feedback = self.llm_agent.evaluate_retrieval(
            query=query,
            docs=docs,
            decision_quality=decision.quality
        )
        
        # Update retriever based on feedback
        self.update_retriever(query, docs, feedback)
        
        return decision
```

---

#### 3. Memento (2025)
- **Paper**: https://arxiv.org/abs/2508.16153
- **Code**: https://github.com/Agent-on-the-Fly/Memento
- **Summary**: Memory system that adapts to agent's needs
- **Key Contribution**: Dynamic memory consolidation and retrieval
- **AI SDM Application**: Organizational knowledge that evolves with usage

**Implementation Concept**:
```python
class AdaptiveMemory:
    def __init__(self):
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
        self.consolidator = MemoryConsolidator()
    
    def store_and_consolidate(self, experience):
        # Store in short-term
        self.short_term.add(experience)
        
        # Periodically consolidate
        if self.short_term.should_consolidate():
            # Identify patterns
            patterns = self.consolidator.find_patterns(
                self.short_term.get_all()
            )
            
            # Create abstractions
            for pattern in patterns:
                abstraction = self.consolidator.create_abstraction(pattern)
                self.long_term.add(abstraction)
            
            # Clear short-term
            self.short_term.clear()
    
    def retrieve(self, query):
        # Try long-term first (abstractions)
        long_term_results = self.long_term.search(query)
        
        # Supplement with recent short-term
        short_term_results = self.short_term.search(query)
        
        return long_term_results + short_term_results
```

---

### 🟡 Medium Priority

#### 4. Proxy-Tuning (2024)
- **Paper**: https://arxiv.org/abs/2401.08565
- **Code**: https://github.com/alisawuffles/proxy-tuning
- **Summary**: Efficient adaptation of frozen models
- **AI SDM Application**: Adapt retrieval without full retraining

#### 5. BBox-Adapter (2024)
- **Paper**: https://arxiv.org/abs/2402.08219
- **Code**: https://github.com/haotiansun14/BBox-Adapter
- **Summary**: Black-box model adaptation
- **AI SDM Application**: Adapt commercial APIs (OpenAI, Cohere)

#### 6. ToolkenGPT (2023)
- **Paper**: https://arxiv.org/abs/2305.11554
- **Code**: https://github.com/Ber666/ToolkenGPT
- **Summary**: Tools as tokens for LLMs
- **AI SDM Application**: Seamless tool integration

---

### 🟢 Low Priority (Future Study)

#### 7. EVOR (2024)
- **Paper**: https://arxiv.org/abs/2402.12317
- **Code**: https://github.com/xlang-ai/EVOR
- **Summary**: Evolutionary tool optimization
- **AI SDM Application**: Automatic tool discovery

#### 8. ARL2 (2024)
- **Paper**: https://arxiv.org/abs/2402.13542
- **Code**: https://github.com/zhanglingxi-cs/ARL2
- **Summary**: Adaptive retrieval learning
- **AI SDM Application**: Advanced retrieval adaptation

---

## 🛠️ Implementation Guide

### Phase 1: Usage Tracking (Week 1-2)
```python
# Step 1: Track retrieval usage
class RetrievalUsageTracker:
    def __init__(self):
        self.log = []
    
    def track_retrieval(self, query, retrieved_docs, used_docs):
        entry = {
            "timestamp": datetime.now(),
            "query": query,
            "retrieved": [doc.id for doc in retrieved_docs],
            "used": [doc.id for doc in used_docs],
            "usage_rate": len(used_docs) / len(retrieved_docs)
        }
        self.log.append(entry)
        
        # Identify which docs were useful
        for doc in retrieved_docs:
            if doc in used_docs:
                self.mark_positive(query, doc)
            else:
                self.mark_negative(query, doc)
```

### Phase 2: Feedback Collection (Week 3-4)
```python
# Step 2: Collect explicit feedback
class FeedbackCollector:
    def collect_retrieval_feedback(self, query, docs, decision):
        # Agent evaluates each document
        feedback = {}
        for doc in docs:
            relevance = self.evaluate_relevance(doc, decision)
            feedback[doc.id] = {
                "relevance": relevance,  # 0-1 score
                "was_used": doc.id in decision.sources,
                "helpfulness": self.evaluate_helpfulness(doc, decision)
            }
        
        return feedback
```

### Phase 3: Retriever Fine-tuning (Month 2)
```python
# Step 3: Fine-tune retriever
class RetrieverAdapter:
    def __init__(self):
        self.base_retriever = DenseRetriever()
        self.adapter = AdapterLayer()
    
    def fine_tune(self, positive_pairs, negative_pairs):
        # Contrastive loss
        for query, pos_doc in positive_pairs:
            pos_score = self.score(query, pos_doc)
            
            # Sample negative
            neg_doc = random.choice([d for q, d in negative_pairs if q == query])
            neg_score = self.score(query, neg_doc)
            
            # Loss: pos_score should be > neg_score
            loss = max(0, neg_score - pos_score + margin)
            
            # Update adapter
            self.adapter.update(loss)
    
    def score(self, query, doc):
        query_emb = self.base_retriever.encode_query(query)
        doc_emb = self.base_retriever.encode_doc(doc)
        
        # Apply adapter
        adapted_query_emb = self.adapter(query_emb)
        
        return cosine_similarity(adapted_query_emb, doc_emb)
```

### Phase 4: Memory Consolidation (Month 3+)
```python
# Step 4: Build adaptive memory
class MemoryConsolidator:
    def consolidate(self, experiences):
        # Cluster similar experiences
        clusters = self.cluster_experiences(experiences)
        
        # Create abstractions
        abstractions = []
        for cluster in clusters:
            pattern = self.identify_pattern(cluster)
            abstraction = {
                "pattern": pattern,
                "frequency": len(cluster),
                "examples": cluster[:5],  # Keep few examples
                "rule": self.extract_rule(pattern)
            }
            abstractions.append(abstraction)
        
        return abstractions
    
    def identify_pattern(self, experiences):
        # Find common elements
        common_context = self.find_common_context(experiences)
        common_action = self.find_common_action(experiences)
        common_outcome = self.find_common_outcome(experiences)
        
        return {
            "context": common_context,
            "action": common_action,
            "outcome": common_outcome
        }
```

---

## 📊 Evaluation Metrics

### Adaptation Metrics
- **Retrieval Improvement**: Quality increase over time
- **Usage Rate**: % of retrieved docs actually used
- **Adaptation Speed**: Samples needed to improve
- **Generalization**: Performance on new queries

### Tracking Template
```python
metrics = {
    "adaptive_retrieval": {
        "initial_top5_accuracy": 0.65,
        "current_top5_accuracy": 0.82,  # Target: >0.80
        "improvement": 0.17,
        "usage_rate": 0.75,  # Target: >0.70
        "samples_used": 500,
    },
    "memory_consolidation": {
        "abstractions_created": 45,
        "avg_abstraction_usage": 8.5,  # Times used
        "consolidation_ratio": 0.15,  # 15% of experiences → abstractions
    }
}
```

---

## 🚧 Common Challenges

### Challenge 1: Cold Start
**Problem**: No usage data initially  
**Solution**: Start with T1 (Agent-Agnostic) tools, gradually adapt

### Challenge 2: Overfitting
**Problem**: Adapter becomes too specific to recent queries  
**Solution**: Regularization, maintain diverse training set

### Challenge 3: Computational Cost
**Problem**: Continuous fine-tuning is expensive  
**Solution**: Batch updates, use efficient adapters (LoRA, Prefix-tuning)

---

## 📝 Next Steps

### This Week
- [ ] Read AAR paper
- [ ] Design usage tracking schema
- [ ] Implement basic tracking

### Next Month
- [ ] Collect 200 retrieval samples
- [ ] Train first adapter
- [ ] Measure improvement

### This Quarter
- [ ] Deploy adaptive retrieval to production
- [ ] Build memory consolidation system
- [ ] Achieve >80% retrieval accuracy

---

**Status**: 🔴 Not Started  
**Priority**: 🟡 Medium (after A1, A2)  
**Estimated Effort**: 4 months  
**Expected Impact**: 30% improvement in decision quality through better context
