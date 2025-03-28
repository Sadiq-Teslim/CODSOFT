import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppresses most TensorFlow warnings

import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model

# Load the pre-trained InceptionV3 model (without the top layer)
base_model = InceptionV3(weights='imagenet')
feature_extractor = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

def extract_features(image_path):
    """Extracts features from an image using InceptionV3."""
    img = image.load_img(image_path, target_size=(299, 299))  # Resize to InceptionV3 input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)  # Preprocess for InceptionV3

    features = feature_extractor.predict(img_array)  # Extract features
    return features  # Shape: (1, 2048)

def generate_caption(image_path, model, tokenizer, max_length):
    """Generates a caption for the given image using a trained model."""

    # Extract features from the image
    image_features = extract_features(image_path)

    # Start caption generation with <startseq> token
    sequence = [tokenizer.word_index.get('startseq', 1)]  # Default to 1 if 'startseq' is missing

    for _ in range(max_length):
        sequence_padded = pad_sequences([sequence], maxlen=max_length)

        # Predict the next word
        preds = model.predict([image_features, sequence_padded], verbose=0)
        predicted_word_index = np.argmax(preds[0])  # Get the highest probability word

        word = tokenizer.index_word.get(predicted_word_index, '')  # Convert index to word

        if word == 'endseq' or word == '':  
            break

        sequence.append(predicted_word_index)

    # Convert index sequence to words & return caption
    return ' '.join([tokenizer.index_word[i] for i in sequence if i not in [tokenizer.word_index.get('startseq', 1)]])

# Example usage (replace with actual model & tokenizer)
# caption = generate_caption("image.jpg", model, tokenizer, max_length=20)
# print("Generated Caption:", caption)
