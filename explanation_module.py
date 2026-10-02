from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from response_cleaner import clean_ai_response


MODEL_NAME = "MBZUAI/LaMini-Flan-T5-783M"

print("Loading LaMini model...")

explain_tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

explain_model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)

print("LaMini model loaded successfully.")


def explain_topic(topic: str) -> str:
    """
    Generate a simple explanation of a topic.
    """

    prompt = f"""
Explain the following topic to a beginner college student.

Topic:
{topic}

Requirements:
- Use simple English.
- Start with a clear definition.
- Explain the main idea.
- Give a simple example.
- Mention important points.
- Keep the explanation easy to understand.
- Avoid complicated words when possible.
- Do not use Markdown.
- Do not use # symbols.
- Do not use * symbols.
"""

    inputs = explain_tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = explain_model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.7,
        do_sample=True
    )

    result = explain_tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return clean_ai_response(result)