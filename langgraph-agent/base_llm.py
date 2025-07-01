# Base LLM

import os
from dotenv import load_dotenv

# Best practice: Load environment variables from a .env file
load_dotenv()

# Securely get the API key from environment variables
# You must set this variable in your environment (e.g., in a .env file)
# The variable should be named GOOGLE_API_KEY
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please get your key from Google AI Studio.")

# 1. Import the correct class for Google Gemini
from langchain_google_genai import ChatGoogleGenerativeAI

# 2. Instantiate the Gemini model with the correct model name
llm = ChatGoogleGenerativeAI(
    google_api_key=google_api_key,
    model="gemini-2.5-flash",
    temperature=0
)