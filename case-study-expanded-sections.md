# Expanded Sections for Case Study

## Supplementary Material for Students

---

## Architecture Diagrams Reference

The following diagrams are provided for this case study:

### Figure 1: MLOps Architecture (Current State)
![MLOps Architecture](./diagrams/mlops-architecture.png)

### Figure 2: LLMOps Architecture (Proposed State)
![LLMOps Architecture](./diagrams/llmops-architecture.png)

### Figure 3: Side-by-Side Comparison
![MLOps vs LLMOps Comparison](./diagrams/mlops-vs-llmops-comparison.png)

### Figure 4: LLMOps Reference Architecture (Layered View)
![LLMOps Reference Architecture](./diagrams/llmops-reference-architecture.png)

---

## Section 2: Comparative Analysis Framework — EXPANDED

### 2.1 Architecture Comparison — Complete Table

Students should understand each dimension in depth. Here is the complete comparison:

| Dimension | MLOps (Current) | LLMOps (Proposed) | Key Insight |
|-----------|-----------------|-------------------|-------------|
| **Core Model** | XGBoost classifier (custom trained) | Claude 3 Sonnet (foundation model via Bedrock) | MLOps requires full training; LLMOps uses pre-trained capabilities |
| **Data Storage** | SageMaker Feature Store (tabular, structured) | OpenSearch Vector Store (dense embeddings) | Different data paradigms: rows vs. semantic vectors |
| **Pipeline Tool** | SageMaker Pipelines (native ML orchestration) | Step Functions + Bedrock (general orchestration) | MLOps has purpose-built tools; LLMOps adapts general tools |
| **Versioning** | Model versions in Model Registry | Model + Prompt versions + RAG config versions | LLMOps has 3x more artifact types to version |
| **Retraining Trigger** | Data drift detected by Model Monitor | Data drift + Prompt updates + Retrieval quality drop | More triggers = more automation complexity |
| **Input Processing** | Batch feature extraction (TF-IDF) | Real-time chunking + embedding | LLMOps processes documents differently |
| **Output Type** | Fixed schema (12 classes + 15 fields) | Flexible (any question, any format) | LLMOps trades structure for flexibility |
| **Latency Profile** | Predictable (2.3s ± 0.3s) | Variable (3-8s depending on context size) | LLMOps latency depends on token count |
| **Cost Driver** | Compute hours (training + inference) | Token consumption (input + output) | Fundamentally different economics |
| **Failure Mode** | Wrong classification (measurable error) | Hallucination (harder to detect) | Different quality assurance approaches |

### 2.2 Artifact Comparison — Complete Answers

| Artifact | MLOps | LLMOps | Why It Matters |
|----------|-------|--------|----------------|
| **Training Data** | 50,000 labeled documents (CSV with labels) | Document chunks + embeddings (vector DB), few-shot examples (10-20 per task) | LLMOps uses retrieval instead of memorization |
| **Features** | TF-IDF vectors (sparse, 10K dimensions) | Dense embeddings (Titan: 1536 dimensions) | Dense embeddings capture semantic meaning |
| **Model Artifact** | XGBoost .pkl file (50MB, self-contained) | Foundation model (API access) + optional LoRA adapter (few MB) | LLMOps separates model from customization |
| **Configuration** | Hyperparameters JSON (learning rate, depth, etc.) | Prompt templates + RAG config (chunk size, overlap, top-k) + guardrails config | 3x more configuration surfaces |
| **Evaluation Data** | Held-out test set (5K documents) | Test suite + human evaluation rubrics + retrieval accuracy tests | LLMOps requires multi-dimensional evaluation |
| **Deployment Package** | Docker container with model + dependencies | API endpoint + prompt registry + vector index | LLMOps deployment is distributed |

### 2.3 Metrics Comparison — Detailed Definitions

#### Quality Metrics

