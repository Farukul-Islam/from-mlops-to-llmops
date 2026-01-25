#!/usr/bin/env python3
"""Generate MLOps Architecture Diagram for Document Intelligence"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.ml import Sagemaker, SagemakerModel, SagemakerTrainingJob
from diagrams.aws.analytics import Glue
from diagrams.aws.storage import S3
from diagrams.aws.database import Dynamodb
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import StepFunctions
from diagrams.custom import Custom
from diagrams.onprem.client import User
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
import os

# Set output directory
os.chdir("/home/oriol/esade/research/diagrams")

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
}

node_attr = {
    "fontsize": "11",
}

with Diagram(
    "MLOps Architecture - Document Intelligence",
    filename="mlops-architecture",
    show=False,
    direction="LR",
    outformat=["svg", "png"],
    graph_attr=graph_attr,
    node_attr=node_attr,
):
    # Input
    docs = Storage("Documents\n(PDF)")

    with Cluster("AWS Cloud", graph_attr={"bgcolor": "#E6F3FF"}):

        with Cluster("Data Ingestion"):
            textract = Lambda("Textract\n(OCR)")

        with Cluster("Feature Engineering"):
            feature_extract = Lambda("TF-IDF\nExtraction")
            feature_store = Sagemaker("Feature\nStore")

        with Cluster("SageMaker Pipelines", graph_attr={"bgcolor": "#CCE5FF"}):
            training = SagemakerTrainingJob("XGBoost\nTraining")
            model_registry = SagemakerModel("Model\nRegistry")

        with Cluster("Inference"):
            endpoint = Sagemaker("SageMaker\nEndpoint")
            monitor = Sagemaker("Model\nMonitor")

    # Output
    output = Storage("Classification\nOutput")

    # Flow
    docs >> Edge(color="#002E5D", style="bold") >> textract
    textract >> Edge(color="#002E5D") >> feature_extract
    feature_extract >> Edge(color="#002E5D") >> feature_store
    feature_store >> Edge(color="#002E5D", style="dashed", label="training") >> training
    training >> Edge(color="#002E5D") >> model_registry
    model_registry >> Edge(color="#002E5D", label="deploy") >> endpoint
    feature_store >> Edge(color="#002E5D", label="inference") >> endpoint
    endpoint >> Edge(color="#002E5D", style="bold") >> output
    endpoint >> Edge(color="#B85450", style="dashed", label="metrics") >> monitor
    monitor >> Edge(color="#B85450", style="dashed", label="drift alert") >> training

print("✅ Generated: mlops-architecture.svg")
