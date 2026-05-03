# 🎙️ English Audio Summarizer

An AI-powered tool that converts audio into text, generates a concise summary, and reads it back to you — all in one click!

🔗 **Live Demo:** [Try it on Hugging Face]([https://lnkd.in/gYTFmB-J](https://huggingface.co/spaces/Mahrukhh/English_audio_summarizer))

---

## ✨ What It Does

1. 🎙️ **Speech to Text** — Upload any audio file (MP3/WAV/OPUS) → transcribed using OpenAI Whisper
2. 📝 **Summarization** — Transcript summarized in 2-3 lines using Groq LLaMA3
3. 🔊 **Text to Speech** — Summary converted back to audio using gTTS
4. ⬇️ **Download** — Save the summary audio file

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Frontend UI |
| OpenAI Whisper | Speech-to-text transcription |
| Groq API (LLaMA3) | Text summarization |
| gTTS | Text-to-speech conversion |
| Hugging Face Spaces | Deployment |

---

## 📁 Project Structure

```
english-audio-summarizer/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
└── README.md
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/mahrukhmobin/english-audio-summarizer.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Groq API key as environment variable
export GROQ_API_KEY="your_key_here"

# 4. Run the app
streamlit run app.py
```

---

## 📦 Requirements

```
openai-whisper
groq
gtts
torch
torchaudio
ffmpeg-python
streamlit
```

---

## 💡 Use Cases

- Summarize long voice notes or lectures
- Quickly digest meeting recordings
- Convert audio content into readable + listenable summaries

---

*Built by [Mahrukh Mobin](https://github.com/mahrukhmobin) — Computer Engineering Student @ UET Lahore*
