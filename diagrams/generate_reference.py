#!/usr/bin/env python3
"""Generate LLMOps Reference Architecture - Layered View"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.ml import Sagemaker
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda, EKS, EC2
from diagrams.aws.integration import StepFunctions, Appsync
from diagrams.aws.security import Shield
from diagrams.aws.management import Cloudtrail
from diagrams.aws.management import Cloudwatch
from diagrams.aws.devtools import Codepipeline
from diagrams.aws.network import APIGateway
from diagrams.generic.device import Mobile
from diagrams.generic.compute import Rack
from diagrams.onprem.client import User
import os

os.chdir("/home/oriol/esade/research/diagrams")

graph_attr = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.8",
    "splines": "ortho",
    "ranksep": "1.0",
}

with Diagram(
    "LLMOps Reference Architecture",
    filename="llmops-reference-architecture",
    show=False,
    direction="TB",
    outformat=["svg", "png"],
    graph_attr=graph_attr,
):
    users = User("Users")

    with Cluster("APPLICATION LAYER", graph_attr={"bgcolor": "#E8F4E8", "fontcolor": "#2E7D32"}):
        api = APIGateway("API Gateway")
        chat = Lambda("Chat\nInterface")
        search = Lambda("Semantic\nSearch")
        agents = Lambda("AI\nAgents")

    with Cluster("ORCHESTRATION LAYER", graph_attr={"bgcolor": "#E3F2FD", "fontcolor": "#1565C0"}):
        step_fn = StepFunctions("Step\nFunctions")
        langchain = Lambda("LangChain /\nLlamaIndex")
        bedrock_agents = Sagemaker("Bedrock\nAgents")

    with Cluster("GOVERNANCE LAYER", graph_attr={"bgcolor": "#FFEBEE", "fontcolor": "#C62828"}):
        guardrails = Shield("Bedrock\nGuardrails")
        audit = Cloudtrail("Audit\nLogs")
        cost = Cloudwatch("Cost\nControls")
        policies = S3("Policy\nRegistry")

    with Cluster("MODEL LAYER", graph_attr={"bgcolor": "#FFF3E0", "fontcolor": "#E65100"}):
        bedrock = Sagemaker("Bedrock\n(Claude, Llama)")
        embeddings = Sagemaker("Titan\nEmbeddings")
        finetuned = Sagemaker("Fine-tuned\nAdapters")

    with Cluster("DATA LAYER", graph_attr={"bgcolor": "#F3E5F5", "fontcolor": "#7B1FA2"}):
        vector_store = ElasticsearchService("OpenSearch\n(Vectors)")
        knowledge = S3("Knowledge\nBases")
        docs = S3("Document\nStore")

    with Cluster("INFRASTRUCTURE LAYER", graph_attr={"bgcolor": "#ECEFF1", "fontcolor": "#37474F"}):
        eks = EKS("EKS\nCluster")
        ec2 = EC2("GPU\nInstances")
        cicd = Codepipeline("CI/CD\nPipeline")
        monitoring = Cloudwatch("Observability")

    # Connections between layers
    users >> Edge(color="#2E7D32") >> api
    api >> Edge(color="#2E7D32") >> [chat, search, agents]

    chat >> Edge(color="#1565C0") >> step_fn
    search >> Edge(color="#1565C0") >> langchain
    agents >> Edge(color="#1565C0") >> bedrock_agents

    step_fn >> Edge(color="#C62828") >> guardrails
    langchain >> Edge(color="#C62828") >> guardrails
    bedrock_agents >> Edge(color="#C62828") >> guardrails
    guardrails >> Edge(color="#C62828", style="dashed") >> audit
    guardrails >> Edge(color="#C62828", style="dashed") >> cost

    guardrails >> Edge(color="#E65100") >> bedrock
    guardrails >> Edge(color="#E65100") >> embeddings

    bedrock >> Edge(color="#7B1FA2") >> vector_store
    embeddings >> Edge(color="#7B1FA2") >> vector_store
    vector_store >> Edge(color="#7B1FA2", style="dashed") >> knowledge
    knowledge >> Edge(color="#7B1FA2", style="dashed") >> docs

    vector_store >> Edge(color="#37474F", style="dashed") >> eks
    eks >> Edge(color="#37474F", style="dashed") >> ec2
    cicd >> Edge(color="#37474F", style="dashed") >> monitoring

print("✅ Generated: llmops-reference-architecture.svg")
