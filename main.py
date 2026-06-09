# main.py
from agents.router_agent import router_agent
from agents.query_agent import query_agent
from agents.lead_agent import lead_agent
from agents.service_agent import service_agent

def handle_customer_message(message: str):
    """
    Main entry point for every customer message.
    Step 1: Router classifies intent
    Step 2: Correct agent handles it
    """
    print(f"\nCustomer: {message}")

    intent = router_agent(message)
    print(f"Router classified as: [{intent}]")
    print("-" * 50)

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
        service_data = service_agent(message)
        print(f"Service booking captured:")
        print(f"  Customer      : {service_data['customer_name']}")
        print(f"  Car model     : {service_data['car_model']}")
        print(f"  Service type  : {service_data['service_type']}")
        print(f"  Preferred date: {service_data['preferred_date']}")
        print(f"  Urgency       : {service_data['urgency']}")
        print(f"  Confirmation  : {service_data['confirmation']}")

    print("=" * 50)

if __name__ == "__main__":
    print("Testing Complete Multi-Agent System")
    print("=" * 50)

    test_messages = [
        "Hi I'm Rahul, looking for a car under 8 lakhs, interested in Swift or Baleno",
        "Tell me about the Maruti Suzuki Swift",
        "I need to book a service for my Brezza next Saturday",
        "My car is making a strange noise, need urgent repair",
    ]

    for message in test_messages:
        handle_customer_message(message)