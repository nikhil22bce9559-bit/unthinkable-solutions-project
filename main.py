import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # CORRECTED: The typo is fixed here
from groq import Groq  # Import the Groq library
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Groq client with your API key
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

class GoalRequest(BaseModel):
    goal: str
    timeline: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_master_prompt(goal, timeline):
    # This prompt is slightly tweaked for open-source models like Llama 3
    return f"""
    You are an expert AI project manager. Your ONLY job is to respond with a valid, raw JSON object. Do not add any conversational text, explanations, or markdown formatting like ```json.

    Your task is to deconstruct the following user goal into a detailed project plan.
    User Goal: "{goal}"
    Project Timeline: "{timeline}"

    The JSON object must have a root key "project_plan" which is a list of tasks. Each task in the list must be an object with the following keys: 'id', 'task_name', 'description', 'category', 'priority', 'start_date', 'end_date', 'dependencies', and 'deliverable'.
    - 'dependencies' must be a list of integers.
    - 'priority' must be one of "High", "Medium", or "Low".
    - Dates must be in "YYYY-MM-DD" format.
    - Do not add any text before or after the JSON object.
    """

@app.post("/generate-master-plan")
async def generate_master_plan(request: GoalRequest):
    raw_response_text = "Response not available"
    try:
        prompt = create_master_prompt(request.goal, request.timeline)
        
        # Make the API call to Groq
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a project management AI that only responds with perfect, raw JSON. You never use markdown."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.1-8b-instant",  # CORRECTED: Using the latest supported model
            temperature=0.6,
            response_format={"type": "json_object"}, # This forces JSON output
        )
        
        raw_response_text = chat_completion.choices[0].message.content
        
        # Parse the JSON text into a Python dictionary
        plan_data = json.loads(raw_response_text)

        # We need to manually add the goal and timeline to the response for the frontend
        final_response = {
            "goal": request.goal,
            "timeline": request.timeline,
            "project_plan": plan_data.get("project_plan", []) # Safely get the plan
        }
        
        return final_response

    except Exception as e:
        print(f"AN ERROR OCCURRED: {e}")
        print("--- RAW AI RESPONSE WAS ---")
        print(raw_response_text)
        print("---------------------------")
        raise HTTPException(status_code=500, detail=str(e))

