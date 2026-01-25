# From MLOps to LLMOps: Architecture and Lifecycle

## Abstract

This document provides a comprehensive explanation of how Large Language Model Operations (LLMOps) extends and transforms traditional MLOps practices. It describes the architectural changes, new components, and operational considerations that organizations face when transitioning from conventional machine learning systems to production-grade LLM applications. The document covers the key differences in artifact management, pipeline design, monitoring requirements, and governance mechanisms. Each component is explained in detail, from prompt engineering through retrieval-augmented generation to hallucination detection. This guide serves as both a conceptual framework for understanding LLMOps principles and a practical reference for teams building production LLM systems.

## Introduction

The emergence of Large Language Models has fundamentally changed how organizations approach artificial intelligence. While traditional MLOps focused on training custom models from labeled data, LLMOps introduces a paradigm shift: instead of building models from scratch, teams now orchestrate pre-trained foundation models, design prompts, and construct retrieval pipelines. This transition brings new challenges that existing MLOps practices do not address.

**Why LLMOps matters:**

- **Prompts are the new models.** In traditional ML, the model weights encode learned behavior. In LLMOps, the prompt—including system instructions, few-shot examples, and context—determines how the model behaves. Prompts require the same versioning, testing, and governance as model artifacts.

- **Retrieval quality determines output quality.** Foundation models have knowledge cutoffs and can hallucinate. Retrieval-Augmented Generation (RAG) grounds responses in actual documents, but the quality of retrieval directly impacts the quality of answers.

- **Token economics replace compute economics.** Traditional ML costs scale with training compute and inference hardware. LLM costs scale with tokens—every input token and output token has a price. This fundamentally changes how teams think about optimization.

- **Hallucination is a new failure mode.** Traditional models can be wrong, but they don't fabricate information. LLMs can generate confident, plausible, and completely false statements. Detecting and preventing hallucination requires new monitoring approaches.

- **Governance requirements are intensifying.** The EU AI Act and similar regulations classify foundation models as requiring transparency and accountability. Organizations must demonstrate how their LLM systems make decisions and what guardrails prevent harmful outputs.

**What you will learn:**

This document walks through each component of a production LLMOps system, explaining how it differs from traditional MLOps, what new artifacts and pipelines it introduces, and how all the pieces connect. By the end, you will understand not just *what* LLMOps adds, but *why* these additions are necessary and how they form a coherent, production-ready architecture.

**Related materials in this repository:**

- [Case Study: MLOps vs LLMOps](./case-study-mlops-llmops.md) — A hands-on comparative study for students
- [Case Study: Expanded Sections](./case-study-expanded-sections.md) — Instructor guide with detailed answers
- [Research Paper Outline](./research-paper-mlops-to-llmops.md) — Academic paper structure for publication
- [Architecture Diagrams](./diagrams/) — Visual representations of MLOps and LLMOps architectures

## 1. High-Level Definition

LLMOps (Large Language Model Operations) is the discipline that extends MLOps to address the unique requirements of deploying and operating Large Language Models in production.

LLMOps combines:

- **Foundation Model Management:** Selecting, accessing, and optionally fine-tuning pre-trained models.
- **Prompt Engineering:** Designing, versioning, and optimizing the instructions that control model behavior.
- **Retrieval Engineering:** Building pipelines that provide relevant context from organizational knowledge bases.
- **Guardrails and Safety:** Implementing filters, validators, and policies that ensure safe and compliant outputs.
- **Token-Based Cost Management:** Monitoring and optimizing the economic efficiency of LLM usage.

Its main purpose is:

> To reliably transform experimental LLM applications into production-grade, safe, cost-effective, and continuously improving systems.

Unlike traditional MLOps, where the primary artifact is a trained model, LLMOps manages multiple artifact types:

