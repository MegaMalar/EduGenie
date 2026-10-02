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


def get_learning_recommendations(topic: str) -> str:
    """
    Generate a structured learning path for a topic.
    """

    prompt = f"""
You are EduGenie, a personalized learning assistant.

Create a learning path for:

{topic}

The student is a college beginner.

Include these sections:

1. Beginner Level
2. Intermediate Level
3. Advanced Level
4. Practice
5. Mini Projects
6. Recommended Resources
7. Suggested Timeline

Instructions:
- Use simple English.
- Make the plan practical.
- Start from the basics.
- Progress gradually.
- Give realistic learning steps.
- Use normal numbered points and hyphen bullets.
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
                "Sorry, I could not generate the learning path right now. "
                "Please try again in a few moments."
            )