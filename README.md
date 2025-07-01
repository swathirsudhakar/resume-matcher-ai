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

🌐 Deployment
Deployed using Streamlit Cloud
🔗 Click to Launch Web App (https://resume-matcher-ai-tmgkvcytq28eghxwbxazab.streamlit.app/
)


📢 Notes
You can generate your OpenAI or OpenRouter API key to enable interview questions.

The voice input feature works via Web Speech API and supports Chrome browser.


🤝 Contributing
Feel free to fork the repo, raise issues, or contribute with pull requests.


📧 Contact
Author: Swathi S
GitHub Profile

![Screenshot 2025-07-02 024515](https://github.com/user-attachments/assets/b8473490-2987-4afc-8960-1d39a2b4b981)
![Screenshot 2025-07-02 024506](https://github.com/user-attachments/assets/2b238720-7f98-4f98-a936-f8e7baf2c4ce)
![Screenshot 2025-07-02 024457](https://github.com/user-attachments/assets/df40ce66-0765-492f-a3b2-879c51319182)
![Screenshot 2025-07-02 024430 - Copy](https://github.com/user-attachments/assets/944e9079-dece-4282-b25b-3914c2ff4e18)









