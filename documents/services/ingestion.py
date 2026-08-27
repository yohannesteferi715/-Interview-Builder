from .pdf import extract_pdf_pages
from .chunking import chunk_pages
from .qdrant import store_chunks


def ingest_document(document):

    document.status = "processing"

    document.error_message = ""

    document.save(
        update_fields=[
            "status",
            "error_message",
            "updated_at",
        ]
    )

    try:

        # 1. Extract PDF text
        pages = extract_pdf_pages(
            document.file.path
        )

        if not pages:
            raise ValueError(
                "No extractable text found in PDF."
            )

        # 2. Split text into chunks
        chunks = chunk_pages(pages)

        if not chunks:
            raise ValueError(
                "No chunks were created."
            )  

        # 3. Generate embeddings
        # 4. Store vectors in Qdrant
        store_chunks(
            chunks=chunks,
            document_id=document.id,
            filename=document.file.name,
        )

        document.status = "completed"

        document.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

    except Exception as error:

        document.status = "failed"

        document.error_message = str(error)

        document.save(
            update_fields=[
                "status",
                "error_message",
                "updated_at",
            ]
        )

        raise