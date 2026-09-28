````python
import json

from pydantic import BaseModel, Field

from gemini_client import generate_json


# --------------------------------
# Data Models
# --------------------------------

class QuizQuestion(BaseModel):

    question: str

    options: list[str] = Field(
        min_length=4,
        max_length=4
    )

    correct_answer: int = Field(
        ge=0,
        le=3
    )

    explanation: str


class QuizResponse(BaseModel):

    questions: list[QuizQuestion] = Field(
        min_length=3,
        max_length=3
    )


# --------------------------------
# Gemini JSON Schema
# --------------------------------

QUIZ_SCHEMA = {

    "type": "object",

    "properties": {

        "questions": {

            "type": "array",

            "minItems": 3,

            "maxItems": 3,

            "items": {

                "type": "object",

                "properties": {

                    "question": {
                        "type": "string"
                    },

                    "options": {

                        "type": "array",

                        "minItems": 4,

                        "maxItems": 4,

                        "items": {
                            "type": "string"
                        }
                    },

                    "correct_answer": {

                        "type": "integer",

                        "minimum": 0,

                        "maximum": 3
                    },

                    "explanation": {

                        "type": "string"
                    }
                },

                "required": [
                    "question",
                    "options",
                    "correct_answer",
                    "explanation"
                ]
            }
        }
    },

    "required": [
        "questions"
    ]
}


# --------------------------------
# Remove Markdown Code Blocks
# --------------------------------

def clean_json_block(text: str) -> str:

    text = text.strip()

    if text.startswith("```"):

        lines = text.splitlines()

        if lines:
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        text = "\n".join(
            lines
        ).strip()

        if text.lower().startswith("json"):
            text = text[4:].strip()

    return text


# --------------------------------
# Generate Quiz
# --------------------------------

def generate_quiz(
    passage: str
) -> dict:

    prompt = f"""
Create exactly 3 multiple-choice questions
from the educational passage below.

PASSAGE:
{passage}

Rules:

1. Create exactly 3 questions.
2. Every question must have exactly 4 options.
3. Options must be plausible.
4. Questions must be based on the supplied passage.
5. correct_answer must be the zero-based option index.
6. correct_answer must therefore be 0, 1, 2 or 3.
7. Give a short explanation for every answer.
"""

    raw_response = generate_json(
        prompt,
        QUIZ_SCHEMA
    )

    cleaned_response = clean_json_block(
        raw_response
    )

    data = json.loads(
        cleaned_response
    )

    validated = QuizResponse.model_validate(
        data
    )

    return validated.model_dump()
````