- **Prompts:** The instructions, examples, and templates that shape model responses.
- **RAG Configurations:** The chunking strategies, embedding models, and retrieval parameters.
- **Vector Indices:** The searchable representations of organizational knowledge.
- **Guardrail Policies:** The rules that filter inputs and validate outputs.
- **Fine-tuning Adapters:** Optional lightweight customizations applied to foundation models.

This architecture is not just a pipeline—it is a **closed-loop system** where monitoring informs prompt refinement, retrieval tuning, and guardrail adjustment.

![LLMOps Reference Architecture](./diagrams/llmops-reference-architecture.png)

*Figure 1: Six-layer LLMOps reference architecture showing component organization*

## 2. How LLMOps Differs from MLOps

Before examining individual components, it is essential to understand the fundamental differences between traditional MLOps and LLMOps.

![MLOps vs LLMOps Comparison](./diagrams/mlops-vs-llmops-comparison.png)

*Figure 2: Side-by-side comparison of MLOps and LLMOps architectures*

### 2.1 Artifact Types

| MLOps Artifact | LLMOps Equivalent | Key Difference |
|----------------|-------------------|----------------|
| Training data (labeled examples) | Few-shot examples, retrieval corpus | LLMOps uses retrieval instead of memorization |
| Feature Store | Vector Store | Dense embeddings replace tabular features |
| Model weights (.pkl, .pt) | Prompt templates + optional adapters | Behavior encoded in prompts, not weights |
| Hyperparameters | RAG configuration (chunk size, top-k) | Different tuning surfaces |
| Model Registry | Prompt Registry + Model Registry | Two registries instead of one |

### 2.2 Pipeline Stages

**Traditional MLOps Pipeline:**
```
Data → Features → Train → Evaluate → Register → Deploy → Monitor
```

**LLMOps Pipeline:**
```
Data → Chunk → Embed → Index → Prompts → Evaluate → Guardrails → Deploy → Monitor
```

The key differences:

- **No training stage** for foundation model usage (only for fine-tuning).
- **Chunking and embedding** replace feature engineering.
- **Guardrails** become a mandatory stage before deployment.
- **Monitoring** expands to include hallucination detection and token cost tracking.

### 2.3 Failure Modes

| MLOps Failure | LLMOps Equivalent | Detection Method |
|---------------|-------------------|------------------|
| Low accuracy | Low accuracy + hallucination | Factuality verification against sources |
| Data drift | Data drift + semantic drift | Embedding space monitoring |
| Model degradation | Retrieval quality degradation | Retrieval accuracy metrics |
| Bias | Bias + toxicity + policy violations | Guardrail trigger rates |

### 2.4 Cost Models

| Aspect | MLOps | LLMOps |
|--------|-------|--------|
| Training cost | GPU hours × price | Fine-tuning tokens × price (if applicable) |
| Inference cost | Compute per request | Input tokens + output tokens × price |
| Storage cost | Model size + features | Vector index size + documents |
| Scaling | Horizontal (more instances) | Vertical (larger context) + horizontal |

This answers:

➡ *What makes LLMOps fundamentally different from MLOps?*

## 3. Component-by-Component Explanation

### 3.1 Document Ingestion

**Purpose:** Convert organizational knowledge into a format suitable for retrieval.

Typical tasks:

- **Document parsing:** The extraction of text and structure from various file formats (PDF, DOCX, HTML) into a unified representation.
- **Metadata extraction:** The identification and preservation of document attributes such as title, author, date, and source.
- **Content cleaning:** The removal of noise, boilerplate, and formatting artifacts that do not contribute to semantic meaning.
- **Language detection:** The identification of the document's language to enable appropriate processing and retrieval.

This phase is:

- Automated
- Format-dependent
- Quality-critical

It answers:

➡ *What knowledge does the organization have?*

### 3.2 Chunking

**Purpose:** Segment documents into retrievable units.

Chunking is one of the most critical decisions in RAG system design. The chunk size determines:

- **Retrieval precision:** Smaller chunks enable more precise matching but may lose context.
- **Context utilization:** Larger chunks provide more context but may dilute relevance.
- **Token efficiency:** Chunk size directly impacts how many tokens are consumed per query.

