import tkinter as tk
import threading

from assistant.speech_to_text import listen
from assistant.text_to_speech import speak
from assistant.chatgpt import ask_chatgpt

from ml.intent_classifier import IntentClassifier
from commands.open_apps import open_youtube, open_google
from commands.play_music import play_music
from utils.memory import remember, recall


# 🔥 Command mapping
commands_map = {
    "open_youtube": open_youtube,
    "open_google": open_google,
    "play_music": play_music
}

# 🔥 ML model
classifier = IntentClassifier()


# 🧠 MAIN LOGIC
def run_assistant():
    # Safe UI update
    root.after(0, lambda: status_label.config(text="Listening..."))

    command = listen()

    if command == "":
        root.after(0, lambda: status_label.config(text="Didn't catch that"))
        root.after(0, lambda: start_button.config(state="normal"))
        return

    command = command.lower()

    # Show user input
    root.after(0, lambda: output_text.delete("1.0", tk.END))
    root.after(0, lambda: output_text.insert(tk.END, f"You: {command}\n\n"))

    # 🧠 MEMORY
    if "my name is" in command:
        name = command.replace("my name is", "").strip()
        remember("name", name)

        speak(f"Okay, I will remember that, {name}")

        root.after(0, lambda: output_text.insert(tk.END, f"AI: Got it, {name}\n"))
        root.after(0, lambda: status_label.config(text="Idle"))
        root.after(0, lambda: start_button.config(state="normal"))
        return

    if "what is my name" in command:
        name = recall("name")

        response = f"Your name is {name}" if name else "I don't know your name yet"
        speak(response)

        root.after(0, lambda: output_text.insert(tk.END, f"AI: {response}\n"))
        root.after(0, lambda: status_label.config(text="Idle"))
        root.after(0, lambda: start_button.config(state="normal"))
        return

    # 🧠 ML INTENT
    intent = classifier.predict(command)
    print("Intent:", intent)

    # ⚡ COMMAND EXECUTION
    if intent in commands_map:
        speak("Executing command")

        root.after(0, lambda: output_text.insert(
            tk.END, f"AI: Executing command...\n"
        ))

        commands_map[intent]()

        root.after(0, lambda: status_label.config(text="Idle"))
        root.after(0, lambda: start_button.config(state="normal"))
        return

    elif intent == "greeting":
        name = recall("name")
        response = f"Hello {name}" if name else "Hello!"

        speak(response)

        root.after(0, lambda: output_text.insert(tk.END, f"AI: {response}\n"))
        root.after(0, lambda: status_label.config(text="Idle"))
        root.after(0, lambda: start_button.config(state="normal"))
        return

    elif intent == "exit":
        speak("Going back to sleep")

        root.after(0, lambda: output_text.insert(tk.END, "AI: Going to sleep\n"))
        root.after(0, lambda: status_label.config(text="Idle"))
        root.after(0, lambda: start_button.config(state="normal"))
        return

    # 🤖 AI FALLBACK
    root.after(0, lambda: status_label.config(text="Thinking..."))

    response = ask_chatgpt(command)

    clean = response.replace("*", "").replace("\n", " ")
    short = clean[:150]

    root.after(0, lambda: output_text.insert(
    tk.END, f"👤 You: {command}\n"
    ))

    root.after(0, lambda: output_text.insert(
        tk.END, f"🤖 AI: {short}\n\n"
    ))

    root.after(0, lambda: output_text.see(tk.END))

    root.after(0, lambda: status_label.config(text="Speaking..."))

    speak(short)

    root.after(0, lambda: status_label.config(text="Idle"))
    root.after(0, lambda: start_button.config(state="normal"))


# 🧵 THREAD START
def start_assistant():
    start_button.config(state="disabled")

    thread = threading.Thread(target=run_assistant)
    thread.start()



# 🎨 GUI
root = tk.Tk()
root.title("AI Voice Assistant")
root.geometry("450x550")
root.configure(bg="#1e1e1e")   # 🔥 Dark background


# Title
title = tk.Label(
    root,
    text="🤖 Voice Assistant",
    font=("Helvetica", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=10)


# Status
status_label = tk.Label(
    root,
    text="Idle",
    fg="#00ffcc",
    bg="#1e1e1e",
    font=("Helvetica", 10)
)
status_label.pack(pady=5)


# Output box (chat style)
output_text = tk.Text(
    root,
    height=18,
    width=45,
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    font=("Consolas", 10),
    bd=0
)
output_text.pack(pady=10)


# 🎤 Button
start_button = tk.Button(
    root,
    text="🎤 Start Listening",
    command=start_assistant,
    bg="#00ffcc",
    fg="black",
    font=("Helvetica", 12, "bold"),
    padx=10,
    pady=5
)
start_button.pack(pady=20)


root.mainloop()