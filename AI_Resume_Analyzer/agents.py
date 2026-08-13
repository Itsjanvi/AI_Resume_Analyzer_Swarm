import re


def ats_agent(resume, job_description):
    """
    Calculates ATS score based on matching keywords
    """

    resume_words = set(re.findall(r"\b\w+\b", resume.lower()))
    job_words = set(re.findall(r"\b\w+\b", job_description.lower()))

    matched = sorted(resume_words.intersection(job_words))
    missing = sorted(job_words.difference(resume_words))

    score = int((len(matched) / max(len(job_words), 1)) * 100)

    return f"""
==========================
ATS ANALYSIS
==========================

ATS Score: {score}/100

Matched Skills:
{', '.join(matched) if matched else 'None'}

Missing Skills:
{', '.join(missing) if missing else 'None'}
"""


def grammar_agent(resume):
    """
    Performs basic grammar/style checks.
    """

    suggestions = []

    if len(resume.split()) < 200:
        suggestions.append("• Resume is too short. Add more details.")

    if "responsible for" in resume.lower():
        suggestions.append("• Replace 'Responsible for' with action verbs like Developed, Built, Created.")

    if "objective" not in resume.lower():
        suggestions.append("• Consider adding a Career Objective section.")

    if "project" not in resume.lower():
        suggestions.append("• Add Projects to strengthen your resume.")

    if len(suggestions) == 0:
        suggestions.append("• No major grammar or formatting issues found.")

    return "\n".join(suggestions)


def skill_gap_agent(resume, job_description):
    """
    Finds skills missing from the resume.
    """

    resume_words = set(re.findall(r"\b\w+\b", resume.lower()))
    job_words = set(re.findall(r"\b\w+\b", job_description.lower()))

    missing = sorted(job_words - resume_words)

    if not missing:
        return "No significant skill gaps found."

    return (
        "Missing Skills:\n\n- "
        + "\n- ".join(missing[:20])
    )


def career_agent(resume):
    """
    Gives career recommendations.
    """

    advice = """
==========================
CAREER RECOMMENDATIONS
==========================

Recommended Skills
• Docker
• Git & GitHub
• SQL
• AWS
• Machine Learning
• Data Structures & Algorithms

Recommended Certifications
• AWS Cloud Practitioner
• Google Data Analytics
• Microsoft Azure Fundamentals

Suggested Projects
• AI Resume Analyzer
• AI Research Assistant
• Network Intrusion Detection System
• Electricity Consumption Prediction

General Advice
• Keep your resume to one page.
• Quantify achievements wherever possible.
• Add GitHub and LinkedIn profile links.
• Include internships and certifications.
"""

    return advice