| Metric | MLOps Definition | LLMOps Definition | Measurement Method |
|--------|------------------|-------------------|-------------------|
| **Accuracy** | % of correctly classified documents | % of factually correct responses | Automated + human review |
| **Precision** | TP / (TP + FP) per class | Not directly applicable | — |
| **Recall** | TP / (TP + FN) per class | Not directly applicable | — |
| **F1 Score** | Harmonic mean of precision/recall | Can be computed for classification tasks | Per-class and weighted |
| **Hallucination Rate** | N/A | % of responses containing fabricated information | Human annotation + automated detection |
| **Factuality Score** | N/A | % of claims that can be verified against source | Citation matching |
| **Relevance** | N/A | How well the response addresses the query | Human rating (1-5 scale) |
| **Coherence** | N/A | Logical flow and readability of response | Human rating (1-5 scale) |

#### Performance Metrics

| Metric | MLOps Definition | LLMOps Definition | Target for TechCorp |
|--------|------------------|-------------------|---------------------|
| **Latency (E2E)** | Time from request to response | Time from request to response | MLOps: <3s, LLMOps: <6s |
| **TTFT** | N/A | Time to first token (streaming) | <500ms |
| **Throughput** | Requests per second | Requests per second | MLOps: 50 RPS, LLMOps: 20 RPS |
| **Tokens/second** | N/A | Generation speed | >30 tokens/sec |

#### Cost Metrics

| Metric | MLOps Calculation | LLMOps Calculation | TechCorp Example |
|--------|-------------------|--------------------|--------------------|
| **Cost per document** | (Monthly compute) / (Documents processed) | (Input tokens + Output tokens) × Price per token | MLOps: $0.084, LLMOps: $0.25 |
| **Training cost** | GPU hours × Price per hour | Fine-tuning tokens × Price (if applicable) | MLOps: $800/mo, LLMOps: $200/mo |
| **Storage cost** | Feature Store GB × Price | Vector Store GB × Price + S3 | MLOps: $400/mo, LLMOps: $1,200/mo |

---

## Section 3: Maturity Level Analysis — EXPANDED

### MLOps Maturity Assessment for TechCorp

#### Evidence-Based Assessment

| Criterion | TechCorp Evidence | Level Assessment |
|-----------|-------------------|------------------|
| **Pipeline automation** | SageMaker Pipelines orchestrates training workflow | Level 1 ✓ |
| **Feature management** | Feature Store in use, features versioned | Level 1 ✓ |
| **Model versioning** | Model Registry tracks versions, but no approval workflow | Level 1 (partial Level 2) |
| **Monitoring** | Model Monitor detects drift, but retraining is manual | Level 1 ✓ |
| **Governance** | Basic CloudTrail logging, no formal audit process | Level 1 (partial) |
| **CI/CD** | No automated testing of models before deployment | Level 0 ✗ |

**Conclusion:** TechCorp is at **Level 1** with partial Level 2 capabilities. The main gaps are:
1. No CI/CD for model validation
2. Manual retraining (not automatic)
3. No approval workflows for production deployment

#### Path to Level 2 (MLOps)

| Gap | Required Action | AWS Service | Effort |
|-----|-----------------|-------------|--------|
| CI/CD for models | Automated model testing pipeline | CodePipeline + SageMaker Projects | 2-3 weeks |
| Auto-retraining | Trigger training on drift detection | EventBridge + Step Functions | 1-2 weeks |
| Approval workflows | Human approval before prod deployment | Model Registry + SNS | 1 week |
| A/B testing | Canary deployments for new models | SageMaker Endpoints (variants) | 2 weeks |

### LLMOps Maturity Model — Detailed Definitions

#### Level 0: Manual/Ad-hoc

**Characteristics:**
- Prompts are hardcoded in application source code
- No version control for prompts (changes require code deployments)
- RAG setup is manual: indexes built once, never updated
- No guardrails or basic string matching only
- Evaluation through manual testing ("looks good to me")
- No cost tracking; token usage unknown
- No audit trail of LLM interactions

