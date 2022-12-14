import streamlit as st
from pandas import DataFrame
from google.oauth2 import service_account
from gspread_pandas import Spread,Client
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd

image1 = Image.open('image/10977.jpg')
image2 = Image.open('image/QR1.jpeg')
image3 = Image.open('image/QR2.jpeg')
image4 = Image.open('image/logo1.jpg')
def puja_icon(image):
    y=image
    x = Image.open('image/puja_icons/' + y)
    return x
st.set_page_config(
    page_title='Sri Prasanna Venkateswara',
    page_icon= image4)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Create a connection object.
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Create a Google Authentication connection object
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"], scopes = scope)
client = Client(scope=scope,creds=credentials)
spreadsheetname = "Pujalu"
spread = Spread(spreadsheetname,client = client)
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
sh = client.open(spreadsheetname)
worksheet_list = sh.worksheets()


def worksheet_names():
    sheet_names = []   
    for sheet in worksheet_list:
        sheet_names.append(sheet.title)  
    return sheet_names

def load_the_spreadsheet(spreadsheetname):
    worksheet = sh.worksheet(spreadsheetname)
    df = DataFrame(worksheet.get_all_records())
    return df
def update_the_spreadsheet(spreadsheetname,dataframe):
    col = ['Date','Name', 'Address', 'Number', 'Name of puja','Names Items I need to get']
    spread.df_to_sheet(dataframe[col],sheet = spreadsheetname,index = False)

def main():
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=['Home', 'Puja Samagri list', 'Chat with Priest', 'Chat with the Chef'],
            icons=['house-door-fill','list', 'chat-dots-fill','chat-dots'],
            menu_icon='cast',
            default_index=0
    )
    # Home code
    if selected == 'Home':
        st.title('Home')
        col1, col2 = st.columns(2)
        with col1:
            st.image(image1)
        with col2:
            st.header('Summary')
            st.write("""We are Sri Prasanna Venkateswara Priest and Food services. For priest service we only server for New Jersey, New York, Pennsylvania.
             If you want us outside these states you have to pay for travles. For food service oder one week before.""") 
    # Puja Samagri list code
    if selected == 'Puja Samagri list':
        st.title("Puja samagri list")
        col1_1, col2_1= st.columns(2)
        with col1_1:
            st.image(puja_icon('images.jpeg'))
            with st.expander('Regular Homam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder | one small packet")
    # Chat with Priest code 
    if selected == 'Chat with Priest':
        st.title('QR code')
        st.write('Scan the QR code to chat with priest')
        st.image(image2)
    # Chat with the Chef code
    if selected == 'Chat with the Chef':
        st.title('QR code')
        st.write('Scan the QR code to chat with the Chef')
        st.image(image3)
    # Don't mess with the Chat with Priest and Chat with the Chef code.

if __name__ == "__main__":
  main()