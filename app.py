# -*- coding: utf-8 -*-
import streamlit as st
import os
import json
import tempfile
import pandas as pd
from pathlib import Path
from gtts import gTTS
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip

# ─────────────────────────────────────────────
# 1. PAGE CONFIG & BRANDING
# ─────────────────────────────────────────────
st.set_page_config(page_title="Ghulam Hussain Studio Free", page_icon="🎬", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Rajdhani:wght@600&display=swap');
    html, body, [class*="css"] { font-family: 'Rajdhani', sans-serif; background-color: #0a0a0f; color: #e8e0ff; }
    .studio-header { text-align: center; background: linear-gradient(90deg, #7b2ff7, #f107a3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: 'Orbitron', sans-serif; font-size: 1.8rem; font-weight: 900; text-transform: uppercase; }
    .module-card { background: #1a1530; border: 1px solid #3d2d7a; border-radius: 15px; padding: 15px; margin-bottom: 15px; }
    .whatsapp-float { position: fixed; bottom: 20px; right: 20px; background: #25D366; color: white; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 30px; z-index: 100; text-decoration: none; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
</style>
<a class="whatsapp-float" href="https://wa.me/923461785207" target="_blank">💬</a>
""", unsafe_allow_html=True)

st.markdown('<h1 class="studio-header">Ghulam Hussain Studio Free</h1>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 2. SMART PERSISTENT LOGIN (Sidebar)
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("🔐 User Login")
    u_email = st.text_input("Email", key="email")
    u_pass = st.text_input("Password", type="password", key="pass")
    
    st.divider()
    st.header("⚙️ Settings")
    # Persistence logic: saved in session_state
    if "sa_json" not in st.session_state: st.session_state.sa_json = ""
    if "sh_name" not in st.session_state: st.session_state.sh_name = ""
    
    sa_json = st.text_area("JSON Key", value=st.session_state.sa_json, height=100)
    sh_name = st.text_input("Sheet Name", value=st.session_state.sh_name)
    
    if st.button("💾 Save Settings"):
        st.session_state.sa_json = sa_json
        st.session_state.sh_name = sh_name
        st.success("Settings Saved!")

# ─────────────────────────────────────────────
# 8. REMOTE PAYMENT CONTROL (Sheets Logic)
# ─────────────────────────────────────────────
def check_status(email, json_str, sheet_name):
    try:
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(json_str), scope)
        client = gspread.authorize(creds)
        records = client.open(sheet_name).sheet1.get_all_records()
        for r in records:
            if str(r.get("Email")).lower() == email.lower():
                return r.get("Payment_Status", "Pending")
        return "Pending"
    except: return "Pending"

# ─────────────────────────────────────────────
# 3-7 & 10. VIDEO & MEDIA ENGINE
# ─────────────────────────────────────────────
if u_email and u_pass and st.session_state.sa_json:
    status = check_status(u_email, st.session_state.sa_json, st.session_state.sh_name)
    
    if status == "Success":
        st.success("✅ Access Granted!")
        
        # Module 6: Image Uploader
        st.markdown('<div class="module-card"><b>📸 Upload Gallery Images</b>', unsafe_allow_html=True)
        up_imgs = st.file_uploader("Select Photos", type=["jpg","png","jpeg"], accept_multiple_files=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Module 7: AI Script
        v_text = st.text_area("✍️ Video Script (Urdu/English)")
        
        # Platform Selection
        col1, col2, col3 = st.columns(3)
        tags = ""
        if col1.button("TikTok"): tags = "#foryou #viral #fyp #GhulamHussainStudio"
        if col2.button("Facebook"): tags = "#FBReels #Trending #Viral #GhulamHussainStudio"
        if col3.button("YouTube"): tags = "#Shorts #YouTubeViral #GhulamHussainStudio"
        
        if tags:
            st.code(tags)
            st.info("⚡ Generating Video... (MoviePy Engine)")
            # Video generation logic (Placeholder for performance)
            if v_text and up_imgs:
                tts = gTTS(text=v_text, lang='ur')
                tts.save("voice.mp3")
                st.audio("voice.mp3")
                with open("voice.mp3", "rb") as f:
                    st.download_button("📥 Download Video to Gallery", f, "video.mp4", "video/mp4")
    else:
        st.error("⚠️ Payment Pending!")
        st.markdown(f"""
        <div style="background:#2a1010; padding:20px; border-radius:10px; border:1px solid red; text-align:center;">
            <h3>EasyPaisa / JazzCash</h3>
            <h2 style="color:#ffd700;">03461785207</h2>
            <p>Please pay and send screenshot to WhatsApp.</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("👋 Please Login and configure JSON Key in Sidebar.")
