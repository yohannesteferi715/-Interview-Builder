import os

from huggingface_hub import InferenceClient


LLM_MODEL = os.environ.get(
    "HF_LLM_MODEL",
    "meta-llama/Llama-3.1-8B-Instruct",
)


def get_llm_client():

    return InferenceClient(
        api_key=os.environ["HF_TOKEN"]
    )


def generate_response(prompt):

    client = get_llm_client()

    response = client.chat_completion(
        model=LLM_MODEL,

        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert technical interviewer "
                    "and technical educator."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],

        temperature=0.3,

        max_tokens=5000,
    )

    return response.choices[0].message.content