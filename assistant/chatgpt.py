import requests

def ask_chatgpt(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 80   # 🔥 limits response length
                }
            }
        )

        result = response.json()
        return result.get("response", "")

    except Exception as e:
        print("ERROR:", e)
        return "AI not working"