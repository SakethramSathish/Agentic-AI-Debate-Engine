import streamlit as st

from graphs.debate_graph import build_debate_graph
from graphs.state import DebateState

from agents.pro_agent import pro_agent_node
from agents.con_agent import con_agent_node
from agents.judge_agent import judge_agent_node

#Page Config

st.set_page_config(
    page_title="AI Debate Engine",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Agentic AI Debate Engine")
st.caption("A multi-agent debate engine powered by LangGraph & Gemini")

#Topic Input
topic = st.text_input(
    "Enter a debate topic",
    placeholder="e.g. Is AI making humans lazy?"
)

start_button = st.button("Start Debate")

#Run Debate
if start_button and topic.strip():

    with st.spinner("Agents are debating..."):
        graph = build_debate_graph(
            pro_agent_node,
            con_agent_node,
            judge_agent_node
        )

        initial_state: DebateState = {
            "topic": topic,
            "pro_arguments": {},
            "con_arguments": {},
            "judgement": {}
        }

        result = graph.invoke(initial_state)

    #Display Results
    st.divider()

    #Pro Arguments
    with st.expander("🟢 Pro Agent — FOR the topic", expanded=True):
        for i, arg in enumerate(result["pro_arguments"].get("arguments", []), 1):
            st.markdown(f"**{i}.** {arg}")

    #Con Arguments
    with st.expander("🔴 Con Agent — AGAINST the topic", expanded=True):
        for i, arg in enumerate(result["con_arguments"].get("arguments", []), 1):
            st.markdown(f"**{i}.** {arg}")

    #Judge Verdict
    st.divider()
    st.subheader("⚖️ Judge Verdict")

    judgment = {
        "pro_score": result["judgement"].get("pro_score", 0),
        "con_score": result["judgement"].get("con_score", 0),
        "bias_analysis": result["judgement"].get("bias_analysis", {}),
        "winner": result["judgement"].get("winner", "DRAW"),
        "reasoning": result["judgement"].get("reasoning", "")
    }
    
    col1, col2 = st.columns(2)
    col1.metric("Pro Score", judgment.get("pro_score", 0))
    col2.metric("Con Score", judgment.get("con_score", 0))

    winner = judgment.get("winner", "DRAW")

    if winner == "PRO":
        st.success("🏆 Winner: PRO side")
    elif winner == "CON":
        st.success("🏆 Winner: CON side")
    else:
        st.info("🤝 Result: DRAW")

    st.markdown("### 📌 Reasoning")
    st.write(judgment.get("reasoning", ""))

elif start_button:
    st.warning("Please enter a debate topic.")