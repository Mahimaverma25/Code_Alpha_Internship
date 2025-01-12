import nltk
from nltk.chat.util import Chat, reflections
import random

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I\'m great, how are you?']),
    (r'what is your name', ['I am ChatBot, nice to meet you!', 'You can call me ChatBot']),
    (r'bye|goodbye|exit', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'what can you do', ['I can chat with you!', 'I can answer basic questions']),
    
    # General questions with placeholders
    (r'what is (.*)', ['%1 is a concept I can try to explain. Could you be more specific?']),
    (r'how do I (.*)', ['To %1, you might want to break down the problem into smaller steps.']),
    
    # Default response
    (r'.*', ['Interesting...', 'Tell me more about that.', 'I see...'])
]

class ImprovedChatBot:
    def __init__(self):
        self.chat = Chat(patterns, reflections)
        self.context = {}  # Memory for user information (e.g., name)
        self.is_asking_for_name = False  # Flag to ask for user's name
    
    def handle_context(self, user_input):
        """Handle contextual responses based on prior interactions."""
        # If the user already told their name, use it in conversation
        if 'name' in self.context:
            if 'name' in user_input:
                return f"Yes, your name is {self.context['name']}. Anything else you'd like to talk about?"
            
            # If the user is talking about something else, incorporate their name
            if 'how are you' in user_input:
                return f"I'm great, {self.context['name']}! How about you?"
            return f"That's interesting, {self.context['name']}! Tell me more."
        
        # If asking for name, get it from user input
        if self.is_asking_for_name:
            name = user_input.split()[-1]  # Naive name extraction from last word
            self.context['name'] = name
            self.is_asking_for_name = False
            return f"Nice to meet you, {name}! What would you like to talk about?"

        # Ask the user for their name if we don't know it
        if 'name' in user_input and 'your name' in user_input:
            self.is_asking_for_name = True
            return "What is your name?"
        
        return None  # No context found; return None to continue with default matching
    
    def respond(self, user_input):
        """Generate the chatbot's response with contextual and pattern matching."""
        user_input = user_input.lower()

        try:
            # Handle context and return response if context matches
            context_response = self.handle_context(user_input)
            if context_response:
                return context_response

            # Otherwise, respond using pattern matching
            return self.chat.respond(user_input)
        
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Error occurred: {e}")  # In a real bot, log this error
            return "Sorry, I didn't quite understand that. Could you rephrase?"
    
    def start_chat(self):
        """Start a conversation with the chatbot."""
        print("ChatBot: Hello! I'm your chatbot assistant. Type 'bye' to exit.")
        
        while True:
            try:
                user_input = input("You: ").strip()

                # Exit the chat if the user says goodbye
                if user_input.lower() in ['bye', 'goodbye', 'exit']:
                    print("ChatBot: Goodbye! Have a great day!")
                    break
                
                # Get a response from the bot
                response = self.respond(user_input)
                print("ChatBot:", response)
            except KeyboardInterrupt:
                print("\nChatBot: Goodbye! Have a great day!")
                break

def main():
    chatbot = ImprovedChatBot()
    chatbot.start_chat()

if __name__ == "__main__":
    main()
