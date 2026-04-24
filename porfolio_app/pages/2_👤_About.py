import streamlit as st


st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background:#F2FFF0;
        }

        [data-testid="stSidebar"] {
            background: #CAE7D0;
        }}
        .stTextInput>div>div>input {
            border-radius: 10px;
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

st.title("👤 About Me")

st.markdown("""
    <div class="card">
        As a Computer science student  in DEBESMSCAT experience on hands on to build any software .
            Being a student I am willing to learn a technologies  and to support that company goal.
    </div>
""", unsafe_allow_html=True)

st.subheader("🎓 Education")

# --- START OF 3-COLUMN LAYOUT ---
# We create 3 columns to hold your 3 education levels
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card">
            <h4>Primary</h5>
            <p>BUGTONG CAWAYAN CABANGCALANN,Elementary School</p>
            <p> TAN,AWAN,PLACER, Masbate</p>
            <p>2011-2017</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <h4>Secondary</h5>
            <p>VERDIDA SABRIDO NATIONAL HIGH SCHOOL</p>
            <p>TAN,AWAN,PLACER, Masbate</p>
            <p>2017-2023</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card">
            <h4>Tertiary</h4> 
            <p>BS Computer Science</p>
            <p>DEBESMSCAT</p> 
            <p>2023 - Present</p> 
        </div>
    """, unsafe_allow_html=True)
# --- END OF 3-COLUMN LAYOUT ---


st.subheader("🚀 GOAL OF MYSELF")
st.info("---WEB DEVELOPER ")
st.info("---FULL STACK DEVELOPER")
st.info("continue and enchance my skill as beginner to become a full stack developer.")