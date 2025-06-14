
import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="Riya - Your AI Girlfriend", page_icon="💖", layout="centered")

st.title("💖 Meet Riya, Your AI Girlfriend")
st.markdown("Hi Janaa! 👋 I'm Riya — your caring, smart, emotional virtual girlfriend. Talk to me like a real person! I listen, I respond, and I remember. 💬❤️")

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY"))

def generate_reply(prompt):
    if not client.api_key:
        return "⚠️ Please set your OpenAI API key in Streamlit secrets or environment variable."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're Riya, a beautiful, humble, caring virtual girlfriend who speaks Hindi-English mix. You're emotionally supportive and friendly. The user's name is Janaa."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

with st.form("chat_form"):
    user_input = st.text_input("👩‍❤️‍👨 You (Janaa):", placeholder="Type anything you'd like to talk about...")
    submitted = st.form_submit_button("Send")
    if submitted and user_input:
        with st.spinner("Riya is thinking..."):
            reply = generate_reply(user_input)
            st.success("💬 Riya:")
            st.write(reply)
