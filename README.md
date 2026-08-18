# 📄 AI Resume Analyzer

An AI-powered web application that analyzes resumes and provides useful insights, including resume evaluation, ATS-focused feedback, skills analysis, and suggestions for improvement.

## 🚀 Overview

The **AI Resume Analyzer** helps users understand how well their resume matches a given job description.

The application uses AI-based analysis to evaluate resume content, identify relevant skills and keywords, and provide actionable feedback to improve the resume.

## ✨ Features

* 📄 Upload and analyze resumes
* 🎯 ATS-focused resume evaluation
* 🔍 Skill and keyword analysis
* 📝 Resume improvement suggestions
* 🤖 AI-powered resume analysis
* 💼 Job description-based evaluation
* 🌐 Simple and interactive web interface

## 🧠 AI Workflow

```text
Resume + Job Description
          ↓
     Resume Parsing
          ↓
     Content Analysis
          ↓
 Skill & Keyword Matching
          ↓
    ATS Evaluation
          ↓
 AI-Generated Feedback
          ↓
 Resume Improvement Suggestions
```

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **OpenAI API**
* **PyPDF2 / pdfplumber**
* **Pandas**
* **NumPy**
* **HTML5**
* **CSS3**
* **JavaScript**

## 📁 Project Structure

```text
AI_Resume_Analyzer_Swarm/
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── agents.py
├── requirements.txt
├── .env
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Itsjanvi/AI_Resume_Analyzer_Swarm.git
cd AI_Resume_Analyzer_Swarm
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Setup

Create a `.env` file and add your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

**Never upload your actual API key to GitHub.**

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000/
```

Upload your resume, provide the job description, and analyze your resume.

## 🎯 Objective

The goal of this project is to demonstrate how AI and Natural Language Processing can be used to automate resume analysis and provide personalized feedback for improving job applications.

## 🔮 Future Scope

* Improve resume-job matching
* Add support for multiple resume formats
* Add more detailed ATS analysis
* Support multiple job descriptions
* Add resume improvement and rewriting features
* Deploy the application online

## 👩‍💻 Author

**Janvi**

GitHub: [Itsjanvi](https://github.com/Itsjanvi)

---

⭐ If you find this project useful, consider giving it a star!
