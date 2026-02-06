from typing import Dict
from app.services.role_detector import ROLE_SKILLS, detect_role

def score_resume(text: str) -> Dict:
    text_lower = text.lower()

    # Step 1: detect role
    role = detect_role(text_lower)

    # Step 2: get skills for that role
    skills = ROLE_SKILLS[role]["skills"]

    found = []
    missing = []

    for skill in skills:
        if skill in text_lower:
            found.append(skill)
        else:
            missing.append(skill)

    score = int((len(found) / len(skills)) * 100)

    suggestions = [
        f"Consider adding experience with {skill}"
        for skill in missing
    ]

    return {
        "detected_role": role,
        "score": score,
        "missing_keywords": missing,
        "suggestions": suggestions
    }
