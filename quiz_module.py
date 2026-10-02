import json
import os
import re

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is not set. Please check your .env file."
    )

client = genai.Client(api_key=api_key)

PRIMARY_MODEL = "gemini-3.8-flash"
FALLBACK_MODEL = "gemini-3.5-flash-lite"


def clean_json_response(text: str) -> str:
    """
    Remove Markdown code fences from a JSON response.
    """

    text = text.strip()

    text = re.sub(
        r"^```json\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^```\s*",
        "",
        text
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    return text.strip()


def generate_quiz(text: str) -> list:
    """
    Generate exactly 3 multiple-choice questions.
    """

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create exactly 3 multiple-choice questions based on the following content.

Content:
{text}

Each question must have:
- question
- options
- answer
- explanation

The options must contain exactly 4 choices.

Return ONLY valid JSON.

Use this exact format:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Correct option",
    "explanation": "Short explanation"
  }}
]

Important:
- Create exactly 3 questions.
- Make the questions educational.
- Use simple English.
- Do not add Markdown.
- Do not add ``` symbols.
"""

    try:
        chat = client.chats.create(
            model=PRIMARY_MODEL
        )

        response = chat.send_message(
            message=prompt
        )

        raw_response = clean_json_response(
            response.text
        )

        quiz = json.loads(raw_response)

        return quiz

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

            raw_response = clean_json_response(
                response.text
            )

            quiz = json.loads(raw_response)

            return quiz

        except Exception as fallback_error:
            print("Fallback Gemini model error:", fallback_error)

            return [
                {
                    "question": "Unable to generate the quiz right now.",
                    "options": [
                        "Try again",
                        "Wait and retry",
                        "Check the connection",
                        "All of the above"
                    ],
                    "answer": "All of the above",
                    "explanation": "Please try again after a short time."
                }
            ]