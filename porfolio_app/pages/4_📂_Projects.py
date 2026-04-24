import streamlit as st

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

st.title("📁 My Projects")

st.markdown("""
    <div class="card">
        <h3>LIBRARY BOOK MANAGEMENT SYSTEM</h3>
        <p>A mathploid and streamlit tool to manage the books  and track who is students borrowed the books and what a name of book.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="card">
        <h3>STUDENT GRADE CALCULATOR</h3>
        <p>A Streamlit tool for automatic can shown a result .</p>
        </a>
    </div>
""", unsafe_allow_html=True)