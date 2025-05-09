import streamlit as st    
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image
import io
st.sidebar.title('image editor')
img=st.sidebar.file_uploader("choose your image")
c=st.sidebar.selectbox("select your editor",("sketch","Black & white"))
st.title("Image convertor")
if c=="sketch":
    a=st.sidebar.number_input("Adjust Pencil Darkness")
b=st.sidebar.button("view image")

if img is not None:
    data=img.getvalue()
    image_bytes=img.read()
    #st.write(image_bytes)
    np_image=np.frombuffer(image_bytes,np.uint8)
    image=cv2.imdecode(np_image,cv2.IMREAD_COLOR)

    img1=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    img_g=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img_inv=cv2.bitwise_not(img_g)
    img_sm=cv2.GaussianBlur(img_inv,(25,25),sigmaX=0,sigmaY=0)
    
   
  
    if b:
        if c=="sketch":
            img_pencil=cv2.divide(img_g,255-img_sm,scale=a)
            st.image(img_pencil,caption='pencil sketch')
            result_image = Image.fromarray(img_pencil)
            buf = io.BytesIO()
            result_image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.sidebar.download_button(
            label="Download Sketch",
            data=byte_im,
            file_name="sketch.png",
            mime="image/png")
        elif c=="Black & white":
            st.image(img_g,caption="Black & white")
            result_image = Image.fromarray(img_g)
            buf = io.BytesIO()
            result_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.sidebar.download_button(
            label="Download Sketch",
            data=byte_im,
            file_name="sketch.png",
            mime="image/png")



hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
