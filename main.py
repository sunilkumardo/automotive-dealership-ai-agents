# main.py
from agents.query_agent import query_agent

if __name__ == "__main__":
    print("Testing Query Agent...")
    print("-" * 40)
    
    test_message = "Tell me about the Maruti Suzuki Swift"
    print(f"Customer: {test_message}")
    print(f"\nAgent: {query_agent(test_message)}")