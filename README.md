# From MLOps to LLMOps: Teaching Materials & Research

A comprehensive teaching package for understanding the evolution from traditional Machine Learning Operations (MLOps) to Large Language Model Operations (LLMOps).

---

## What's This About?

This repository contains educational materials that compare two approaches to deploying AI in production:

| Approach | Description | Example |
|----------|-------------|---------|
| **MLOps** | Traditional ML: train custom models with labeled data | XGBoost classifier trained on 50K documents |
| **LLMOps** | Modern GenAI: use pre-trained models (GPT, Claude) + retrieval | Claude + RAG pipeline for document Q&A |

The materials use a **case study** of a company migrating from MLOps to LLMOps for document intelligence (contract analysis, invoice processing).

---

## Repository Contents

```
research/
├── README.md                           # This file
├── case-study-mlops-llmops.md          # Student assignment
├── case-study-expanded-sections.md     # Instructor guide + answer key
├── research-paper-mlops-to-llmops.md   # Academic paper outline
└── diagrams/
    ├── mlops-architecture.png          # Traditional ML pipeline
    ├── llmops-architecture.png         # LLM + RAG pipeline
    ├── mlops-vs-llmops-comparison.png  # Side-by-side comparison
    └── llmops-reference-architecture.png # 6-layer reference architecture
```

---

## File Descriptions

### For Teaching

| File | Audience | Purpose |
|------|----------|---------|
| `case-study-mlops-llmops.md` | **Students** | The assignment they complete (2-3 weeks) |
| `case-study-expanded-sections.md` | **Instructors** | Answer key, detailed explanations, grading support |
| `diagrams/*.png` | **Both** | Visual aids for lectures and reports |

### For Research

| File | Purpose |
|------|---------|
| `research-paper-mlops-to-llmops.md` | Full academic paper outline ready for development |

---

## Case Study Overview

### The Scenario

**TechCorp Solutions** processes 50,000 documents/month using a traditional MLOps pipeline:
- Document classification (12 categories)
- Field extraction (15 predefined fields)
- Compliance checking

**The Challenge:** Users want new capabilities (Q&A, summarization, flexible extraction) that the current ML system cannot provide.

**The Proposal:** Migrate to an LLMOps architecture using AWS Bedrock (Claude) + RAG.

### What Students Do

1. **Compare architectures** — MLOps vs LLMOps components and data flows
2. **Assess maturity levels** — Using Google's MLOps maturity model (Level 0-1-2)
3. **Analyze governance** — EU AI Act compliance, guardrails design
4. **Calculate costs** — Cost-benefit analysis of migration
5. **Design migration plan** — Phased rollout with risk mitigation

### Deliverables

- Written report (10-15 pages)
- Architecture diagrams
- Optional presentation

---

## Architecture Diagrams

### MLOps Architecture (Current State)
![MLOps Architecture](./diagrams/mlops-architecture.png)

Traditional pipeline: Documents → OCR → TF-IDF Features → XGBoost → Classification

### LLMOps Architecture (Proposed State)
![LLMOps Architecture](./diagrams/llmops-architecture.png)

Modern pipeline: Documents → Chunking → Embeddings → Vector Store → RAG → LLM → Guardrails → Response

### Side-by-Side Comparison
![Comparison](./diagrams/mlops-vs-llmops-comparison.png)

### LLMOps Reference Architecture
![Reference Architecture](./diagrams/llmops-reference-architecture.png)

Six-layer architecture: Application → Orchestration → Governance → Model → Data → Infrastructure

---

## Quick Start

### For Instructors

1. **Assign the case study:** Give students `case-study-mlops-llmops.md`
2. **Use diagrams in lectures:** Reference `diagrams/*.png` for visual explanations
3. **Grade with answer key:** Use `case-study-expanded-sections.md` for solutions

### For Students

1. Read the case study in `case-study-mlops-llmops.md`
2. Study the architecture diagrams in `diagrams/`
3. Complete all six parts of the analysis
4. Submit your written report

### For Researchers

1. Use `research-paper-mlops-to-llmops.md` as a starting point
2. The case study provides validation material
3. Diagrams are publication-ready (SVG versions included)

---

## Key Concepts Covered

| Topic | Description |
|-------|-------------|
| **MLOps Maturity Model** | Google's Level 0-1-2 framework |
| **LLMOps Extensions** | Prompt versioning, RAG pipelines, vector stores |
| **New Metrics** | Hallucination rate, TTFT, token costs |
| **Governance** | EU AI Act, guardrails, audit trails |
| **Cost Analysis** | Compute-based vs token-based economics |
| **AWS Services** | SageMaker, Bedrock, OpenSearch, Step Functions |

---

## Target Audience

- **Academic Level:** Undergraduate
- **Prerequisites:** Basic understanding of ML concepts
- **Platform:** AWS (SageMaker + Bedrock)
- **Duration:** 2-3 weeks for case study completion

---

## Learning Objectives

After completing this case study, students will be able to:

1. Distinguish between MLOps and LLMOps architectures
2. Apply maturity models to assess operational readiness
3. Analyze governance requirements for AI systems (EU AI Act)
4. Conduct cost-benefit analysis for ML/LLM systems
5. Design practical migration strategies with risk mitigation

---

## License

Educational use. Materials created for ESADE teaching purposes.

---

## Author

Generated with Claude Code (Scientific Writer)
