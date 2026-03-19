import speech_recognition as sr

def detect_wake_word():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Say wake word to activate...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio).lower()

                print("Heard (wake):", text)

                if any(word in text for word in ["hey shubhi", "hello krishna", "hey assistant"]):
                    print("✅ Wake word detected!")
                    return

            except:
                continue