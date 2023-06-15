import spacy
import json

class ChatBot:

    def __init__(self) -> None:
        # self.dummy_knowledge_graph = {
        #     "apple": "A fruit that is red or green in color and grows on trees.",
        #     "banana": "A fruit that is yellow and grows on trees.",
        #     "orange": "A citrus fruit that is typically orange in color.",
        #     "watermelon": "A large fruit with green skin and red flesh."
        # }
        self.nlp = spacy.load('en_core_web_sm')

    def process_input(self, user_input: str):
        doc = self.nlp(user_input)
        return [token.text for token in doc]
    
    def get_information(self, tokens):
        # Search the knowledge graph based on the keywords
        for token in tokens:
            if token in self.dummy_knowledge_graph:
                return self.dummy_knowledge_graph[token]
        
        # If no relevant information is found
        return None

    def generate_response(self, user_input):
        processed_input = self.process_input(user_input)
        information = self.get_information(processed_input)

        if information:
            return information
        else:
            return "I don't know."
        
    def get_json_data(self, file = 'data/knowledge_graph.json') -> dict:
        with open(file, 'r') as file:
            return json.load(file)