**Symptoms:**
- "The prompt worked yesterday, what changed?"
- "How much did we spend on Claude last month?" → "No idea"
- "Can you show me why the system gave this answer?" → "Not possible"

#### Level 1: Pipeline Automation

**Characteristics:**
- Prompt registry with version control (S3 + metadata)
- Automated RAG index updates (scheduled or event-driven)
- Basic guardrails: PII detection, toxicity filtering
- Structured evaluation with test suites (golden datasets)
- Cost monitoring with alerts (CloudWatch)
- Human-in-the-loop for critical decisions
- Basic logging of inputs/outputs

**Indicators:**
- Can roll back to previous prompt version
- Know token usage per application/user
- Can reproduce any past interaction
- Guardrails catch obvious violations

#### Level 2: Full CI/CD + Governance

**Characteristics:**
- Prompt CI/CD: changes go through PR review, automated testing, staged rollout
- A/B testing for prompts: measure impact before full deployment
- Continuous RAG optimization: automatic reindexing, chunk size tuning
- Adaptive guardrails: feedback loops adjust sensitivity
- Automated hallucination detection: citation verification, fact-checking
- Cost optimization: caching, model routing (use cheaper models when possible)
- Full audit trail: complete lineage from query to response with reasoning
- Compliance-ready: meets EU AI Act requirements

**Indicators:**
- "This prompt increased accuracy by 3%" (measured via A/B test)
- Hallucination rate tracked and trending downward
- Cost per request decreasing through optimization
- Can explain any decision to auditors

---

## Section 4: Governance & Compliance — EXPANDED

### EU AI Act Classification

#### Risk Categories Explained

| Risk Level | Description | Requirements | Examples |
|------------|-------------|--------------|----------|
| **Unacceptable** | Banned AI practices | Prohibited | Social scoring, real-time biometric surveillance |
| **High Risk** | AI in critical domains | Strict requirements | Healthcare, legal, employment, credit |
| **Limited Risk** | AI with transparency needs | Disclosure only | Chatbots, emotion recognition |
| **Minimal Risk** | Low-risk AI | No requirements | Spam filters, video games |

#### TechCorp Classification Analysis

**MLOps System (Document Classifier):**
- **Proposed classification:** Limited Risk
- **Reasoning:**
  - Processes business documents, not personal data primarily
  - No direct impact on individuals' rights
  - Internal workflow optimization tool
  - Outputs are reviewed by humans before action
- **Requirements:** Transparency that AI is being used

**LLMOps System (Claude-based):**
- **Proposed classification:** Could be High Risk if:
  - Used for contract decisions affecting parties
  - Provides legal or compliance advice
  - Outputs directly influence business decisions without human review
- **Reasoning:**
  - Foundation model (Claude) is considered "General Purpose AI" under EU AI Act
  - If integrated into high-risk system, inherits requirements
  - Q&A and summarization may influence important decisions
- **Requirements if High Risk:**
  - Risk management system
  - Data governance
  - Technical documentation
  - Record-keeping
  - Transparency to users
  - Human oversight
  - Accuracy, robustness, cybersecurity

### Guardrails Design for TechCorp LLMOps

#### Input Guardrails

| Guardrail | Purpose | Implementation | Action on Trigger |
|-----------|---------|----------------|-------------------|
| **PII Detection** | Prevent processing of sensitive personal data | AWS Comprehend PII detection | Mask PII before sending to LLM |
| **Prompt Injection Detection** | Prevent manipulation of system behavior | Pattern matching + classifier | Reject request, log incident |
| **Content Policy** | Block inappropriate content | Bedrock Guardrails content filters | Reject request |
| **Rate Limiting** | Prevent abuse and cost overrun | API Gateway throttling | Return 429, queue request |

#### Output Guardrails

