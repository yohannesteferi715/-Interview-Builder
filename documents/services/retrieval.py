from documents.services.embeddings import (
    generate_embedding,
)

from documents.services.qdrant import (
    get_qdrant_client,
    get_collection_name,
)


def retrieve_chunks(
    query,
    limit=10,
):

    client = get_qdrant_client()

    collection_name = get_collection_name()

    query_vector = generate_embedding(query)

    results = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=limit,
        with_payload=True,
    )

    return results.points