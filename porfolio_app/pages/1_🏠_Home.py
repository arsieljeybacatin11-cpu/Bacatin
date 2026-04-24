import streamlit as st
import os

current_dir = os.path.dirname(__file__) 
img_path = os.path.join(current_dir, "jey.jpg")
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background:#F2FFF0;
        }

        [data-testid="stSidebar"] {
            background: #CAE7D0;
        }

        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #ffffff;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)
# Header Section
st.title("✨ My Portfolio ✨")
st.subheader("Future full stack  Developer ")

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("""
    # Hi, I'm ARSIEL JEY BACATIN👋!
    Turning complex logic into a elegant high performance applications.

    I specialize in build offline capable system optimized data of workflows and modern responsive interfaces that work wherever you are.

    🚀 check out my latest work in that sidebar!
    """)

with col2:
    st.image(img_path)
st.divider()

# Feature Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card">👤 <b> About Me</b><br>Explore to know more about me</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">🛠️ <b>Skills</b><br>My technical stack</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">💻 <b>Projects</b><br>check my work</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card">📩 <b>Contact</b><br>contact me easily</div>', unsafe_allow_html=True)