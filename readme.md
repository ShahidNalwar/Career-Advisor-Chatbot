# 🎓 Production-Ready AI Career Advisor Chatbot

🚀 **Live Cloud Deployment:** [http://51.20.86.199:8501/](http://51.20.86.199:8501/)

## 📌 Project Overview
This project is a domain-specific, production-ready chatbot powered by the Google Gemini 2.5 Flash API. It acts as an expert Career Advisor, providing structured, actionable guidance for students and job seekers in the tech industry. The application is built with a clean, modular backend and deployed on an AWS EC2 Ubuntu instance, adhering to real-world AI engineering standards.

## ✨ Key Features
* **Domain-Specific AI:** Engineered with strict system prompts to focus strictly on career advice, technical assessments, and resume building.
* **Multi-Turn Memory:** Implements token-optimized session memory to maintain conversational context across multiple interactions.
* **Streaming Responses:** Utilizes Python generators to stream AI responses to the UI in real-time (typewriter effect).
* **Clean Architecture:** Strict separation of concerns between the Streamlit UI, API handling, memory management, and prompt engineering.
* **Secure & Scalable:** API credentials secured via environment variables; deployed as a continuous background process on AWS.

## 🏗️ System Architecture
The application follows a modular, layered architecture:
`User Input → Streamlit UI → Chatbot Core Module → Prompt Engine + Memory → Gemini API → Response Stream → UI`

* **`app.py`**: The frontend UI layer built with Streamlit.
* **`backend/config.py`**: Centralized configuration and environment variable management.
* **`backend/gemini_client.py`**: A robust API wrapper with fallback model selection and error handling.
* **`backend/prompts.py`**: Centralized prompt engineering and role-definition module.
* **`backend/memory.py`**: Context management with built-in token optimization limits.

## ⚙️ Tech Stack
* **Language:** Python 3
* **Frontend:** Streamlit
* **AI Engine:** Google GenAI SDK (Gemini 2.5 Flash)
* **Environment Management:** python-dotenv
* **Cloud Infrastructure:** AWS EC2 (Ubuntu 24.04 LTS), tmux/nohup for background execution

## 🚀 Local Setup Instructions
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/career-advisor-chatbot.git](https://github.com/YOUR_USERNAME/career-advisor-chatbot.git)
   cd career-advisor-chatbot
