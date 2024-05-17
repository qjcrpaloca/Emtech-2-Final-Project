import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import keras.utils as ku

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('FineTunedTrashCNN.h5')
  return model
model=load_model()
st.title(':blue-background[cool]')
st.write("""
# Garbage Classification\n
Determines if Cardboard,Glass,Metal,Paper,Plastic, or others(trash)"""
)
file=st.file_uploader("Choose photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(32,32)
    image=img_to_array(image_data,dtype=np.uint8)
    image=np.array(image)/255.0
    image=ImageOps.fit(image_data,size)
    #img=np.asarray(image)
    img=np.array(image)/255.0
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    # Load the image into the model for prediction
    prediction = import_and_predict(image, model)
    class_names=['cardboard',
                 'glass',
                 'metal',
                 'paper',
                 'plastic',
                 'trash']
    result_class = np.argmax(prediction)
    result_class1 = np.max(prediction)
    result_label = class_names[result_class]
    string = f"This image is a: {result_label}"
    st.success(string)
    string = f"Probability: {result_class1:.2%}"
    st.success(string)
