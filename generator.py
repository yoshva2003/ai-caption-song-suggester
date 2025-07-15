import os
import io
import json
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def image_to_bytes(img):
    buf = io.BytesIO()
    img.save(buf, format='JPEG')
    return buf.getvalue()

def generate_caption_and_songs(image, mood_choice=None, lang="English"):
    model = genai.GenerativeModel("gemini-1.5-flash")

    mood_part = f"The mood of the image should be interpreted as: {mood_choice}." if mood_choice else "Detect the mood from the image."

    prompt = f"""
You are an AI meme assistant.

{mood_part}

1. Write a short, catchy 2–3 word caption in {lang}.
2. Suggest a matching song in English, Tamil, and Hindi.

Respond only in this JSON format:
{{
  "mood": "detected or selected mood",
  "caption": "2–3 word caption in chosen language",
  "songs": {{
    "English": "song - artist",
    "Tamil": "song - artist",
    "Hindi": "song - artist"
  }}
}}
"""

    image_bytes = image_to_bytes(image)
    response = model.generate_content(
        [prompt, {"mime_type": "image/jpeg", "data": image_bytes}]
    )

    try:
        text = response.text.strip()
        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except Exception:
        return None
