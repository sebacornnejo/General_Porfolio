import os
# Set the TF_ENABLE_ONEDNN_OPTS environment variable to 0
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import numpy as np
import tensorflow as tf
import cv2
import scipy

# Specify the paths to the training and validation data directories
train_data_path = "TheSimpsonsDataset/train/"
val_data_path = "TheSimpsonsDataset/validation/"

# Create a list to store the names of characters
name_character = []
for character in os.listdir(train_data_path):
    data = [character]
    name_character.append(data)

# Load the saved model
model = tf.keras.models.load_model('TheSimpsons_CharacterClassification.keras')

# Load and preprocess a test image
img = cv2.imread("Test/prueba02.png")
img = cv2.resize(img, (224, 224))
img = np.array([img])
# img = np.invert(np.array([img]))
img = img / 255.0

# Make a prediction using the loaded model
output = model.predict(img)

# Get the index of the predicted class
np.argmax(output)

# Get the name of the predicted character using the index
data = name_character[np.argmax(output)]

# Print the predicted character name
print(data)