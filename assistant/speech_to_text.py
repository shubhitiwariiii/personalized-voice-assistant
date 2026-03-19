import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)

            print("You said:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            print("Listening timeout...")
            return ""

        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return ""

        except sr.RequestError:
            print("API error.")
            return ""