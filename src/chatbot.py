import spacy
import json

class ChatBot:

    def __init__(self) -> None:
        self.knowledge_graph = {
            "apple": "A fruit that is red or green in color and grows on trees.",
            "banana": "A fruit that is yellow and grows on trees.",
            "orange": "A citrus fruit that is typically orange in color.",
            "watermelon": "A large fruit with green skin and red flesh."
        }
        self.nlp = spacy.load('en_core_web_sm')

    def process_input(self, user_input: str):
        doc = self.nlp(user_input)
        return [token.text for token in doc]
    
    def get_information(self, tokens):
        # Search the knowledge graph based on the keywords
        for token in tokens:
            if token in self.knowledge_graph:
                return self.knowledge_graph[token]
        
        # If no relevant information is found
        return None

    def generate_response(self, user_input):
        processed_input = self.process_input(user_input)
        information = self.get_information(processed_input)

        if information:
            return information
        else:
            return "I don't know."
        
    def get_json_data(self) -> dict:
        with open('data/knowledge_graph.json', 'r') as file:
            knowledge_graph = json.load(file)

        nodes = knowledge_graph["nodes"]
        links = knowledge_graph["links"]

        # Extracting node IDs
        node_ids = [node["id"] for node in nodes]

        # Extracting link information
        relations = [link["relation"] for link in links]
        sources = [link["source"] for link in links]
        targets = [link["target"] for link in links]

        return {"node_ids": node_ids, "relations": relations, "sources": sources, "targets": targets}

