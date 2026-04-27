import streamlit as st 
import pdfplumber
import re from sklearn.feature_extraction.text 
import TfidfVectorizer from sklearn.metrics.pairwise 
import cosine_similarity

----------------------

Extract text from PDF resume

----------------------

def extract_text_from_pdf(uploaded_file): text = "" with pdfplumber.open(uploaded_file) as pdf: for page in pdf.pages: text += page.extract_text() + " " return text.lower()

----------------------

Skill extraction

----------------------

skills_db = [ "python", "java", "machine learning", "sql", "tensorflow", "pandas", "numpy", "data analysis", "deep learning", "power bi", "excel", "nlp", "opencv" ]

def extract_skills(resume_text): found_skills = [] for skill in skills_db: if skill in resume_text: found_skills.append(skill) return found_skills

----------------------

ATS Score Calculation

----------------------

def calculate_ats_score(resume_text, job_description): documents = [resume_text, job_description.lower()] tfidf = TfidfVectorizer() tfidf_matrix = tfidf.fit_transform(documents)

similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
score = round(similarity[0][0] * 100, 2)
return score

----------------------

Resume Suggestions

----------------------

def give_suggestions(resume_text): suggestions = []

if "projects" not in resume_text:
    suggestions.append("Add Projects section")

if "internship" not in resume_text:
    suggestions.append("Add Internship experience")

if "certification" not in resume_text:
    suggestions.append("Add Certifications section")

if len(resume_text.split()) < 300:
    suggestions.append("Resume content looks short, add more details")

return suggestions

----------------------

Streamlit UI

----------------------

st.title("AI Resume Analyzer") st.write("Upload your resume and compare it with job description")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"]) job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description: resume_text = extract_text_from_pdf(uploaded_file)

st.subheader("Extracted Skills")
skills = extract_skills(resume_text)
st.write(skills)

st.subheader("ATS Score")
score = calculate_ats_score(resume_text, job_description)
st.success(f"Your ATS Score: {score}%")

st.subheader("Suggestions")
suggestions = give_suggestions(resume_text)

if suggestions:
    for s in suggestions:
        st.write("-", s)
else:
    st.success("Your resume looks strong!")