# 🎙 Personalized Voice Assistant (Alexa-like AI)

A Python-based intelligent voice assistant that can listen to voice commands, understand user intent using machine learning, and perform tasks such as opening websites, playing music, and responding with speech.

## 🚀 Features

* 🎤 Speech Recognition (Speech → Text)
* 🗣 Text to Speech responses
* 🧠 Machine Learning Intent Classification
* 🌐 Open websites like YouTube and Google
* 🎵 Play music from local system
* 🧩 Modular project architecture
* ⚡ Fast NLP using Naive Bayes and Scikit-learn

## 🏗 Project Architecture

```
voice-assistant/
│
├── main.py
│
├── assistant/
│   ├── speech_to_text.py      # Converts user speech → text
│   └── text_to_speech.py      # Converts text → speech response
│
├── commands/
│   ├── open_apps.py           # Opens websites like YouTube, Google
│   └── play_music.py          # Plays music from local system
│
├── ml/
│   ├── intent_classifier.py   # Machine Learning model for intent detection
│   └── training_data.json     # Training dataset for intents
│
├── utils/
│   └── helpers.py             # Helper utility functions
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🧠 How It Works

```
User Speech
     ↓
Speech Recognition
     ↓
Text Command
     ↓
Machine Learning Intent Classifier
     ↓
Command Execution
     ↓
Voice Response
```
🧩 System Architecture
The assistant follows a modular pipeline-based architecture:

```id="3n6e8b"
[ Microphone Input ]
          ↓
[ Speech Recognition Module ]
          ↓
[ Text Processing ]
          ↓
[ Machine Learning Intent Classifier ]
          ↓
[ Command Execution Layer ]
          ↓
[ Text-to-Speech Engine ]
          ↓
[ Audio Output ]
```

### Explanation

* **Speech Recognition Module**
  Captures audio input and converts it into text using SpeechRecognition.

* **Intent Classifier (ML Model)**
  Uses Natural Language Processing to predict user intent from text.

* **Command Execution Layer**
  Maps predicted intent to specific functions like opening apps or playing music.

* **Text-to-Speech Engine**
  Converts response text into audible speech using pyttsx3.


## 🛠 Tech Stack

* Python
* SpeechRecognition
* Pyttsx3
* Scikit-learn
* PyAudio
* JSON

## ⚙ Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/voice-assistant.git

Navigate to the project folder

cd voice-assistant

Create virtual environment

python -m venv venv

Activate environment

Windows
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the assistant

python main.py

## 🎯 Example Commands

hello
open youtube
open google
play music
exit

## 📚 Future Improvements

* Wake word detection ("Hey Assistant")
* Weather API integration
* Smart home automation
* ChatGPT integration
* Context-aware conversation

## 👩‍💻 Author

Shubhi Tiwari
B.Tech Computer Science Student

GitHub: https://github.com/shubhitiwariiii
