#!/usr/bin/env python3
"""Generate MLOps vs LLMOps Side-by-Side Comparison Diagram"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.ml import Sagemaker, SagemakerModel, SagemakerTrainingJob
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import StepFunctions
from diagrams.aws.security import Shield
from diagrams.generic.storage import Storage
import os

os.chdir("/home/oriol/esade/research/diagrams")

graph_attr = {
    "fontsize": "16",
    "bgcolor": "white",
    "pad": "0.8",
    "splines": "polyline",
    "ranksep": "0.8",
    "nodesep": "0.5",
}

with Diagram(
    "MLOps vs LLMOps - Architecture Comparison",
    filename="mlops-vs-llmops-comparison",
    show=False,
    direction="TB",
    outformat=["svg", "png"],
    graph_attr=graph_attr,
):
    # Shared input
    docs = Storage("Documents\n(PDF/Images)")

    with Cluster("Traditional MLOps Approach", graph_attr={"bgcolor": "#E6F3FF", "style": "rounded"}):

        with Cluster("Feature Pipeline"):
            ml_ocr = Lambda("OCR")
            ml_features = Lambda("TF-IDF\nFeatures")

        with Cluster("Model Pipeline"):
            ml_train = SagemakerTrainingJob("XGBoost\nTraining")
            ml_registry = SagemakerModel("Model\nRegistry")

        with Cluster("Serving"):
            ml_endpoint = Sagemaker("Endpoint")
            ml_monitor = Sagemaker("Drift\nMonitor")

        ml_output = Storage("Classification\n(12 categories)")

    with Cluster("LLMOps Approach", graph_attr={"bgcolor": "#FFF8E6", "style": "rounded"}):

        with Cluster("Vector Pipeline"):
            llm_ocr = Lambda("OCR")
            llm_chunk = Lambda("Chunking")
            llm_embed = Sagemaker("Embeddings")
            llm_vector = ElasticsearchService("Vector\nStore")

        with Cluster("RAG + LLM"):
            llm_prompts = S3("Prompt\nRegistry")
            llm_bedrock = Sagemaker("Claude\n(Bedrock)")
            llm_guard = Shield("Guardrails")

        llm_output = Storage("Q&A, Summary,\nClassification,\nExplanation")

    # MLOps flow
    docs >> Edge(color="#002E5D", style="bold") >> ml_ocr
    ml_ocr >> Edge(color="#002E5D") >> ml_features
    ml_features >> Edge(color="#002E5D") >> ml_train
    ml_train >> Edge(color="#002E5D") >> ml_registry
    ml_registry >> Edge(color="#002E5D") >> ml_endpoint
    ml_endpoint >> Edge(color="#002E5D", style="bold") >> ml_output
    ml_endpoint >> Edge(color="#B85450", style="dashed") >> ml_monitor
    ml_monitor >> Edge(color="#B85450", style="dashed", label="retrain") >> ml_train

    # LLMOps flow
    docs >> Edge(color="#B8860B", style="bold") >> llm_ocr
    llm_ocr >> Edge(color="#B8860B") >> llm_chunk
    llm_chunk >> Edge(color="#B8860B") >> llm_embed
    llm_embed >> Edge(color="#B8860B") >> llm_vector
    llm_vector >> Edge(color="#DAA520") >> llm_bedrock
    llm_prompts >> Edge(color="#DAA520", style="dashed") >> llm_bedrock
    llm_bedrock >> Edge(color="#DAA520") >> llm_guard
    llm_guard >> Edge(color="#B8860B", style="bold") >> llm_output

print("✅ Generated: mlops-vs-llmops-comparison.svg")
