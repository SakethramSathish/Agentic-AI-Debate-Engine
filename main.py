from graphs.debate_graph import build_debate_graph
from graphs.state import DebateState

from agents.pro_agent import pro_agent_node
from agents.con_agent import con_agent_node
from agents.judge_agent import judge_agent_node

if __name__ == "__main__":
    graph = build_debate_graph(
        pro_agent_node,
        con_agent_node,
        judge_agent_node
    )

    initial_state: DebateState = {
        "topic": "Is AI making humans lazy?",
        "pro_arguments": {},
        "con_arguments": {},
        "judgement": {}
    }

    result = graph.invoke(initial_state)

    print("\n🟢 PRO ARGUMENTS:\n")
    print(result["pro_arguments"])

    print("\n🔴 CON ARGUMENTS:\n")
    print(result["con_arguments"])

    print("\n⚖️ JUDGE VERDICT:\n")
    print(result["judgment"])