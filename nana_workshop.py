import streamlit as st
import streamlit.components.v1 as stc
import codecs
from streamlit_option_menu import option_menu
from puja_list import puja_list
from dont_mess import home,config,Chef,Priest,hide_st
from puja_sign_up import puja_sign

config()
hide_st()
def B_T_P_botton():
    file = codecs.open('btn.html','r')
    page = file.read()
    stc.html(page,scrolling=False)
def btn():
    bt ="""
    <script>
            const btnTTf = document.querySelector("#btnTT");
            btnTTf.addEventListener("click", function(){
            //window.scrollTo(0,0);
            window.scrollTo({
                top:0,
                left:0,
                behavior:"smooth"
            });
            });
    </script>
    """
def main():
    st.cache()
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
        B_T_P_botton()
        st.button('Top',on_click=btn())
    # Puja sign-up form
    if selected == 'Puja sign-up form':
        puja_sign()
        B_T_P_botton()
    # Chat with Priest code 
    if selected == 'Chat with Priest':
        Priest()
    # Chat with the Chef code
    if selected == 'Chat with the Chef':
        Chef()
    # Don't mess with the Chat with Priest and Chat with the Chef code.
if __name__ == "__main__":
  main()