# -*- coding: utf-8 -*-
import streamlit as st
import os
import json
import tempfile
import time
from pathlib import Path

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Ghulam Hussain Studio Free",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# GLOBAL CSS — Mobile-first, dark luxury theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
    background-color: #0a0a0f;
    color: #e8e0ff;
}

.stApp {
    background: linear-gradient(135deg, #0a0a0f 0%, #12101e 50%, #0a0a0f 100%);
    min-height: 100vh;
}

/* Header */
.studio-header {
    text-align: center;
    padding: 1.5rem 0 1rem 0;
    background: linear-gradient(90deg, #7b2ff7, #f107a3, #ff6b35);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.2rem, 5vw, 2rem);
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.studio-sub {
    text-align: center;
    color: #9d8fff;
    font-size: 0.85rem;
    letter-spacing: 3px;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
}

/* Cards */
.module-card {
    background: linear-gradient(135deg, #1a1530 0%, #1e1840 100%);
    border: 1px solid #3d2d7a;
    border-radius: 16px;
    padding: 1.2rem;
    margin: 0.8rem 0;
    box-shadow: 0 4px 24px rgba(123,47,247,0.15);
    transition: transform 0.2s, box-shadow 0.2s;
}
.module-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(123,47,247,0.3);
}

.module-title {
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

/* Platform colors */
.tiktok-title  { color: #69c9d0; }
.fb-title      { color: #4267B2; }
.youtube-title { color: #FF0000; }
.voice-title   { color: #f107a3; }
.payment-title { color: #ffd700; }

/* Buttons */
.stButton > button {
    width: 100% !important;
    border-radius: 12px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    padding: 0.7rem 1rem !important;
    border: none !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
}

/* Primary button */
.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #7b2ff7, #f107a3) !important;
    color: white !important;
}

/* Default button */
.stButton > button:not([kind="primary"]) {
    background: linear-gradient(90deg, #1e1840, #2d2060) !important;
    color: #c5b8ff !important;
    border: 1px solid #4d3a8a !important;
}

/* Status badges */
.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.badge-success { background: #1a4a1a; color: #4dff4d; border: 1px solid #4dff4d; }
.badge-warning { background: #4a3a00; color: #ffd700; border: 1px solid #ffd700; }
.badge-info    { background: #0a2a4a; color: #4db8ff; border: 1px solid #4db8ff; }

/* Hashtag box */
.hashtag-box {
    background: #0d0d1a;
    border: 1px solid #3d2d7a;
    border-radius: 10px;
    padding: 0.8rem;
    font-size: 0.8rem;
    color: #a0ff9d;
    word-break: break-word;
    line-height: 1.8;
    margin: 0.5rem 0;
}

/* WhatsApp floating button */
.whatsapp-float {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    background: #25D366;
    color: white;
    border-radius: 50%;
    width: 58px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    box-shadow: 0 4px 20px rgba(37,211,102,0.5);
    text-decoration: none;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%   { box-shadow: 0 0 0 0 rgba(37,211,102,0.6); }
    70%  { box-shadow: 0 0 0 14px rgba(37,211,102,0); }
    100% { box-shadow: 0 0 0 0 rgba(37,211,102,0); }
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0d1f 0%, #1a1535 100%) !important;
    border-right: 1px solid #2d2060;
}
section[data-testid="stSidebar"] .stTextInput > label,
section[data-testid="stSidebar"] .stTextArea > label {
    color: #9d8fff !important;
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.8rem;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Divider */
.neon-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #7b2ff7, #f107a3, transparent);
    margin: 1.5rem 0;
    border: none;
}

/* Payment box */
.payment-box {
    background: linear-gradient(135deg, #1a1000, #2a2000);
    border: 1px solid #ffd700;
    border-radius: 14px;
    padding: 1.2rem;
    text-align: center;
}
.payment-number {
    font-family: 'Orbitron', monospace;
    font-size: 1.5rem;
    color: #ffd700;
    letter-spacing: 3px;
    margin: 0.5rem 0;
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #7b2ff7; border-radius: 4px; }
</style>

<!-- WhatsApp Floating Button -->
<a class="whatsapp-float" href="https://wa.me/923461785207?text=Hello%20Ghulam%20Hussain%20Studio%20-%20I%20need%20support!" target="_blank" title="Chat on WhatsApp">
    💬
</a>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────────
defaults = {
    "logged_in": False,
    "user_email": "",
    "gsheet_name": "",
    "service_account_json": "",
    "payment_status": "Pending",
    "generated_video_path": None,
    "tiktok_tags": "",
    "fb_tags": "",
    "yt_tags": "",
    "voice_text": "",
    "uploaded_images": [],
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────
def check_payment_status_from_sheet(email, json_key_str, sheet_name):
    """Connect to Google Sheets and check Payment_Status for this email."""
    try:
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds_dict = json.loads(json_key_str)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        sheet = client.open(sheet_name).sheet1
        records = sheet.get_all_records()
        for row in records:
            if str(row.get("Email", "")).strip().lower() == email.strip().lower():
                return str(row.get("Payment_Status", "Pending")).strip()
        return "Pending"
    except Exception as e:
        st.error(f"Google Sheets error: {e}")
        return "Pending"

TIKTOK_HASHTAGS = (
    "#foryou #foryoupage #fyp #viral #trending #tiktok #explore"
    " #viralvideo #GhulamHussainStudio #tiktokviral #reels #newvideo"
    " #trending2024 #subscribe #share #like #follow #video #content"
)
FB_HASHTAGS = (
    "#FacebookReels #Reels #Trending #Viral #FacebookVideo #Explore "
    "#NewVideo #GhulamHussainStudio #Follow #Like #Share #Facebook "
    "#ViralContent #ReelsFacebook #Shorts2024"
)
YT_HASHTAGS = (
    "#YouTubeShorts #Shorts #Viral #Trending #Subscribe #YouTube "
    "#NewShorts #GhulamHussainStudio #YoutubeViral #Explore #Like "
    "#Share #Comment #Videos #ShortsFeed"
)

def generate_video(images, voice_text, platform="tiktok"):
    """Generate MP4 video using MoviePy + gTTS."""
    try:
        from moviepy.editor import (
            ImageClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip
        )
        from gtts import gTTS
        import numpy as np

        with tempfile.TemporaryDirectory() as tmpdir:
            # 1. Generate voice
            audio_path = os.path.join(tmpdir, "voice.mp3")
            tts = gTTS(text=voice_text, lang="ur" if any(
                '\u0600' <= c <= '\u06FF' for c in voice_text) else "en")
            tts.save(audio_path)

            # 2. Build clips
            target_w, target_h = (1080, 1920)  # 9:16
            clips = []
            n = len(images)
            audio_clip = AudioFileClip(audio_path)
            clip_duration = max(audio_clip.duration / max(n, 1), 2)

            for img_file in images:
                # Save uploaded file to tmp
                img_path = os.path.join(tmpdir, img_file.name)
                with open(img_path, "wb") as f:
                    f.write(img_file.getbuffer())
                clip = (ImageClip(img_path)
                        .set_duration(clip_duration)
                        .resize(height=target_h)
                        .on_color(size=(target_w, target_h),
                                  color=(0, 0, 0), pos='center'))
                clips.append(clip)

            if not clips:
                # Fallback: black screen
                from moviepy.editor import ColorClip
                clips = [ColorClip(size=(target_w, target_h),
                                   color=(10, 10, 20),
                                   duration=audio_clip.duration)]

            video = concatenate_videoclips(clips, method="compose")
            # Trim/loop audio to match video
            if audio_clip.duration < video.duration:
                audio_clip = audio_clip.audio_loop(duration=video.duration)
            else:
                audio_clip = audio_clip.subclip(0, video.duration)

            final = video.set_audio(audio_clip)
            out_path = os.path.join(tmpdir, f"GH_Studio_{platform}.mp4")
            final.write_videofile(out_path, fps=30, codec="libx264",
                                  audio_codec="aac", logger=None)

            # Copy to persistent temp
            import shutil
            persistent = tempfile.NamedTemporaryFile(
                delete=False, suffix=f"_{platform}.mp4"
            )
            shutil.copy(out_path, persistent.name)
            return persistent.name

    except Exception as e:
        st.error(f"Video generation error: {e}")
        return None


# ─────────────────────────────────────────────
# SIDEBAR — LOGIN + GOOGLE SHEET CONFIG
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p class="studio-header" style="font-size:1rem;">🔐 LOGIN</p>', unsafe_allow_html=True)

    email_input = st.text_input("📧 Email", value=st.session_state.user_email,
                                placeholder="your@email.com", key="email_field")
    password_input = st.text_input("🔑 Password", type="password",
                                   placeholder="••••••••", key="pass_field")

    st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)
    st.markdown("**🔗 Google Integration**")

    sa_json = st.text_area(
        "Service Account JSON Key",
        value=st.session_state.service_account_json,
        placeholder='{"type":"service_account","project_id":...}',
        height=100,
        key="sa_json_field"
    )
    sheet_name = st.text_input(
        "Google Sheet Name",
        value=st.session_state.gsheet_name,
        placeholder="MyPaymentSheet",
        key="sheet_name_field"
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save & Login", use_container_width=True):
            if email_input and password_input:
                # Persist to session state
                st.session_state.user_email = email_input
                st.session_state.service_account_json = sa_json
                st.session_state.gsheet_name = sheet_name
                st.session_state.logged_in = True

                # Check payment if sheet configured
                if sa_json and sheet_name:
                    status = check_payment_status_from_sheet(
                        email_input, sa_json, sheet_name
                    )
                    st.session_state.payment_status = status
                st.success("✅ Saved!")
                st.rerun()
            else:
                st.error("Fill email & password")

    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            for k in defaults:
                st.session_state[k] = defaults[k]
            st.rerun()

    if st.session_state.logged_in:
        st.markdown(f"""
        <div style="margin-top:1rem; padding:0.8rem; background:#0d1a0d;
             border:1px solid #4dff4d; border-radius:10px; text-align:center;">
            <span class="badge badge-success">● LOGGED IN</span><br>
            <small style="color:#9d8fff;">{st.session_state.user_email}</small>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# MAIN CONTENT
# ─────────────────────────────────────────────
st.markdown('<h1 class="studio-header">🎬 Ghulam Hussain Studio Free</h1>', unsafe_allow_html=True)
st.markdown('<p class="studio-sub">Professional Video Creation Suite</p>', unsafe_allow_html=True)

# Auth gate
if not st.session_state.logged_in:
    st.markdown("""
    <div class="module-card" style="text-align:center; padding:2.5rem;">
        <div style="font-size:3rem;">🔐</div>
        <div style="font-family:'Orbitron',monospace; color:#9d8fff; margin-top:1rem;">
            Please login from the sidebar<br>to access all features
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ─── PAYMENT STATUS BANNER ───
pay_status = st.session_state.payment_status
if pay_status == "Success":
    st.markdown('<div style="text-align:center;margin-bottom:1rem;"><span class="badge badge-success">✅ PAYMENT VERIFIED — ALL FEATURES UNLOCKED</span></div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="text-align:center;margin-bottom:1rem;"><span class="badge badge-warning">⏳ PAYMENT PENDING — LIMITED ACCESS</span></div>', unsafe_allow_html=True)

unlocked = (pay_status == "Success")

# ═══════════════════════════════════════════
# MODULE 6 — Custom Image Uploader
# ═══════════════════════════════════════════
st.markdown('<div class="module-card">', unsafe_allow_html=True)
st.markdown('<p class="module-title" style="color:#c5b8ff;">📸 Module 6 — Image Gallery Uploader</p>', unsafe_allow_html=True)
uploaded_files = st.file_uploader(
    "Pick photos from your gallery (multiple allowed)",
    type=["jpg", "jpeg", "png", "webp"],
    accept_multiple_files=True,
    label_visibility="collapsed"
)
if uploaded_files:
    st.session_state.uploaded_images = uploaded_files
    cols = st.columns(min(len(uploaded_files), 4))
    for i, f in enumerate(uploaded_files[:4]):
        cols[i].image(f, use_column_width=True)
    if len(uploaded_files) > 4:
        st.caption(f"+ {len(uploaded_files)-4} more images")
    st.markdown(f'<span class="badge badge-info">📷 {len(uploaded_files)} image(s) ready</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# MODULE 7 — AI Voice Input
# ═══════════════════════════════════════════
st.markdown('<div class="module-card">', unsafe_allow_html=True)
st.markdown('<p class="module-title voice-title">🎙️ Module 7 — AI Voice & Script (gTTS)</p>', unsafe_allow_html=True)
voice_text = st.text_area(
    "Enter script in Urdu or English",
    placeholder="آپ کا ویڈیو اسکرپٹ یہاں لکھیں... / Type your video script here...",
    height=100,
    value=st.session_state.voice_text,
    label_visibility="collapsed"
)
st.session_state.voice_text = voice_text
if voice_text:
    lang_detected = "Urdu 🇵🇰" if any('\u0600' <= c <= '\u06FF' for c in voice_text) else "English 🇬🇧"
    st.markdown(f'<span class="badge badge-info">Language detected: {lang_detected}</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# MODULES 3, 4, 5 — Video Engines
# ═══════════════════════════════════════════

# ── TikTok ──────────────────────────────────
st.markdown('<div class="module-card">', unsafe_allow_html=True)
st.markdown('<p class="module-title tiktok-title">🎵 Module 3 — TikTok Video Engine (9:16)</p>', unsafe_allow_html=True)

if unlocked:
    if st.button("🚀 Generate TikTok Video", key="tiktok_btn", use_container_width=True):
        if not voice_text:
            st.warning("Please enter a voice script first.")
        else:
            with st.spinner("⚡ Generating TikTok video..."):
                path = generate_video(
                    st.session_state.uploaded_images,
                    voice_text, "tiktok"
                )
                if path:
                    st.session_state.generated_video_path = path
                    st.session_state.tiktok_tags = TIKTOK_HASHTAGS
                    st.success("✅ TikTok video ready!")
else:
    st.info("🔒 Unlock by completing payment below.")

if st.session_state.tiktok_tags:
    st.markdown("**📋 Viral TikTok Hashtags:**")
    st.markdown(f'<div class="hashtag-box">{st.session_state.tiktok_tags}</div>', unsafe_allow_html=True)
    st.code(st.session_state.tiktok_tags, language=None)
    st.caption("⬆️ Tap & hold to copy hashtags")

st.markdown('</div>', unsafe_allow_html=True)

# ── Facebook ─────────────────────────────────
st.markdown('<div class="module-card">', unsafe_allow_html=True)
st.markdown('<p class="module-title fb-title">📘 Module 4 — Facebook Reels Engine</p>', unsafe_allow_html=True)

if unlocked:
    if st.button("🚀 Generate Facebook Video", key="fb_btn", use_container_width=True):
        if not voice_text:
            st.warning("Please enter a voice script first.")
        else:
            with st.spinner("⚡ Generating Facebook Reel..."):
                path = generate_video(
                    st.session_state.uploaded_images,
                    voice_text, "facebook"
                )
                if path:
                    st.session_state.generated_video_path = path
                    st.session_state.fb_tags = FB_HASHTAGS
                    st.success("✅ Facebook Reel ready!")
else:
    st.info("🔒 Unlock by completing payment below.")

if st.session_state.fb_tags:
    st.markdown("**📋 Trending Facebook Hashtags:**")
    st.markdown(f'<div class="hashtag-box">{st.session_state.fb_tags}</div>', unsafe_allow_html=True)
    st.code(st.session_state.fb_tags, language=None)
    st.caption("⬆️ Tap & hold to copy hashtags")

st.markdown('</div>', unsafe_allow_html=True)

# ── YouTube Shorts ───────────────────────────
st.markdown('<div class="module-card">', unsafe_allow_html=True)
st.markdown('<p class="module-title youtube-title">▶️ Module 5 — YouTube Shorts Engine (9:16)</p>', unsafe_allow_html=True)

if unlocked:
    if st.button("🚀 Generate YouTube Short", key="yt_btn", use_container_width=True):
        if not voice_text:
            st.warning("Please enter a voice script first.")
        else:
            with st.spinner("⚡ Generating YouTube Short..."):
                path = generate_video(
                    st.session_state.uploaded_images,
                    voice_text, "youtube"
                )
                if path:
                    st.session_state.generated_video_path = path
                    st.session_state.yt_tags = YT_HASHTAGS
                    st.success("✅ YouTube Short ready!")
else:
    st.info("🔒 Unlock by completing payment below.")

if st.session_state.yt_
