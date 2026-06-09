# agents/router_agent.py

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def load_prompt(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()

def router_agent(customer_message: str) -> str:
    """
    Classifies customer message intent.
    Returns exactly one of: 'lead', 'service', 'query'
    
    This is intent classification — a core AI agent pattern.
    The router never talks to the customer directly.
    It only decides which specialist agent should handle the message.
    """

    system_prompt = load_prompt("prompts/router_prompt.txt")

    full_prompt = f"{system_prompt}\n\nCustomer message: {customer_message}"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=full_prompt
    )

    # Clean the response — remove whitespace, lowercase
    # LLMs sometimes return "Lead" or " query " — we normalize it
    intent = response.text.strip().lower()

    # Output validation — if LLM returns unexpected value, default to query
    valid_intents = ["lead", "service", "query"]
    if intent not in valid_intents:
        intent = "query"

    return intent