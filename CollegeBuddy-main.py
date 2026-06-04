import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests
import json
import os
from pathlib import Path

st.set_page_config(
    page_title="College Buddy",
    page_icon="src/Logo College.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)

# Load CSS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "src" / "main.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None


def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception:
        return None


# --- Header ---
lottie_home = load_lottiefile("src/Home_student.json")
col1, col2 = st.columns([1, 9])
with col1:
    if lottie_home:
        st_lottie(lottie_home, height=100, width=100)
with col2:
    st.header(":rainbow[Welcome to College Buddy 🎓]", divider="rainbow")

st.markdown("### Your All-in-One College Companion")
st.write(
    "College Buddy helps you build your profile, ace interviews, explore jobs & hackathons, "
    "and sharpen your knowledge — all in one place."
)

st.markdown("---")

# --- Feature Cards ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🧑‍🏫 Profile Builder")
    st.write("Build your coding profile, track LeetCode, Codeforces stats, and showcase your GitHub.")
    st.page_link("pages/🧑\u200d🏫ProfileBuilder.py", label="Go to Profile Builder →")

with col2:
    st.markdown("#### 🗃️ Job & Hack Hub")
    st.write("Discover hackathons, job listings, and exam resources curated for college students.")
    st.page_link("pages/🗃️JobHackHub.py", label="Go to Job & Hack Hub →")

with col3:
    st.markdown("#### 🧠 Knowledge Builder")
    st.write("Get personalized roadmaps, practice mock interviews, and use the AI-powered code editor.")

st.markdown("---")
st.caption("College Buddy • Built for students, by students 🚀")
