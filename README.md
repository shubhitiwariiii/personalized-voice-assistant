# 🎙 AI-Powered Personalized Voice Assistant

A Python-based intelligent voice assistant inspired by Alexa, capable of understanding voice commands, detecting intents using Machine Learning, and generating responses using a local AI model (LLaMA3 via Ollama). The assistant includes a GUI interface and supports personalized interactions.

---

## 🚀 Features

* 🎤 Speech Recognition (Speech → Text)
* 🗣 Text-to-Speech (Voice Output)
* 🧠 ML-based Intent Classification (Naive Bayes)
* 🎯 Dynamic Command Execution System
* 🤖 AI Responses using Local LLM (LLaMA3 via Ollama)
* 🧩 Memory System (JSON-based personalization)
* 🖥 GUI Interface (Tkinter)
* ⚡ Multithreading for smooth UI
* 🎨 Dark-themed UI with chat-style interaction

---

## 🛠 Tech Stack

* **Language:** Python
* **Machine Learning:** Scikit-learn (Naive Bayes, CountVectorizer)
* **Speech Processing:** SpeechRecognition, Pyttsx3
* **AI Model:** Ollama (LLaMA3)
* **GUI:** Tkinter
* **Storage:** JSON (memory system)
* **Other:** Threading, Requests

---

## 📂 Project Structure

```bash
voice-assistant/
│
├── main.py
├── gui.py
│
├── assistant/
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   ├── wake_word.py
│   └── chatgpt.py
│
├── commands/
│   ├── open_apps.py
│   └── play_music.py
│
├── ml/
│   ├── intent_classifier.py
│   └── training_data.json
│
├── utils/
│   ├── memory.py
│   └── memory.json
│
├── requirements.txt
└── README.md
```

---

## 🧠 System Architecture

```
User Voice Input
        ↓
Speech Recognition
        ↓
Intent Classification (ML)
        ↓
 ┌────────────────────────────┐
 │ Known Intent               │ → Execute Command
 └────────────────────────────┘
        ↓
 ┌────────────────────────────┐
 │ Unknown Query              │ → LLM (Ollama)
 └────────────────────────────┘
        ↓
Text-to-Speech Output
```

---

## 🧠 Key Components

### 🎤 Speech Recognition

* Converts voice input into text using Google Speech API.

### 🗣 Text-to-Speech

* Uses pyttsx3 for offline speech output.

### 🧠 Intent Classifier

* Multinomial Naive Bayes model with Bag-of-Words.
* Uses confidence threshold for unknown queries.

### 🤖 AI Integration

* Local LLM (LLaMA3 via Ollama) for open-ended queries.
* No API cost, works offline.

### 🧩 Memory System

* Stores user-specific data in JSON.
* Enables personalized interaction.

### 🖥 GUI System

* Built using Tkinter.
* Includes chat-style interface and status indicators.

### ⚡ Multithreading

* Prevents GUI freezing.
* Uses threading + `root.after()` for safe updates.

### 🔄 Command System

* Dynamic command mapping using dictionary.
* Scalable and maintainable design.

---

## ⚙ Installation

### 1. Clone Repository

```bash
git clone https://github.com/shubhitiwariiii/personalized-voice-assistant
cd personalized-voice-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download from: https://ollama.com/download

Run model:

```bash
ollama run llama3
```

### 5. Run GUI

```bash
python gui.py
```

---

## 🎯 Example Commands

* "Open YouTube"
* "Play music"
* "What is artificial intelligence?"
* "My name is Shubhi"
* "What is my name?"

---

## ⚠️ Challenges & Solutions

| Challenge         | Solution                   |
| ----------------- | -------------------------- |
| GUI freezing      | Used threading             |
| Thread safety     | Used `root.after()`        |
| API quota issue   | Switched to Ollama         |
| Speech issues     | Reinitialized TTS engine   |
| Wrong predictions | Added confidence threshold |

---

## 📚 Future Improvements

* 🎨 UI animations (mic effects, typing)
* 🧠 Context-aware conversations
* 🔊 Offline speech recognition (Vosk)
* 📱 Web or mobile interface

---

## 👩‍💻 Author

**Shubhi Tiwari**
🔗 GitHub: https://github.com/shubhitiwariiii

---

## ⭐ Project Status

✅ Completed 
🚀 Open for improvements and scaling
