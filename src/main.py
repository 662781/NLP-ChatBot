from src.chatbot import ChatBot

# Main chatbot loop
bot = ChatBot()
while True:
    user_input = input("User: ")
    if user_input.lower() == "see ya":
        break
    response = bot.generate_response(user_input)
    print("ChatBot:", response)