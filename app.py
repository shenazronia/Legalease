import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Legalease - AI Legal Document Generator", page_icon="📜"
)

st.title("📜 Legalease: AI Legal Document Generator")
st.write(
    "Generate professional legal documents instantly using Gemini AI & FastAPI."
)

# Sidebar input options
st.sidebar.header("Document Settings")
doc_type = st.sidebar.selectbox(
    "Select Document Type",
    [
        "Rental Agreement",
        "Non-Disclosure Agreement (NDA)",
        "Affidavit",
        "Employment Contract",
    ],
)

# User inputs
st.subheader("Enter Details")
party_one = st.text_input("First Party Name (e.g., Owner/Employer)")
party_two = st.text_input("Second Party Name (e.g., Tenant/Employee)")
terms = st.text_area(
    "Additional Terms / Details",
    placeholder="Mention key terms like duration, amount, location, etc.",
)

# Submit button
if st.button("Generate Legal Document"):
    if not party_one or not party_two:
        st.warning("Please fill in both party names!")
    else:
        st.info("Generating document... Please wait.")

        # Backend API payload
        payload = {
            "doc_type": doc_type,
            "party_one": party_one,
            "party_two": party_two,
            "terms": terms,
        }

        try:
            # FastAPI Backend URL (Localhost)
            response = requests.post("http://127.0.0.1:8000/generate", json=payload)

            if response.status_code == 200:
                result = response.json()
                st.success("Document Generated Successfully!")

                # Display Document Text
                st.subheader("Generated Document:")
                st.text_area(
                    "Result",
                    value=result.get("document", "No content received."),
                    height=300,
                )
            else:
                st.error(
                    f"Failed to generate. Server error: {response.status_code}"
                )
        except Exception as e:
            st.error(
                "Could not connect to FastAPI backend. Make sure Uvicorn is running on port 8000!"
            )
