import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

def get_gemini_model():
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel(GEMINI_MODEL)

def generate_response(prompt: str) -> str:
    model = get_gemini_model()
    response = model.generate_content(prompt)
    return response.text