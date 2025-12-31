from typing import TypedDict, Dict, Any

class DebateState(TypedDict):
    #Input
    topic: str

    #Agent Outputs
    pro_arguments: Dict[str, Any]
    con_arguments: Dict[str, Any]

    #Judge Output
    judgement: Dict[str, Any]