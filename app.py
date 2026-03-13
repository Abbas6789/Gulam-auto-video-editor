import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import time

# --- 1. گوگل شیٹ کنکشن (JSON ڈیٹا یہاں آئے گا) ---
def get_sheet_data():
    try:
        # یہاں آپ اپنی JSON فائل کا ڈیٹا ڈالیں گے
        credentials_info = {
            "type": "service_account",
            "project_id": "YOUR_PROJECT_ID",
            "private_key": "YOUR_PRIVATE_KEY",
            "client_email": "YOUR_CLIENT_EMAIL",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(credentials_info, scopes=scopes)
        client = gspread.authorize(creds)
        # اپنی شیٹ کا نام یہاں لکھیں
        sheet = client.open("Hussain_Studio_Sheet").sheet1
        return sheet
    except:
        return None

sheet = get_sheet_data()

# --- 2. ایپ کا پریمیم ڈیزائن (CSS) ---
st.set_page_config(page_title="Hussain Studio Pro", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { 
        background: linear-gradient(45deg, #FFD700, #FFA500); 
        color: black; border-radius: 15px; font-weight: bold; border: none; height: 3.5em; width: 100%;
    }
    .update-bar { background: #1f1f1f; padding: 10px; border-radius: 10px; border-left: 5px solid #FFD700; color: #FFD700; }
    .whatsapp-float {
        position: fixed; bottom: 20px; right: 20px; background-color: #25d366; color: white;
        padding: 15px; border-radius: 50px; z-index: 1000; box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        text-decoration: none; display: flex; align-items: center; font-weight: bold;
    }
    .premium-card { background: #1a1c23; padding: 20px; border-radius: 20px; border: 1px solid #30363d; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. فیچر کنٹرول (شیٹ سے) ---
announcement = sheet.acell('A1').value if sheet else "خوش آمدید! پریمیم ویڈیو ٹولز اب سب کے لیے فری ہیں۔"
st.markdown(f'<div class="update-bar"><marquee scrollamount="6">{announcement}</marquee></div>', unsafe_allow_html=True)

# واٹس ایپ بٹن
st.markdown("""
    <a href="https://wa.me/923461785207" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="30px" style="margin-right:10px;">
        رابطہ کریں
    </a>
""", unsafe_allow_html=True)

# --- 4. مین انٹرفیس ---
st.title("🎬 Hussain Digital Studio")
st.write("فیس بک، ٹک ٹاک اور یوٹیوب کے لیے مکمل اسٹوڈیو")

# فیوچر لاگ ان سیکشن (ابھی چھپا ہوا ہے)
# st.text_input("ای میل درج کریں (ویریفکیشن کے لیے)", placeholder="example@mail.com")

with st.container():
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    platform = st.selectbox("پلیٹ فارم منتخب کریں", ["Facebook Reels", "TikTok Video", "YouTube Shorts"])
    topic = st.text_input("ویڈیو کا ٹاپک لکھیں", placeholder="مثلاً: Viral Food Vlog")
    
    if st.button("🚀 ویڈیو اور ہیش ٹیگز تیار کریں"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # رینڈرنگ کا احساس
        for percent in range(100):
            time.sleep(0.04)
            progress_bar.progress(percent + 1)
            if percent < 30: status_text.text("⚙️ AI اسکرپٹ اور ہیش ٹیگز تیار ہو رہے ہیں...")
            elif percent < 70: status_text.text("🎵 بیک گراؤنڈ میوزک اور ریل سائز سیٹ ہو رہا ہے...")
            else: status_text.text("📥 فائل ڈاؤن لوڈ کے لیے فائنل کی جا رہی ہے...")
        
        st.success("✅ آپ کا مواد کامیابی سے تیار کر لیا گیا ہے!")
        
        # ڈیٹا نکالنا (شیٹ سے یا ڈیفالٹ)
        tags_data = sheet.acell('B1').value if sheet else "#Viral #HussainStudio #Trending"
        video_link = sheet.acell('C1').value if sheet else "https://example.com/video.mp4"
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="⬇️ ڈاؤن لوڈ ہیش ٹیگز (TXT)",
                data=f"Platform: {platform}\nTopic: {topic}\n\n{tags_data}",
                file_name="viral_tags.txt",
                mime="text/plain"
            )
        with col2:
            st.markdown(f'<a href="{video_link}" target="_blank"><button style="width:100%; height:3.5em; border-radius:15px; background:#FF4B4B; color:white; border:none; cursor:pointer; font-weight:bold;">⬇️ ڈاؤن لوڈ ویڈیو (MP4)</button></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# فیوچر پیمنٹ میتھڈ (نوٹ)
st.caption("🔒 محفوظ پیمنٹ گیٹ وے (Easypaisa/JazzCash) جلد آ رہا ہے۔")
    
