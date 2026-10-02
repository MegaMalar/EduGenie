from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import answer_question_with_gemini
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations


# =========================================
# EduGenie FastAPI Application
# =========================================

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# =========================================
# Templates
# =========================================

templates = Jinja2Templates(
    directory="templates"
)


# =========================================
# Static Files
# =========================================

app.mount(
    "/static",
    StaticFiles(
        directory="static"
    ),
    name="static"
)


# =========================================
# Home Page
# =========================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# =========================================
# Q&A
# GET /qa?question=What is Python?
# =========================================

@app.get("/qa")
async def answer_question(
    question: str = Query(...)
):

    if not question.strip():

        return JSONResponse(
            content={
                "error": "Please provide a question."
            },
            status_code=400
        )

    answer = answer_question_with_gemini(
        question
    )

    return {
        "question": question,
        "answer": answer
    }


# =========================================
# Explanation
# POST /explain/
# =========================================

@app.post("/explain/")
async def explain_api(
    request: Request
):

    data = await request.json()

    topic = data.get(
        "topic",
        ""
    )

    if not topic.strip():

        return JSONResponse(
            content={
                "error": "Please provide a topic."
            },
            status_code=400
        )

    explanation = explain_topic(
        topic
    )

    return {
        "topic": topic,
        "explanation": explanation
    }


# =========================================
# Summarization
# POST /summarize/
# =========================================

@app.post("/summarize/")
async def summarize_api(
    request: Request
):

    data = await request.json()

    text = data.get(
        "text",
        ""
    )

    if not text.strip():

        return JSONResponse(
            content={
                "error": "Please provide text to summarize."
            },
            status_code=400
        )

    summary = summarize_text(
        text
    )

    return {
        "summary": summary
    }


# =========================================
# Quiz
# POST /quiz
# =========================================

@app.post("/quiz")
async def quiz_api(
    request: Request
):

    data = await request.json()

    text = data.get(
        "text",
        ""
    )

    if not text.strip():

        return JSONResponse(
            content={
                "error": "Please provide text for quiz generation."
            },
            status_code=400
        )

    quiz = generate_quiz(
        text
    )

    return {
        "quiz": quiz
    }


# =========================================
# Learning Path
# GET /learn/recommendations?topic=Python
# =========================================

@app.get("/learn/recommendations")
async def learning_recommendation_api(
    topic: str = Query(...)
):

    if not topic.strip():

        return JSONResponse(
            content={
                "error": "Please provide a topic."
            },
            status_code=400
        )

    recommendation = get_learning_recommendations(
        topic
    )

    return {
        "topic": topic,
        "recommendation": recommendation
    }


# =========================================
# Health Check
# GET /health
# =========================================

@app.get("/health")
async def health_check():

    return {
        "status": "online",
        "application": "EduGenie",
        "message": "Backend is running successfully"
    }