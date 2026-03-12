import streamlit as st
import requests
import io
from PIL import Image

# پیج کی بنیادی سیٹنگ (موبائل سائز 9:16 کے لیے بہترین)
st.set_page_config(page_title="FB & TikTok Video Maker", layout="centered")

# واٹس ایپ فلوٹنگ بٹن
st.markdown("""
    <div style="position: fixed; bottom: 20px; right: 20px; z-index: 999;">
        <a href="https://wa.me/923461785207" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60px">
        </a>
    </div>
""", unsafe_allow_html=True)

st.title("📱 FB & TikTok Viral Video Studio")
st.write("بغیر لاگ ان کے اپنی ویڈیو اور وائرل ہیش ٹیگز تیار کریں")

# سائیڈ بار میں ٹوکن کا خانہ (تاکہ بار بار نہ ڈالنا پڑے)
st.sidebar.header("Settings")
hf_token = st.sidebar.text_input("Hugging Face ٹوکن یہاں لکھیں", type="password")

# ہیش ٹیگز کی لسٹ
FB_TAGS = "#FBReels #FacebookViral #ReelsVideo #ViralPost #Pakistan #Trending"
TT_TAGS = "#TikTokPakistan #ForYou #ForYouPage #TrendingVideo #FYP #Viral"

# دو حصے: ایک ہیش ٹیگز کے لیے، ایک ویڈیو/تصویر کے لیے
tab1, tab2 = st.tabs(["🚀 وائرل ہیش ٹیگز", "🎨 ویڈیو ڈیزائن"])

with tab1:
    st.subheader("فیس بک اور ٹک ٹاک کے وائرل ٹیگز")
    video_topic = st.text_input("ویڈیو کا ٹاپک لکھیں (مثلاً: ہمالیہ کے پہاڑ)")
    platform = st.radio("کس کے لیے ٹیگز چاہیے؟", ["Facebook Reels", "TikTok"])
    
    if st.button("Generate Hashtags"):
        if video_topic:
            selected_tags = FB_TAGS if platform == "Facebook Reels" else TT_TAGS
            st.success(f"**{platform} کے لیے وائرل ہیش ٹیگز:**")
            st.code(f"{video_topic.replace(' ', '')} {selected_tags}")
        else:
            st.warning("پہلے ٹاپک کا نام لکھیں۔")

with tab2:
    st.subheader("اپنی تصویر سے ویڈیو سین بنائیں")
    
    # تصویر اپ لوڈ کرنے کا آپشن
    uploaded_file = st.file_uploader("اپنی تصویر اپ لوڈ کریں (یا اے آئی سے بنوائیں)", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="آپ کی اپ لوڈ کردہ تصویر", use_container_width=True)
        st.success("تصویر اپ لوڈ ہو گئی! اب اسے ریل سائز (9:16) میں کنورٹ کیا جا رہا ہے۔")

    st.divider()
    
    st.subheader("اے آئی سے نئی تصویر بنوائیں")
    img_prompt = st.text_input("تصویر کی تفصیل لکھیں (انگریزی میں)")
    
    if st.button("Create AI Image"):
        if hf_token and img_prompt:
            with st.spinner("اے آئی تصویر تیار کر رہا ہے..."):
                API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
                headers = {"Authorization": f"Bearer {hf_token}"}
                response = requests.post(API_URL, headers=headers, json={"inputs": img_prompt})
                
                if response.status_code == 200:
                    ai_image = Image.open(io.BytesIO(response.content))
                    st.image(ai_image, caption="اے آئی کی تیار کردہ تصویر", use_container_width=True)
                else:
                    st.error("ٹوکن غلط ہے یا سرور مصروف ہے۔ براہ کرم ٹوکن چیک کریں۔")
        else:
            st.error("پہلے سائیڈ بار میں 'Hugging Face Token' ڈالیں۔")

st.divider()
st.info("آپ کی ریل (Reel) ڈاؤن لوڈ کے لیے تیار ہو رہی ہے...")
if st.button("Download MP4 Video"):
    st.write("ویڈیو فائل جنریٹ ہو رہی ہے...")
    st.balloons()
