# Case Study: MLOps vs LLMOps for Document Intelligence

## Comparative Study for Undergraduate Students

---

## Case Study Overview

| Element | Details |
|---------|---------|
| **Title** | "TechCorp's Document Intelligence Transformation: From ML Classification to LLM-Powered Analysis" |
| **Type** | Comparative Study |
| **Level** | Undergraduate |
| **Platform** | AWS (SageMaker + Bedrock) |
| **Duration** | 2-3 weeks |
| **Deliverable** | Written report (10-15 pages) + architecture diagrams |

---

## Part 1: The Business Scenario

### Company Background

**TechCorp Solutions** is a mid-sized B2B software company (500 employees) that processes approximately 50,000 contracts, invoices, and legal documents per month for its enterprise clients. Their document processing system is critical for:

- **Contract review:** Extracting key terms, dates, obligations
- **Invoice processing:** Validating amounts, matching POs
- **Compliance checking:** Identifying regulatory clauses

### Current State (MLOps Approach — 2022)

TechCorp implemented a traditional ML pipeline two years ago:

![MLOps Architecture - Current State](./diagrams/mlops-architecture.png)

*Figure 1: Traditional MLOps architecture for document intelligence using SageMaker*

**What the ML system does:**
- Classifies documents into 12 categories (contract, invoice, NDA, etc.)
- Extracts 15 predefined fields (date, amount, parties, etc.)
- Flags documents for human review based on confidence scores

**Current performance:**
- Classification accuracy: 94%
- Field extraction accuracy: 87%
- Processing time: 2.3 seconds per document
- Monthly AWS cost: $4,200

**Current limitations reported by users:**
1. Cannot answer questions about document content
2. Cannot summarize complex contracts
3. Cannot identify clauses not in the predefined list
4. Cannot explain why a document was flagged
5. Adding new document types requires 3-4 weeks of retraining

---

### Proposed Future State (LLMOps Approach — 2025)

TechCorp's CTO proposes migrating to an LLM-based system using AWS Bedrock:

![LLMOps Architecture - Proposed State](./diagrams/llmops-architecture.png)

*Figure 2: LLMOps architecture with RAG pipeline, vector store, and guardrails*

**What the LLM system would do:**
- All current capabilities PLUS:
- Answer natural language questions about any document
- Summarize contracts in plain language
- Identify any clause type (not just predefined)
- Explain reasoning behind flags
- Handle new document types with prompt changes only

**Projected performance:**
- Classification accuracy: 96%
- Field extraction accuracy: 92%
- Processing time: 4.8 seconds per document
- Monthly AWS cost: $12,500 (estimated)

---

## Part 2: Comparative Analysis Framework

![MLOps vs LLMOps - Side by Side Comparison](./diagrams/mlops-vs-llmops-comparison.png)

*Figure 3: Side-by-side comparison of MLOps and LLMOps architectures*

Students must analyze both approaches across these dimensions:

### 2.1 Architecture Comparison

| Dimension | MLOps (Current) | LLMOps (Proposed) |
|-----------|-----------------|-------------------|
| **Core Model** | XGBoost classifier | Claude 3 (Bedrock) |
| **Data Storage** | Feature Store (tabular) | Vector Store (embeddings) |
| **Pipeline Tool** | SageMaker Pipelines | Bedrock + Step Functions |
| **Versioning** | Model versions | Model + Prompt versions |
| **Retraining Trigger** | Data drift detected | Data drift + prompt updates |

**Student Task:** Complete the comparison table with 5 additional dimensions.

### 2.2 Artifact Comparison

| Artifact | MLOps | LLMOps |
|----------|-------|--------|
| Training Data | Labeled documents (CSV) | ? |
| Features | TF-IDF vectors | ? |
| Model | XGBoost .pkl file | ? |
| Config | Hyperparameters JSON | ? |
| Evaluation | Confusion matrix | ? |

**Student Task:** Fill in the LLMOps column and explain the differences.

### 2.3 Metrics Comparison

| Metric Category | MLOps Metrics | LLMOps Metrics |
|-----------------|---------------|----------------|
| **Quality** | Accuracy, Precision, Recall, F1 | + Hallucination rate, Factuality |
| **Performance** | Latency (ms), Throughput | + TTFT, Tokens/second |
| **Cost** | Compute hours, Storage | + Token usage, Cost per request |
| **Reliability** | Uptime, Error rate | + Guardrail trigger rate |