Strategies include:

- **Fixed-size chunking:** Dividing text into segments of a predetermined token or character count.
- **Semantic chunking:** Splitting at natural boundaries such as paragraphs, sections, or sentences.
- **Recursive chunking:** Progressively splitting large segments until they meet size constraints.
- **Overlap chunking:** Including redundant content at chunk boundaries to preserve context across splits.

Key parameters:

- **Chunk size:** The target length of each segment, typically 256-1024 tokens.
- **Chunk overlap:** The number of tokens shared between adjacent chunks, typically 10-20%.
- **Separator hierarchy:** The priority order of split points (section > paragraph > sentence).

This answers:

➡ *How should knowledge be divided for retrieval?*

### 3.3 Embedding

**Purpose:** Transform text into dense vector representations.

Embedding models convert chunks into high-dimensional vectors that capture semantic meaning. Similar concepts produce similar vectors, enabling semantic search.

Key considerations:

- **Model selection:** The choice of embedding model (e.g., OpenAI ada-002, Titan, sentence-transformers) affects both quality and cost.
- **Dimensionality:** Higher dimensions capture more nuance but increase storage and computation costs.
- **Normalization:** Vectors are typically normalized to enable cosine similarity comparisons.
- **Batch processing:** Embeddings are computed in batches to optimize throughput and cost.

The embedding model determines the semantic space in which retrieval operates. Changing the embedding model requires re-indexing all documents.

This is where:

> Text becomes mathematics.

### 3.4 Vector Store

**Purpose:** Centralized, searchable index of document embeddings.

The Vector Store is the LLMOps equivalent of the Feature Store. It ensures:

- **Fast retrieval:** Approximate nearest neighbor algorithms enable sub-second search over millions of vectors.
- **Metadata filtering:** Queries can be constrained by document attributes (date, source, category).
- **Scalability:** The index grows with organizational knowledge without degrading performance.
- **Consistency:** The same vectors are used for all queries, preventing training-serving skew equivalent.

It usually has:

- **Online store:** Optimized for low-latency retrieval during inference.
- **Offline store:** Optimized for batch operations like re-indexing and analysis.

Common implementations:

- Pinecone
- Weaviate
- OpenSearch
- pgvector
- Chroma

This prevents the classic problem:

> "The retrieval results in development were different from production."

### 3.5 Prompt Engineering

**Purpose:** Design the instructions that control LLM behavior.

Prompt engineering is the primary means of customizing foundation model behavior without fine-tuning. A prompt typically includes:

- **System instructions:** The high-level directives that define the model's role, constraints, and output format.
- **Few-shot examples:** Representative input-output pairs that demonstrate the desired behavior.
- **Context injection point:** The location where retrieved documents are inserted.
- **Output format specification:** The structure expected in the response (JSON, markdown, specific fields).

Characteristics:

- **Iterative:** Prompts are refined through experimentation and evaluation.
- **Version-controlled:** Changes to prompts must be tracked like code changes.
- **Environment-specific:** Different prompts may be used for development, staging, and production.
- **A/B testable:** Multiple prompt variants can be compared in production.

This is where:

> Instructions become behavior.

### 3.6 Prompt Registry

**Purpose:** Centralized, versioned repository of prompts.

The Prompt Registry serves the same function for prompts that the Model Registry serves for models. It stores:

- **Prompt versions:** Immutable snapshots of prompt templates, each uniquely identified.
- **Prompt metadata:** Information about purpose, author, creation date, and associated evaluations.
- **Performance metrics:** Historical data on how each prompt version performed in production.
- **Lifecycle stages:** Labels such as *draft*, *testing*, *production*, or *deprecated*.
- **Rollback history:** The ability to instantly revert to any previous version.

This enables:

- **Reproducibility:** Any past system behavior can be recreated by restoring the prompt version.
- **Governance:** Changes to prompts pass through approval workflows before reaching production.
- **Experimentation:** Multiple prompt versions can run simultaneously for comparison.