| Guardrail | Purpose | Implementation | Action on Trigger |
|-----------|---------|----------------|-------------------|
| **Hallucination Check** | Detect fabricated information | Citation verification against source docs | Add confidence warning, request human review |
| **Factuality Verification** | Ensure claims match source | Cross-reference with retrieved chunks | Highlight unverified claims |
| **PII in Output** | Prevent leaking sensitive data | Scan output before returning | Redact PII, log incident |
| **Confidence Scoring** | Flag low-confidence responses | Model self-assessment + retrieval scores | Add warning banner, require confirmation |
| **Toxicity Filtering** | Block harmful content | Bedrock Guardrails | Block response, return safe alternative |

#### Guardrail Configuration Example (Bedrock)

```json
{
  "name": "TechCorp-DocIntelligence-Guardrails",
  "contentPolicyConfig": {
    "filtersConfig": [
      {"type": "HATE", "inputStrength": "HIGH", "outputStrength": "HIGH"},
      {"type": "INSULTS", "inputStrength": "HIGH", "outputStrength": "HIGH"},
      {"type": "SEXUAL", "inputStrength": "HIGH", "outputStrength": "HIGH"},
      {"type": "VIOLENCE", "inputStrength": "MEDIUM", "outputStrength": "HIGH"}
    ]
  },
  "sensitiveInformationPolicyConfig": {
    "piiEntitiesConfig": [
      {"type": "EMAIL", "action": "ANONYMIZE"},
      {"type": "PHONE", "action": "ANONYMIZE"},
      {"type": "SSN", "action": "BLOCK"},
      {"type": "CREDIT_DEBIT_CARD_NUMBER", "action": "BLOCK"}
    ]
  },
  "topicPolicyConfig": {
    "topicsConfig": [
      {
        "name": "Legal Advice",
        "definition": "Providing specific legal recommendations or interpretations",
        "action": "BLOCK"
      },
      {
        "name": "Financial Advice",
        "definition": "Recommending specific financial decisions",
        "action": "BLOCK"
      }
    ]
  }
}
```

---

## Section 5: Cost-Benefit Analysis — EXPANDED

### Detailed Cost Breakdown

#### MLOps Monthly Costs

| Cost Element | Calculation | Monthly Cost |
|--------------|-------------|--------------|
| **SageMaker Training** | 2 retraining runs × 4 hours × ml.m5.xlarge ($0.23/hr) | $1.84 |
| **SageMaker Training (GPU)** | 2 runs × 4 hours × ml.g4dn.xlarge ($0.526/hr) | $800 (estimated) |
| **SageMaker Endpoint** | 1 × ml.m5.large × 720 hours × $0.115/hr | $82.80 |
| **SageMaker Endpoint (prod)** | 2 × ml.m5.xlarge × 720 hours × $0.23/hr | $331.20 |
| **Feature Store** | 50GB online + 500GB offline | $400 |
| **Model Monitor** | 50K inferences × $0.01/1K | $500 |
| **Data Labeling** | 1,000 new labels/month × $1/label | $1,000 |
| **S3 Storage** | 100GB × $0.023 | $2.30 |
| **Data Transfer** | 500GB × $0.09 | $45 |
| **Other (CloudWatch, etc.)** | — | $200 |
| **TOTAL** | — | **~$4,200** |

#### LLMOps Monthly Costs

