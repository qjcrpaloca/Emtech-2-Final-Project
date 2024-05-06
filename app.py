import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('Garbagemodel.h5')
  return model
model=load_model()
st.write("""
# Weather System"""
)
file=st.file_uploader("Choose photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(32,32)
    image=ImageOps.fit(image_data,size)
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
    result_class = np.argmax(prediction[0],axis=-1)
    result_label = class_names[result_class]
    string = f"Prediction: {result_label}"
    st.success(string)
