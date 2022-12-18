import streamlit as st
from pandas import DataFrame
from puja_list import puja_list_down
from google.oauth2 import service_account
from gspread_pandas import Spread,Client
import ssl
import requests
from email.message import EmailMessage
import smtplib

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

def message(to,name,puja,date,time,address,number,items):
        resp = requests.post('https://textbelt.com/text', {
            'phone': f'{to}',
            'message': f'Name: {name}\nPuja: {puja}\nDate: {date}\nTime: {time}\nAddress: {address}\nNumber: {number}\nItems: {items}',
            'key': 'textbelt',
        })
        print(resp.json())
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


def puja_sign():
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
                message('6097210322',name,name_of_puja,date,time,address,number,items)
            st.success("You are good to go.")