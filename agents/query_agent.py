# agents/query_agent.py

from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read API key from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client (new SDK style)
client = genai.Client(api_key=GEMINI_API_KEY)

def load_prompt(filepath: str) -> str:
    """Load prompt text from file"""
    with open(filepath, "r") as f:
        return f.read()

def query_agent(customer_message: str) -> str:
    """
    Handles general customer queries about cars.
    Takes customer message, returns AI response.
    """

    # Load system prompt
    system_prompt = load_prompt("prompts/query_prompt.txt")

    # Build full prompt
    full_prompt = f"{system_prompt}\n\nCustomer message: {customer_message}"

    # Call Gemini API with latest model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    return response.text