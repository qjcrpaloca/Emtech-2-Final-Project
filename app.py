import streamlit as st
import tensorflow as tf
import keras.utils as ku

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('Garbagemodel.h5')
  return model
model=load_model()
st.write("""
# Garbage Classification\n
Detects Garbage if cardboard,glass,metal,paper,plastic or other(trash)"""
)
file=st.file_uploader("Choose photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image,model):
    size=(32,32)
    # Ensure image_data is in the correct data type and range
    image_data = (image_data * 255).astype(np.uint8)
    # Convert the NumPy array to an Image instance
    image = Image.fromarray(image_data)
    # Use ImageOps.fit with the Image instance
    image=ImageOps.fit(image,size)
    img=np.asarray(image)
    img = img[:, :, 0]
    img_reshape = img[np.newaxis, ..., np.newaxis]
    prediction=model.predict(img_reshape)
    return prediction
  
def load_image():
    # Check if the image is grayscale, if so, add a channel dimension
    if len(img.shape) == 2:
        img = np.expand_dims(img, axis=-1)
    
    img = img / 255.0
    img = np.reshape(img, (1, 64, 64, img.shape[-1]))
    return img
  
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    image_array = img_to_array(image)

    # Normalize the image
    image_array = image_array / 255.0

    # Load the image into the model for prediction
    prediction = import_and_predict(image_array, model)
    class_names=['cardboard',
                 'glass',
                 'metal',
                 'paper',
                 'plastic',
                 'trash']
    result_class = np.argmax(prediction)
    result_label = class_names[result_class]
    string = f"Prediction: {result_label} ({prediction[0][result_class]:.2%} confidence)"
    st.success(string)