| Cost Element | Calculation | Monthly Cost |
|--------------|-------------|--------------|
| **Bedrock (Claude 3 Sonnet)** | | |
| — Input tokens | 50K docs × 2K tokens × $0.003/1K | $300 |
| — Output tokens | 50K docs × 500 tokens × $0.015/1K | $375 |
| — RAG context | 50K docs × 4K context × $0.003/1K | $600 |
| **Titan Embeddings** | 50K docs × 5 chunks × 500 tokens × $0.0001/1K | $12.50 |
| **OpenSearch (Vector Store)** | 2 × r6g.large.search × 720 hours | $500 |
| **OpenSearch Storage** | 200GB × $0.10/GB | $20 |
| **Step Functions** | 50K executions × $0.025/1K | $1.25 |
| **Lambda (chunking, orchestration)** | 50K invocations + compute | $50 |
| **Textract** | 50K pages × $0.0015/page | $75 |
| **S3 (documents + prompts)** | 500GB | $11.50 |
| **CloudWatch (monitoring)** | Logs, metrics, alarms | $200 |
| **Bedrock Guardrails** | 50K assessments × $0.75/1K | $37.50 |
| **Reserved capacity buffer** | 20% overhead | $2,000 |
| **TOTAL** | — | **~$12,500** |

### Cost Per Document Analysis

| Metric | MLOps | LLMOps | Difference |
|--------|-------|--------|------------|
| **Monthly cost** | $4,200 | $12,500 | +198% |
| **Documents processed** | 50,000 | 50,000 | — |
| **Cost per document** | $0.084 | $0.25 | +198% |
| **Capabilities** | Classification + extraction | + Q&A + summarization + explanation | Significantly more |

### Break-Even Analysis

**Question:** At what point does LLMOps become cost-competitive?

**Scenario 1: Reduced Human Review**
- Current: 20% of documents flagged for human review
- Human reviewer cost: $50/hour, 5 min per document
- Monthly human cost: 10,000 docs × $4.17 = $41,700
- If LLMOps reduces review rate to 5%: 2,500 × $4.17 = $10,425
- Savings: $31,275/month → LLMOps pays for itself 2.5x over

**Scenario 2: Value of New Capabilities**
- Q&A feature eliminates 500 support tickets/month
- Support ticket cost: $25/ticket
- Monthly savings: $12,500 → Exactly covers LLMOps premium

### Cost Optimization Strategies for LLMOps

| Strategy | Description | Potential Savings |
|----------|-------------|-------------------|
| **Prompt caching** | Cache common prompts/responses | 20-40% |
| **Model routing** | Use Haiku for simple tasks, Sonnet for complex | 30-50% |
| **Batch processing** | Process during off-peak hours | 10-20% |
| **Chunk optimization** | Reduce context window size | 15-25% |
| **Output length limits** | Cap max tokens for routine tasks | 10-20% |
| **Semantic caching** | Cache similar queries | 20-30% |

---

## Section 6: Migration Roadmap — EXPANDED

### Phase 1: Pilot (Weeks 1-8)

#### Week 1-2: Infrastructure Setup
| Task | Owner | Deliverable |
|------|-------|-------------|
| Provision OpenSearch cluster | DevOps | Running cluster with vector support |
| Configure Bedrock access | Platform | API access, guardrails configured |
| Set up Step Functions | Platform | Basic orchestration workflow |
| Create prompt registry (S3) | ML Team | Versioned prompt storage |

#### Week 3-4: RAG Pipeline Development
| Task | Owner | Deliverable |
|------|-------|-------------|
| Implement chunking strategy | ML Team | Tested chunking Lambda |
| Build embedding pipeline | ML Team | Automated embedding generation |
| Configure vector indexing | ML Team | Searchable vector index |
| Create retrieval function | ML Team | Top-k retrieval working |

#### Week 5-6: LLM Integration
| Task | Owner | Deliverable |
|------|-------|-------------|
| Design prompt templates | ML Team | Versioned prompts for invoice processing |
| Implement guardrails | ML Team | PII, hallucination checks active |
| Build response parsing | ML Team | Structured output extraction |
| Create evaluation suite | QA | Golden dataset + metrics |

#### Week 7-8: Pilot Testing
| Task | Owner | Deliverable |
|------|-------|-------------|
| Process 1,000 invoices | QA | Accuracy metrics |
| Compare with MLOps baseline | QA | Side-by-side analysis |
| User acceptance testing | Business | Feedback report |
| Cost analysis | Finance | Actual vs. projected costs |

