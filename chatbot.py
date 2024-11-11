def chatbot():
    print("Hello! I am a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input:
            print("Chatbot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but thanks for asking! How can I assist you?")
        elif "your name" in user_input:
            print("Chatbot: I am a simple Python chatbot. What about you?")
        else:
            print("Chatbot: I'm not sure I understand. Can you try asking something else?")

if __name__ == "__main__":
    chatbot()
