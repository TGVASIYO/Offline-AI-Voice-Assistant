# 🤖 AURA — Offline AI Voice Assistant

<p align="center">
  <b>Private by Design • Natural by Default</b>
</p>

<p align="center">
  An intelligent, voice-enabled AI assistant designed to run locally,
  combining speech recognition, an AI brain, memory, and natural voice interaction.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![AI](https://img.shields.io/badge/AI-Local%20AI-purple?style=for-the-badge)
![STT](https://img.shields.io/badge/STT-Whisper-orange?style=for-the-badge)
![TTS](https://img.shields.io/badge/TTS-Piper-green?style=for-the-badge)
![Wake Word](https://img.shields.io/badge/Wake%20Word-openWakeWord-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge)

</p>

---

## 🧠 What is AURA?

**AURA** is a localized AI voice assistant built with the goal of providing a more **private, natural, and interactive AI experience**.

Instead of depending entirely on cloud-based services, AURA is designed around **local/offline components wherever practical**.

The assistant listens for its wake word, converts speech into text, processes the request through its AI brain, and converts the generated response back into natural speech.

### ✨ Core Idea

> **Speak → Understand → Think → Respond → Speak**

---

# ⚡ AURA at a Glance

```text
                         ┌─────────────────┐
                         │      👤 USER    │
                         └────────┬────────┘
                                  │
                             🎙️ Voice Input
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │   🔔 WAKE WORD          │
                    │      openWakeWord       │
                    │     "Hey AURA"          │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   🎧 SPEECH TO TEXT     │
                    │         Whisper          │
                    └────────────┬────────────┘
                                 │
                              Text
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      🧠 AURA BRAIN      │
                    │       Qwen 4B            │
                    │                         │
                    │ Understanding           │
                    │ Reasoning               │
                    │ Response Generation     │
                    └────────────┬────────────┘
                                 │
                           Response Text
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      🔊 TEXT TO SPEECH  │
                    │          Piper          │
                    └────────────┬────────────┘
                                 │
                              🔊 Voice
                                 │
                                 ▼
                         ┌───────────────┐
                         │ 👤 USER HEARS │
                         └───────────────┘
```

---

# 🏗️ System Architecture

```text
┌────────────────────────────────────────────────────────────┐
│                         AURA                               │
│                                                            │
│  ┌──────────┐     ┌───────────┐     ┌──────────────────┐  │
│  │ 🎙️ Mic   │ ──▶ │ Wake Word │ ──▶ │   Speech to Text │  │
│  │          │     │ openWake  │     │      Whisper     │  │
│  └──────────┘     └───────────┘     └────────┬─────────┘  │
│                                               │            │
│                                               ▼            │
│                                    ┌──────────────────┐   │
│                                    │    🧠 AI BRAIN   │   │
│                                    │      Qwen 4B     │   │
│                                    │                  │   │
│                                    │ • Understanding  │   │
│                                    │ • Reasoning      │   │
│                                    │ • Response       │   │
│                                    └────────┬─────────┘   │
│                                             │             │
│                                             ▼             │
│                                    ┌──────────────────┐   │
│                                    │   Text to Speech │   │
│                                    │      Piper       │   │
│                                    └────────┬─────────┘   │
│                                             │             │
│                                             ▼             │
│                                         🔊 Speaker        │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

# 🧩 Core Components

| Component         | Technology                                 | Purpose                                        |
| ----------------- | ------------------------------------------ | ---------------------------------------------- |
| 🔔 Wake Word      | **openWakeWord**                           | Detects `"Hey AURA"`                           |
| 🎧 Speech-to-Text | **Whisper**                                | Converts speech → text                         |
| 🧠 AI Brain       | **Qwen 4B**                                | Understands input and generates responses      |
| 🔊 Text-to-Speech | **Piper**                                  | Converts text → spoken response                |
| 💾 Memory         | SQLite / Vector DB *(planned)*             | Stores useful conversational context           |
| 🔎 RAG            | Retrieval-Augmented Generation *(planned)* | Provides relevant stored information to the AI |
| 🖥️ Interface     | 2D / expressive UI *(planned)*             | Visual interaction with AURA                   |

---

# 🔄 How AURA Works

### 1️⃣ Wake Word Detection

AURA continuously monitors the microphone for the activation phrase:

```text
"Hey AURA"
```

The wake-word component detects the phrase before the main voice-processing pipeline begins.

---

### 2️⃣ Speech Recognition

After activation, the user's speech is captured and processed by **Whisper**.

```text
🎙️ "Hey AURA, what is machine learning?"

                    ↓

        Whisper Speech Recognition

                    ↓

"What is machine learning?"
```

---

### 3️⃣ AI Processing

The recognized text is sent to the **Qwen 4B** local AI model.

```text
User Text
    ↓
Qwen 4B
    ↓
Understanding
    ↓
Reasoning
    ↓
Response Generation
```

---

### 4️⃣ Voice Response

The generated response is passed to **Piper**.

```text
AI Response
     ↓
   Piper
     ↓
   🔊 Voice
```

AURA then speaks the response through the speaker.

---

# 🧠 AI Pipeline

```text
             USER
               │
               ▼
        ┌─────────────┐
        │  Microphone │
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │ Wake Word   │
        │ openWakeWord│
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │   Whisper   │
        │     STT     │
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │   Qwen 4B   │
        │  AI Brain   │
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │    Piper    │
        │     TTS     │
        └──────┬──────┘
               ▼
             🔊
            AUDIO
```

---

# 🔐 Why Local AI?

AURA follows a **local-first approach**.

### ☁️ Traditional Cloud Assistant

```text
User
 ↓
Internet
 ↓
Cloud Server
 ↓
AI Model
 ↓
Internet
 ↓
User
```

### 🖥️ AURA

```text
User
 ↓
Local Computer
 ↓
Local AI Pipeline
 ↓
Response
 ↓
User
```

### Benefits

* 🔒 Greater privacy
* 🌐 Reduced dependence on internet connectivity
* ⚡ Potentially lower interaction latency
* 💻 Local processing
* 🧩 More control over the AI pipeline

> AURA aims to keep sensitive voice and conversational data local wherever the implementation allows.

---

# 🧠 Planned Memory + RAG

AURA can be extended with a memory system.

```text
                User Query
                    │
                    ▼
             ┌─────────────┐
             │   Memory    │
             │   Search    │
             └──────┬──────┘
                    │
             Relevant Context
                    │
                    ▼
             ┌─────────────┐
             │   Qwen 4B   │
             │   AI Brain  │
             └──────┬──────┘
                    │
                    ▼
                Response
```

### RAG can help AURA:

* 📚 Retrieve stored information
* 🧠 Provide conversational context
* 🔎 Search a local knowledge base
* 📄 Answer questions from selected documents
* 💾 Improve personalized interactions

---

# 📁 Project Structure

```text
AURA/
│
├── main.py
│
├── voice/
│   ├── wake_word.py
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── tts/
│   └── piper/
│
├── audio/
│   └── input.wav
│
├── models/
│
├── memory/
│
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact folder structure may evolve as additional AURA modules are integrated.

---

# 🛠️ Technology Stack

```text
                 AURA TECHNOLOGY STACK

       ┌──────────────────────────────┐
       │       🐍 Python 3.12         │
       └──────────────┬───────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   openWakeWord    Whisper        Piper
     🔔 Wake       🎧 STT         🔊 TTS
                      │
                      ▼
                 Qwen 4B
                  🧠 AI
                      │
              ┌───────┴───────┐
              ▼               ▼
           SQLite            RAG
          💾 Memory        🔎 Retrieval
```

---

# 🚀 Current Development Status

| Feature                          | Status         |
| -------------------------------- | -------------- |
| Python environment               | ✅ Completed    |
| Microphone recording             | ✅ Completed    |
| Whisper STT                      | ✅ Working      |
| Piper TTS                        | ✅ Working      |
| openWakeWord installation        | ✅ Completed    |
| `"Hey AURA"` wake-word detection | 🔄 Integration |
| Qwen 4B integration              | 🔄 Development |
| AI response pipeline             | 🔄 Development |
| Memory                           | 🔜 Planned     |
| RAG                              | 🔜 Planned     |
| Emotion state                    | 🔜 Planned     |
| 2D Avatar                        | 🔜 Planned     |
| Full offline assistant           | 🔄 Development |

---

# 🎯 Project Goals

### 🔒 Privacy

Keep processing local wherever possible.

### 🗣️ Natural Interaction

Make interaction feel conversational rather than command-based.

### 🧠 Intelligence

Use a local AI model to understand and respond to user requests.

### ⚡ Accessibility

Allow users to interact naturally through voice.

### 🧩 Modularity

Keep AURA's voice, AI, memory, and interface components modular so they can be improved independently.

---

# 🧪 Example Interaction

```text
👤 User:
"Hey AURA"

        ↓

🔔 Wake Word Detected

        ↓

🎙️ User:
"What is artificial intelligence?"

        ↓

🎧 Whisper:
"What is artificial intelligence?"

        ↓

🧠 Qwen 4B:
Generates response

        ↓

🔊 Piper:
Speaks the response

        ↓

🤖 AURA:
"Artificial intelligence is..."
```

---

# 📸 Screenshots

### 🎙️ Voice Input

> Add screenshot here

```text
[ SCREENSHOT ]
```

### 🔔 Wake Word Detection

> Add screenshot here

```text
[ SCREENSHOT ]
```

### 🧠 AI Response

> Add screenshot here

```text
[ SCREENSHOT ]
```

### 🔊 Voice Output

> Add screenshot here

```text
[ SCREENSHOT ]
```

---

# 📊 Future Roadmap

```text
                    AURA ROADMAP

      ┌─────────────────────────────┐
      │ Phase 1                     │
      │ 🎙️ Voice Pipeline           │
      │ STT + TTS + Wake Word       │
      └──────────────┬──────────────┘
                     ▼
      ┌─────────────────────────────┐
      │ Phase 2                     │
      │ 🧠 Local AI Brain           │
      │ Qwen + Ollama               │
      └──────────────┬──────────────┘
                     ▼
      ┌─────────────────────────────┐
      │ Phase 3                     │
      │ 💾 Memory + RAG             │
      │ Context + Knowledge         │
      └──────────────┬──────────────┘
                     ▼
      ┌─────────────────────────────┐
      │ Phase 4                     │
      │ 🎭 Interactive Avatar       │
      │ Emotion + Animation         │
      └──────────────┬──────────────┘
                     ▼
      ┌─────────────────────────────┐
      │ Phase 5                     │
      │ 🚀 Full AI Assistant        │
      │ Local + Natural + Personal  │
      └─────────────────────────────┘
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/TGVASIYO/AURA.git
cd AURA
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run AURA

```bash
python main.py
```

---

# 📦 Dependencies

Core components currently include:

```text
Python
Whisper
openWakeWord
Piper
PyAudio
NumPy
```

Additional dependencies will be added as the AI brain, memory, RAG, and interface modules are integrated.

---

# 👨‍💻 Team AURA

**AURA is being developed as a collaborative project with modular responsibilities across the team.**

### Voice Module

Responsible for:

* 🎙️ Speech input
* 🎧 Speech-to-Text
* 🔔 Wake-word detection
* 🔊 Text-to-Speech integration

---

# 📚 Learning Focus

This project explores:

* Artificial Intelligence
* Speech Recognition
* Natural Language Processing
* Local/Offline AI
* Large/Small Language Models
* Text-to-Speech
* Retrieval-Augmented Generation
* Vector-based memory
* Human-AI interaction

---

# 🌟 Vision

> **AURA is not just designed to answer questions.
> It is designed to become a private, natural and locally running AI companion.**

```text
        ┌──────────────────────────────┐
        │                              │
        │       PRIVATE BY DESIGN      │
        │                              │
        │      NATURAL BY DEFAULT      │
        │                              │
        │           🤖 AURA            │
        │                              │
        └──────────────────────────────┘
```

---

## 📄 Project Documentation

Additional project documentation, architecture diagrams, testing information and design documents can be found in the `docs/` directory.

---

## ⭐ Support the Project

If you find the project interesting, consider giving the repository a ⭐.

---

<p align="center">
  <b>Built with Python • AI • Voice • Curiosity</b>
</p>

<p align="center">
  🤖 <b>AURA — Private by Design. Natural by Default.</b>
</p>
