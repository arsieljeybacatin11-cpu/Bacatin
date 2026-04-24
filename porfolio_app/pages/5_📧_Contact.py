import streamlit.components.v1 as components
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Contact Me", page_icon="📧")

# Custom CSS
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background:#F2FFF0;
        }

        [data-testid="stSidebar"] {
            background: #CAE7D0;
        }

        .stButton>button {
            background-color: #00c6ff;
            color: black;
            border-radius: 10px;
            padding: 10px 20px;
        }

        .stTextInput>div>div>input {
            border-radius: 10px;
        }

        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #1c1f26;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📧 Contact Me")
st.write("Building things is better together. Whether you have a technical question or a project idea, drop me a message below! ")

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Send a Message")

    # ✅ HTML FORM (CLIENT-SIDE) — WORKS WITH FREE Web3Forms
    components.html("""
        <style>
            body {
                font-family: Arial, sans-serif;
            }

            .form-container {
                background: white;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
                max-width: 100%;
            }

            input, textarea {
                width: 90%;
                padding: 10px;
                margin-top: 8px;
                margin-bottom: 15px;
                border-radius: 10px;
                border: 1px solid #ccc;
                font-size: 16px;
            }

            textarea {
                min-height: 120px;
                resize: vertical;
            }

            button {
                width: 100%;
                background-color: #7d3cff;
                color: white;
                border-radius: 12px;
                border: none;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
            }

            button:hover {
                background-color: #6a32d4;
            }

            label {
                font-weight: 600;
            }
        </style>

        <div class="form-container">
            <form action="https://api.web3forms.com/submit" method="POST">

                <input type="hidden" name="access_key" value="a76b0ab4-3f85-4ee4-bdde-d0e0ac5a624a">

                <label>Name</label>
                    <input type="text" name="name" placeholder="Enter your full name" required>

                <label>Email Address</label>
                    <input type="email" name="email" placeholder="Enter your email address" required>

                <label>Message</label>
                    <textarea name="message" placeholder="Write your message here..." required></textarea>

                <input type="hidden" name="subject" value="New Contact Form Message">

                <button type="submit">Send Message</button>
            </form>
        </div>
    """, height=450)

with col2:
    st.subheader("Connect with Me")
    st.write("You can also find me here:")

    st.link_button("🌐 GitHub", "https://github.com/arsieljeybacatin11-cpu")
    st.link_button("📱 Facebook", "https://www.facebook.com/arsieljey.pones")

    st.markdown("---")
    st.info("📍 **Location:** Masbate, Philippines")