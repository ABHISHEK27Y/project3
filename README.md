# 🧠 MindfulAI - AI Mental Health Therapist

MindfulAI is an AI-powered mental health therapist designed to provide empathetic, evidence-based guidance in a conversational tone. Built with a responsive Streamlit frontend and a robust FastAPI backend, the agent leverages advanced language models to offer a safe, supportive environment for users.

## 🚀 Features

- **Empathetic Conversations**: Powered by MedGemma (via Ollama) and GPT-4, the AI provides emotionally attuned and practical support.
- **Emergency Action**: Integrated with Twilio to automatically place an emergency call if a user expresses a crisis or suicidal ideation.
- **Therapist Locator**: Automatically recommends nearby licensed therapists when professional help is requested.
- **Modern UI**: A clean, accessible chat interface built with Streamlit for a seamless user experience.

## 🛠️ Tech Stack

- **Frontend**: Streamlit, Python
- **Backend**: FastAPI, Uvicorn
- **AI / Agent Framework**: LangChain, LangGraph, OpenAI GPT-4, Ollama (MedGemma:4b)
- **External Services**: Twilio API (for emergency calling)

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ABHISHEK27Y/project3.git
   cd project3
   ```

2. **Environment Variables**:
   Create a `.env` file in the `backend` directory and add your API keys:
   ```env
   TWILIO_ACCOUNT_SID=your_sid
   TWILIO_AUTH_TOKEN=your_token
   TWILIO_FROM_NUMBER=your_twilio_number
   EMERGENCY_CONTACT=emergency_number
   OPENAI_API_KEY=your_openai_key
   ```

3. **Run the Backend**:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

4. **Run the Frontend**:
   Open a new terminal and run:
   ```bash
   streamlit run frontend.py
   ```

## 🎯 How it Works

1. The user interacts with the Streamlit UI, sending their thoughts or concerns.
2. The FastAPI backend receives the request and processes it using the LangGraph agent.
3. The agent dynamically decides which tool to use based on the user's input:
   - `ask_mental_health_specialist`: For general therapeutic guidance.
   - `emergency_call_tool`: To trigger Twilio if a crisis is detected.
   - `find_nearby_therapists_by_location`: To provide local therapist contacts.
4. The response is sent back to the frontend, indicating which tool was utilized.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

---
*Disclaimer: This is an AI tool and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.*
