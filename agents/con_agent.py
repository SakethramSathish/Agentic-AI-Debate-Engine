import json
from llm.gemini_client import generate_response
from config import MAX_ARGUMENTS
from graphs.state import DebateState
from utils.json_parser import extract_json


def con_agent_node(state: DebateState):
    topic = state["topic"]

    with open("prompts/con_prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(
        topic=topic,
        max_arguments=MAX_ARGUMENTS
    )

    raw_response = generate_response(prompt)

    parsed = extract_json(raw_response)

    return {
        "con_arguments": parsed
    }