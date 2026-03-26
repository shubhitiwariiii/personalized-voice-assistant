from assistant.speech_to_text import listen
from assistant.text_to_speech import speak
from assistant.wake_word import detect_wake_word
from assistant.chatgpt import ask_chatgpt
from commands.open_apps import open_youtube, open_google
from commands.play_music import play_music
from ml.intent_classifier import IntentClassifier
from utils.memory import remember, recall


def main():
    classifier = IntentClassifier()

    while True:
    # Wait for wake word
        detect_wake_word()

        speak("Yes, I am listening")

        # 🔥 FIRST get command
        command = listen()
        commands_map = {
            "open_youtube": open_youtube,
            "open_google": open_google,
            "play_music": play_music
        }

        if command == "":
            continue

        # 🧠 MEMORY HANDLING (NOW CORRECT PLACE)

        if "my name is" in command:
            name = command.replace("my name is", "").strip()
            remember("name", name)
            speak(f"Okay, I will remember that, {name}")
            continue

        if "what is my name" in command:
            name = recall("name")

            if name:
                speak(f"Your name is {name}")
            else:
                speak("I don't know your name yet")

            continue

        # 🔥 ML INTENT CLASSIFIER

        intent = classifier.predict(command)

        if intent in commands_map:
            speak("Executing command")
            commands_map[intent]()

        elif intent == "greeting":
            speak("Hello!")

        elif intent == "unknown":
            speak("Let me think...")
            response = ask_chatgpt(command)
            speak(response)

        elif intent == "exit":
            speak("Going back to sleep")

        else:
            speak("Sorry, I don't understand")
if __name__ == "__main__":
    main()