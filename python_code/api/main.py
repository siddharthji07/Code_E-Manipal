from agent_controller import AgentController
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import uvicorn

app = FastAPI(title="Coffee Shop Customer Service Chatbot API",
             description="API for interacting with the coffee shop customer service chatbot",
             version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Initialize the agent controller
agent_controller = AgentController()

@app.post("/chat")
async def chat(messages: List[Dict[str, str]]):
    try:
        # Format the input as expected by agent_controller
        input_data = {"input": {"messages": messages}}
        response = agent_controller.get_response(input_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()