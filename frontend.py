# Step1: Setup Streamlit
import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="SafeSpace - AI Therapist", page_icon="🧠", layout="centered")

st.title("🧠 SafeSpace")
st.subheader("Your Personal AI Mental Health Therapist")
st.write("Welcome! This is a safe space to share your thoughts and feelings. We are here to listen and support you.")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Step2: User is able to ask question
# Chat input
user_input = st.chat_input("What's on your mind today?")
if user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # AI Agent exists here
    response = requests.post(BACKEND_URL, json={"message": user_input})
    if response.status_code == 200:
        data = response.json()
        content = data.get("response", "I'm here to listen, but I'm having trouble understanding right now.")
        tool = data.get("tool_called", "None")
        if tool != "None":
            content += f"\n\n*(Used tool: {tool})*"
        st.session_state.chat_history.append({"role": "assistant", "content": content})
    else:
        st.session_state.chat_history.append({"role": "assistant", "content": "Sorry, I am having trouble connecting to my brain right now."})


# Step3: Show response from backend
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])