import re


def clean_ai_response(text: str) -> str:
    """
    Remove unnecessary Markdown formatting from AI responses
    while keeping the actual content readable.
    """

    if not text:
        return ""

    text = str(text)

    # Remove Markdown headings
    text = re.sub(r"^\s*#{1,6}\s*", "", text, flags=re.MULTILINE)

    # Convert unordered Markdown bullets to normal hyphen bullets
    text = re.sub(r"^\s*[\*\+]\s+", "- ", text, flags=re.MULTILINE)

    # Remove bold formatting
    text = text.replace("**", "")

    # Remove italic Markdown markers
    text = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"\1", text)

    # Remove inline code backticks
    text = text.replace("`", "")

    # Remove Markdown horizontal lines
    text = re.sub(r"^\s*[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)

    # Remove spaces at the beginning/end of lines
    lines = [line.strip() for line in text.splitlines()]

    # Remove empty lines at beginning and end
    while lines and not lines[0]:
        lines.pop(0)

    while lines and not lines[-1]:
        lines.pop()

    return "\n".join(lines).strip()