from assistant.speech_to_text import listen
from assistant.text_to_speech import speak
from assistant.wake_word import detect_wake_word
from assistant.chatgpt import ask_chatgpt
from commands.open_apps import open_youtube, open_google
from commands.play_music import play_music
from ml.intent_classifier import IntentClassifier


def main():
    classifier = IntentClassifier()

    while True:
        # Wait for wake word
        detect_wake_word()

        speak("Yes, I am listening")

        # Now process ONE command
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
            speak("Going back to sleep")
            continue

        elif intent == "unknown":
            print("⚡ Entered AI block")

            speak("Let me think...")

            response = ask_chatgpt(command)

            print("RAW AI RESPONSE:", response)

            if not response or response.strip() == "":
                speak("I could not generate a response")
                return

            # 🔥 Clean response
            clean_response = response.replace("*", "").replace("\n", " ")

            short_response = clean_response[:150]

            print("Speaking:", short_response)

            speak(short_response)
        else:
            speak("Sorry, I don't understand")
if __name__ == "__main__":
    main()