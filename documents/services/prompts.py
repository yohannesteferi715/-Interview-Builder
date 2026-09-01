def build_question_prompt(
    topic,
    difficulty,
    question_type,
    number_of_questions,
    context,
):

    return f"""
You are an expert technical interviewer.

Generate interview questions using ONLY the
provided source material.

INTERVIEW REQUIREMENTS
======================

Topic:
{topic}

Difficulty:
{difficulty}

Question type:
{question_type}

Number of questions:
{number_of_questions}


SOURCE MATERIAL
===============

{context}


INSTRUCTIONS
============

Generate exactly {number_of_questions} interview questions.

Every question MUST be answerable from the provided
source material.

For every question provide:

1. The interview question.
2. A technically correct answer.
3. A clear explanation.

Do not use information that is not contained
in the source material.

Questions should test understanding rather than
simply asking the user to repeat a sentence.

Return ONLY the following format:

QUESTION 1:
<question>

ANSWER:
<answer>

EXPLANATION:
<explanation>


QUESTION 2:
<question>

ANSWER:
<answer>

EXPLANATION:
<explanation>


Continue until exactly {number_of_questions}
questions have been generated.

Do not include introductions.
Do not include conclusions.
""" 