from app.services.role_detector import detect_role

def test_detect_data_scientist():
    text = "Experienced Data Scientist with Python, pandas, SQL and machine learning"
    role = detect_role(text)
    assert role == "data_scientist"

def test_detect_devops_engineer():
    text = "DevOps engineer skilled in Docker, Kubernetes, AWS and CI/CD pipelines"
    role = detect_role(text)
    assert role == "devops_engineer"

def test_detect_full_stack():
    text = "Full stack developer working with React, Node, HTML, CSS and APIs"
    role = detect_role(text)
    assert role == "full_stack"
