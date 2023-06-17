import spacy
import json
from services.fuzzy_matcher import FuzzyMatcher
from services.kggenerator import KGGenerator

class ChatBot:

    def __init__(self) -> None:
        self.dummy_knowledge_graph = {
            "apple": "A fruit that is red or green in color and grows on trees.",
            "banana": "A fruit that is yellow and grows on trees.",
            "orange": "A citrus fruit that is typically orange in color.",
            "watermelon": "A large fruit with green skin and red flesh."
        }
        self.fuzzmatch = FuzzyMatcher()
        self.nlp = spacy.load('en_core_web_sm')

    def process_input(self, user_input: str):
        return self.fuzzmatch.find_answer(user_input)
    
    def respond(self, user_input):
        information = self.process_input(user_input)

        if information:
            return information
        else:
            return "I don't know."

