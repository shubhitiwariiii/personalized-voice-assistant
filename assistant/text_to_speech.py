import pyttsx3
import time

def speak(text):
    try:
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate', 170)

        engine.say(text)
        engine.runAndWait()

        time.sleep(0.5)   # small buffer

    except Exception as e:
        print("Speech Error:", e)