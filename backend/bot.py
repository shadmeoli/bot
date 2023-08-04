import json
import random
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load the intents data from the JSON file
with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Preprocess the data
corpus = []
tags = []
responses = {}
for intent in data["intents"]:
    for pattern in intent["question"]:
        corpus.append(pattern.lower())
        tags.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]

# Create training data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
y = tags

# Train the model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(corpus, y)


# Implement the chatbot
def get_response(user_input):
    user_input = user_input.lower()
    predicted_tag = model.predict([user_input])[0]
    if predicted_tag in responses:
        return random.choice(responses[predicted_tag])
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"


if __name__ == "__main__":
    # Test the chatbot
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = get_response(user_input)
        print("Bot:", response)
