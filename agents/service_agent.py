# agents/service_agent.py

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

def service_agent(customer_message: str) -> dict:
    """
    Handles service and repair booking requests.

    Returns structured dict with:
    - customer_name, car_model, service_type
    - preferred_date, urgency
    - confirmation (what to say back to customer)

    Structured output allows this data to feed
    directly into a service scheduling system.
    """

    system_prompt = load_prompt("prompts/service_prompt.txt")
    full_prompt = f"{system_prompt}\n\nCustomer message: {customer_message}"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=full_prompt
    )

    raw_text = response.text.strip()

    # Output validation — same pattern as lead agent
    try:
        if "```json" in raw_text:
            raw_text = raw_text.split("```json")[1].split("```")[0].strip()
        elif "```" in raw_text:
            raw_text = raw_text.split("```")[1].split("```")[0].strip()

        service_data = json.loads(raw_text)

        # Validate required fields
        required_fields = ["customer_name", "car_model", "service_type",
                          "preferred_date", "urgency", "confirmation"]
        for field in required_fields:
            if field not in service_data:
                service_data[field] = "unknown"

        return service_data

    except json.JSONDecodeError:
        return {
            "customer_name": "unknown",
            "car_model": "not specified",
            "service_type": "general service",
            "preferred_date": "not specified",
            "urgency": "normal",
            "confirmation": raw_text
        }