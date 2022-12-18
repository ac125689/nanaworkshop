import streamlit as st
from PIL import Image


image1 = Image.open('image/10977.jpg')
image2 = Image.open('image/QR1.jpeg')
image3 = Image.open('image/QR2.jpeg')
image5 = Image.open('image/logo1.jpg')

def hide_st():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def home():
    st.title('Home')
    col1, col2 = st.columns(2)
    with col1:
            st.image(image1)
    with col2:
            st.header('Summary')
            st.write("""We are Sri Prasanna Venkateswara Priest and Food services. For priest service we only server for New Jersey, New York, Pennsylvania.
             If you want us outside these states you have to pay for travles. For food service oder one week before.""")

def config():
    st.set_page_config(
    page_title='Sri Prasanna Venkateswara',
    page_icon= image5)

def Priest():
    st.title('QR code')
    st.write('Scan the QR code to chat with priest')
    st.image(image2)

def Chef():
    st.title('QR code')
    st.write('Scan the QR code to chat with the Chef')
    st.image(image3)