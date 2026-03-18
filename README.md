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

voice-assistant
│
├── main.py
├── assistant
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── commands
│   ├── open_apps.py
│   └── play_music.py
│
├── ml
│   ├── intent_classifier.py
│   └── training_data.json
│
├── utils
│   └── helpers.py
│
├── requirements.txt
└── README.md

## 🧠 How It Works

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
