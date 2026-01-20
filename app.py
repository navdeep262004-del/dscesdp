import streamlit as st
from groq import Groq

import streamlit as st
import base64

def set_bg_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
st.set_page_config("PragyanAI Content Generator", layout="wide")
set_bg_image("image.jpg")
st.set_page_config("PragyanAI Content Generator", layout="wide")

st.markdown("""
<style>
[data-testid="stVerticalBlock"] {
    background: rgba(0, 0, 0, 0.6);
    padding: 2rem;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title(" OHMIES - YOUR NEIGHBOURHOOD AI 🫦")

client = Groq(api_key=st.secrets["navdeep"])

col1, col2 = st.columns(2)

with col1:
    product = st.text_input("Product")
    audience = st.text_input("Audience")

    if st.button("Generate Content"):
        prompt = f"Write marketing content for {product} targeting {audience}."
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        st.session_state.text = response.choices[0].message.content

with col2:
    if "text" in st.session_state:
        content = st.text_area("Generated Content", st.session_state.text, height=300)

        st.download_button(
            label="⬇️ Download as TXT",
            data=content,
            file_name="marketing_copy.txt",
            mime="text/plain"
        )
    else:
        st.info("Generate content first")
