# 🎵 SnapTuneAI – AI-Powered Caption + Song Generator for Images

SnapTuneAI is a creative tool that uses **Google Gemini Vision AI** and **Generative AI** to automatically generate:

- 🗨️ A **funny, emotional, or relatable caption**
- 🎶 A **matching song suggestion**
- 🈶 Supports **Tamil & English**
- 🖼️ Outputs a **social media–ready image** (1080x1080 with watermark)

---

## 📸 How It Works

1. Upload any photo (selfie, travel, food, nature… anything!)
2. The AI analyzes the image using **Google Gemini Vision**
3. It generates a:
   - Caption that suits the content + vibe
   - Song that matches the mood
4. Optionally export with:
   - Language (Tamil / English)
   - Mood (happy, romantic, sad, etc.)
   - Watermark or branding
5. Output is saved as a square meme-style image, ready for Instagram, WhatsApp, etc.

---

## 🧠 Tech Stack

| Component            | Tool / Library               |
|---------------------|------------------------------|
| Image Understanding | [Gemini Vision API](https://ai.google.dev/) |
| Caption + Song Generation | Gemini Pro / LLMs |
| Frontend UI         | Streamlit                    |
| Image Processing    | Pillow (PIL)                 |
| Language Support    | Google Translate API / Custom prompts |
| Export Tools        | Custom Python logic (Pillow) |

---

## 🖥️ Demo (Coming Soon)

> Web version coming soon using **Streamlit Cloud**

---

## 🚀 Features

- ✅ Upload your image from file or webcam
- ✅ Choose your **language** (English or Tamil)
- ✅ Choose a **mood/theme** (funny, sad, love, nature, etc.)
- ✅ Auto caption + song recommendation
- ✅ Export image in **1080x1080** for social media
- ✅ Add watermark for branding

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/SnapTuneAI.git
cd SnapTuneAI
pip install -r requirements.txt
streamlit run app.py
