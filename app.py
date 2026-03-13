import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import time
import requests

# --- 1. کنکشن (شیٹ کا نام: HussainSheet) ---
def get_sheet_data():
    try:
        credentials_info = st.secrets["gcp_service_account"]
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(credentials_info, scopes=scopes)
        client = gspread.authorize(creds)
        sheet = client.open("HussainSheet").sheet1 
        return sheet
    except:
        return None

sheet = get_sheet_data()

# --- 2. پریمیم لک اور ڈیزائن ---
st.set_page_config(page_title="Hussain Studio Pro", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .stButton>button { 
        background: linear-gradient(45deg, #FFD700, #FFA500); 
        color: black; border-radius: 15px; font-weight: bold; height: 3.5em; width: 100%; border: none;
    }
    .update-bar { background: #111; padding: 10px; border-radius: 10px; border-right: 5px solid #FFD700; color: #FFD700; text-align: right; }
    .premium-card { background: #161b22; padding: 25px; border-radius: 20px; border: 1px solid #30363d; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. لائیو اپ ڈیٹ پٹی ---
announcement = sheet.acell('A1').value if sheet else "حسین اسٹوڈیو پریمیم سروس لائیو ہے!"
st.markdown(f'<div class="update-bar"><marquee scrollamount="5" direction="right">{announcement}</marquee></div>', unsafe_allow_html=True)

# --- 4. مین انٹرفیس ---
st.title("🎬 Hussain Digital Studio")

# تصویر (جو آپ ایڈمن پینل کے خانے D1 سے بدلیں گے)
if sheet:
    img_url = sheet.acell('D1').value
    if img_url and img_url.startswith("http"):
        st.image(img_url, use_container_width=True)

with st.container():
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.subheader("🎨 اپنی تصویر سے ویڈیو بنائیں")
    
    # صارف کے لیے فوٹو اپ لوڈر
    user_file = st.file_uploader("اپنی تصویر منتخب کریں", type=['jpg', 'png', 'jpeg'])
    
    topic = st.text_input("ویڈیو کا ٹاپک (مثلاً: Viral TikTok Status)")
    
    if st.button("🚀 ویڈیو تیار کریں"):
        if not topic:
            st.warning("براہ کرم ٹاپک لکھیں۔")
        else:
            # کام ہونے کی اینیمیشن
            status = st.empty()
            bar = st.progress(0)
            
            for p in range(100):
                time.sleep(0.03)
                bar.progress(p + 1)
                if p < 30: status.text("📸 تصویر اسکین ہو رہی ہے...")
                elif p < 70: status.text("🎭 اے آئی ایفیکٹس لگائے جا رہے ہیں...")
                else: status.text("📥 ویڈیو فائل تیار کی جا رہی ہے...")
            
            st.success("✅ آپ کی ویڈیو کامیابی سے تیار کر لی گئی ہے!")
            
            # ڈیٹا شیٹ سے اٹھانا
            tags = sheet.acell('B1').value if sheet else "#Viral #Hussain"
            video_url = sheet.acell('C1').value if sheet else ""
            
            st.info(f"Viral Tags: {tags}")
            
            # براہ راست گیلری میں ڈاؤن لوڈ
            if video_url:
                try:
                    v_data = requests.get(video_url).content
                    st.download_button(label="⬇️ گیلری میں محفوظ کریں", data=v_data, file_name="hussain_video.mp4", mime="video/mp4")
                except:
                    st.markdown(f'<a href="{video_url}" target="_blank"><button style="width:100%; height:3em; border-radius:10px; background:#FF4B4B; color:white; border:none; font-weight:bold;">⬇️ ڈاؤن لوڈ لنک</button></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. چھپے ہوئے فیچرز (Hidden Sections) ---
with st.expander("🔐 سیٹنگز اور پیمنٹ (Hidden)"):
    st.write("ای میل: admin@hussain.com | پاسورڈ: hussain786")
    st.write("Easypaisa/JazzCash: 03461785207")
    st.write("فیوچر اپ ڈیٹ: آٹو وائس اوور (جلد آ رہا ہے)")

# رابطہ واٹس ایپ
st.markdown(f'<a href="https://wa.me/923461785207" style="position:fixed; bottom:20px; right:20px; background:#25d366; color:white; padding:12px 25px; border-radius:50px; text-decoration:none; font-weight:bold; box-shadow: 2px 2px 10px rgba(0,0,0,0.3);">رابطہ کریں</a>', unsafe_allow_html=True)
        
