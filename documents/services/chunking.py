from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_pages(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    chunks = []

    global_chunk_index = 0

    for page in pages:

        page_chunks = splitter.split_text(
            page["text"]
        )

        for chunk in page_chunks:

            chunks.append(
                {
                    "document_id": page["document_id"],
                    "text": chunk,
                    "page": page["page"],
                    "chunk_index": global_chunk_index,
                }
            )

            global_chunk_index += 1

    return chunks