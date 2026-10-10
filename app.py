import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages.")

languages = {
    "English": "en",
    "Malayalam": "ml",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Korean": "ko"
}

source_options = ["Auto Detect"] + list(languages.keys())
target_options = list(languages.keys())

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Translate from",
        source_options
    )

with col2:
    target = st.selectbox(
        "Translate to",
        target_options,
        index=1
    )

text = st.text_area(
    "Enter your text",
    placeholder="Type something to translate...",
    height=150
)

if st.button("Translate", type="primary"):
    if not text.strip():
        st.warning("Please enter some text.")
    elif source == target:
        st.warning("Choose two different languages.")
    else:
        try:
            source_code = (
                "auto" if source == "Auto Detect"
                else languages[source]
            )

            translator = GoogleTranslator(
                source=source_code,
                target=languages[target]
            )

            result = translator.translate(text)

            st.subheader("Translated Text")
            st.text_area(
                "Translation result",
                value=result,
                height=150
            )

            st.download_button(
                "Download Translation",
                data=result,
                file_name="translation.txt",
                mime="text/plain"
            )

        except Exception as error:
            st.error(
                f"Translation failed :{error}"
            )

st.caption("Built with Python and Streamlit")