**Student Task:** Define how each new LLMOps metric would be measured for TechCorp.

---

## Part 3: Maturity Level Analysis

Using Google's MLOps Maturity Model (extended for LLMOps):

### Current State Assessment

**Student Task:** Assess TechCorp's current MLOps maturity level and justify your answer.

| Criterion | Level 0 | Level 1 | Level 2 |
|-----------|---------|---------|---------|
| Pipeline automation | Manual | Automated | CI/CD |
| Feature management | Ad-hoc | Feature Store | Versioned + monitored |
| Model versioning | None | Registry | + Approval workflows |
| Monitoring | None | Basic drift | + Auto-retraining |
| Governance | None | Basic logging | Full audit trail |

**Questions:**
1. What maturity level is TechCorp currently at? Provide evidence.
2. What would TechCorp need to reach Level 2 in MLOps?
3. If they migrate to LLMOps, what maturity level would they start at?

### LLMOps Maturity Assessment

**Student Task:** Define what Level 0, 1, and 2 look like for LLMOps:

| Level | LLMOps Characteristics |
|-------|------------------------|
| **Level 0** | (Students define) |
| **Level 1** | (Students define) |
| **Level 2** | (Students define) |

---

## Part 4: Governance & Compliance Analysis

TechCorp processes contracts for EU-based clients and must comply with the EU AI Act.

### Risk Classification

**Student Task:** Classify both systems under EU AI Act risk categories:

| System | Risk Level | Justification |
|--------|------------|---------------|
| MLOps (classifier) | ? | ? |
| LLMOps (Claude-based) | ? | ? |

### Compliance Checklist

**Student Task:** Complete the compliance checklist for the LLMOps system:

| Requirement | How MLOps Addresses | How LLMOps Must Address |
|-------------|---------------------|-------------------------|
| Lineage tracking | SageMaker tracks data→model | ? |
| Explainability | Feature importance | ? |
| Bias detection | SageMaker Clarify | ? |
| Human oversight | Confidence thresholds | ? |
| Audit trail | CloudTrail logs | ? |

### Guardrails Design

**Student Task:** Design guardrails for the LLMOps system:

1. What PII types must be detected and redacted?
2. What content policies should be enforced?
3. How should hallucinations be detected?
4. What should happen when a guardrail is triggered?

---

## Part 5: Cost-Benefit Analysis

### Cost Comparison

| Cost Element | MLOps (Monthly) | LLMOps (Monthly) |
|--------------|-----------------|------------------|
| Compute (training) | $800 | $200 (fine-tuning optional) |
| Compute (inference) | $1,500 | $8,000 (token costs) |
| Storage | $400 | $1,200 (vector store) |
| Monitoring | $500 | $800 |
| Data labeling | $1,000 | $300 (few-shot only) |
| **Total** | **$4,200** | **$12,500** |

**Student Task:**
1. Calculate the cost per document for each approach
2. At what volume does LLMOps become cost-competitive?
3. What strategies could reduce LLMOps costs?

### Benefit Analysis

**Student Task:** Quantify the business value of LLMOps capabilities:

| Capability | Business Impact | Value Estimate |
|------------|-----------------|----------------|
| Natural language Q&A | Reduced support tickets | ? |
| Contract summarization | Faster review time | ? |
| Flexible clause detection | Reduced custom development | ? |
| Explainable flagging | Improved user trust | ? |

---

## Part 6: Migration Roadmap

**Student Task:** Design a phased migration plan:

### Phase 1: Pilot (Month 1-2)
- What document type to start with?
- What success metrics?
- What team structure?

### Phase 2: Parallel Run (Month 3-4)
- How to compare outputs?
- What decision criteria for go/no-go?

### Phase 3: Full Migration (Month 5-6)
- What cutover strategy?
- What rollback plan?

---

## Deliverables

Students must submit:

1. **Written Report (10-15 pages)**
   - Executive summary (1 page)
   - Architecture comparison with diagrams (3 pages)
   - Maturity level analysis (2 pages)
   - Governance and compliance analysis (2 pages)
   - Cost-benefit analysis (2 pages)
   - Migration roadmap (2 pages)
   - Recommendation with justification (1 page)

2. **Architecture Diagrams**
   - Current state (MLOps) — detailed
   - Future state (LLMOps) — detailed
   - Comparison view — side by side

