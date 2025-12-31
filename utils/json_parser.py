import json
import re

def extract_json(text: str):
    #Extracts JSON from LLm output that may include Markdown code fences.
    cleaned = re.sub(r"```json|```", "", text).strip()

    try:
        return json.loads(cleaned)
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON after cleaning: \n{cleaned}") from e