import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from etext import send_sms_via_email
from puja_list import puja_list
from dont_mess import home,config,Chef,Priest,hide_st
from puja_sign_up import puja_sign

image5 = Image.open('image/logo1.jpg')
# Create a connection object.
hide_st()
st.set_page_config(
    page_title='Sri Prasanna Venkateswara',
    page_icon= image5)
def main():
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=['Home', 'Puja Samagri list', 'Puja sign-up form','Chat with Priest', 'Chat with the Chef'],
            icons=['house-door-fill','list', 'card-checklist','chat-dots-fill','chat-dots'],
            menu_icon='cast',
            default_index=0
    )
    # Home code
    if selected == 'Home':
        home()
    # Puja Samagri list code
    if selected == 'Puja Samagri list':
        puja_list()
    # Puja sign-up form
    if selected == 'Puja sign-up form':
        puja_sign()
    # Chat with Priest code 
    if selected == 'Chat with Priest':
        Priest()
    # Chat with the Chef code
    if selected == 'Chat with the Chef':
        Chef()
    # Don't mess with the Chat with Priest and Chat with the Chef code.
if __name__ == "__main__":
  main()