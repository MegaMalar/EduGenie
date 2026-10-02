import os

from dotenv import load_dotenv
from google import genai

from response_cleaner import clean_ai_response


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is not set. Please check your .env file."
    )

client = genai.Client(api_key=api_key)

PRIMARY_MODEL = "gemini-3.8-flash"
FALLBACK_MODEL = "gemini-3.5-flash-lite"


def ask_gemini(prompt: str) -> str:
    """
    Send a prompt to Gemini.
    Uses the primary model first and fallback model if needed.
    """

    try:
        chat = client.chats.create(model=PRIMARY_MODEL)

        response = chat.send_message(
            message=prompt
        )

        return clean_ai_response(response.text)

    except Exception as primary_error:
        print("Primary Gemini model error:", primary_error)
        print("Trying fallback model...")

        try:
            chat = client.chats.create(model=FALLBACK_MODEL)

            response = chat.send_message(
                message=prompt
            )

            return clean_ai_response(response.text)

        except Exception as fallback_error:
            print("Fallback Gemini model error:", fallback_error)

            return (
                "Sorry, I could not generate an answer right now. "
                "Please try again in a few moments."
            )


def answer_question_with_gemini(question: str) -> str:
    """
    Generate a simple and student-friendly answer.
    """

    prompt = f"""
You are EduGenie, a friendly AI learning assistant for college students.

Answer the student's question clearly and accurately.

Question:
{question}

Instructions:
- Use simple English.
- Explain the concept in a beginner-friendly way.
- Give a short example when useful.
- Keep the answer reasonably concise.
- Use plain text.
- Do not use Markdown headings.
- Do not use # symbols.
- Do not use * symbols.
- Do not use ** formatting.
- Use simple numbered points or hyphen bullets when needed.
"""

    return ask_gemini(prompt)