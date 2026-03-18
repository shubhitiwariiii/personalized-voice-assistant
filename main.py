from assistant.speech_to_text import listen
from assistant.text_to_speech import speak
from commands.open_apps import open_youtube, open_google
from commands.play_music import play_music
from ml.intent_classifier import IntentClassifier


def main():
    speak("Hello Shubhi. I am your assistant.")

    classifier = IntentClassifier()

    while True:
        command = listen()

        if command == "":
            continue

        intent = classifier.predict(command)
        print("Detected intent:", intent)

        if intent == "greeting":
            speak("Hello! How can I help you?")

        elif intent == "open_youtube":
            speak("Opening YouTube")
            open_youtube()

        elif intent == "open_google":
            speak("Opening Google")
            open_google()

        elif intent == "exit":
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I don't know how to do that yet.")


if __name__ == "__main__":
    main()