import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Setup Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Language options
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "Chinese": "zh"
}

# App UI
st.set_page_config(page_title="Business Idea Assistant", layout="centered")
st.title("💡 Founders’ Forge")

industry = st.text_input("Enter an Industry (e.g. Arts, Finance, Retail):")
language_choice = st.selectbox("Select Language:", list(languages.keys()))
generate = st.button("✨ Brainstorm Now")

if generate:
    if not industry:
        st.warning("Please enter an industry.")
    else:
        st.info("Generating startup ideas...")

        # Prompt for Gemini
        prompt = f"""
Act as a business startup expert. Generate 5 unique startup ideas in the industry: {industry}.
For each idea, include the following:
- Name of the startup
- The problem it solves
- The solution
- Target user
- Why it's innovative

Translate the entire response to {language_choice}.
Make sure each idea is clearly separated.
"""

        try:
            response = model.generate_content(prompt)
            st.success("Here are your startup ideas:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error generating ideas: {e}")