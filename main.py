# main.py
from agents.router_agent import router_agent
from agents.query_agent import query_agent

def handle_customer_message(message: str):
    """
    Main entry point for every customer message.
    Step 1: Router classifies intent
    Step 2: Correct agent handles it
    """
    print(f"\nCustomer: {message}")
    
    # Step 1 — classify intent
    intent = router_agent(message)
    print(f"Router classified as: {intent}")
    
    # Step 2 — route to correct agent
    if intent == "query":
        response = query_agent(message)
    elif intent == "lead":
        response = f"[LEAD AGENT - coming soon] Handling: {message}"
    elif intent == "service":
        response = f"[SERVICE AGENT - coming soon] Handling: {message}"
    
    print(f"Agent response: {response}")
    print("-" * 50)

if __name__ == "__main__":
    print("Testing Multi-Agent Router System")
    print("=" * 50)
    
    # Test all three intents
    test_messages = [
        "Tell me about the Maruti Suzuki Swift",
        "I want to buy a car under 10 lakhs",
        "I need to book a service for my Brezza next Saturday"
    ]
    
    for message in test_messages:
        handle_customer_message(message)