#### Pilot Success Criteria
| Metric | Target | Must Have |
|--------|--------|-----------|
| Classification accuracy | ≥95% | ≥93% |
| Field extraction accuracy | ≥90% | ≥87% |
| Hallucination rate | <2% | <5% |
| Latency (P95) | <6s | <10s |
| Cost per document | <$0.30 | <$0.40 |
| User satisfaction | >4/5 | >3.5/5 |

### Phase 2: Parallel Run (Weeks 9-16)

#### Architecture
```
                    ┌─────────────────┐
                    │   Load Balancer │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                              ▼
    ┌─────────────────┐            ┌─────────────────┐
    │  MLOps Pipeline │            │ LLMOps Pipeline │
    │   (Production)  │            │    (Shadow)     │
    └────────┬────────┘            └────────┬────────┘
             │                              │
             ▼                              ▼
    ┌─────────────────┐            ┌─────────────────┐
    │ Production DB   │            │  Comparison DB  │
    └─────────────────┘            └─────────────────┘
                                            │
                                            ▼
                                   ┌─────────────────┐
                                   │ Analysis Dashboard│
                                   └─────────────────┘
```

#### Comparison Metrics Dashboard
| Metric | MLOps | LLMOps | Delta | Status |
|--------|-------|--------|-------|--------|
| Classification match | — | — | — | Auto-calculated |
| Extraction match | — | — | — | Auto-calculated |
| Processing time | — | — | — | Auto-calculated |
| Cost per doc | — | — | — | Auto-calculated |
| Error rate | — | — | — | Auto-calculated |

#### Go/No-Go Decision Criteria

**GO if ALL of these are true:**
- [ ] LLMOps accuracy ≥ MLOps accuracy for 4 consecutive weeks
- [ ] Hallucination rate < 3% for 4 consecutive weeks
- [ ] Cost per document < 3× MLOps cost
- [ ] Latency P95 < 2× MLOps latency
- [ ] No critical guardrail failures
- [ ] User feedback score > 4/5
- [ ] Audit requirements satisfied

**NO-GO if ANY of these are true:**
- [ ] Accuracy drops below MLOps baseline
- [ ] Hallucination rate > 5%
- [ ] Cost exceeds budget by > 50%
- [ ] Critical data exposure incident
- [ ] Compliance violation identified

### Phase 3: Full Migration (Weeks 17-24)

#### Cutover Strategy: Blue-Green Deployment

```
Week 17-18: Preparation
├── Notify all stakeholders
├── Document rollback procedure
├── Train support team on LLMOps
└── Freeze MLOps pipeline changes

Week 19-20: Gradual Cutover
├── Day 1: 10% traffic to LLMOps
├── Day 3: 25% traffic (if metrics OK)
├── Day 7: 50% traffic (if metrics OK)
├── Day 10: 75% traffic (if metrics OK)
└── Day 14: 100% traffic (if metrics OK)

Week 21-22: Stabilization
├── Monitor all metrics intensively
├── Address any issues immediately
├── Keep MLOps on standby
└── Document lessons learned

Week 23-24: Decommissioning
├── Archive MLOps artifacts
├── Terminate MLOps infrastructure (after 30 days)
├── Complete documentation
└── Project retrospective
```

#### Rollback Plan

**Trigger conditions for rollback:**
1. Accuracy drops > 5% below baseline for > 24 hours
2. Hallucination rate > 10% for any 4-hour period
3. System unavailability > 1 hour
4. Data breach or PII exposure
5. Cost exceeds 200% of projection for > 1 week

**Rollback procedure:**
1. **Immediate (< 5 minutes):** Route 100% traffic to MLOps endpoint
2. **Communication (< 15 minutes):** Notify stakeholders via Slack/email
3. **Investigation (< 2 hours):** Root cause analysis
4. **Resolution (variable):** Fix issue, test, plan re-cutover
5. **Documentation (< 24 hours):** Incident report

