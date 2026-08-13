# 📄 AI Resume Analyzer (Swarm Intelligence)

An advanced multi-agent collaborative web application designed to parse, evaluate, score, and optimize candidate resumes using Swarm AI paradigms and advanced natural language processing.

---

## 📋 Table of Contents
* [About the Project](#-about-the-project)
* [Key Features](#-key-features)
* [Tech Stack & Libraries](#️-tech-stack--libraries)
* [Project Structure](#-project-structure)
* [Workflow Architecture](#-workflow-architecture)
* [How to Run Locally](#-how-to-run-locally)
* [Usage Guide](#-usage-guide)
* [Future Scope](#-future-scope)
* [Contributing](#-contributing)
* [License](#-license)
* [Author](#-author)

---

## 🚀 About the Project
Screening resumes efficiently is a major bottleneck in recruitment. This project implements a Swarm AI framework where multiple specialized AI agents collaborate dynamically (e.g., parsing agent, skill-matching agent, ATS-scoring agent, and feedback writer agent) to analyze a candidate's profile against specific job descriptions, delivering comprehensive evaluations through an interactive web interface.

---

## 🌟 Key Features
* **Multi-Agent Evaluation:** Utilizes a swarm of specialized agent roles to handle deep text analysis, keyword matching, and formatting assessment.
* **ATS Compatibility Scoring:** Instantly calculates Applicant Tracking System (ATS) scores based on targeted industry requirements.
* **Constructive Feedback Generation:** Provides actionable suggestions for improving summary sections, technical skill lists, and project descriptions.
* **Interactive Web Dashboard:** Clean, modern interface designed to upload documents and track real-time agent assessments.

---

## 🛠️ Tech Stack & Libraries
* **Programming Language:** Python 🐍
* **Web Framework:** Flask
* **AI & Multi-Agent Frameworks:** OpenAI API / Custom Swarm Orchestration, LangChain / CrewAI concepts
* **Data Processing:** PyPDF2 / pdfplumber, Pandas, NumPy
* **Frontend:** HTML5, CSS3, JavaScript
* **Development Tools:** Git, GitHub, VS Code

---

## 📂 Project Structure
```text
AI_Resume_Analyzer_Swarm/
│
├── templates/              
│   └── index.html          # Main HTML user interface for resume uploads and job description inputs
├── static/                 
│   └── style.css           # Styling and dashboard design files
├── app.py                  # Main Flask backend application server
├── agents.py               # Multi-agent definitions and prompt orchestrations
├── requirements.txt        # Project dependencies list
└── .env                    # Environment configuration (API keys)
