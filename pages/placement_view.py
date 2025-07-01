import streamlit as st
import streamlit.components.v1 as components
import os
import re
from matcher import compute_match_score
from resume_parser import extract_text_from_pdf, extract_text_from_txt

st.set_page_config(page_title="Placement Officer", layout="wide")

st.markdown("""
    <h2 style='text-align: center; color: #38bdf8;'>🎓 Resume Matcher for Placement Officers</h2>
    <p style='text-align: center; color: #94a3b8;'>Compare multiple resumes against job descriptions and highlight missing skills.</p>
    <hr>
""", unsafe_allow_html=True)

# 📥 Upload Resumes
resume_files = st.file_uploader("📄 Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

# 📤 Upload JD
jd_file = st.file_uploader("📝 Upload Job Description (TXT)", type=["txt"])

# 🎤 Voice Input via Web Speech API
st.subheader("🎤 Speak your Job Description")
components.html(
    """
    <script>
    var recognition;
    function startDictation() {
        if (!('webkitSpeechRecognition' in window)) {
            alert("Web Speech API is not supported.");
        } else {
            recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = "en-US";

            recognition.start();

            recognition.onresult = function(e) {
                document.getElementById('speech_output').value = e.results[0][0].transcript;
                recognition.stop();
            };

            recognition.onerror = function(e) {
                recognition.stop();
            };
        }
    }
    </script>
    <textarea id="speech_output" rows="6" style="width: 100%; font-size: 16px;" placeholder="Paste or speak job description here..."></textarea>
    <button onclick="startDictation()" style="margin-top: 10px; padding: 10px 20px; font-size: 16px;">🎤 Click to Speak</button>
    """,
    height=250,
)

# ✍️ Textarea to Confirm/Update
jd_voice_text = st.text_area("📝 Confirm or Edit JD Below", key="jd_input")



# Extract JD Text
jd_input_text = ""
if jd_voice_text.strip():
    jd_input_text = jd_voice_text.strip()
elif jd_file:
    with open("temp_jd.txt", "wb") as f:
        f.write(jd_file.read())
    jd_input_text = extract_text_from_txt("temp_jd.txt")

# Start Analysis
# Start Analysis
if st.button("🔍 Analyze Resumes"):
    if not jd_input_text:
        st.error("❌ Please provide a Job Description.")
        st.stop()

    if not resume_files:
        st.error("❌ Please upload at least one resume.")
        st.stop()

    results = []  # ✅ Define the list here

    # Clean skill extraction from JD
    technical_skills = [
        "python", "java", "c++", "c#", "sql", "javascript", "html", "css", "react", "node.js",
        "aws", "azure", "google cloud", "tensorflow", "pytorch", "docker", "kubernetes", 
        "linux", "git", "machine learning", "deep learning", "nlp", "opencv", "power bi",
        "excel", "tableau", "flask", "django", "mongodb", "postgresql", "redis"
    ]
    
    jd_lower = jd_input_text.lower()
    jd_skills = set(skill for skill in technical_skills if skill in jd_lower)

    for file in resume_files:
        with open(f"temp_{file.name}", "wb") as f:
            f.write(file.read())
        resume_text = extract_text_from_pdf(f"temp_{file.name}")

        resume_lower = resume_text.lower()
        resume_skills = set(skill for skill in technical_skills if skill in resume_lower)

        score = compute_match_score(resume_text, jd_input_text)

        missing_skills = sorted(list(jd_skills - resume_skills))
        missing_text = ", ".join(missing_skills) if missing_skills else "None ✅"

        results.append({
            "Resume": file.name,
            "Match Score": f"{score}%",
            "Missing Skills": missing_text
        })

    st.subheader("📊 Results")
    st.table(results)
