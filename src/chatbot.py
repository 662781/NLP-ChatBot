import spacy

class ChatBot:

    def __init__(self) -> None:
        self.knowledge_graph = {
            "apple": "A fruit that is red or green in color and grows on trees.",
            "banana": "A fruit that is yellow and grows on trees.",
            "orange": "A citrus fruit that is typically orange in color.",
            "watermelon": "A large fruit with green skin and red flesh."
        }
        self.nlp = spacy.load('en_core_web_sm')

    # Function to process user input
    def process_input(self, user_input: str):
        doc = self.nlp(user_input)
        return [token.text for token in doc]
    
    # Function to retrieve information from the knowledge graph
    def get_information(self, tokens):
        # Search the knowledge graph based on the keywords
        for token in tokens:
            if token in self.knowledge_graph:
                return self.knowledge_graph[token]
        
        # If no relevant information is found
        return None

    # Function to generate responses
    def generate_response(self, user_input):
        processed_input = self.process_input(user_input)
        information = self.get_information(processed_input)

        if information:
            return information
        else:
            return "I don't know."

# Main chatbot loop
bot = ChatBot()
while True:
    user_input = input("User: ")
    if user_input.lower() == "see ya":
        break
    response = bot.generate_response(user_input)
    print("ChatBot:", response)
