# Research Inbox

## 📥 Purpose

This folder is a **temporary storage space for new papers, articles, and research materials**.  
AI Agent automatically classifies and moves them to appropriate categories.

## 🤖 Automatic Classification Process

### 1. Add Materials
Add new research materials to this folder:
- PDF papers
- Markdown notes
- Link collections (links.md)
- Code examples

### 2. Run AI Agent Classification
```bash
# Agent analyzes and classifies Inbox contents
python scripts/classify_research.py
```

### 3. Automatic Classification Rules

Agent classifies materials based on the following criteria:

#### A1: Tool Execution Signaled
**Keywords**: RL, reinforcement learning, tool execution, API feedback, action selection, reward model  
**Characteristics**: Methodologies that learn from tool execution results  
**Example**: "Agent learns from API call success/failure"

#### A2: Agent Output Signaled
**Keywords**: self-refinement, output quality, human feedback, preference learning, self-evaluation  
**Characteristics**: Methodologies that learn from output quality evaluation  
**Example**: "Iterative improvement based on feedback"

#### T1: Agent-Agnostic
**Keywords**: pre-trained, CLIP, Whisper, embedding, general-purpose, plug-and-play  
**Characteristics**: General-purpose pre-trained models  
**Example**: "Use existing embedding models"

#### T2: Agent-Supervised
**Keywords**: adaptive retrieval, memory system, tool adaptation, agent feedback, fine-tuning  
**Characteristics**: Tools that improve based on agent feedback  
**Example**: "Retrieval model adapts based on agent usage"

## 📝 File Naming Conventions

### Papers
```
[Year]_[FirstAuthor]_[ShortTitle].pdf
Example: 2025_ByteDance_Agent-R.pdf
```

### Notes
```
[Category]_[Topic]_notes.md
Example: A1_RL_for_Tool_Use_notes.md
```

### Link Collections
```
[Category]_links.md
Example: A2_Self_Refinement_links.md
```

## 🔄 Post-Classification Processing

When Agent completes classification:
1. Files are moved to appropriate category folders
2. Automatically added to respective category README
3. Classification log generated in Inbox (`_classification_log.md`)

## 📋 Current Inbox Status

### Unclassified Files
- (None currently)

### Recent Classification History
- (None yet)

---

**Usage Tips**: 
- Adding a simple note file along with paper PDFs improves classification accuracy
- If applicable to multiple categories, it will be classified to the primary category with links added to other categories
