from chatbot import ChatBot
from services.kggenerator import KGGenerator

# Main chatbot loop
# bot = ChatBot()
# while True:
#     user_input = input("User: ")
#     if user_input.lower() == "see ya":
#         break
#     response = bot.generate_response(user_input)
#     print("ChatBot:", response)

kg_gen = KGGenerator()
kg_gen.draw_kg_for_most_common(kg_gen.text_py)
