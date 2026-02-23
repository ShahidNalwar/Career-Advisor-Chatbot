import streamlit as st
from backend.chatbot import CareerAdvisorBot
from backend.config import Config

# Page settings
st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon="🎓",
    layout="centered"
)

# Initialize backend bot in session state
if "bot" not in st.session_state:
    st.session_state.bot = CareerAdvisorBot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Sidebar ---
with st.sidebar:
    st.title("🎓 Career Advisor AI")
    st.markdown("""
    **Popular Topics:**
    - Data Science Internship prep
    - Python & Java roadmaps
    - Aptitude & logical reasoning tips
    - Resume building for freshers
    """)

    if st.button("🗑️ Clear Conversation"):
        st.session_state.bot.reset()
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("Powered by Google Gemini 2.5 Flash")

# --- Main UI ---
st.title("🎓 Career Advisor Chatbot")
st.write("Welcome! Ask me anything about tech careers, internships, or skill building.")

# Render previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input
user_input = st.chat_input("E.g., How do I prepare for a tech internship?")

if user_input:
    # Render user message instantly
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Fetch and render AI response with STREAMING
    with st.chat_message("assistant"):
        # We call our new chat_stream function
        stream = st.session_state.bot.chat_stream(user_input)
        
        # st.write_stream automatically handles the typewriter effect!
        # It also returns the final combined string when it finishes.
        response = st.write_stream(stream)

    # Save the final combined response to session state history
    st.session_state.messages.append({"role": "assistant", "content": response})