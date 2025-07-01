 🤖 AI-Powered Resume Matcher and Optimizer

This is an AI-based web app built using **Streamlit** that matches resumes with job descriptions and provides helpful feedback — such as a match score, missing skills, and interview questions — tailored for students, recruiters, and placement officers.


 🚀 Features

 👩‍🎓 Student View
- Upload your resume (PDF)
- Provide job description (upload or voice input)
- View your **Match Score**
- Generate **Downloadable Match Report (PDF)**
- Optional: Get **AI-Generated Interview Questions**

🧑‍💼 Recruiter View
- Upload multiple resumes
- Input job description and set:
  - Minimum Match Score
  - Minimum CGPA
- Get filtered results with eligibility status

 🎓 Placement Officer View
- Upload resumes and JD
- Use **Voice Input** for JD
- View **Missing Skills** per candidate
- Bulk match resumes and see scores



 📂 Project Structure
 resume_matcher_ai/
├── app.py or home.py # Main homepage (role-based navigation)
├── matcher.py # Match score logic
├── resume_parser.py # Text extraction from PDF
├── report_generator.py # PDF report generation
├── requirements.txt # All dependencies
├── pages/
│ ├── student_view.py
│ ├── recruiter_view.py
│ └── placement_view.py
├── assets/ # Optional: images/icons
└── README.md # This file


 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Models**: OpenAI / OpenRouter API (for interview Qs)
- **Backend Logic**: Python, scikit-learn
- **PDF Handling**: PyMuPDF, ReportLab
- **Deployment**: [Streamlit Cloud](https://streamlit.io/cloud)


📦 Installation

# Clone this repo
git clone https://github.com/swathirsudhakar/resume-matcher-ai.git
cd resume-matcher-ai

# (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app locally
streamlit run app.py





