import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="✨",
    layout="wide"
)

# Custom CSS for modern UI
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
            background-color: #1c1f26;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }
            
        .st.write{
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

st.title("WELCOME TO MY PORFOLIO")
st.write("NAV SLIDE THAT WE HAVE BAR LEARNING ABOUT MY WORK ACTIVITY AND MY SKILL.")
st.success("choose and  click select page about me!")