#!/usr/bin/env python3
"""Generate LLMOps Architecture Diagram for Document Intelligence"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.ml import Sagemaker
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import StepFunctions
from diagrams.aws.security import Shield
from diagrams.aws.management import Cloudwatch
from diagrams.generic.storage import Storage
import os

os.chdir("/home/oriol/esade/research/diagrams")

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
}

with Diagram(
    "LLMOps Architecture - Document Intelligence",
    filename="llmops-architecture",
    show=False,
    direction="LR",
    outformat=["svg", "png"],
    graph_attr=graph_attr,
):
    docs = Storage("Documents\n(PDF)")

    with Cluster("AWS Cloud", graph_attr={"bgcolor": "#FFF8E6"}):

        with Cluster("Data Ingestion"):
            textract = Lambda("Textract\n(OCR)")
            chunking = Lambda("Chunking\nStrategy")

        with Cluster("Vector Pipeline", graph_attr={"bgcolor": "#FFE6B3"}):
            embedding = Sagemaker("Titan\nEmbeddings")
            vector_store = ElasticsearchService("OpenSearch\n(Vector Store)")

        with Cluster("RAG Pipeline", graph_attr={"bgcolor": "#FFD966"}):
            step_fn = StepFunctions("Step\nFunctions")
            prompt_registry = S3("Prompt\nRegistry")

        with Cluster("LLM Inference", graph_attr={"bgcolor": "#E6B800"}):
            bedrock = Sagemaker("Bedrock\n(Claude)")
            guardrails = Shield("Bedrock\nGuardrails")

        with Cluster("Observability"):
            cost_monitor = Cloudwatch("Cost &\nToken Monitor")
            quality = Cloudwatch("Quality\nMetrics")

    output = Storage("Intelligent\nResponse")

    # Main flow
    docs >> Edge(color="#B8860B", style="bold") >> textract
    textract >> Edge(color="#B8860B") >> chunking
    chunking >> Edge(color="#B8860B") >> embedding
    embedding >> Edge(color="#B8860B") >> vector_store

    # RAG flow
    vector_store >> Edge(color="#DAA520", label="retrieve") >> step_fn
    prompt_registry >> Edge(color="#DAA520", style="dashed") >> step_fn
    step_fn >> Edge(color="#DAA520", label="augmented\nprompt") >> bedrock
    bedrock >> Edge(color="#DAA520") >> guardrails
    guardrails >> Edge(color="#B8860B", style="bold") >> output

    # Monitoring
    bedrock >> Edge(color="#B85450", style="dashed") >> cost_monitor
    guardrails >> Edge(color="#B85450", style="dashed") >> quality

print("✅ Generated: llmops-architecture.svg")
