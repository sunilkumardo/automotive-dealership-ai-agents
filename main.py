# main.py
from agents.router_agent import router_agent
from agents.query_agent import query_agent
from agents.lead_agent import lead_agent

def handle_customer_message(message: str):
    """
    Main entry point for every customer message.
    Step 1: Router classifies intent
    Step 2: Correct agent handles it
    """
    print(f"\nCustomer: {message}")

    # Step 1 — classify intent
    intent = router_agent(message)
    print(f"Router classified as: [{intent}]")
    print("-" * 50)

    # Step 2 — route to correct agent
    if intent == "query":
        response = query_agent(message)
        print(f"Agent: {response}")

    elif intent == "lead":
        lead_data = lead_agent(message)
        print(f"Lead captured:")
        print(f"  Name          : {lead_data['name']}")
        print(f"  Budget        : {lead_data['budget']}")
        print(f"  Interested in : {lead_data['interested_model']}")
        print(f"  Lead quality  : {lead_data['lead_quality']}")
        print(f"  Response      : {lead_data['response']}")

    elif intent == "service":
        print("[SERVICE AGENT - coming soon]")

    print("=" * 50)

if __name__ == "__main__":
    print("Testing Multi-Agent System")
    print("=" * 50)

    test_messages = [
        "Hi I'm Rahul, looking for a car under 8 lakhs, interested in Swift or Baleno",
        "Tell me about the Maruti Suzuki Swift",
        "I need to book a service for my Brezza next Saturday"
    ]

    for message in test_messages:
        handle_customer_message(message)