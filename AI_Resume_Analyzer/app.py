<<<<<<< HEAD
import os
import re
import PyPDF2
import spacy
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# SpaCy NLP Model Load
try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    import en_core_web_sm
    nlp = en_core_web_sm.load()

# 1. Extract Text from PDF
def extract_text_from_pdf(file_obj) -> str:
    pdf_reader = PyPDF2.PdfReader(file_obj)
    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

# 2. Extract Contact Information using Regex
def extract_contact_info(text: str):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}'
    
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    
    # Simple Link Extraction
    github = "Found" if "github.com" in text.lower() else "Not Found"
    linkedin = "Found" if "linkedin.com" in text.lower() else "Not Found"
    
    return {
        "email": emails[0] if emails else "Not Detected",
        "phone": phones[0] if phones else "Not Detected",
        "github": github,
        "linkedin": linkedin
    }

# 3. Comprehensive Analysis Engine
def analyze_resume(text: str, jd_text: str):
    # Skills DB
    skills_db = [
        "python", "java", "c++", "c#", "javascript", "html", "css", "sql",
        "react", "angular", "node.js", "fastapi", "flask", "django",
        "machine learning", "deep learning", "nlp", "spacy", "pandas",
        "numpy", "git", "github", "docker", "aws", "azure", "spring boot", 
        "postgresql", "mysql", "mongodb", "rest apis", "dsa"
    ]
    
    text_lower = text.lower()
    found_resume_skills = set(skill for skill in skills_db if skill in text_lower)
    
    # If JD is provided
    jd_lower = jd_text.lower()
    jd_skills = set(skill for skill in skills_db if skill in jd_lower) if jd_text.strip() else set()
    
    found_skills = [s.title() for s in found_resume_skills]
    missing_skills = [s.title() for s in (jd_skills - found_resume_skills)] if jd_skills else []
    matched_skills = [s.title() for s in (found_resume_skills & jd_skills)] if jd_skills else []

    # ML Cosine Similarity Score Calculation
    score = 0
    if jd_text.strip():
        documents = [text, jd_text]
        count_vectorizer = TfidfVectorizer(stop_words='english')
        sparse_matrix = count_vectorizer.fit_transform(documents)
        doc_term_matrix = sparse_matrix.todense()
        
        # Cosine similarity between Resume and JD
        similarity = cosine_similarity(sparse_matrix[0:1], sparse_matrix[1:2])[0][0]
        score = round(similarity * 100, 1)
    
    # Generate Smart Suggestions
    suggestions = []
    word_count = len(text.split())
    
    if word_count < 200:
        suggestions.append("Resume ka length bohot chota hai. Action verbs aur project details add karein.")
    if missing_skills:
        suggestions.append(f"In key skills ko target karein: {', '.join(missing_skills[:4])}")
    if "github.com" not in text.lower():
        suggestions.append("Portfolio grow karne ke liye GitHub profile link zaroor add karein.")
    if not suggestions:
        suggestions.append("Aapka resume solid hai! Job profile ke saath accha match ho raha hai.")

    return {
        "word_count": word_count,
        "match_score": score,
        "found_skills": found_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "contact_info": extract_contact_info(text),
        "suggestions": suggestions
    }

# Routes
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"result": None}
    )

@app.post("/")
@app.post("/analyze")
@app.post("/upload")
async def analyze(request: Request):
    try:
        form = await request.form()
        uploaded_file = form.get("file") or form.get("resume") or form.get("pdf")
        jd_text = str(form.get("job_description") or form.get("jd") or "")

        if not uploaded_file or not hasattr(uploaded_file, "file"):
            return templates.TemplateResponse(
                request=request, 
                name="index.html", 
                context={"error": "Kripya PDF file upload karein."}
            )
            
        extracted_text = extract_text_from_pdf(uploaded_file.file)
        
        if not extracted_text.strip():
            return templates.TemplateResponse(
                request=request, 
                name="index.html", 
                context={"error": "PDF se text read nahi ho paya."}
            )
            
        analysis_result = analyze_resume(extracted_text, jd_text)
        
        return templates.TemplateResponse(
            request=request, 
            name="index.html", 
            context={
                "filename": getattr(uploaded_file, "filename", "Resume.pdf"), 
                "result": analysis_result,
                "jd_text": jd_text
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            request=request, 
            name="index.html", 
            context={"error": f"Error aaya: {str(e)}"}
        )
=======
from flask import Flask, render_template, request
import os

from resume_parser import extract_resume
from manager import run_swarm


app = Flask(__name__)


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



@app.route("/")
def home():

    return render_template("index.html")



@app.route("/analyze", methods=["POST"])
def analyze():

    resume_file = request.files["resume"]

    job_description = request.form["job_description"]


    resume_path = os.path.join(
        UPLOAD_FOLDER,
        resume_file.filename
    )


    resume_file.save(resume_path)



    print("Extracting Resume...")

    resume = extract_resume(resume_path)



    print("Running Swarm AI...")

    results = run_swarm(
        resume,
        job_description
    )


    return render_template(
        "result.html",
        results=results
    )



if __name__ == "__main__":

    app.run(debug=True)
>>>>>>> 550b47c16537225651743dd04529751240e618c0
