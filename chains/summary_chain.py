"""
summary_chain.py — Generates dynamic patient and clinician summaries
based entirely on the parsed LLM triage and action outputs.
"""

from typing import Dict, Any
from datetime import datetime
import os

try:
    from langchain_community.chat_models import ChatOllama
    from langchain_core.prompts import ChatPromptTemplate
    OLLAMA_AVAILABLE = True
except Exception:
    OLLAMA_AVAILABLE = False

def generate_summaries(user_input: str, symptoms: Dict[str, Any], triage_result: Dict[str, Any], action_plan: Dict[str, Any]) -> Dict[str, Any]:
    """
    Returns:
    {
      "user": {...},
      "clinician": {...}
    }
    """

    # Base summaries (LLM can refine these later)
    user_summary = {
        "what_you_reported": user_input,
        "triage_level": triage_result.get("severity_level"),
        "reasoning": triage_result.get("rationale"),
        "what_to_do_now": triage_result.get("recommended_action"),
        "next_steps": action_plan.get("tasks", []),
        "follow_up_due": action_plan.get("follow_up_due"),
        "note": "This information is for triage support and not a medical diagnosis."
    }

    clinician_summary = {
        "chief_complaint": symptoms.get("chief_complaint"),
        "duration_days": symptoms.get("duration_days"),
        "associated_symptoms": symptoms.get("associated_symptoms"),
        "severity_self": symptoms.get("severity_self"),
        "triage_level": triage_result.get("severity_level"),
        "rationale": triage_result.get("rationale"),
        "red_flags": triage_result.get("red_flags_triggered"),
        "recommended_action": triage_result.get("recommended_action"),
        "tasks": action_plan.get("tasks", []),
        "follow_up_due": action_plan.get("follow_up_due"),
    }

    # Optional LLM enhancement (summarize in natural language)
    if OLLAMA_AVAILABLE:
        try:
            model_name = os.getenv("OLLAMA_MODEL", "medllama2")
            chat = ChatOllama(model=model_name, temperature=0)
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a medical triage assistant summarizing structured JSON into a patient-friendly summary."),
                ("user", f"Summarize this triage result in plain English:\n{triage_result}\n{action_plan}")
            ])
            msg = prompt.format_messages()
            result = chat.invoke(msg)
            user_summary["llm_summary"] = result.content.strip()
        except Exception:
            pass

    return {"user": user_summary, "clinician": clinician_summary}
