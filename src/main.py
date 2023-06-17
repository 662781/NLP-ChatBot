from chatbot import ChatBot
from services.kggenerator import KGGenerator

# Create Knowledge Graph
kg_gen = KGGenerator()
kg_gen.create_kg()

bot = ChatBot()
bot.welcome_msg()
# Instatiate chatbot loop
while True:
    user_input = input("User: ")
    if user_input.lower() == "see ya":
        print("ChatBot: Bye!")
        break
    print("ChatBot:", bot.respond(user_input))
