import streamlit as st
from streamlit_option_menu import option_menu
from puja_list import puja_list
from dont_mess import home,config,Chef,Priest,hide_st
from puja_sign_up import puja_sign

config()
hide_st()
def B_T_P_botton():
    BC = """
    <script>
    const btnTTf = document.querySelector("#btnTT");
    btnTTf.addEventListener("click", function(){
       window.scrollTo(0,0);
    })
    </script>
    <link rel="stylesheet" href = "https://use.fontawesome.com/releases/v5.4.1/css/all.css">
    <button id = "btnTT" style = "position: fixed;width: 50px;height: 50px;background: red;bottom: 50px;right: 50px;text-decoration: none;text-align: center;line-height: 50px;color: white; border: none;box-shadow: 0 0 10px rgb(0,0,0,0.25);border-radius: 50%;outline: none;cursor: pointer;"href = "#"><i class= "fas fa-arrow-up"></i></button>
    """
    st.markdown(BC,unsafe_allow_html=True)
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