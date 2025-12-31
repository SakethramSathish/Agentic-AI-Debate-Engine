# Agentic AI Debate Engine

A multi-agent debate engine that generates structured arguments and an impartial judgment using LangGraph and Gemini (Google Generative AI).

**Features**
- Multi-agent workflow: `pro_agent`, `con_agent`, and `judge_agent`.
- Streamlit UI for interactive debates (`app.py`).
- Structured JSON outputs for arguments and judgments.
- Prompt templates for agent behavior under `prompts/`.

**Requirements**
Install dependencies from `requirements.txt`:

```
pip install -r requirements.txt
```

Notable packages: `streamlit`, `langgraph`, `langchain`, `google-generativeai`, `python-dotenv`, `pydantic`.

**Quick Start**
1. Create a `.env` file in the project root and set your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Or run the CLI demo:

```bash
python main.py
```

**Configuration**
- `config.py` contains LLM and debate tuning values: `GEMINI_MODEL`, `MAX_ARGUMENTS`, scoring weights, and other flags.

**Project Structure (key files)**
- `app.py` — Streamlit front-end and orchestration.
- `main.py` — CLI/demo runner that invokes the debate graph.
- `config.py` — Environment and debate configuration.
- `llm/gemini_client.py` — Thin wrapper for the Gemini client.
- `graphs/debate_graph.py` — LangGraph workflow definition.
- `agents/` — Agent implementations: `pro_agent.py`, `con_agent.py`, `judge_agent.py`.
- `prompts/` — Prompt templates used by agents.
- `utils/` — Helpers: `json_parser.py`, `formatting.py`, `scoring.py`.

**Agents**
- `pro_agent` and `con_agent` load their respective prompt templates from `prompts/`, generate responses via Gemini and return structured JSON arguments.
- `judge_agent` evaluates both sides and returns numeric scores, bias analysis, a winner, and reasoning.

**Prompts & Output**
Prompt templates live in `prompts/` and instruct the model to return STRICT valid JSON. The project includes `utils/json_parser.py` which strips code fences and parses the JSON output.

**LLM Integration**
The project uses a small wrapper in `llm/gemini_client.py` that calls Google Generative AI (Gemini). Ensure your `GEMINI_API_KEY` is set and `config.py` matches your chosen model.

**Contributing**
- Open issues or PRs for bug fixes and feature requests.
- Keep prompts and JSON output contracts stable to avoid breaking downstream parsing.

**License**
This project is licensed under the GNU General Public License v3.0 — see `LICENSE` for details.
