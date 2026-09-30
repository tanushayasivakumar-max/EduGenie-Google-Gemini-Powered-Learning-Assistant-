from gemini_client import generate_text


def summarize_text(text: str) -> str:

    prompt = f"""
Summarize the following educational passage.

PASSAGE:
{text}

Requirements:

1. Keep the important information.
2. Remove unnecessary repetition.
3. Use simple language.
4. Make it useful for quick revision.
5. Include a short heading.
6. Use 5 to 8 bullet points.
7. Do not change the meaning of the original passage.
"""

    return generate_text(prompt)
