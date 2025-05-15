import streamlit as st
from post_examples import PostExamples
from post_creator import create_linkedin_post



length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Banglish"]

st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="LI",
    layout="wide"
)

def main():
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🚀 LinkedIn Post Generator</h1>", unsafe_allow_html=True)
    st.markdown("### ✨ Create engaging posts based on topic, tone, and language")

    fs = PostExamples()
    tags = fs.available_tags()

    col1, col2 = st.columns([1.2, 2])

    with col1:
        st.markdown("#### 🎯 Select Your Preferences")

        selected_tag = st.selectbox("📌 Topic", options=tags)
        selected_length = st.selectbox("📏 Post Length", options=length_options)
        selected_language = st.selectbox("🌐 Language", options=language_options)

        generate = st.button("✨ Generate Post")

    with col2:
        st.markdown("#### ✅ Generated Post:")
        if 'generated_post' not in st.session_state:
            st.session_state.generated_post = ""

        if generate:
            with st.spinner("🧠 Thinking..."):
                st.session_state.generated_post = create_linkedin_post(selected_length, selected_language, selected_tag)

        if st.session_state.generated_post:
            st.success(st.session_state.generated_post)


    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: gray;'>Made with ❤️ by Tahajib Jakir Khan</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