It answers:

➡ *What instructions were the model given at any point in time?*

### 3.7 RAG Pipeline

**Purpose:** Orchestrate the retrieval and generation process.

![LLMOps Architecture](./diagrams/llmops-architecture.png)

*Figure 3: LLMOps pipeline showing the flow from documents through RAG to response*

The RAG (Retrieval-Augmented Generation) pipeline connects the Vector Store, Prompt Registry, and LLM into a coherent system. It:

- **Receives queries:** Accepts user input through an API or interface.
- **Embeds queries:** Converts the query into the same vector space as the documents.
- **Retrieves context:** Finds the most relevant chunks from the Vector Store.
- **Constructs prompts:** Assembles the system instructions, retrieved context, and user query.
- **Calls the LLM:** Sends the constructed prompt to the foundation model.
- **Post-processes responses:** Extracts structured data, adds citations, or formats output.

Key parameters:

- **Top-k:** The number of chunks to retrieve.
- **Similarity threshold:** The minimum relevance score for inclusion.
- **Reranking:** Optional second-stage ranking to improve precision.
- **Context window management:** Strategies for handling retrieved content that exceeds token limits.

This is the core of most production LLM applications.

### 3.8 Guardrails

**Purpose:** Ensure safe, compliant, and high-quality outputs.

Guardrails are filters and validators that operate on inputs, outputs, or both. They are not optional—they are essential for production deployment.

**Input guardrails:**

- **PII detection:** Identifies and optionally redacts personal identifiable information before sending to the LLM.
- **Prompt injection detection:** Recognizes attempts to manipulate the system through malicious inputs.
- **Content policy filtering:** Blocks inputs that violate organizational or legal policies.
- **Rate limiting:** Prevents abuse through excessive requests.

**Output guardrails:**

- **Hallucination detection:** Verifies that claims in the response are supported by retrieved context.
- **Toxicity filtering:** Blocks responses containing harmful, offensive, or inappropriate content.
- **PII leakage prevention:** Ensures the model does not expose sensitive information in outputs.
- **Format validation:** Confirms that structured outputs conform to expected schemas.

Guardrails answer:

➡ *Is this interaction safe and compliant?*

### 3.9 Foundation Model Access

**Purpose:** Interface with pre-trained Large Language Models.

Unlike traditional MLOps where the model is a local artifact, LLMOps typically accesses models through:

- **API providers:** Cloud services (OpenAI, Anthropic, AWS Bedrock) that host and serve models.
- **Self-hosted deployments:** Running open-source models (Llama, Mistral) on organizational infrastructure.
- **Hybrid approaches:** Using different models for different use cases based on cost, latency, or capability requirements.

Key considerations:

- **Model selection:** Choosing the appropriate model for the task (capability vs. cost trade-off).
- **Version pinning:** Ensuring consistent behavior by specifying exact model versions.
- **Fallback strategies:** Handling provider outages or rate limits gracefully.
- **Cost optimization:** Routing simpler queries to smaller, cheaper models.

### 3.10 Fine-tuning (Optional)

**Purpose:** Customize foundation model behavior through additional training.

Fine-tuning is not always necessary—prompt engineering and RAG often suffice. However, fine-tuning is valuable when:

- **Consistent style is required:** The model must always respond in a specific tone or format.
- **Domain expertise is needed:** The task requires specialized knowledge not well-represented in pre-training.
- **Latency constraints exist:** A smaller fine-tuned model can outperform a larger prompted model.
- **Cost optimization is critical:** Fine-tuning can reduce prompt length and thus token costs.

Modern fine-tuning approaches:

- **LoRA (Low-Rank Adaptation):** Trains small adapter layers while keeping base weights frozen.
- **QLoRA:** Combines LoRA with quantization for memory-efficient fine-tuning.
- **PEFT (Parameter-Efficient Fine-Tuning):** A family of techniques that update only a small subset of parameters.

