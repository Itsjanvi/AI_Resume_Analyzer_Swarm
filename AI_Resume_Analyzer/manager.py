from agents import (
    ats_agent,
    grammar_agent,
    skill_gap_agent,
    career_agent
)


def run_swarm(resume, job_description):

    print("\nResume Parser Agent Finished")

    print("ATS Agent Running...")
    ats = ats_agent(resume, job_description)

    print("Grammar Agent Running...")
    grammar = grammar_agent(resume)

    print("Skill Gap Agent Running...")
    skills = skill_gap_agent(resume, job_description)

    print("Career Agent Running...")
    career = career_agent(resume)

    return {
        "ats": ats,
        "grammar": grammar,
        "skills": skills,
        "career": career
    }