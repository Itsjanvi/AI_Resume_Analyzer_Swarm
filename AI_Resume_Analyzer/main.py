from resume_parser import extract_resume
from manager import run_swarm
from report_generator import generate_report
import os


print("=" * 50)
print("🤖 AI Resume Analyzer using Swarm AI")
print("=" * 50)


# Resume input
resume_path = input("\nEnter Resume Path: ")


if not os.path.exists(resume_path):
    print("❌ Resume file not found!")
    exit()


# Job description input
job_description = input("\nPaste Job Description:\n")


print("\n📄 Extracting Resume...")
resume = extract_resume(resume_path)


print("\n🐝 Running Swarm AI Agents...")
results = run_swarm(
    resume,
    job_description
)


print("\n📝 Generating Report...")
generate_report(results)


print("\n✅ Analysis Completed Successfully!")
print("Report saved in reports folder.")