3. **Presentation (Optional)**
   - 10-minute presentation to "TechCorp leadership"

---

## Grading Rubric

| Criterion | Weight | Excellent (90-100%) | Good (70-89%) | Needs Work (<70%) |
|-----------|--------|---------------------|---------------|-------------------|
| **Architecture Understanding** | 25% | Accurately describes both architectures with correct AWS services | Minor errors in service mapping | Significant misunderstandings |
| **Comparative Analysis** | 25% | Thorough comparison across all dimensions | Covers most dimensions | Incomplete or superficial |
| **Governance Analysis** | 20% | Correctly applies EU AI Act, designs practical guardrails | Understands concepts, some gaps | Missing key compliance requirements |
| **Cost-Benefit Analysis** | 15% | Realistic calculations, creative cost optimization | Reasonable estimates | Unrealistic or missing calculations |
| **Migration Roadmap** | 10% | Practical, phased plan with risk mitigation | Reasonable plan | Unrealistic or vague |
| **Communication Quality** | 5% | Clear, professional, well-structured | Minor issues | Difficult to follow |

---

## Supporting Materials for Students

### LLMOps Reference Architecture

The following layered architecture shows how LLMOps components are organized:

![LLMOps Reference Architecture](./diagrams/llmops-reference-architecture.png)

*Figure 4: Six-layer LLMOps reference architecture with AWS service mapping*

### Recommended Readings
1. Google MLOps Whitepaper (Levels 0-1-2)
2. AWS SageMaker Documentation (Pipelines, Model Registry)
3. AWS Bedrock Documentation (Guardrails, Knowledge Bases)
4. EU AI Act Summary (risk classification)

### AWS Services Reference

| Service | Purpose in Case |
|---------|-----------------|
| SageMaker Pipelines | ML workflow orchestration |
| SageMaker Feature Store | Feature management |
| SageMaker Model Registry | Model versioning |
| SageMaker Clarify | Bias detection |
| Bedrock | Foundation model access |
| Bedrock Guardrails | Safety controls |
| OpenSearch | Vector store |
| Textract | Document OCR |
| Step Functions | LLMOps orchestration |

---

## Instructor Notes

### Learning Objectives
1. Understand the differences between MLOps and LLMOps architectures
2. Apply maturity models to assess operational readiness
3. Analyze governance requirements for AI systems
4. Conduct cost-benefit analysis for ML/LLM systems
5. Design practical migration strategies

### Common Student Mistakes to Address
- Assuming LLMOps replaces all MLOps practices (it extends them)
- Underestimating token costs at scale
- Overlooking the need for prompt versioning
- Ignoring hallucination risks in document intelligence

### Discussion Questions for Class
1. When should a company NOT migrate from MLOps to LLMOps?
2. How would you handle a hybrid approach (ML + LLM)?
3. What happens when the LLM provider changes their model?

---

## Sample Answer Key (Instructor Only)

### Part 2.2 Artifact Comparison — Sample Answers

| Artifact | MLOps | LLMOps |
|----------|-------|--------|
| Training Data | Labeled documents (CSV) | Document chunks + embeddings, few-shot examples |
| Features | TF-IDF vectors | Dense embeddings (Titan), retrieved context |
| Model | XGBoost .pkl file | Foundation model (API) + optional LoRA adapter |
| Config | Hyperparameters JSON | Prompt templates + RAG config + guardrails config |
| Evaluation | Confusion matrix | + Hallucination rate, factuality score, retrieval accuracy |

### Part 3 LLMOps Maturity — Sample Answers

| Level | LLMOps Characteristics |
|-------|------------------------|
| **Level 0** | Prompts hardcoded, no versioning, manual RAG setup, no guardrails, ad-hoc evaluation |
| **Level 1** | Prompt registry, automated RAG indexing, basic guardrails, structured evaluation with human review |
| **Level 2** | Prompt CI/CD, A/B testing, automatic guardrail updates, hallucination detection, cost optimization, full audit trail |

### Part 4 Risk Classification — Sample Answers

| System | Risk Level | Justification |
|--------|------------|---------------|
| MLOps (classifier) | Limited Risk | Document classification for internal workflow, no direct impact on individuals |
| LLMOps (Claude-based) | High Risk (potentially) | If used for contract decisions affecting parties, requires transparency and human oversight |
