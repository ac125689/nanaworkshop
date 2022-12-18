import streamlit as st
from puja_list import puja_list
from dont_mess import home,config,Chef,Priest,hide_st,select
from puja_sign_up import puja_sign

config()
hide_st()
def main():
    select()
    # Home code
    if select() == 'Home':
        home()
    # Puja Samagri list code
    if select() == 'Puja Samagri list':
        puja_list()
    # Puja sign-up form
    if select() == 'Puja sign-up form':
        puja_sign()
    # Chat with Priest code 
    if select() == 'Chat with Priest':
        Priest()
    # Chat with the Chef code
    if select() == 'Chat with the Chef':
        Chef()
    # Don't mess with the Chat with Priest and Chat with the Chef code.
if __name__ == "__main__":
  main()