Fine-tuning outputs are stored in the Model Registry alongside prompt versions.

### 3.11 LLM Monitoring

**Purpose:** Observe system behavior in production.

LLM monitoring extends traditional model monitoring with new metrics:

**Quality metrics:**

- **Hallucination rate:** The percentage of responses containing fabricated information.
- **Factuality score:** The proportion of claims that can be verified against source documents.
- **Relevance:** How well responses address the user's actual question.
- **Coherence:** The logical consistency and readability of responses.

**Performance metrics:**

- **Time-to-first-token (TTFT):** The latency before the model begins generating output.
- **Tokens per second:** The generation speed once output begins.
- **End-to-end latency:** Total time from request to complete response.
- **Retrieval latency:** Time spent in vector search.

**Cost metrics:**

- **Input tokens per request:** The context size being sent to the model.
- **Output tokens per request:** The response length being generated.
- **Cost per request:** The dollar amount spent on each interaction.
- **Cost per user/application:** Aggregated spending by consumer.

**Safety metrics:**

- **Guardrail trigger rate:** How often input or output filters activate.
- **Policy violation rate:** Frequency of content policy breaches.
- **PII exposure incidents:** Occurrences of sensitive data in outputs.

This answers:

➡ *Is the system performing safely, correctly, and economically?*

### 3.12 Feedback and Triggers

**Purpose:** Close the loop between production behavior and system improvement.

Triggers initiate updates based on:

- **Quality degradation:** Hallucination rate or relevance scores fall below thresholds.
- **Retrieval quality drop:** Retrieved documents become less relevant to queries.
- **Cost overrun:** Token usage exceeds budgets.
- **New knowledge:** Documents are added that should be indexed.
- **Guardrail patterns:** Repeated triggers suggest prompt or policy adjustments needed.
- **User feedback:** Explicit signals (thumbs up/down) or implicit signals (follow-up questions).

Triggered actions include:

- **Prompt refinement:** Adjusting instructions based on failure patterns.
- **RAG retuning:** Modifying chunk size, overlap, or retrieval parameters.
- **Index updates:** Adding, updating, or removing documents from the Vector Store.
- **Guardrail adjustment:** Tightening or loosening filters based on trigger patterns.
- **Model routing changes:** Shifting traffic between models based on performance.

This closes the loop.

## 4. The LLMOps Maturity Model

Organizations adopt LLMOps practices incrementally. This maturity model provides a framework for assessment and improvement.

### Level 0: Manual / Ad-hoc

**Characteristics:**

- Prompts are hardcoded in application source code.
- No version control for prompts or RAG configurations.
- Vector indices are built once and never updated.
- No guardrails or only basic string matching.
- Evaluation through manual testing ("looks good to me").
- No cost tracking; token usage is unknown.
- No audit trail of LLM interactions.

**Symptoms:**

- "The prompt worked yesterday, what changed?"
- "How much did we spend on Claude last month?" → "No idea."
- "Can you show me why the system gave this answer?" → "Not possible."

### Level 1: Pipeline Automation

**Characteristics:**

- Prompt Registry with version control.
- Automated Vector Store index updates (scheduled or event-driven).
- Basic guardrails: PII detection, toxicity filtering.
- Structured evaluation with golden test datasets.
- Cost monitoring with alerts and budgets.
- Human-in-the-loop for critical decisions.
- Basic logging of inputs and outputs.

**Indicators:**

- Can roll back to any previous prompt version.
- Know token usage per application and user.
- Can reproduce any past interaction.
- Guardrails catch obvious violations.

### Level 2: Full CI/CD + Governance

**Characteristics:**

- Prompt CI/CD: changes pass through review, testing, and staged rollout.
- A/B testing for prompts: measure impact before full deployment.
- Continuous RAG optimization: automatic reindexing, parameter tuning.
- Adaptive guardrails: feedback loops adjust sensitivity.
- Automated hallucination detection: citation verification, fact-checking.
- Cost optimization: caching, model routing, context compression.
- Full audit trail: complete lineage from query to response.
- Compliance-ready: meets EU AI Act and organizational policy requirements.

