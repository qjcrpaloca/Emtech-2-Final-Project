import streamlit as st
import tensorflow as tf
import keras.utils as ku

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('Garbagemodel.h5')
  return model
model=load_model()
st.write("""
# Garbage Classification"""
)
file=st.file_uploader("Choose photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image,model):
    size=(32,32)
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
    string="Probability : "+np.max(prediction[0]
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)
