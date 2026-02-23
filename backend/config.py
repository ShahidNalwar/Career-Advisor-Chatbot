import os
from dotenv import load_dotenv
from pathlib import Path

# Explicitly load .env from the project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    # Current free-tier optimized model
    MODEL_NAME = "gemini-2.5-flash"
    
    APP_NAME = "Career Advisor AI"
    MAX_HISTORY = 10  # Token optimization limit

    if not GEMINI_API_KEY:
        raise ValueError(f"GEMINI_API_KEY not found. Checked path: {env_path}")