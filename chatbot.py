import re  # Import regex module
import nltk  # Import Natural Language Toolkit
from nltk.tokenize import word_tokenize  # Import word_tokenize function from NLTK
from nltk.corpus import stopwords  # Import stopwords from NLTK corpus
nltk.download("punkt")  # For word tokenization
nltk.download("stopwords")  # For filtering unnecessary words

def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    words = word_tokenize(text)  # Tokenize into words
    filtered_words = [word for word in words if word not in stopwords.words("english")]  # Remove stop words
    return " ".join(filtered_words)  # Convert list back to string

def chatbot():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ").lower()

        # Use regex for pattern matching
        if re.search(r"\b(hello|hi|hey|holla|heyyo)\b", user_input):
            print("Chatbot: Hi there! How can I help?")
        elif re.search(r"\b(how are you?|how's it going?|how are you doing today?|how are you|how's it going|how are you doing today)\b", user_input):
            print("Chatbot: I'm just a bot, but I'm doing great!")
        elif re.search(r"\b(bye|goodbye|see you|later)\b", user_input):
            print("Chatbot: Goodbye! Have a great day!")
        elif re.search(r"\b(clear|cls)\b", user_input):
            # Clear terminal screen
            print("\033c", end="Chatbot Terminal cleared! Let's continue...")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
