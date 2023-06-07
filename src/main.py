from chatbot import ChatBot
from services.kggenerator import KGGenerator
import pprint

kg_gen = KGGenerator()
# Create Knowledge Graph
kg_gen.create_kg(kg_gen.text_py)

# Main chatbot loop
bot = ChatBot()
pprint.pprint(bot.get_json_data())
# while True:
#     user_input = input("User: ")
#     if user_input.lower() == "see ya":
#         break
#     response = bot.generate_response(user_input)
#     print("ChatBot:", response)
