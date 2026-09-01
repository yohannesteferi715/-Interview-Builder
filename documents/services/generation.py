from django.db import transaction

from .llm import generate_response
from .parser import parse_questions
from .prompts import build_question_prompt
from .retrieval import retrieve_chunks

from ..models import (
    Question,
    QuestionSource,
)


def build_context(points):

    context_parts = []

    for index, point in enumerate(points):

        payload = point.payload or {}

        text = payload.get(
            "text",
            "",
        )

        if not text:
            continue

        document_id = payload.get(
            "document_id"
        )

        filename = payload.get(
            "filename",
            "Unknown document",
        )

        page = payload.get(
            "page"
        )

        chunk_index = payload.get(
            "chunk_index"
        )

        context_parts.append(
            f"""
SOURCE {index + 1}

Document ID:
{document_id}

Document:
{filename}

Page:
{page}

Chunk:
{chunk_index}

Content:
{text}
"""
        )

    return "\n".join(context_parts)

