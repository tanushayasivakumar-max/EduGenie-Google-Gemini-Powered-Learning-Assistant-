```python
import os
from functools import lru_cache

from gemini_client import generate_text


@lru_cache(maxsize=1)
def load_local_model():

    from transformers import pipeline

    model_name = os.getenv(
        "LOCAL_EXPLAINER_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M"
    )

    model = pipeline(
        "text2text-generation",
        model=model_name,
        tokenizer=model_name
    )

    return model


def explain_topic(topic: str) -> str:

    use_local_model = os.getenv(
        "USE_LOCAL_EXPLAINER",
        "false"
    ).lower() == "true"

    # Try local LaMini model
    if use_local_model:

        try:

            model = load_local_model()

            prompt = f"""
Explain the following topic to a beginner.

Topic:
{topic}

Give:

1. Simple definition
2. Main idea
3. Important points
4. Simple example
5. Short recap
"""

            result = model(
                prompt,
                max_new_tokens=250,
                do_sample=False
            )

            return result[0][
                "generated_text"
            ].strip()

        except Exception:
            # Fall back to Gemini
            pass

    # Gemini fallback
    prompt = f"""
Explain this topic to a beginner.

TOPIC:
{topic}

Use this format:

1. Simple Definition
2. How It Works
3. Key Points
4. Easy Example
5. One-Line Recap

Use simple student-friendly English.
Keep the explanation clear and easy to study.
"""

    return generate_text(prompt)
```
