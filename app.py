import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Read unstructured email text
with open("sample_email.txt", "r", encoding="utf-8") as file:
    email_text = file.read()

prompt = f"""
Extract the following information from the email and return ONLY valid JSON.

Fields:
- customer_name
- requested_dates
- destination

Email:
{email_text}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are an information extraction assistant. Return only JSON."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

result = response.choices[0].message.content

# Save output to output.json
with open("output.json", "w", encoding="utf-8") as file:
    file.write(result)

print("Extracted Data:")
print(result)
