import streamlit as st
from google import genai
import random

# ---------------------------------------------------------
# MILESTONE 1 & 2: SETUP & CONFIGURATION
# ---------------------------------------------------------

# 🔴 REPLACE WITH YOUR NEW API KEY
API_KEY = "AIzaSyBnQULMueUYSofEEKsl77o-m4OW9-ymBfA"

# Configure the Client (Modern equivalent of Activity 2.2)
try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"Setup Error: {e}")

# Activity 2.3: Configure the model generation settings (Source 67)
# We pass these directly during generation in the new library
generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# ---------------------------------------------------------
# MILESTONE 3: JOKE GENERATION (Source 79)
# ---------------------------------------------------------

def get_joke():
    """Selects and returns a random programming joke."""
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do Python programmers prefer using snake_case? Because it's easier to read!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
        "Why did the programmer get kicked out of the beach? Because he kept using the 'C' language!",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)

# ---------------------------------------------------------
# MILESTONE 4: RECIPE GENERATION (Source 84)
# ---------------------------------------------------------

def recipe_generation(user_input, word_count):
    """
    Function to generate a blog based on user input and word count.
    """
    # Display a message while the blog is being generated
    st.info("### 🕒 Generating your recipe...")
    st.write(f"While I work on creating your blog, here's a little joke to keep you entertained:\n\n**{get_joke()}**")
    
    try:
        # Prompt logic from Source 84
        prompt = f"Write a recipe based on the input topic: {user_input} and number of words: {word_count}\n"
        
        # Using Gemini 1.5 Flash as requested in Source 23
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt,
            config=generation_config
        )
        
        st.success("🎉 Your recipe is ready!")
        return response.text
        
    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None

# ---------------------------------------------------------
# UI IMPLEMENTATION (Source 94)
# ---------------------------------------------------------

st.title("Flavour Fusion: AI-Driven Recipe Blogging")

# Inputs matching the Screenshot in Source 94
topic = st.text_input("Topic")
words = st.number_input("Number of words", min_value=100, max_value=2000, step=100, value=300)

if st.button("Generate recipe"):
    if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
        st.error("Please provide a valid API Key in the code.")
    elif topic:
        result = recipe_generation(topic, words)
        if result:
            st.markdown("### 📜 Recipe Blog:")
            st.write(result)
    else:
        st.warning("Please enter a topic")