import streamlit as st

# Page setup
st.set_page_config(page_title="Sarthak Shandilya - Resume", page_icon="📄")

# Title
st.title("📄 Sarthak Shandilya - Resume")

# Info text
st.write("Click the button below to download my resume (PDF format).")

# Load and provide resume file
with open("Sarthak_Shandilya_Resume.pdf", "rb") as file:
    resume_bytes = file.read()

st.download_button(
    label="📥 Download Resume",
    data=resume_bytes,
    file_name="Sarthak_Shandilya_Resume.pdf",
    mime="application/pdf"
)
