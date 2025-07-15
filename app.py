import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
from generator import generate_caption_and_songs

st.set_page_config(page_title="AI Meme Generator", layout="centered")

st.title("🤖 AI Caption & songs Generator")
st.caption("Generate funny, stylish, or emotional memes + matching songs!")

uploaded = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

mood = st.selectbox("🎭 Choose a Mood (or leave auto)", ["Auto Detect", "Funny", "Classy", "Romantic", "Swag", "Peaceful", "Sad"])
lang = st.selectbox("🌐 Caption Language", ["English", "Tamil", "Hindi"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("✨ Generate Caption & song"):
        mood_choice = None if mood == "Auto Detect" else mood
        result = generate_caption_and_songs(image, mood_choice, lang)

        if result:
            caption = result["caption"]
            songs = result["songs"]
            mood_detected = result["mood"]

            st.success(f"🧠 Mood: {mood_detected}")
            st.markdown(f"**🎯 Caption:** {caption}")

            st.markdown("**🎵 Suggested Songs:**")
            for lang, song in songs.items():
                st.write(f"- {lang}: {song}")

            # Draw caption
            draw = ImageDraw.Draw(image)
            font_path = "fonts/NotoSansTamil-Regular.ttf" if lang == "Tamil" else "fonts/arial.ttf"
            try:
                font = ImageFont.truetype(font_path, 40)
            except:
                font = ImageFont.load_default()

            draw.text((10, 10), caption, font=font, fill="white", stroke_width=2, stroke_fill="black")

            os.makedirs("output", exist_ok=True)
            output_path = "output/caption & songs.jpg"
            image.save(output_path)
            st.image(image, caption="🖼️ caption preview")

            with open(output_path, "rb") as f:
                st.download_button("📥 Download caption + song ", f, file_name="caption & songs.jpg", mime="image/jpeg")
        else:
            st.error("❌ Failed to generate caption. Try again.")