**Indicators:**

- "This prompt increased accuracy by 3%" (measured via A/B test).
- Hallucination rate is tracked and trending downward.
- Cost per request is decreasing through optimization.
- Can explain any decision to auditors.

### Maturity Assessment

| Dimension | Level 0 | Level 1 | Level 2 |
|-----------|---------|---------|---------|
| Prompt Management | Hardcoded | Registry | CI/CD + A/B |
| RAG Pipeline | Manual | Automated refresh | Continuous optimization |
| Guardrails | None/Ad-hoc | Basic filters | Adaptive + monitored |
| Evaluation | Manual | Test suites | Automated + continuous |
| Cost Management | Unknown | Monitored | Optimized |
| Governance | None | Logging | Full audit + compliance |

## 5. Governance and Compliance

### 5.1 Regulatory Context

The EU AI Act classifies foundation models as requiring specific transparency and accountability measures. Organizations using LLMs must:

- **Document model selection:** Justify why a particular foundation model was chosen.
- **Disclose AI usage:** Inform users when they are interacting with an AI system.
- **Maintain audit trails:** Record interactions for review and accountability.
- **Implement human oversight:** Ensure humans can intervene in high-stakes decisions.
- **Monitor for bias and harm:** Continuously evaluate system behavior for fairness and safety.

### 5.2 Governance Components

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| **Prompt Auditing** | Track prompt changes and their effects | Version control, change logs, approval workflows |
| **Interaction Logging** | Archive all inputs and outputs | Structured logs with retention policies |
| **Guardrails-as-Code** | Codified safety policies | Policy files, automated enforcement, testing |
| **Cost Allocation** | Attribute costs to business units | Tagging, chargeback, budget enforcement |
| **Lineage Tracking** | End-to-end traceability | Query → retrieval → prompt → response chain |

### 5.3 Key Questions Governance Must Answer

- ➡ *What prompt was used for this interaction?*
- ➡ *What documents were retrieved and why?*
- ➡ *What guardrails were applied?*
- ➡ *Who approved this prompt for production?*
- ➡ *How much did this interaction cost?*

## 6. Why This Is Not Traditional MLOps

A common misconception is that LLMOps is simply MLOps with larger models. In reality, the architecture is fundamentally different for several reasons:

**The model is not the artifact.**

In traditional MLOps, the trained model is the primary deliverable. In LLMOps, the foundation model is a shared resource—the artifacts are prompts, RAG configurations, and guardrails. This changes what is versioned, tested, and deployed.

**Training is optional.**

Most LLMOps systems never train a model. They configure and orchestrate pre-trained models. Fine-tuning, when used, produces lightweight adapters rather than full model weights.

**Context is the feature.**

Traditional ML uses engineered features derived from structured data. LLMOps uses retrieved documents as context. The quality of retrieval—not feature engineering—determines system performance.

**Hallucination is a unique failure mode.**

Traditional models can be inaccurate, but they do not fabricate. LLMs can generate confident, detailed, and completely false statements. This requires entirely new monitoring and mitigation approaches.

**Cost scales with usage, not infrastructure.**

Traditional ML costs are dominated by training compute and inference hardware. LLM costs are dominated by tokens. Optimizing an LLM system means reducing tokens, not reducing compute.

**Key properties of LLMOps architecture:**

| Property | Description |
|----------|-------------|
| **Prompt-centric** | Behavior is controlled by instructions, not weights |
| **Retrieval-augmented** | External knowledge grounds responses in facts |
| **Guardrail-protected** | Safety is enforced at input and output boundaries |
| **Token-economic** | Cost optimization focuses on context efficiency |
| **Continuously monitored** | Hallucination and quality tracking are always active |

## 7. Key Takeaways

