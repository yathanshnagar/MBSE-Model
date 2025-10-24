"""
safety_rules.py — defines red flag checks and safety filters
Phase 1: ready for use in Phase 2
"""

# Simple red-flag keywords (expand later)
RED_FLAGS = [
    "chest pain",
    "difficulty breathing",
    "stiff neck",
    "drooling",
    "cannot swallow",
    "confusion",
    "fainting",
    "bleeding",
    "seizure",
    "rash and fever",
    "fever more than 3 days",
    "infant",
    "pregnant"
]

def check_red_flags(user_input: str) -> list:
    """Return list of red-flag terms detected in text."""
    found = [flag for flag in RED_FLAGS if flag in user_input.lower()]
    return found
