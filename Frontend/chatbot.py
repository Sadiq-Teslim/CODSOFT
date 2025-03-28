import os
import re
import nltk
from gpt4all import GPT4All
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data (only needed once)
nltk.download("punkt")
nltk.download("stopwords")

# Load GPT4All Model
MODEL_PATH = os.path.expanduser("~/GPT4All/models")  # Update this path if needed
model = GPT4All("mistral-7b.Q4_0.gguf", model_path=MODEL_PATH)  # Adjust model file if needed

# List of predefined greetings
greetings = [
    "hello", "hi", "hey", "holla", "heyyo",
    "good morning", "good afternoon", "good evening", "good day",
    "what's up", "whats up", "howdy"
]

# Mood-based responses
moods = {
    "happy": ["I'm glad to hear that! 😊", "That's awesome! Keep shining! ✨"],
    "sad": ["I'm here for you. 💙", "Stay strong! Better days are ahead."],
    "angry": ["Take a deep breath. You got this. 💪", "Let's talk it out. I'm listening. 🤗"],
    "excited": ["That's amazing! 🎉", "Woohoo! Keep the energy up! 🚀"],
    "bored": ["Why not try something fun? 🎮", "Let's chat! I can tell you a joke. 😄"]
}

def is_greeting(text):
    """Check if the input contains any greeting phrase."""
    text = text.lower()
    return any(greet in text for greet in greetings)

def detect_mood(text):
    """Basic mood detection from keywords."""
    mood_keywords = {
        "happy": ["happy", "great", "good", "fantastic", "awesome", "amazing"],
        "sad": ["sad", "down", "depressed", "unhappy", "bad"],
        "angry": ["angry", "mad", "furious", "upset"],
        "excited": ["excited", "thrilled", "pumped", "hyped"],
        "bored": ["bored", "boring", "nothing to do", "dull"]
    }
    
    for mood, keywords in mood_keywords.items():
        if any(word in text.lower() for word in keywords):
            return mood
    return None

def get_gpt4all_response(question):
    """Generate a response using GPT4All."""
    with model.chat_session():
        response = model.generate(question, max_tokens=200)
    return response

def chatbot():
    """Main chatbot loop."""
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ").strip().lower()

        # Greeting detection
        if is_greeting(user_input):
            print("Chatbot: Hi there! How can I help?")
        # Mood detection
        elif detect_mood(user_input):
            mood = detect_mood(user_input)
            print(f"Chatbot: {moods[mood][0]}")  # Choose a mood response
        # "How are you?" detection
        elif re.search(r"\b(how are you\??|how's it going\??|how are you doing today\??)\b", user_input):
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        # Farewell detection
        elif re.search(r"\b(bye|goodbye|see you|later)\b", user_input):
            print("Chatbot: Goodbye! Have a great day! 👋")
            break
        # Clear terminal command
        elif re.search(r"\b(clear|cls)\b", user_input):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Our previous chat(s) has been cleared! Let's continue...")
        # Use GPT4All for everything else
        else:
            response = get_gpt4all_response(user_input)
            print(f"Chatbot: {response}")

# Run chatbot
chatbot()
