# AI Mental Health Therapist

SafeSpace is an AI-powered companion for emotional support. It listens, responds with empathy, and knows when to escalate to real help — combining a conversational agent with practical tools like emergency calling and therapist lookup.

It's built with an agentic architecture using LangGraph and LangChain, a healthcare-focused LLM (MedGemma, run through Ollama), a FastAPI backend, and a Streamlit chat interface on top.

**Disclaimer:** This is a learning project and is not a replacement for professional mental health care. If you or someone you know is in crisis, please reach out to a licensed professional or local emergency services.

## Features

- Conversational chat interface built with Streamlit
- An AI agent (LangGraph) that decides when to use which tool
- Healthcare-tuned responses via MedGemma
- Emergency call escalation through Twilio
- Location-aware lookup for therapists/professional support
- FastAPI backend connecting the frontend and the agent

## Architecture

```
User (Streamlit) → FastAPI Backend → AI Agent (LangGraph + LLM)
                                        ├── Emergency Call Tool (Twilio)
                                        ├── Ask Expert Tool (MedGemma)
                                        └── Find Therapists Tool
```

## Getting Started

### Prerequisites
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) for dependency management
- [Ollama](https://ollama.com/) installed locally (for MedGemma)
- A Twilio account (for the emergency call feature)

### Setup

1. Clone the repo
   ```bash
   git clone https://github.com/apoorvayadav/safespace-ai-therapist.git
   cd safespace-ai-therapist
   ```

2. Install dependencies
   ```bash
   uv sync
   ```
   This sets up a virtual environment and installs everything from `uv.lock`.

3. Add your environment variables

   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_key_here
   TWILIO_ACCOUNT_SID=your_sid_here
   TWILIO_AUTH_TOKEN=your_token_here
   TWILIO_PHONE_NUMBER=your_twilio_number
   ```

4. Run the backend
   ```bash
   uv run uvicorn backend.main:app --reload
   ```

5. Run the frontend
   ```bash
   uv run streamlit run frontend.py
   ```

## Project Structure

```
safespace-ai-therapist/
├── backend/           # FastAPI app + AI agent logic
├── frontend.py        # Streamlit chat UI
├── main.py            # Entry point
├── pyproject.toml     # Project dependencies
├── uv.lock             # Locked dependency versions
└── README.md
```

## Tech Stack

| Layer                | Tools |
|-----------------------|-------|
| Frontend               | Streamlit |
| Backend                | FastAPI |
| Agent / Orchestration | LangGraph, LangChain |
| LLMs                   | MedGemma (Ollama), OpenAI |
| Tools                  | Twilio (calls), location services |

## Contributing

Contributions and issues are welcome — feel free to open a PR or start a discussion.

## License

This project is open source under the MIT License.

## Author

Apoorva Yadav
