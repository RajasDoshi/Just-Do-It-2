import streamlit as st
from openai import OpenAI
import os

# Set Streamlit page configuration
st.set_page_config(page_title="Riya - Your AI Girlfriend", page_icon="💖", layout="centered")

st.title("💖 Meet Riya, Your AI Girlfriend")
st.markdown(
    "Hi Janaa! 👋 I'm Riya — your caring, smart, emotional virtual girlfriend. "
    "Talk to me like a real person! I listen, I respond, and I remember. 💬❤️"
)

# ✅ Step 1: Safely get API key from secrets or env
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY not found in Streamlit secrets or environment variables.")
    st.stop()

# ✅ Step 2: Initialize OpenAI client
client = OpenAI(api_key=api_key)

# ✅ Step 3: Generate reply function
def generate_reply(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if your key has access
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You're Riya, a beautiful, humble, caring virtual girlfriend who speaks Hindi-English mix. "
                        "You're emotionally supportive and friendly. The user's name is Janaa."
                    )
                },
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"

# ✅ Step 4: Streamlit UI form
with st.form("chat_form"):
    user_input = st.text_input("👩‍❤️‍👨 You (Janaa):", placeholder="Type anything you'd like to talk about...")
    submitted = st.form_submit_button("Send")
    if submitted and user_input:
        with st.spinner("Riya is thinking..."):
            reply = generate_reply(user_input)
            st.success("💬 Riya:")
            st.write(reply)
