import json
import random

import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Load the intents data from the JSON file - contains the questions and some of the answers 
file = open("intents.json", "r", encoding="utf-8")
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

# Createing training data from the intents 
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
y = tags

# Training the model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(corpus, y)

class InputValueError(Exception):
    pass

# Implementing the chatbot
def get_response(user_input: str):
    try:
        user_input = user_input.lower()
        predicted_tag = model.predict([user_input])[0]
    
        if predicted_tag in responses:
            return random.choice(responses[predicted_tag])
        else:
            return "I'm sorry, I don't understand. Can you please rephrase your question?"
    except Exception as error:
        logging.error(error)
        raise InputValueError

if __name__ == "__main__":
    # Test the chatbot
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = get_response(user_input)
        print("Bot:", response)
