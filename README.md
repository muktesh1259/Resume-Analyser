# AI Resume Analyzer

AI Resume Analyzer is a machine learning-based web application that helps users evaluate their resumes against a job description.

## Features
- Upload resume in PDF format
- Extract text from resume using PDFPlumber
- Identify technical skills from resume
- Calculate ATS score using TF-IDF and Cosine Similarity
- Provide resume improvement suggestions

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- PDFPlumber

## How It Works
1. User uploads a resume PDF
2. System extracts resume text
3. Skills are identified from the resume
4. Job description is compared with resume
5. ATS score is generated
6. Suggestions are provided for improvement

## Installation
```bash
pip install -r requirements.txt
streamlit run app.py
