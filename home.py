import streamlit as st

# Set page config
st.set_page_config(
    page_title="AI Resume Matcher",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🤖"
)

# Custom sidebar layout
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6463/6463929.png", width=40)
    st.markdown("<h3 style='color:#38bdf8;'>Resume Matcher AI</h3>", unsafe_allow_html=True)
    st.markdown("---")



    st.markdown("<p style='color:#94a3b8;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)

# Main homepage body (centered)
st.markdown(
    """
    <h1 style='text-align: center; color: #38bdf8;'>💼 AI Resume Matcher</h1>
    <h4 style='text-align: center; color: #94a3b8;'>Select your role from the left to get started</h4>
    """,
    unsafe_allow_html=True
)



# Initialize session state
if "role" not in st.session_state:
    st.session_state.role = None

# Custom styles
st.markdown(
    """
    <style>
        body {
            background-color: #0f172a;
            color: #f1f5f9;
        }
        .stButton>button {
            height: 100px;
            font-size: 20px;
            border-radius: 12px;
            background-color: #1e293b;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)



st.write("\n\n")

# Layout for role selection
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/4333/4333609.png", width=80)
    if st.button("👩‍🎓 I'm a Student", use_container_width=True):
        st.session_state.role = "Student"

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135823.png", width=80)
    if st.button("🧑‍💼 I'm a Recruiter", use_container_width=True):
        st.session_state.role = "Recruiter"

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=80)
   # New icon
    if st.button("🎓 Placement Officer", use_container_width=True):
        st.session_state.role = "Placement"

# Redirect to selected role page
if st.session_state.role == "Student":
    st.switch_page("pages/student_view.py")
elif st.session_state.role == "Recruiter":
    st.switch_page("pages/recruiter_view.py")
elif st.session_state.role == "Placement":
    st.switch_page("pages/placement_view.py")

