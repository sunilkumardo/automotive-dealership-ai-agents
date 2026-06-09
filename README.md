# 🚗 Automotive Dealership AI Agent System

A multi-agent AI chatbot system built with Python and Google Gemini API that automates customer interactions for automotive dealerships.

![CI Pipeline](https://github.com/sunilkumardo/automotive-dealership-ai-agents/actions/workflows/ci.yml/badge.svg)

---

## 🎯 Problem Statement

Automotive dealerships lose potential customers because they cannot respond fast enough to every lead and service request. Salespeople are overwhelmed with repetitive queries about prices, features, and service bookings.

This system solves that using specialised AI agents that handle customer interactions 24/7 — automatically.

---

## 🏗️ System Architecture

```
Customer Message
        │
        ▼
  ┌─────────────┐
  │ Router Agent│ ◄── Intent Classification
  └─────────────┘
    │     │     │
    ▼     ▼     ▼
 Lead  Service Query
 Agent  Agent  Agent
    │     │     │
    └─────┼─────┘
          ▼
   ┌─────────────┐
   │FastAPI Back │
   └─────────────┘
          │
          ▼
   ┌─────────────┐
   │  Chat UI    │
   └─────────────┘
```

## 🤖 Agents

| Agent | Role | Output |
|---|---|---|
| **Router Agent** | Classifies customer intent | `lead` / `service` / `query` |
| **Lead Agent** | Handles car purchase inquiries | Structured JSON with name, budget, lead quality |
| **Service Agent** | Handles service bookings | Structured JSON with car model, date, urgency |
| **Query Agent** | Answers general questions | Natural language response |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| AI Agents | Python 3.12 |
| LLM API | Google Gemini 2.5 Flash |
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Testing | pytest |
| CI/CD | GitHub Actions |

---

## 📁 Project Structure

    automotive-dealership-ai-agents/
    ├── agents/
    │   ├── router_agent.py      # Intent classification
    │   ├── lead_agent.py        # Lead management
    │   ├── service_agent.py     # Service booking
    │   └── query_agent.py       # General queries
    ├── prompts/
    │   ├── router_prompt.txt
    │   ├── lead_prompt.txt
    │   ├── service_prompt.txt
    │   └── query_prompt.txt
    ├── frontend/
    │   ├── index.html
    │   ├── style.css
    │   └── app.js
    ├── tests/
    │   └── test_agents.py
    ├── .github/workflows/
    │   └── ci.yml
    ├── main.py
    └── requirements.txt


---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/sunilkumardo/automotive-dealership-ai-agents.git
cd automotive-dealership-ai-agents
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API key
```bash
cp .env.example .env
# Add your Gemini API key to .env file
# Get free key at: https://aistudio.google.com
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

### 6. Open the chat UI

http://127.0.0.1:8000/static/index.html

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

All 6 tests run without requiring an API key — testing agent logic and error handling independently.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/chat` | Send message, get AI response |
| GET | `/docs` | Interactive API documentation |

### Example Request
```json
POST /chat
{
  "message": "I want to buy a car under 8 lakhs"
}
```

### Example Response
```json
{
  "intent": "lead",
  "response": "Great! I can help you find the perfect car...",
  "data": {
    "name": "unknown",
    "budget": "8 lakhs",
    "interested_model": "not specified",
    "lead_quality": "warm"
  }
}
```

---

## 💡 Key Concepts Implemented

**Intent Classification** — Router agent classifies every message before routing to specialist agent.

**Structured Output** — Lead and service agents return JSON data designed to feed into CRM and scheduling systems.

**Prompt Engineering** — Each agent uses chain-of-thought prompting with few-shot examples and strict output schemas.

**Output Validation** — All agent responses validated before returning to customer. Malformed JSON falls back gracefully.

**CI/CD Pipeline** — GitHub Actions runs full test suite on every push automatically.

---

## 👨‍💻 Author

**Sunil Kumar D O**
B.E. Computer Science — New Horizon College of Engineering, Bengaluru (2026)

[![GitHub](https://img.shields.io/badge/GitHub-sunilkumardo-black?logo=github)](https://github.com/sunilkumardo)

---

## 📄 License

MIT License