from typing import Dict

ROLE_SKILLS: Dict[str, Dict] = {
    "data_scientist": {
        "title_keywords": [
            "data scientist", "data science", "ml engineer",
            "machine learning", "data analyst", "AI Engineer"
        ],
        "skills": [
            "python", "pandas", "numpy", "sql","Apache Spark"
            "scikit-learn", "machine learning","Kafka","PowerBI","PyTorch","Transformers", "BERT"
            "statistics", "tensorflow", "matplotlib","Predictive Modeling","Hadoop"
        ]
    },

    "devops_engineer": {
        "title_keywords": [
            "devops", "site reliability", "sre", "platform engineer","DeSecOps"
            "Cloud Engineer", "Platform Enginner"
        ],
        "skills": [
            "docker", "kubernetes", "aws", "azure",
            "ci/cd", "terraform", "linux", "jenkins"
        ]
    },

    "full_stack": {
        "title_keywords": [
            "full stack", "software engineer", "web developer",
        ],
        "skills": [
            "javascript", "react", "node",
            "html", "css", "api",
            "mongodb", "postgresql"
        ]
    }
}

def detect_role(text: str) -> str:
    text = text.lower()
    role_scores = {}

    for role, data in ROLE_SKILLS.items():
        score = 0

        for keyword in data["title_keywords"]:
            if keyword in text:
                score += 2  # title keywords weighted higher

        for skill in data["skills"]:
            if skill in text:
                score += 1

        role_scores[role] = score

    # Return role with highest score
    detected_role = max(role_scores, key=role_scores.get)
    return detected_role
