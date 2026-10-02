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


def summarize_with_gemini(text: str) -> str:
    """
    Generate a concise summary using Gemini.
    """

    prompt = f"""
You are EduGenie, an educational AI assistant.

Summarize the following text for a college student.

Text:
{text}

Instructions:
- Keep the important information.
- Remove unnecessary details.
- Use simple English.
- Make the summary easy to read.
- Use short paragraphs or simple hyphen bullets when useful.
- Do not use Markdown headings.
- Do not use # symbols.
- Do not use * symbols.
- Do not use ** formatting.
"""

    try:
        chat = client.chats.create(
            model=PRIMARY_MODEL
        )

        response = chat.send_message(
            message=prompt
        )

        return clean_ai_response(response.text)

    except Exception as primary_error:
        print("Primary Gemini model error:", primary_error)
        print("Trying fallback model...")

        try:
            chat = client.chats.create(
                model=FALLBACK_MODEL
            )

            response = chat.send_message(
                message=prompt
            )

            return clean_ai_response(response.text)

        except Exception as fallback_error:
            print("Fallback Gemini model error:", fallback_error)

            return (
                "Sorry, I could not summarize the text right now. "
                "Please try again in a few moments."
            )


def summarize_text(text: str) -> str:
    """
    Public function used by main.py.
    """

    return summarize_with_gemini(text)