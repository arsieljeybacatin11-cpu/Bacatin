import streamlit as st
import os

base_path = os.path.dirname(__file__)

st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background:#F2FFF0;
        }

        [data-testid="stSidebar"] {
            background: #CAE7D0;
        }

            
        .cert-badge {
            background-color: #ffffff;
            padding: 2px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            display: inline-block;
            margin-top: 5px;
        }
        .skill-card {
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🛠️ My Skills")
st.subheader(" Programming Languages")
skills = {
    "Python": 50,
    "Streamlit": 40,
    "HTML/CSS/JAVASCRIPT": 70,
    "PHP/XAMPP" : 30
}

for skill, level in skills.items():
    st.markdown(f'<p class="skill-label">{skill}</p>', unsafe_allow_html=True)
    st.progress(level)

# --- Skills & Certificates Section ---
st.subheader(" Certificates")

# 1. Define your data (You can replace the URLs with your local image paths)
skills_data = [
    {"name":"Grapich Design","img": "GD.jpg"},
    {"name":"Python for beginners - Simplilearn","img": "Arsiel.jpg"},
    {"name":"Javascript for begginers","img": "bacatin.jpg"},
    
]


cols_per_row = 3
for i in range(0, len(skills_data), cols_per_row):
    cols = st.columns(cols_per_row)
    chunk = skills_data[i : i + cols_per_row]
    
    for idx, skill in enumerate(chunk):
        with cols[idx]:
            # 2. UPDATED PATH LOGIC: No more ".." or "assets"
            img_path = os.path.join(base_path, skill["img"])
            
            # We ONLY draw the card if the image is actually found in 'pages/'
            if os.path.exists(img_path):
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.image(img_path, use_container_width=True)
                st.caption(f"**{skill['name']}**")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                # This helps you debug if the filename is misspelled
                st.error(f"Not found: {skill['img']}")