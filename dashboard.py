import streamlit as st
from core.agent import Agent

# Set page configuration
st.set_page_config(page_title="Simulated AI Dashboard", layout="wide")

# Initialize agent (persistent session state)
if "agent" not in st.session_state:
    st.session_state.agent = Agent()

agent = st.session_state.agent

st.title("🧠 Simulated AI Agent Dashboard")

# Input panel
st.subheader("💬 Interact with the Agent")
user_input = st.text_input("Send a message to the AI agent:")

if st.button("Submit") and user_input:
    agent.perceive_and_remember(user_input)
    st.success("Experience submitted!")

# Emotion state visualization
st.subheader("📊 Emotional State")
emotion_state = agent.emotion.get_emotional_state()
st.bar_chart(emotion_state)

# Memory recall
st.subheader("🧾 Memory Log")
memories = agent.memory.get_memories()

for mem in reversed(memories[-10:]):  # Show last 10 memories
    tag = mem.get("emotional_tag", "none")
    st.markdown(f"- **{mem['text']}** *(tag: {tag})*")