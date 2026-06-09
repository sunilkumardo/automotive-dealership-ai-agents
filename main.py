# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from agents.router_agent import router_agent
from agents.query_agent import query_agent
from agents.lead_agent import lead_agent
from agents.service_agent import service_agent

# Initialize FastAPI app
app = FastAPI(
    title="Automotive Dealership AI Agent System",
    description="Multi-agent AI chatbot for automotive dealerships",
    version="1.0.0"
)

# CORS middleware — allows frontend HTML/JS to call this API
# Without this, browser blocks requests from frontend to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Request model — defines what JSON the frontend sends
class ChatRequest(BaseModel):
    message: str

# Response model — defines what JSON we send back
class ChatResponse(BaseModel):
    intent: str
    response: str
    data: dict = {}

@app.get("/")
def root():
    """Health check endpoint"""
    return {"status": "running", "system": "Automotive Dealership AI Agents"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Main chat endpoint.
    Receives customer message, routes to correct agent, returns response.
    
    This is the single entry point for the entire multi-agent system.
    Frontend calls POST /chat with a message.
    Backend returns intent + response + structured data.
    """

    message = request.message.strip()

    if not message:
        return ChatResponse(
            intent="error",
            response="Please enter a message.",
            data={}
        )

    # Step 1 — classify intent
    intent = router_agent(message)

    # Step 2 — route to correct agent
    if intent == "query":
        response_text = query_agent(message)
        return ChatResponse(
            intent=intent,
            response=response_text,
            data={}
        )

    elif intent == "lead":
        lead_data = lead_agent(message)
        return ChatResponse(
            intent=intent,
            response=lead_data.get("response", ""),
            data={
                "name": lead_data.get("name"),
                "budget": lead_data.get("budget"),
                "interested_model": lead_data.get("interested_model"),
                "lead_quality": lead_data.get("lead_quality")
            }
        )

    elif intent == "service":
        service_data = service_agent(message)
        return ChatResponse(
            intent=intent,
            response=service_data.get("confirmation", ""),
            data={
                "customer_name": service_data.get("customer_name"),
                "car_model": service_data.get("car_model"),
                "service_type": service_data.get("service_type"),
                "preferred_date": service_data.get("preferred_date"),
                "urgency": service_data.get("urgency")
            }
        )

    else:
        return ChatResponse(
            intent="unknown",
            response="I didn't understand that. Could you rephrase?",
            data={}
        )