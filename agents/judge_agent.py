from llm.gemini_client import generate_response
from graphs.state import DebateState
from utils.json_parser import extract_json
import json


def normalize_judgment(j):
    """
    Ensures judge output matches UI expectations
    """
    return {
        "pro_score": j.get("pro_score") or j.get("Pro Score") or j.get("proScore") or 0,
        "con_score": j.get("con_score") or j.get("Con Score") or j.get("conScore") or 0,
        "bias_analysis": j.get("bias_analysis") or {
            "pro": "Not provided",
            "con": "Not provided"
        },
        "winner": j.get("winner") or j.get("Winner") or "DRAW",
        "reasoning": j.get("reasoning") or j.get("Explanation") or ""
    }


def judge_agent_node(state: DebateState):
    print("\n🔥 JUDGE AGENT CALLED 🔥")
    topic = state["topic"]
    pro_arguments = state["pro_arguments"]
    con_arguments = state["con_arguments"]

    with open("prompts/judge_prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(
        topic=topic,
        pro_arguments=json.dumps(pro_arguments, indent=2),
        con_arguments=json.dumps(con_arguments, indent=2)
    )

    raw_response = generate_response(prompt)
    parsed = extract_json(raw_response)

    normalized = normalize_judgment(parsed)
    print("\n📦 PARSED JUDGMENT:\n", parsed)
    print("\n📦 NORMALIZED JUDGMENT:\n", normalized)


    return {
        "judgement": normalized
    }
