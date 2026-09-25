import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


class GeminiDocumentGenerator:

    def generate_document(self, document_type, parties, terms, dates):

        prompt = f"""
Generate a professional legal document.

Document Type: {document_type}

Parties: {parties}

Terms and Conditions: {terms}

Effective Date: {dates}

Create a structured document with:
- Title
- Introduction
- Parties involved
- Terms and conditions
- Responsibilities
- Confidentiality where applicable
- Termination where applicable
- Signature section

Use clear and formal language.
"""

        for attempt in range(3):
            try:
                response = client.models.generate_contenT(model="gemini-3.8-flash",
                    contents=prompt
                )

                return response.text

            except Exception as e:
                if attempt < 2:
                    time.sleep(5)
                else:
                    raise e
