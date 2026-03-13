import streamlit as st

# پیج سیٹنگ
st.set_page_config(page_title="FB & TikTok Video Maker", layout="centered")

st.title("📱 Free FB & TikTok Video Studio")
st.write("بغیر کسی ٹوکن یا لاگ ان کے تصویریں اور وائرل ٹیگز بنائیں")

# واٹس ایپ بٹن
st.markdown("""
    <div style="position: fixed; bottom: 20px; right: 20px; z-index: 999;">
        <a href="https://wa.me/923461785207" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60px">
        </a>
    </div>
""", unsafe_allow_html=True)

# وائرل ہیش ٹیگز
FB_TAGS = "#FBReels #ViralPost #Pakistan #Trending"
TT_TAGS = "#TikTokPakistan #ForYouPage #FYP #Viral"

tab1, tab2 = st.tabs(["🚀 ہیش ٹیگز", "🎨 ویڈیو سین"])

with tab1:
    topic = st.text_input("ویڈیو کا ٹاپک لکھیں")
    platform = st.radio("پلیٹ فارم", ["Facebook Reels", "TikTok"])
    if st.button("Generate Tags"):
        tags = FB_TAGS if platform == "Facebook Reels" else TT_TAGS
        st.code(f"{topic.replace(' ', '')} {tags}")

with tab2:
    img_desc = st.text_input("تصویر کی تفصیل (انگریزی میں لکھیں، مثلا: beautiful village sunset)")
    
    if st.button("Create Image"):
        if img_desc:
            # بغیر ٹوکن والا نیا طریقہ
            encoded_prompt = img_desc.replace(" ", "%20")
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=540&height=960&nologo=true"
            
            st.image(image_url, caption="آپ کی ویڈیو کا سین تیار ہے", use_container_width=True)
            st.success("تصویر تیار ہے! اسے سیو کر کے اپنی ریل میں استعمال کریں۔")
        else:
            st.warning("پہلے تفصیل لکھیں۔")

st.divider()
st.info("نوٹ: اس سسٹم میں کسی ٹوکن کی ضرورت نہیں ہے، یہ ان لمیٹڈ چلے گا۔")
