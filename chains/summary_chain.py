"""
summary_chain.py — Generates patient-facing and clinician-facing summaries.
"""

from typing import Dict, Any


def generate_summary(case_data: Dict[str, Any]) -> Dict[str, str]:
    user_input = case_data.get("user_input", "")
    symptoms = case_data.get("symptoms", {})
    triage = case_data.get("triage", {})
    action = case_data.get("action", {})

    patient_summary = (
        "Summary for you:\n"
        f"- What you reported: {user_input}\n"
        f"- Triage level: {triage.get('severity_level', 'UNKNOWN')}\n"
        f"- What to do now: {action.get('action_type', 'self-care')}\n"
        f"- Next steps: {', '.join(action.get('tasks', []))}\n"
        "Note: This is general information for triage support and not a medical diagnosis."
    )

    clinician_summary = (
        "Clinician Hand-over Summary:\n"
        f"- Chief complaint: {symptoms.get('chief_complaint')}\n"
        f"- Duration (days): {symptoms.get('duration_days')}\n"
        f"- Associated symptoms: {', '.join(symptoms.get('associated_symptoms', []))}\n"
        f"- Risk factors: {', '.join(symptoms.get('risk_factors', []))}\n"
        f"- Severity (self): {symptoms.get('severity_self')}\n"
        f"- Triage level: {triage.get('severity_level')}\n"
        f"- Red flags: {', '.join(triage.get('red_flags_triggered', []))}\n"
        f"- Recommended action: {triage.get('recommended_action')}\n"
        f"- Plan: {', '.join(action.get('tasks', []))}"
    )

    return {
        "patient_summary": patient_summary,
        "clinician_summary": clinician_summary
    }
