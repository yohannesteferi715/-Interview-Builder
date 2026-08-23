import os

from huggingface_hub import InferenceClient


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def get_hf_client():

    return InferenceClient(
        api_key=os.environ["HF_TOKEN"]
    )


def generate_embedding(text):

    client = get_hf_client()

    embedding = client.feature_extraction(
        text,
        model=EMBEDDING_MODEL,
    )

    return embedding.tolist()