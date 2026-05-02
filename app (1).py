import os
import whisper
import streamlit as st
from groq import Groq
from gtts import gTTS
import tempfile
import re

# 🔐 Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# ✅ Load Whisper model (base = best balance for Hugging Face)
@st.cache_resource
def load_model():
    return whisper.load_model("base")

whisper_model = load_model()

# 🔁 Summarization function
def summarize_audio(audio_path):
    # Step 1: Transcribe with Whisper
    result = whisper_model.transcribe(audio_path)
    transcript = result["text"]

    # Step 2: Summarize with Groq (LLaMA3)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes casual audio conversations."},
            {"role": "user", "content": f"Summarize this transcript in 2-3 lines:\n\n{transcript}"}
        ]
    )
    raw_summary = response.choices[0].message.content.strip()

    # 🧹 Clean unwanted phrases like "Here is a 2-3 line summary:"
    summary_text = re.sub(r'(?i)^.*summary.*?:\s*', '', raw_summary).strip()

    # Step 3: Convert summary to speech (MP3)
    tts = gTTS(text=summary_text, lang='en')
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio.name)

    return transcript, summary_text, temp_audio.name

# 🎨 Streamlit UI
st.set_page_config(page_title="🎙️ English Audio Summarizer", page_icon="😻", layout="wide")

# Custom CSS for Beautiful UI
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Centered Header */
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #fff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
    }

    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        color: #f1f1f1;
    }

    /* Card Style */
    .stTextArea, .stTextInput, .stFileUploader, .stAudio, .stDownloadButton button {
        border-radius: 15px !important;
        background: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        padding: 10px;
    }

    .stSuccess, .stInfo {
        background-color: rgba(0, 0, 0, 0.25);
        color: white !important;
        border-radius: 15px;
        padding: 10px;
    }

    /* Buttons */
    .stDownloadButton button, .stButton button {
        background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: bold;
        padding: 8px 18px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    .stDownloadButton button:hover, .stButton button:hover {
        background: linear-gradient(135deg, #ff5f6d 0%, #ffc371 100%) !important;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-title'>😻🎙️ English Audio Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Upload an audio file, get a transcript, summary, and listen back instantly.</p>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("📂 Upload Audio File (MP3/WAV/OPUS)", type=["mp3", "wav", "opus"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.info("⏳ Processing your audio... Please wait...")
    transcript, summary_text, summary_audio = summarize_audio(tmp_path)

    st.subheader("📜 Full Transcript")
    st.text_area("Transcript", transcript, height=200)

    st.subheader("📝 Summarized Text")
    st.success(summary_text)

    st.subheader("🔊 Summary Audio")
    st.audio(summary_audio, format="audio/mp3")

    # Download button for summary audio
    with open(summary_audio, "rb") as f:
        st.download_button(
            label="⬇️ Download Summary Audio",
            data=f,
            file_name="summary.mp3",
            mime="audio/mp3"
        )
