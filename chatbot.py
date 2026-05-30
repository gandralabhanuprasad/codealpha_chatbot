# Simple Chatbot Program

print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("ChatBot: Hi! How are you?")
    
    elif user == "how are you":
        print("ChatBot: I'm fine. How can I help you?")
    
    elif user == "what is your name":
        print("ChatBot: My name is ChatBot.")
    
    elif user == "who created you":
        print("ChatBot: I was created using Python.")
    
    elif user == "bye":
        print("ChatBot: Goodbye!")
        break
    
    else:
        print("ChatBot: Sorry, I don't understand that.")