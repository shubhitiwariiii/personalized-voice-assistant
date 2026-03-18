import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


class IntentClassifier:

    def __init__(self):
        with open("ml/training_data.json") as file:
            data = json.load(file)

        self.patterns = []
        self.tags = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                self.patterns.append(pattern)
                self.tags.append(intent["tag"])

        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(self.patterns)

        self.model = MultinomialNB()
        self.model.fit(X, self.tags)

    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]
    
if __name__ == "__main__":
    classifier = IntentClassifier()

    while True:
        text = input("You: ")
        intent = classifier.predict(text)
        print("Predicted intent:", intent)