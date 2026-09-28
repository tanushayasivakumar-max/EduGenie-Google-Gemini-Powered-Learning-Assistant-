```python
from gemini_client import generate_text


def get_learning_recommendations(
    topic: str
) -> str:

    prompt = f"""
Create a personalized learning path for:

{topic}

Assume the learner is a beginner unless
another level is clearly specified.

Include:

1. Learning goal
2. Beginner concepts
3. Intermediate concepts
4. Advanced concepts
5. Suggested weekly progression
6. Practice exercises
7. Mini-project ideas
8. Recommended resource types
9. Final project idea

The learning path should move step-by-step
from beginner to advanced.

Use simple language.

Do not invent specific URLs.
"""

    return generate_text(prompt)
```
