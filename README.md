# LLM-Powered Code Review & Bug Detection System

An AI-powered static analysis tool that reviews source code and returns annotated bug reports, security vulnerability flags, performance suggestions, and corrected code snippets — all via a clean REST API.

**Live demo:** [llm-powered-code-review-and-bug-det.vercel.app](https://llm-powered-code-review-and-bug-det.vercel.app)

---

## What it does

Paste any Python code snippet and the system automatically:

- Detects bugs and logic errors
- Flags security vulnerabilities (e.g. SQL injection, hardcoded secrets, unsafe eval)
- Suggests performance optimisations
- Enforces coding best practices and style standards
- Explains *why* each issue is a problem
- Returns a corrected version of the code

---

## Architecture

```
User (Browser)
     │
     ▼
 Frontend (HTML/JS)
     │  HTTP POST /review
     ▼
 FastAPI Backend
     │  Groq API call
     ▼
 LLaMA-3 (via Groq)
     │
     ▼
 Structured JSON response
 (bugs, fixes, explanations)
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | LLaMA-3 via Groq API |
| Backend | Python, FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Vercel |
| Containerisation | Docker (local dev) |

---

## Local Setup

### Prerequisites
- Python 3.10+
- A free [Groq API key](https://console.groq.com)

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/sampurnamondal004/LLM-Powered-Code-Review-and-Bug-Detection-System.git
cd LLM-Powered-Code-Review-and-Bug-Detection-System

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
export GROQ_API_KEY=your_key_here

# 4. Start the backend
cd backend
uvicorn main:app --reload

# 5. Open the frontend
# Open frontend/index.html in your browser
```

---

## API Reference

### `POST /review`

Accepts source code and returns a structured review.

**Request body:**
```json
{
  "code": "def add(a, b):\n    return a - b"
}
```

**Response:**
```json
{
  "bugs": ["Line 2: subtraction used instead of addition"],
  "security_issues": [],
  "performance_suggestions": [],
  "best_practices": ["Add type hints for parameters"],
  "explanation": "The function is named 'add' but performs subtraction...",
  "corrected_code": "def add(a: int, b: int) -> int:\n    return a + b"
}
```

---

## Project Structure

```
├── backend/
│   └── main.py          # FastAPI app and /review endpoint
├── frontend/
│   └── index.html       # Single-page UI for code submission
├── requirements.txt     # Python dependencies
├── vercel.json          # Vercel deployment config
└── .gitignore
```

---

## Key Design Decisions

- **Groq over OpenAI** — Groq's inference speed is significantly faster for real-time code review, making the UX feel responsive rather than slow.
- **Structured prompt engineering** — The LLM is instructed to return responses in a consistent JSON schema, making the output reliably parseable.
- **Stateless REST design** — Each `/review` call is independent, making the service horizontally scalable with no session management overhead.

---

## Future Improvements

- [ ] Support for multiple languages (JavaScript, Java, C++)
- [ ] GitHub PR integration via webhook
- [ ] Severity scoring for each detected issue
- [ ] Rate limiting and API key authentication
- [ ] Batch file upload support

---

## Author

**Sampurna Mondal** — [github.com/sampurnamondal004](https://github.com/sampurnamondal004)

B.Tech CSE, IIIT Agartala | Summer Research Intern, IIT Guwahati (2024)
