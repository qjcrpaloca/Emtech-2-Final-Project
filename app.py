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
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
  
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['cardboard',
                 'glass',
                 'metal',
                 'paper',
                 'plastic',
                 'trash']
    string="This image is a : "+np.argmax(prediction)
    string="This image is a : "+class_names[np.argmax(prediction)]
    st.success(string)
