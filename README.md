🚀 Project Genesis Engine

A smart task planner that transforms high-level goals into comprehensive, actionable project dashboards using a live AI.

This project was built for the UNTHINKABLE SOLUTIONS placement assignment. It uses a FastAPI backend and a dynamic JavaScript frontend to generate a complete project plan, including a visual Gantt chart, in real-time.


### 🎬 [Click Here to Watch the 90-Second Demo Video](https://drive.google.com/file/d/1Paf67liJxv7A6H3QPhCIbasGOonh2aFO/view?usp=drivesdk)


![Demo GIF](https://github.com/nikhil22bce9559-bit/unthinkable-solutions-project/blob/main/ProjectGenesisEngine-GoogleChrome2025-10-1501-45-56-ezgif.com-video-to-gif-converter.gif)

## 🌟 Core Features

🌟 Core Features

Live AI-Powered Task Decomposition: Connects to the Groq API to break down any goal into detailed, actionable steps in real-time.

Dynamic Project Dashboard: Displays the generated plan in a clean, user-friendly interface.

Intelligent Task Analysis: Each task is enriched with a category, priority level, and a clear deliverable.

Visual Gantt Chart: Automatically generates a timeline using Mermaid.js to visualize task dependencies and project flow.



🛠️ Tech Stack

Backend: Python, FastAPI

AI: Groq API (Llama 3.1)

Frontend: HTML, CSS, Vanilla JavaScript

Visualization: Mermaid.js


🚀 Getting Started

Clone the repository:

git clone [https://github.com/nikhil22bce9559-bit/unthinkable-solutions-project.git](https://github.com/nikhil22bce9559-bit/unthinkable-solutions-project.git)
cd unthinkable-solutions-project

Set up the backend:

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your Groq API key
echo "GROQ_API_KEY='your_api_key_here'" > .env

Run the server:

uvicorn main:app --reload

Launch the frontend:

Open the index.html file in your web browser.
