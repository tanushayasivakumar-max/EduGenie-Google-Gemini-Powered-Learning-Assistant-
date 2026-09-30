from gemini_client import generate_text


def answer_question(question: str) -> str:

    prompt = f"""
Answer the student's question below.

QUESTION:
{question}

Instructions:

1. Answer the question directly.
2. Use simple language.
3. Explain difficult terms.
4. Add a simple example when useful.
5. Keep the answer concise but useful.
6. If the question is ambiguous, clearly state your assumption.
"""

    return generate_text(prompt)
