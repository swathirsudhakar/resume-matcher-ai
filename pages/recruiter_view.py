import streamlit as st
import os
import re
from matcher import compute_match_score
from resume_parser import extract_text_from_pdf, extract_text_from_txt
from report_generator import generate_match_report

st.set_page_config(page_title="Recruiter Resume Filter", layout="wide")

st.markdown("""
    <h2 style='text-align: center; color: #38bdf8;'>🧑‍💼 Resume Matcher for Recruiters</h2>
    <p style='text-align: center; color: #94a3b8;'>Upload multiple resumes and specify job requirements to filter candidates.</p>
    <hr>
""", unsafe_allow_html=True)


# 📥 Upload multiple resumes
resume_files = st.file_uploader("📄 Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

# 📤 Upload Job Description (Voice or File)
jd_file = st.file_uploader("📝 Upload Job Description (TXT)", type=["txt"])

# 🎙️ Voice Input Button (Mic)
st.markdown("### 🎙️ Use Voice to Speak Job Description")

st.components.v1.html(
    """
    <button onclick="startRecording()" style="font-size:18px;padding:8px 16px;border-radius:8px;background-color:#1f2937;color:white;">🎙️ Start Speaking</button>
    <p id="output" style="color:white;font-size:16px;margin-top:10px;"></p>
    <script>
      function startRecording() {
        var recognition = new webkitSpeechRecognition();
        recognition.lang = "en-IN";
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;
        recognition.onresult = function(event) {
          var transcript = event.results[0][0].transcript;
          document.getElementById("output").innerText = "You said: " + transcript;
          navigator.clipboard.writeText(transcript);
        };
        recognition.onerror = function(event) {
          document.getElementById("output").innerText = "❌ Error: " + event.error;
        };
        recognition.start();
      }
    </script>
    """,
    height=220,
)

jd_voice_text = st.text_area("🎤 Or paste your spoken Job Description here")

# 🧮 Sidebar Filter Inputs — Must come before button!
st.sidebar.header("📋 Eligibility Criteria")
min_score = st.sidebar.slider("Minimum Match Score (%)", 0, 100, 75)
min_cgpa = st.sidebar.number_input("Minimum CGPA", min_value=0.0, max_value=10.0, value=8.0, step=0.1)


# 📚 Extract Job Description Text
jd_input_text = ""
if jd_voice_text.strip():
    jd_input_text = jd_voice_text.strip()
elif jd_file:
    with open("temp_jd.txt", "wb") as f:
        f.write(jd_file.read())
    jd_input_text = extract_text_from_txt("temp_jd.txt")

# 🚀 Filter Button Logic
if st.button("🚀 Filter Candidates"):
    if not jd_input_text:
        st.error("❌ Please provide a Job Description (uploaded or spoken).")
        st.stop()

    if not resume_files:
        st.error("❌ Please upload at least one resume.")
        st.stop()

    results = []

    for file in resume_files:
        with open(f"temp_{file.name}", "wb") as f:
            f.write(file.read())

        resume_text = extract_text_from_pdf(f"temp_{file.name}")

        # Extract CGPA using regex (fallback to mock value if not found)
        cgpa_match = re.search(r'CGPA\s*[:\-]?\s*(\d+\.\d+)', resume_text, re.IGNORECASE)
        cgpa = float(cgpa_match.group(1)) if cgpa_match else round(7.0 + (hash(file.name) % 30) / 10.0, 2)

        score = compute_match_score(resume_text, jd_input_text)

        eligibility = "✅ Eligible" if score >= min_score and cgpa >= min_cgpa else "❌ Not Eligible"

        results.append({
            "Resume": file.name,
            "Match Score": f"{score}%",
            "CGPA": cgpa,
            "Status": eligibility
        })

    st.subheader("📊 Filtered Results")
    st.table(results)

