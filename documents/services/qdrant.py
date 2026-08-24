import os
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from .embeddings import generate_embedding


VECTOR_SIZE = 384


def get_qdrant_client():

    return QdrantClient(
        url=os.environ["QDRANT_URL"],
        api_key=os.environ["QDRANT_API_KEY"],
    )


def get_collection_name():

    return os.environ.get(
        "QDRANT_COLLECTION",
        "interview_documents",
    )


def ensure_collection():

    client = get_qdrant_client()

    collection_name = get_collection_name()

    collections = client.get_collections()

    exists = any(
        collection.name == collection_name
        for collection in collections.collections
    )

    if not exists:

        client.create_collection(
            collection_name=collection_name,

            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )
        
        
def store_chunks(
    chunks,
    document_id,
    filename,
):

    client = get_qdrant_client()

    collection_name = get_collection_name()

    ensure_collection()

    points = []

    for chunk in chunks:

        vector = generate_embedding(
            chunk["text"]
        )

        point = PointStruct(
            id=str(uuid.uuid4()),

            vector=vector,

            payload={
                "document_id": document_id,
                "filename": filename,
                "page": chunk["page"],
                "chunk_index": chunk["chunk_index"],
                "text": chunk["text"],
            },
        )

        points.append(point)

    if points:

        client.upsert(
            collection_name=collection_name,
            points=points,
        )