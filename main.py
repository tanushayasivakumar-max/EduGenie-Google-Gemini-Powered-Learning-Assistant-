```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

# Load environment variables from .env
load_dotenv()

# Create FastAPI application
app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# HTML templates
templates = Jinja2Templates(directory="templates")


# -----------------------------
# Request Models
# -----------------------------

class QARequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=10000
    )


class ExplainRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=1,
        max_length=10000
    )


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=30000
    )


# -----------------------------
# Home Page
# -----------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "application": "EduGenie"
    }


# -----------------------------
# Q&A Endpoint
# -----------------------------

@app.post("/qa")
async def qa(request: QARequest):

    try:
        answer = answer_question(
            request.question
        )

        return {
            "answer": answer
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# -----------------------------
# Explanation Endpoint
# -----------------------------

@app.post("/explain")
async def explain(request: ExplainRequest):

    try:

        explanation = explain_topic(
            request.topic
        )

        return {
            "explanation": explanation
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# -----------------------------
# Quiz Endpoint
# -----------------------------

@app.post("/quiz")
async def quiz(request: TextRequest):

    try:

        result = generate_quiz(
            request.text
        )

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# -----------------------------
# Summary Endpoint
# -----------------------------

@app.post("/summarize")
async def summarize(request: TextRequest):

    try:

        summary = summarize_text(
            request.text
        )

        return {
            "summary": summary
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# -----------------------------
# Learning Path Endpoint
# -----------------------------

@app.post("/learn/recommendations")
async def learning_recommendations(
    request: TextRequest
):

    try:

        learning_path = get_learning_recommendations(
            request.text
        )

        return {
            "learning_path": learning_path
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
```
