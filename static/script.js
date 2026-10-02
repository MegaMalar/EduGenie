// ========================================
// EduGenie Frontend JavaScript
// ========================================


// ========================================
// Helper Function
// ========================================

function showResult(elementId, content) {
    const element = document.getElementById(elementId);

    element.innerHTML = content;
    element.classList.add("show");
}


// ========================================
// Loading Message
// ========================================

function showLoading(elementId, message = "EduGenie is thinking...") {
    showResult(
        elementId,
        `<p>${message}</p>`
    );
}


// ========================================
// Q&A
// ========================================

document
    .getElementById("qaForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const question =
            document.getElementById("question").value.trim();

        if (!question) {
            return;
        }

        showLoading(
            "qaResult",
            "🤖 EduGenie is preparing your answer..."
        );

        try {

            const response = await fetch(
                `/qa?question=${encodeURIComponent(question)}`
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error || "Unable to get an answer."
                );
            }

            showResult(
                "qaResult",
                `
                <strong>Answer:</strong>

                <p>${escapeHTML(data.answer)}</p>
                `
            );

        } catch (error) {

            showResult(
                "qaResult",
                `<strong>Error:</strong> ${escapeHTML(error.message)}`
            );

        }
    });


// ========================================
// Explanation
// ========================================

document
    .getElementById("explainForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const topic =
            document.getElementById("topic").value.trim();

        if (!topic) {
            return;
        }

        showLoading(
            "explanationResult",
            "📚 EduGenie is creating a simple explanation..."
        );

        try {

            const response = await fetch(
                "/explain/",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        topic: topic
                    })
                }
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error || "Unable to generate explanation."
                );
            }

            showResult(
                "explanationResult",
                `
                <strong>Explanation:</strong>

                <p>${escapeHTML(data.explanation)}</p>
                `
            );

        } catch (error) {

            showResult(
                "explanationResult",
                `<strong>Error:</strong> ${escapeHTML(error.message)}`
            );

        }
    });


// ========================================
// Summary
// ========================================

document
    .getElementById("summaryForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const text =
            document.getElementById("summaryText").value.trim();

        if (!text) {
            return;
        }

        showLoading(
            "summaryResult",
            "📝 EduGenie is summarizing your text..."
        );

        try {

            const response = await fetch(
                "/summarize/",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        text: text
                    })
                }
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error || "Unable to summarize the text."
                );
            }

            showResult(
                "summaryResult",
                `
                <strong>Summary:</strong>

                <p>${escapeHTML(data.summary)}</p>
                `
            );

        } catch (error) {

            showResult(
                "summaryResult",
                `<strong>Error:</strong> ${escapeHTML(error.message)}`
            );

        }
    });


// ========================================
// Quiz
// ========================================

document
    .getElementById("quizForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const text =
            document.getElementById("quizText").value.trim();

        if (!text) {
            return;
        }

        showLoading(
            "quizResult",
            "🧠 EduGenie is generating your quiz..."
        );

        try {

            const response = await fetch(
                "/quiz",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        text: text
                    })
                }
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error || "Unable to generate quiz."
                );
            }

            displayQuiz(data.quiz);

        } catch (error) {

            showResult(
                "quizResult",
                `<strong>Error:</strong> ${escapeHTML(error.message)}`
            );

        }
    });


// ========================================
// Display Quiz
// ========================================

function displayQuiz(quiz) {

    const result = document.getElementById("quizResult");

    result.innerHTML = "";

    result.classList.add("show");

    if (!Array.isArray(quiz) || quiz.length === 0) {

        result.innerHTML =
            "<p>Unable to generate quiz questions.</p>";

        return;
    }

    quiz.forEach(function (item, index) {

        if (item.error) {

            result.innerHTML += `
                <div class="quiz-question">
                    <strong>${escapeHTML(item.error)}</strong>
                </div>
            `;

            return;
        }

        let optionsHTML = "";

        if (Array.isArray(item.options)) {

            item.options.forEach(function (option) {

                optionsHTML += `
                    <div class="quiz-option">
                        ${escapeHTML(option)}
                    </div>
                `;

            });

        }

        result.innerHTML += `
            <div class="quiz-question">

                <h3>
                    Question ${index + 1}
                </h3>

                <p>
                    <strong>
                        ${escapeHTML(item.question)}
                    </strong>
                </p>

                <div>
                    ${optionsHTML}
                </div>

                <div class="quiz-answer">
                    Correct Answer:
                    ${escapeHTML(item.answer)}
                </div>

                <p>
                    <strong>Explanation:</strong>
                    ${escapeHTML(item.explanation)}
                </p>

            </div>
        `;

    });
}


// ========================================
// Learning Path
// ========================================

document
    .getElementById("learningForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const topic =
            document
                .getElementById("learningTopic")
                .value
                .trim();

        if (!topic) {
            return;
        }

        showLoading(
            "learningResult",
            "🗺️ EduGenie is creating your learning path..."
        );

        try {

            const response = await fetch(
                `/learn/recommendations?topic=${encodeURIComponent(topic)}`
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.error ||
                    "Unable to create learning path."
                );
            }

            showResult(
                "learningResult",
                `
                <strong>Personalized Learning Path:</strong>

                <p>${escapeHTML(data.recommendation)}</p>
                `
            );

        } catch (error) {

            showResult(
                "learningResult",
                `<strong>Error:</strong> ${escapeHTML(error.message)}`
            );

        }
    });


// ========================================
// HTML Escape Function
// ========================================

function escapeHTML(value) {

    if (value === null || value === undefined) {
        return "";
    }

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}