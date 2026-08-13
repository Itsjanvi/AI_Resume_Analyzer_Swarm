import os


def generate_report(results):

    os.makedirs("reports", exist_ok=True)

    report_path = "reports/Resume_Report.txt"


    with open(report_path, "w", encoding="utf-8") as file:

        file.write("=" * 70 + "\n")
        file.write("        SWARM AI RESUME ANALYZER REPORT\n")
        file.write("=" * 70 + "\n\n")


        # ATS Analysis
        file.write("1. ATS ANALYSIS\n")
        file.write("-" * 70 + "\n")
        file.write(results["ats"])
        file.write("\n\n")


        # Grammar Analysis
        file.write("2. GRAMMAR ANALYSIS\n")
        file.write("-" * 70 + "\n")
        file.write(results["grammar"])
        file.write("\n\n")


        # Skill Gap Analysis
        file.write("3. SKILL GAP ANALYSIS\n")
        file.write("-" * 70 + "\n")
        file.write(results["skills"])
        file.write("\n\n")


        # Career Advice
        file.write("4. CAREER RECOMMENDATIONS\n")
        file.write("-" * 70 + "\n")
        file.write(results["career"])
        file.write("\n\n")


        file.write("=" * 70 + "\n")
        file.write("End of Report\n")
        file.write("=" * 70 + "\n")


    print("\n========================================")
    print("✅ Resume Analysis Completed Successfully")
    print(f"📄 Report saved as: {report_path}")
    print("========================================")


    return report_path