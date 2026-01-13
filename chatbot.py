import time

# UI Colors
MAGENTA = '\033[95m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def get_bot_response(user_input):
    # Normalize input: lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # Predefined rules/replies
    responses = {
        "hello": "Hi there! How can I help you today? 👋",
        "hi": "Hello! Nice to meet you. 😊",
        "how are you": "I'm just a bundle of code, but I'm functioning perfectly! How are you?",
        "bye": "Goodbye! Have a productive day! 🚀",
        "name": "I am 'PythonBot', your friendly rule-based assistant.",
        "help": "I can chat with you! Try saying 'hello', 'how are you', or 'bye'."
    }

    # Enhanced logic: Check if any keyword exists in the input
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I'm sorry, I don't understand that yet. Could you try saying 'help'?"

def start_chat():
    print(f"{MAGENTA}====================================")
    print("      🤖 ENHANCED PYTHON CHATBOT")
    print(f"    (Type 'bye' to exit the chat)")
    print(f"===================================={RESET}")

    while True:
        user_msg = input(f"\n{YELLOW}You:{RESET} ")
        
        if not user_msg:
            continue
            
        print(f"{BLUE}Bot is thinking...{RESET}")
        time.sleep(0.5)
        
        response = get_bot_response(user_msg)
        print(f"{BLUE}Bot:{RESET} {response}")

        if "bye" in user_msg.lower():
            break

if __name__ == "__main__":
    start_chat()