1. **LLMOps extends MLOps, it does not replace it.** Organizations need both disciplines. Traditional ML remains appropriate for many tasks. LLMOps addresses the unique requirements of foundation model deployment.

2. **Prompts require the same rigor as models.** Version control, testing, staged deployment, and rollback capabilities are essential. Treat the Prompt Registry with the same seriousness as the Model Registry.

3. **Retrieval quality is paramount.** A well-designed RAG pipeline with high-quality retrieval will outperform a poorly designed one with a more capable model. Invest in chunking, embedding, and index quality.

4. **Guardrails are not optional.** Production LLM systems without guardrails are liabilities. Hallucination detection, PII protection, and content filtering must be implemented before deployment.

5. **Monitor tokens, not just latency.** Cost visibility is essential. Track token usage by application, user, and request type. Set budgets and alerts. Optimize aggressively.

6. **Plan for governance from the start.** Audit trails, interaction logging, and prompt versioning are easier to implement at the beginning than to retrofit later. Regulatory requirements are intensifying.

## 8. Conclusion

LLMOps represents the maturation of Large Language Model deployment from experimental demos to production-grade systems. It builds on the foundations of MLOps while introducing new components, new artifacts, and new operational concerns.

The architecture presented here is not theoretical—it corresponds to real tools and practices:

- **Vector Stores:** Pinecone, Weaviate, OpenSearch, pgvector
- **Orchestration:** LangChain, LlamaIndex, Semantic Kernel
- **Guardrails:** Bedrock Guardrails, NeMo Guardrails, Guardrails AI
- **Foundation Models:** AWS Bedrock, Azure OpenAI, Anthropic API
- **Monitoring:** LangSmith, Weights & Biases, custom dashboards

However, tools alone do not create a successful LLMOps practice. The architecture must be accompanied by:

- **Organizational alignment:** Prompt engineers, ML engineers, and platform teams must share a common understanding of the system.
- **Cultural commitment:** Testing, guardrails, and monitoring must be valued, not treated as obstacles to shipping.
- **Iterative adoption:** Start with basic prompt versioning and guardrails, then expand to full CI/CD and optimization.

The ultimate goal is a system where deploying a new prompt is routine, not risky—where hallucinations are detected and prevented automatically, where costs are visible and controlled, and where the entire team can focus on improving user experience rather than fighting production fires.

This is what production LLM deployment looks like. This is LLMOps.

---

## Further Resources

This repository contains additional materials for learning and teaching LLMOps:

### For Students

- **[Case Study: MLOps vs LLMOps](./case-study-mlops-llmops.md)** — A hands-on comparative analysis assignment where you analyze a company migrating from traditional ML to LLM-based document intelligence. Includes architecture comparison, cost analysis, governance assessment, and migration planning.

### For Instructors

- **[Case Study: Expanded Sections](./case-study-expanded-sections.md)** — Complete answer key and detailed explanations for all case study sections. Includes sample answers, grading guidance, and discussion points.

### For Researchers

- **[Research Paper Outline](./research-paper-mlops-to-llmops.md)** — Full academic paper structure following Design Science Research methodology. Ready for development into a publication for venues like IEEE Software, ICSE SEIP, or MLSys.

### Architecture Diagrams

All diagrams are available in both PNG and SVG formats in the [diagrams/](./diagrams/) directory:

| Diagram | Description |
|---------|-------------|
| [mlops-architecture.png](./diagrams/mlops-architecture.png) | Traditional MLOps pipeline |
| [llmops-architecture.png](./diagrams/llmops-architecture.png) | LLMOps pipeline with RAG |
| [mlops-vs-llmops-comparison.png](./diagrams/mlops-vs-llmops-comparison.png) | Side-by-side comparison |
| [llmops-reference-architecture.png](./diagrams/llmops-reference-architecture.png) | Six-layer reference architecture |

### External References

- [MLOps Lifecycle](https://github.com/oriolrius/data-platform-ops/blob/main/mlops-lifecycle.md) — The companion document explaining traditional MLOps architecture in the same style as this document.
