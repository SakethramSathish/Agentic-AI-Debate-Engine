from langgraph.graph import StateGraph, END
from graphs.state import DebateState

def build_debate_graph(
        pro_node,
        con_node,
        judge_node
):
    #Builds the LangGraph workflow for the debate engine

    graph = StateGraph(DebateState)

    #Register Nodes

    graph.add_node("pro_agent", pro_node)
    graph.add_node("con_agent", con_node)
    graph.add_node("judge_agent", judge_node)

    #Define Flow

    graph.set_entry_point("pro_agent")

    graph.add_edge("pro_agent", "con_agent")
    graph.add_edge("con_agent", "judge_agent")
    graph.add_edge("judge_agent", END)

    return graph.compile()