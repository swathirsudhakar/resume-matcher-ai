from reportlab.pdfgen import canvas

def generate_match_report(resume_text, jd_text, score, filename="match_report.pdf"):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "AI Resume Matcher Report")
    c.setFont("Helvetica", 12)
    c.drawString(100, 780, f"Match Score: {score}%")
    c.drawString(100, 760, "Summary:")
    c.setFont("Helvetica", 10)
    c.drawString(100, 740, "This score represents how closely your resume matches the job description.")
    c.save()

