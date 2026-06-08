# agents/lead_agent.py

from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def load_prompt(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()

def lead_agent(customer_message: str) -> dict:
    """
    Handles customers interested in buying a car.
    
    Returns structured dict with:
    - name, budget, interested_model, lead_quality
    - response (what to say back to customer)
    
    Why dict and not string?
    In production this data goes to CRM database.
    Structured data is more useful than raw text.
    """

    system_prompt = load_prompt("prompts/lead_prompt.txt")
    full_prompt = f"{system_prompt}\n\nCustomer message: {customer_message}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    raw_text = response.text.strip()

    # Output validation — parse JSON safely
    # LLMs sometimes wrap JSON in ```json ``` blocks — we clean that
    try:
        # Remove markdown code blocks if present
        if "```json" in raw_text:
            raw_text = raw_text.split("```json")[1].split("```")[0].strip()
        elif "```" in raw_text:
            raw_text = raw_text.split("```")[1].split("```")[0].strip()

        lead_data = json.loads(raw_text)

        # Validate required fields exist
        required_fields = ["name", "budget", "interested_model", "lead_quality", "response"]
        for field in required_fields:
            if field not in lead_data:
                lead_data[field] = "unknown"

        return lead_data

    except json.JSONDecodeError:
        # Fallback if JSON parsing fails
        return {
            "name": "unknown",
            "budget": "unknown",
            "interested_model": "unknown",
            "lead_quality": "cold",
            "response": raw_text
        }