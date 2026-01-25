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

## Start Here

> **New to LLMOps?** Begin with the **[LLMOps Lifecycle](./llmops-lifecycle.md)** document — a comprehensive explanation of LLMOps architecture, components, and how it differs from traditional MLOps.

---

## Repository Contents

```
├── README.md                           # This file
├── llmops-lifecycle.md                 # Core document: LLMOps architecture & lifecycle
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

### Core Documentation

| File | Description |
|------|-------------|
| **[llmops-lifecycle.md](./llmops-lifecycle.md)** | Comprehensive explanation of LLMOps architecture and lifecycle. Covers all components from document ingestion through monitoring, the LLMOps maturity model, and governance requirements. **Start here for conceptual understanding.** |

### For Teaching

| File | Audience | Purpose |
|------|----------|---------|
| [case-study-mlops-llmops.md](./case-study-mlops-llmops.md) | **Students** | Hands-on assignment comparing MLOps and LLMOps (2-3 weeks) |
| [case-study-expanded-sections.md](./case-study-expanded-sections.md) | **Instructors** | Answer key, detailed explanations, grading support |
| [diagrams/](./diagrams/) | **Both** | Visual aids for lectures and reports |

### For Research

| File | Purpose |
|------|---------|
| [research-paper-mlops-to-llmops.md](./research-paper-mlops-to-llmops.md) | Full academic paper outline ready for development |

---

## LLMOps Lifecycle Overview

The **[llmops-lifecycle.md](./llmops-lifecycle.md)** document explains:

1. **How LLMOps differs from MLOps** — artifact types, pipeline stages, failure modes, cost models
2. **Component-by-component breakdown** — from document ingestion to monitoring
3. **The LLMOps maturity model** — Level 0 (ad-hoc) → Level 1 (automated) → Level 2 (CI/CD + governance)
4. **Governance and compliance** — EU AI Act, guardrails, audit trails
5. **Key takeaways** — practical recommendations for adoption

This document follows the same structure and style as the [MLOps Lifecycle](https://github.com/oriolrius/data-platform-ops/blob/main/mlops-lifecycle.md) document, making them companion pieces for understanding both traditional and modern ML operations.

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

### For Self-Study

1. **Read [llmops-lifecycle.md](./llmops-lifecycle.md)** — Understand the concepts and architecture
2. **Study the diagrams** — Visualize the differences between MLOps and LLMOps
3. **Review the case study** — See concepts applied to a realistic scenario

### For Instructors

1. **Assign reading:** Start with [llmops-lifecycle.md](./llmops-lifecycle.md) as foundational material
2. **Assign the case study:** Give students [case-study-mlops-llmops.md](./case-study-mlops-llmops.md)
3. **Use diagrams in lectures:** Reference `diagrams/*.png` for visual explanations
4. **Grade with answer key:** Use [case-study-expanded-sections.md](./case-study-expanded-sections.md) for solutions

### For Students

1. Read [llmops-lifecycle.md](./llmops-lifecycle.md) for background
2. Study the case study in [case-study-mlops-llmops.md](./case-study-mlops-llmops.md)
3. Reference the architecture diagrams in [diagrams/](./diagrams/)
4. Complete all six parts of the analysis
5. Submit your written report

### For Researchers

1. Use [research-paper-mlops-to-llmops.md](./research-paper-mlops-to-llmops.md) as a starting point
2. Reference [llmops-lifecycle.md](./llmops-lifecycle.md) for conceptual framework
3. The case study provides validation material
4. Diagrams are publication-ready (SVG versions included)

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

After completing these materials, learners will be able to:

1. Explain the key differences between MLOps and LLMOps architectures
2. Identify LLMOps-specific components (prompt registry, vector store, guardrails)
3. Apply maturity models to assess operational readiness
4. Analyze governance requirements for AI systems (EU AI Act)
5. Conduct cost-benefit analysis comparing ML and LLM approaches
6. Design practical migration strategies with risk mitigation

---

## Related Resources

- **[MLOps Lifecycle](https://github.com/oriolrius/data-platform-ops/blob/main/mlops-lifecycle.md)** — Companion document explaining traditional MLOps architecture in the same style

---

## License

Educational use. Materials created for ESADE teaching purposes.

---

## Author

Generated with Claude Code (Scientific Writer)
