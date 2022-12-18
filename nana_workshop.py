import streamlit as st
from pandas import DataFrame
from google.oauth2 import service_account
from gspread_pandas import Spread,Client
from streamlit_option_menu import option_menu
from PIL import Image
import ssl
from etext import send_sms_via_email
from puja_list import puja_list, puja_list_down
import datetime as dt

image1 = Image.open('image/10977.jpg')
image2 = Image.open('image/QR1.jpeg')
image3 = Image.open('image/QR2.jpeg')
image5 = Image.open('image/logo1.jpg')
st.set_page_config(
    page_title='Sri Prasanna Venkateswara',
    page_icon= image5)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Create a connection object.
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
    col = ['Date','Time','Name', 'Address', 'Number', 'Email','Name of puja','Names Items we need to get']
    spread.df_to_sheet(dataframe[col],sheet = spreadsheetname,index = False)

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
        puja_list()
    # Puja sign-up form
    if selected == 'Puja sign-up form':
        #'Date','Time','Name', 'Address', 'Number', 'Email','Name of puja','Names Items we need to get'
        st.title("Puja sign-up form")
        name = st.text_input("Your name")
        name_of_puja = st.selectbox("which puja do you want?", ('Aksharabhyasam','Annaprasana','Gruha Pravesam','Hair Offering','Hiranya sraddham','Homam','Chandi Homam','Namakaranam','Engagement','Punyahavachanam','Sri Satyanarayana Swami Vratam','Kalyna Utsvam','Seemantam','Upanayanam','Wedding','60th or 80th Birthday','Bhu puja','Rudrabhishekam'))
        if name_of_puja == 'Aksharabhyasam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Aksharabhyasam list",
                    data=puja_list_down('Aksharabhyasam_list.csv'),
                    file_name= "Aksharabhyasam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Annaprasana':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Annaprasana list",
                    data=puja_list_down('Annaprasana list.csv'),
                    file_name= "Annaprasana list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Gruha Pravesam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Gruha Pravesam list",
                    data=puja_list_down('Gruha Pravesam list.csv'),
                    file_name= "Gruha Pravesam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Hair Offering':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Hair Offering list",
                    data=puja_list_down('Hair offering list.csv'),
                    file_name= "Hair offering list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Hiranya sraddham':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Hiranya sraddham list",
                    data=puja_list_down('Hiranya sraddham list.csv'),
                    file_name= "Hiranya sraddham list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Homam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Homam list",
                    data=puja_list_down('Regular Homam list.csv'),
                    file_name= "Regular Homam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Chandi Homam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Chandi Homam list",
                    data=puja_list_down('Chandi Homam list.csv'),
                    file_name= "Chandi Homam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Namakaranam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Namakaranam list",
                    data=puja_list_down('Namakaranam list.csv'),
                    file_name= "Namakaranam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Engagement':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Engagement list",
                    data=puja_list_down('Engagement list.csv'),
                    file_name= "Engagement list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Punyahavachanam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Punyahavachanam list",
                    data=puja_list_down('Punyahavachanam list.csv'),
                    file_name= "Punyahavachanam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Sri Satyanarayana Swami Vratam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Sri Satyanarayana Swami Vratam list",
                    data=puja_list_down('Sri Satyanarayana Swami Vratam list.csv'),
                    file_name= "Sri Satyanarayana Swami Vratam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Kalyna Utsvam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Kalyna Utsvam list",
                    data=puja_list_down('Kalyna Utsvam list.csv'),
                    file_name= "Kalyna Utsvam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Seemantam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Seemantam list",
                    data=puja_list_down('Seemantam list.csv'),
                    file_name= "Seemantam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Upanayanam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Upanayanam list",
                    data=puja_list_down('Upanayanam list.csv'),
                    file_name= "Upanayanam list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Wedding':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Wedding list",
                    data=puja_list_down('Wedding list.csv'),
                    file_name= "Wedding list.csv",
                    mime='text/csv'
                )
        if name_of_puja == '60th or 80th Birthday':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download 60th or 80th Birthday list",
                    data=puja_list_down('60th or 80th Birthday list.csv'),
                    file_name= "60th or 80th Birthday list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Bhu puja':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Bhu puja list",
                    data=puja_list_down('Bhu puja list.csv'),
                    file_name= "Bhu puja list.csv",
                    mime='text/csv'
                )
        if name_of_puja == 'Rudrabhishekam':
            st.info("The cost priest service will be ")
            st.download_button(
                    label="Download Rudrabhishekam list",
                    data=puja_list_down('Rudrabhishekam list.csv'),
                    file_name= "Rudrabhishekam list.csv",
                    mime='text/csv'
                )
        st.markdown('Please get **Date** and **Time** from the priest')
        date = st.date_input('Date of the puja.')
        time = st.time_input('Which time? The time is in 24 hour. Example 1pm will be 13')
        address = st.text_input('your address')
        number = st.text_input('your number')
        email = st.text_input('your email')
        items = st.text_area('Names Items we need to get')
        if st.button("Submit"):
            with st.spinner('Wait for it...'):
                opt = { 'Date': [date],
            'Time' : time,
            'Name': name,
            'Address': address,
            'Number': number,
            'Email': email,
            'Name of puja': name_of_puja,
            'Names Items we need to get': items}
                opt_df = DataFrame(opt)
                df = load_the_spreadsheet('Puja')
                new_df = df.append(opt_df,ignore_index=True)
                update_the_spreadsheet('Puja',new_df)
            st.success("You are good to go.")
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