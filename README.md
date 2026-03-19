# 🎙 Personalized Voice Assistant (AI Powered)

A Python-based intelligent voice assistant inspired by Alexa, capable of understanding voice commands, detecting wake words, and responding using Machine Learning and a local AI model (LLaMA3 via Ollama).

---

## 🚀 Features

* 🎤 Speech Recognition (Speech → Text)
* 🗣 Text-to-Speech (Voice Output)
* 🧠 Machine Learning Intent Classification
* 🎯 Wake Word Detection (e.g., "Hey Assistant")
* 🤖 AI-powered responses using **Ollama (LLaMA3)**
* 🌐 Open websites (YouTube, Google)
* 🎵 Play music from local system
* ⚡ Optimized response time
* 🧩 Modular architecture

---

## 🛠 Tech Stack

### 👨‍💻 Programming Language

* Python

### 🧠 Machine Learning & NLP

* Scikit-learn (Naive Bayes, CountVectorizer)
* Natural Language Processing (Intent Classification)

### 🎤 Speech Processing

* SpeechRecognition
* Pyttsx3
* PyAudio

### 🤖 AI / LLM

* Ollama (Local AI Runtime)
* LLaMA3 Model

### 🌐 System & Utilities

* Requests
* Webbrowser
* OS Module

### ⚙ Development Tools

* VS Code
* Git & GitHub

### 🧩 Architecture Style

* Modular Architecture
* Event-driven System (Wake Word Activation)
* Hybrid AI System (ML + LLM)

---

## 📂 Project Architecture

```bash
voice-assistant/
│
├── main.py
│
├── assistant/
│   ├── speech_to_text.py      # Speech → Text
│   ├── text_to_speech.py      # Text → Speech
│   ├── wake_word.py           # Wake word detection
│   └── chatgpt.py             # AI (Ollama integration)
│
├── commands/
│   ├── open_apps.py           # Open websites
│   └── play_music.py          # Play local music
│
├── ml/
│   ├── intent_classifier.py   # ML model
│   └── training_data.json     # Training dataset
│
├── utils/
│   └── helpers.py             # Utility functions
│
├── requirements.txt
└── README.md
```
## 🧠 System Architecture

```text
Microphone Input
        ↓
Wake Word Detection
        ↓
Speech Recognition
        ↓
Intent Classifier (ML)
        ↓
 ┌─────────────────────────────┐
 │ Known Intent                │ → Execute Command
 └─────────────────────────────┘
        ↓
 ┌─────────────────────────────┐
 │ Unknown Input               │ → Local AI (LLaMA3 via Ollama)
 └─────────────────────────────┘
        ↓
Text-to-Speech Output
```

---

## 🤖 Machine Learning Model

* Algorithm: Multinomial Naive Bayes
* Vectorization: Bag of Words (CountVectorizer)

### Pipeline:

1. Convert text → numerical vectors
2. Train model on intents
3. Predict user intent
4. Execute command or call AI

---

## 🤖 AI Integration (Offline)

* Model: LLaMA3
* Runtime: Ollama
* Works completely offline

### Advantages:

* No API cost
* Faster response
* Privacy-friendly

---

## ⚙ Installation

### 1. Clone Repository

git clone https://github.com/shubhitiwariiii/PERSONALIZED-VOICE-ASSISTANT.git
cd personalized-voice-assistant

### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Install Ollama

Download from: https://ollama.com/download

Run model:
ollama run llama3

### 5. Run Project

python main.py

---

## 🎯 Example Commands

* "Hey assistant"
* "Open YouTube"
* "Play music"
* "What is artificial intelligence?"
* "Exit"

---

## ⚡ Key Highlights

* Event-driven wake word system
* ML + AI hybrid architecture
* Offline AI assistant using Ollama
* Optimized speech pipeline
* Clean modular code structure

---

## 📚 Future Improvements

* 🧠 Memory system (personalization)
* 🌦 Weather API integration
* 📱 GUI interface
* 🔐 Face recognition login
* 🔊 Offline speech recognition

---

## 👩‍💻 Author

**Shubhi Tiwari**
B.Tech Computer Science

🔗 GitHub: https://github.com/shubhitiwariiii

---

## ⭐ Project Status

🚀 Actively improving with advanced AI features
