import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import tempfile
import os

st.set_page_config(page_title="Ghulam Hussain Studio Free", layout="centered")

# Branding
st.title("🎬 Ghulam Hussain Studio Free")
st.caption("AI Powered Mobile Video Creator")

# SESSION PERSISTENCE
if "google_key" not in st.session_state:
    st.session_state.google_key = ""

if "sheet_name" not in st.session_state:
    st.session_state.sheet_name = ""

if "login" not in st.session_state:
    st.session_state.login = False

# SIDEBAR LOGIN
st.sidebar.title("🔐 Login Panel")

email = st.sidebar.text_input("Email")
password = st.sidebar.text_input("Password", type="password")

google_key = st.sidebar.text_area("Google Service Account JSON Key")
sheet_name = st.sidebar.text_input("Google Sheet Name")

if st.sidebar.button("Save Keys"):
    st.session_state.google_key = google_key
    st.session_state.sheet_name = sheet_name
    st.sidebar.success("Saved!")

if st.sidebar.button("Login"):
    if email and password:
        st.session_state.login = True
        st.sidebar.success("Logged in!")

# GOOGLE SHEET CHECK
payment_status = "Pending"

def check_payment():
    global payment_status
    try:
        scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
        ]

        creds_dict = eval(st.session_state.google_key)

        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

        client = gspread.authorize(creds)

        sheet = client.open(st.session_state.sheet_name).sheet1

        data = pd.DataFrame(sheet.get_all_records())

        payment_status = data.loc[0,"Payment_Status"]

    except:
        payment_status = "Pending"

if st.session_state.login:
    check_payment()

# PAYMENT CONTROL
if payment_status == "Pending":
    st.warning("⚠ Payment Required")

    st.info("""
    Easypaisa / JazzCash
    Send Payment and contact support
    """)

# WHATSAPP SUPPORT
st.markdown(
"""
<a href="https://wa.me/923461785207" target="_blank">
<button style="position:fixed;bottom:30px;right:30px;
background:#25D366;color:white;border:none;padding:15px;
border-radius:50px;">WhatsApp</button>
</a>
""",
unsafe_allow_html=True
)

# MAIN VIDEO ENGINE
st.header("🎬 Video Creator")

text = st.text_area("Enter Script (Urdu / English)")

uploaded_files = st.file_uploader(
"Upload Images",
accept_multiple_files=True
)

if st.button("Generate Video"):

    if payment_status == "Pending":
        st.error("Payment Required")
    else:

        with st.spinner("Creating Video..."):

            # AI VOICE
            tts = gTTS(text)
            audio_path = tempfile.mktemp(".mp3")
            tts.save(audio_path)

            audio = AudioFileClip(audio_path)

            duration = audio.duration / len(uploaded_files)

            clips = []

            for file in uploaded_files:
                temp_img = tempfile.mktemp(".jpg")

                with open(temp_img,"wb") as f:
                    f.write(file.read())

                clip = (
                    ImageClip(temp_img)
                    .set_duration(duration)
                    .resize((720,1280))
                )

                clips.append(clip)

            video = concatenate_videoclips(clips)

            final = video.set_audio(audio)

            output = tempfile.mktemp(".mp4")

            final.write_videofile(output,fps=24)

            with open(output,"rb") as f:
                st.download_button(
                "⬇ Download Video",
                f,
                file_name="video.mp4"
                )

# SOCIAL MEDIA ENGINES

st.header("📱 Social Media Hashtags")

if st.button("TikTok Hashtags"):
    tags = "#foryou #viral #tiktokviral #trending #fyp"
    st.code(tags)
    st.write("Copy above hashtags")

if st.button("Facebook Hashtags"):
    tags = "#facebookreels #viralvideo #trending #reelsviral"
    st.code(tags)

if st.button("YouTube Shorts Hashtags"):
    tags = "#shorts #youtubeshorts #viralshorts #trendingshorts"
    st.code(tags)
