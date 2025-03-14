import os  # For clearing the terminal screen
import re  # For handling pattern matching (regular expressions)
import nltk  # For natural language processing
from nltk.tokenize import word_tokenize  # Splits sentences into words
from nltk.corpus import stopwords  # Common words like "is", "the", "and" that don't add meaning

# Download necessary NLTK data (only needed once)
nltk.download("punkt")  # For tokenization
nltk.download("stopwords")  # For filtering out unimportant words

# List of greetings that the chatbot should recognize
greetings = [
    "hello", "hi", "hey", "holla", "heyyo", 
    "good morning", "good afternoon", "good evening", "good day",
    "what's up", "whats up", "howdy"
]

# Dictionary for detecting emotions/moods in user input
mood_responses = {
    "happy": {
        "keywords": {"happy", "excited", "great", "amazing", "fantastic", "awesome", "joyful", "good"},
        "response": "😊 That's awesome! I'm glad you're feeling great!"
    },
    "sad": {
        "keywords": {"sad", "down", "depressed", "not okay", "tired", "upset", "unhappy"},
        "response": "😔 I'm sorry to hear that. Remember, you're not alone. Keep pushing forward! 💪"
    },
    "angry": {
        "keywords": {"angry", "mad", "furious", "annoyed", "frustrated"},
        "response": "😡 I see you're angry. Take a deep breath, and try to relax. You've got this! ✨"
    },
    "stressed": {
        "keywords": {"stressed", "overwhelmed", "pressured", "burned out"},
        "response": "😓 Stress can be tough, but don't forget to take breaks and care for yourself! 💙"
    },
    "confused": {
        "keywords": {"confused", "lost", "unsure", "don't understand"},
        "response": "🤔 No worries! Sometimes things take time to make sense. Keep asking questions!"
    },
    "excited": {
        "keywords": {"excited", "thrilled", "pumped", "can't wait"},
        "response": "🎉 That's amazing! Excitement is the fuel for great things. Keep the energy up! 🚀"
    }
}

def is_greeting(text):
    """
    Check if the user input contains a greeting.
    Returns True if a greeting is found, otherwise False.
    """
    text = text.lower()  # Convert input to lowercase to make matching easier
    return any(greet in text for greet in greetings)  # Check if any greeting exists in the input

def detect_mood(text):
    """
    Check if the user expresses a mood (happy, sad, angry, etc.).
    If a mood is detected, returns an appropriate response.
    If no mood is detected, returns None.
    """
    words = set(text.lower().split())  # Convert input text into a set of words for faster lookup
    for mood, data in mood_responses.items():  # Loop through each mood category
        if data["keywords"].intersection(words):  # Check if any mood keyword is in the input
            return data["response"]  # Return the corresponding mood response
    return None  # If no mood is found, return None

def preprocess_text(text):
    """
    Preprocess user input by:
    - Lowercasing
    - Removing punctuation
    - Tokenizing (splitting into words)
    - Removing stopwords (e.g., "is", "the", "and")
    Returns the cleaned-up string.
    """
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation using regex
    words = word_tokenize(text)  # Split text into words
    filtered_words = [word for word in words if word not in stopwords.words("english")]  # Remove stopwords
    return " ".join(filtered_words)  # Rejoin words into a cleaned-up sentence

def chatbot():
    """
    The main chatbot function.
    Keeps running until the user says a farewell phrase (e.g., "bye").
    """
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ").strip()  # Get user input and remove extra spaces
        processed_input = preprocess_text(user_input)  # Clean up the input
        user_input_lower = user_input.lower()  # Lowercase input for case-insensitive matching

        # 1️⃣ Greeting Detection
        if is_greeting(user_input_lower):
            print("Chatbot: Hi there! How can I help?")

        # 2️⃣ Mood Detection
        mood_response = detect_mood(user_input_lower)
        if mood_response:
            print(f"Chatbot: {mood_response}")

        # 3️⃣ "How are you?" Detection (Using Regular Expressions)
        elif re.search(r"\b(how are you\??|how's it going\??|how are you doing\??)\b", user_input_lower):
            print("Chatbot: I'm just a bot, but I'm doing great!")

        # 4️⃣ Farewell Detection
        elif re.search(r"\b(bye|goodbye|see you|later)\b", user_input_lower):
            print("Chatbot: Goodbye! Have a great day!")
            break  # Stop the chatbot when a farewell is detected

        # 5️⃣ Terminal Clear Command
        elif re.search(r"\b(clear|cls)\b", user_input_lower):
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print("Chatbot: Terminal cleared! Let's continue...")

        # 6️⃣ Default Response (If No Matches)
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
