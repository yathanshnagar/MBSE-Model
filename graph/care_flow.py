"""
care_flow.py — defines LangGraph workflow structure for the Healthcare AI Assistant
Fixed for latest LangGraph version (no END constant)
"""

from typing import TypedDict, Optional
from langgraph.graph import StateGraph

# Define the state schema for passing data between nodes
class CareState(TypedDict, total=False):
    user_input: Optional[str]
    symptoms: Optional[dict]
    triage: Optional[dict]
    action: Optional[dict]
    summary: Optional[dict]

def initialize_care_graph():
    # Initialize the graph with the CareState schema
    graph = StateGraph(CareState)

    # ------------------- Node definitions (Phase 1 placeholders) -------------------
    def collect_symptoms(state: CareState):
        print("🩺 [Node] Collecting symptoms...")
        return {"user_input": state.get("user_input", "")}

    def retrieve_knowledge(state: CareState):
        print("📚 [Node] Retrieving medical knowledge...")
        return state

    def classify_severity(state: CareState):
        print("⚖️ [Node] Classifying severity...")
        return state

    def execute_action(state: CareState):
        print("🏃 [Node] Executing action plan...")
        return state

    def follow_up(state: CareState):
        print("🔁 [Node] Scheduling follow-up...")
        return state

    def generate_summary(state: CareState):
        print("📝 [Node] Generating summary...")
        return state

    def emergency_exit(state: CareState):
        print("🚨 [Node] Emergency path triggered!")
        return state

    # ------------------- Add nodes -------------------
    graph.add_node("collect_symptoms", collect_symptoms)
    graph.add_node("retrieve_knowledge", retrieve_knowledge)
    graph.add_node("classify_severity", classify_severity)
    graph.add_node("execute_action", execute_action)
    graph.add_node("follow_up", follow_up)
    graph.add_node("generate_summary", generate_summary)
    graph.add_node("emergency_exit", emergency_exit)

    # ------------------- Define edges (workflow sequence) -------------------
    graph.add_edge("collect_symptoms", "retrieve_knowledge")
    graph.add_edge("retrieve_knowledge", "classify_severity")
    graph.add_edge("classify_severity", "execute_action")
    graph.add_edge("execute_action", "follow_up")
    graph.add_edge("follow_up", "generate_summary")
    graph.add_edge("classify_severity", "emergency_exit")

    # ------------------- Define start and end points -------------------
    graph.set_entry_point("collect_symptoms")
    graph.set_finish_point("generate_summary")  # ✅ fixed — specify last node by name

    return graph
