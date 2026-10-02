# EduGenie – Google Gemini Powered Learning Assistant

EduGenie is an AI-powered learning assistant designed to help students understand topics, summarize study material, generate quizzes, and create personalized learning paths.

## Features

### 🤖 Ask EduGenie

Ask questions on academic or general learning topics and receive simple, student-friendly answers.

### 📖 Simple Explanation

Enter a difficult topic and get an easy-to-understand explanation with examples.

### 📝 Text Summarization

Convert long study material into concise and useful summaries.

### 🧠 Quiz Generator

Generate multiple-choice questions from a given topic or study material.

### 🛣️ Personalized Learning Path

Get a structured learning plan from beginner to advanced level, including practice and project suggestions.

## Technologies Used

* Python
* FastAPI
* Google Gemini API
* Google GenAI Python SDK
* LaMini-Flan-T5
* Hugging Face Transformers
* HTML
* CSS
* JavaScript
* Jinja2
* Uvicorn

## Project Structure

```text
EduGenie/
│
├── main.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── learning_path.py
├── summary_module.py
├── response_cleaner.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── venv/
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/EduGenie.git
cd EduGenie
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Do not upload the `.env` file to GitHub.

### 6. Start the application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/
```

## API Documentation

EduGenie provides interactive API documentation through FastAPI.

After starting the application, open:

```text
http://127.0.0.1:8000/docs
```

## Main API Endpoints

| Endpoint                 | Method | Purpose                  |
| ------------------------ | ------ | ------------------------ |
| `/`                      | GET    | EduGenie web interface   |
| `/qa`                    | GET    | Ask questions            |
| `/explain/`              | POST   | Explain a topic          |
| `/summarize/`            | POST   | Summarize text           |
| `/quiz`                  | POST   | Generate a quiz          |
| `/learn/recommendations` | GET    | Generate a learning path |
| `/health`                | GET    | Check backend status     |

## Project Goal

EduGenie aims to make AI-assisted learning simple, accessible, and useful for students by combining question answering, explanations, summarization, quiz generation, and personalized learning recommendations in one platform.

## Future Improvements

* User authentication
* Learning progress tracking
* Student profiles
* Saved quizzes and summaries
* Voice-based interaction
* PDF and document support
* Deployment to a cloud platform
* Personalized recommendations based on learning history

## Author

**Mega Malar M**

BE Computer Science and Engineering Student

## License

This project is created for educational and project-development purposes.
