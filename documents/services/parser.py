import re


def parse_questions(response):

    pattern = re.compile(
        r"QUESTION\s+\d+:\s*(.*?)"
        r"\s*ANSWER:\s*(.*?)"
        r"\s*EXPLANATION:\s*(.*?)"
        r"(?=\s*QUESTION\s+\d+:|$)",
        re.DOTALL | re.IGNORECASE,
    )

    matches = pattern.findall(response)

    questions = []

    for question, answer, explanation in matches:

        question = question.strip()
        answer = answer.strip()
        explanation = explanation.strip()

        if not question or not answer:
            continue

        questions.append(
            {
                "question": question,
                "answer": answer,
                "explanation": explanation,
            }
        )

    return questions