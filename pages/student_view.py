import streamlit as st
import streamlit.components.v1 as components
import requests
import os

from matcher import compute_match_score
from resume_parser import extract_text_from_pdf, extract_text_from_txt
from report_generator import generate_match_report

st.set_page_config(page_title="Student Resume Matcher", layout="wide")

st.markdown("""
    <h2 style='text-align: center; color: #38bdf8;'>👩‍🎓 Resume Matcher for Students</h2>
    <p style='text-align: center; color: #94a3b8;'>Upload your resume and job description to get a match score and AI-generated interview questions.</p>
    <hr>
""", unsafe_allow_html=True)

# Upload Resume
resume_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])

# Upload or Speak JD
jd_file = st.file_uploader("📝 Upload Job Description (TXT)", type=["txt"])

st.subheader("🎤 Speak your JD")

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

# Textarea to confirm/edit
jd_voice_text = st.text_area("📝 Confirm or Edit JD Below", key="jd_input")

# === Process JD Input ===
jd_input_text = ""
if jd_voice_text.strip():
    jd_input_text = jd_voice_text.strip()
elif jd_file is not None:
    with open("temp_jd.txt", "wb") as f:
        f.write(jd_file.read())
    jd_input_text = extract_text_from_txt("temp_jd.txt")

# === Process Resume and Show Score ===
if resume_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())
    resume_text = extract_text_from_pdf("temp_resume.pdf")

    if jd_input_text:
        score = compute_match_score(resume_text, jd_input_text)

        st.success(f"🎯 Match Score: {score}%")
        st.progress(min(score / 100, 1.0))

        generate_match_report(resume_text, jd_input_text, score, filename="match_report.pdf")
        with open("match_report.pdf", "rb") as f:
            st.download_button(
                label="📥 Download Match Report (PDF)",
                data=f,
                file_name="match_report.pdf",
                mime="application/pdf"
            )

        # === Optional Interview Questions ===
        if st.checkbox("💬 I'm interested in Interview Questions"):
            try:
                headers = {
                    "Authorization": "Bearer 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",  # Replace with yours
                    "Content-Type": "application/json"
                }

                payload = {
                    "model": "anthropic/claude-3-haiku",
                    "messages": [
                        {"role": "system", "content": "You are an expert interviewer."},
                        {"role": "user", "content": f"Generate 5 interview questions based on this job description:\n\n{jd_input_text}"}
                    ]
                }

                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

                if response.status_code == 200:
                    questions = response.json()["choices"][0]["message"]["content"]
                    st.success("✅ Interview Questions Generated:")
                    st.write(questions)
                else:
                    st.error(f"❌ Failed to generate questions: {response.status_code}")
                    st.json(response.json())

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")


