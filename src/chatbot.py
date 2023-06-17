import spacy
import json
import random
from services.fuzzy_matcher import FuzzyMatcher
from services.kggenerator import KGGenerator

class ChatBot:

    def __init__(self) -> None:
        self.negative_responses = [
            "I don't know.",
            "I couldn't find the answer, please formulate your question differently.",
            "I don't know this. Feel free to ask another question."
        ]
        self.fuzzmatch = FuzzyMatcher()
        self.nlp = spacy.load('en_core_web_sm')

    def process_input(self, user_input: str):
        return self.fuzzmatch.find_answer(user_input)
    
    def respond(self, user_input):
        answer = self.process_input(user_input)

        if answer:
            return answer
        else:
            # Return random negative response 
            return random.choice(self.negative_responses)

