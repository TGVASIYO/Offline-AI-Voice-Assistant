<div align="center">

# 🎙️ Offline AI Voice Assistant

### *An assistant with ears and a mouth — that never needs the internet.*

![Status](https://img.shields.io/badge/status-in%20progress-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Offline](https://img.shields.io/badge/runs-100%25%20offline-2ea44f?style=for-the-badge)
![License](https://img.shields.io/badge/license-TBD-lightgrey?style=for-the-badge)

</div>

---

## 🌟 Overview

This project is an AI-powered voice assistant designed to work **completely offline** — no cloud, no API calls, no internet connection required.

Unlike Siri, Alexa, or Google Assistant, everything happens **on the device itself**:

| 👂 Ears | 🧠 Brain | 🗣️ Mouth |
|:---:|:---:|:---:|
| Listens to speech | Understands & responds | Speaks the answer back |

---

## 💡 Why Offline?

| Problem with cloud assistants | 🔧 How this project solves it |
|---|---|
| 🌐 Needs constant internet | Runs fully on-device |
| 🔓 Sends your voice to servers | 100% private — nothing leaves your machine |
| 🐢 Network lag on every request | Local inference = faster response |

---

## 🛠️ Planned Tech Stack

> *Still being finalized — this is the current direction!*

| Layer | Tool (candidate) | Badge |
|---|---|---|
| 🎤 Speech-to-Text | Whisper / whisper.cpp | ![Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?style=flat-square&logo=openai&logoColor=white) |
| 🧠 Language Model | Local LLM via Ollama (Gemma / Phi) | ![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=flat-square) |
| 🔊 Text-to-Speech | Piper TTS | ![Piper](https://img.shields.io/badge/Piper-TTS-FF6B6B?style=flat-square) |
| 🐍 Language | Python | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) |

---

## 🔄 How It Works

```
        🎤  MIC INPUT
            │
            ▼
   ┌─────────────────────┐
   │   Speech → Text      │   (Whisper)
   └─────────────────────┘
            │
            ▼
   ┌─────────────────────┐
   │  Local LLM Thinks 🧠  │   (Ollama)
   └─────────────────────┘
            │
            ▼
   ┌─────────────────────┐
   │   Text → Speech       │   (Piper)
   └─────────────────────┘
            │
            ▼
        🔊  SPOKEN REPLY
```

**Zero cloud calls. Zero data leaves the device.** ✅

---

## ✅ Goals / Roadmap

- [x] Define project concept & pipeline
- [ ] Finalize the tech stack (STT / LLM / TTS)
- [ ] Build working end-to-end pipeline
- [ ] Optimize latency on limited hardware
- [ ] Add wake-word detection 🎯
- [ ] Package into an easy-to-run app 📦

---

## 🚀 Getting Started

> Setup instructions coming soon — once the pipeline is working!

---

## 👤 Author

<div align="center">

**Priyabrata Patra**
Integrated M.Tech, Computer Science & Engineering (Artificial Intelligence)
Vellore Institute of Technology, Bhopal

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/priyabrata-patra-bb47b0366)

</div>

---

<div align="center">
<sub>⭐ Star this repo if you're curious where it goes!</sub>
</div>
