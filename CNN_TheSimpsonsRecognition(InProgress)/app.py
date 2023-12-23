import streamlit as st
import tensorflow as tf
from tensorflow.keras import models
import numpy as np
import os
import cv2

model = models.load_model('FaceEmotionsClassification.keras')
emotions = [['Angry'], ['Disgust'], ['Fear'], ['Happy'], ['Sad'], ['Surprise'], ['Neutral']]

st.header('Human Emotion Recognition')
img_path = st.text_input('Enter Image Path')

img = cv2.imread(img)[:,:,0]
img = cv2.resize(img,(48,48))
img = np.invert(np.array([img]))

output = np.argmax(model.predict(img))
outcome = emotions[output]
stn = 'Emotion in the image is ' + str(outcome[0])
st.markdown(stn)

image_name = os.path.basename(img_path)
st.image('Google_Images/' + image_name, width = 300)