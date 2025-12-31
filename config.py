import os
from dotenv import load_dotenv

load_dotenv()

#LLM Config

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

#Debate Config
MAX_ARGUMENTS = 4
ALLOW_DRAW = True

#Scoring Weights
LOGIC_WEIGHT= 0.4
EVIDENCE_WEIGHT = 0.4
BIAS_PENALTY = 0.2