import streamlit as st
from pandas import DataFrame
from google.oauth2 import service_account
from gspread_pandas import Spread,Client
from streamlit_option_menu import option_menu
from PIL import Image

image1 = Image.open('image/10977.jpg')
image2 = Image.open('image/QR1.jpeg')
image3 = Image.open('image/QR2.jpeg')
image5 = Image.open('image/logo1.jpg')
def puja_icon(image):
    x = Image.open('image/puja_icons/' + image)
    return x
def resize_image(name,hight,width):
    x = puja_icon(name)
    y = x.resize((width,hight))
    return y
def puja_list_down(name):
    x = open('puja_list_downloads/'+name)
    return x
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
    st.cache()
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=['Home', 'Puja Samagri list', 'Puja samagri list Downloads','Chat with Priest', 'Chat with the Chef'],
            icons=['house-door-fill','list', 'arrow-down-square','chat-dots-fill','chat-dots'],
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
            st.image(resize_image('images.jpeg',219,261))
            with st.expander('Regular Homam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 30 each")
                st.write("Flower | 3 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 20")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Camphor | One small packet")
                st.write("Aluminium trays | 3 Big size")
                st.write("Ghee | One small bottle")
                st.write("Navadhanyas | Small Packets Seperately")
                st.write("Yellow Mustard Seeds (Vastu Homam) | One small packet")
                st.write("Dry Coconut Pieces (Copra) | 6")
                st.write("Sand | 5 lbs")
                st.write("Kalasam | 1")
                st.write("Towel | 1")
                st.write("Blouse Piece | 1")
                st.write("Coconuts | 2")
                st.write("Rice | 3 lbs")
                st.write("Coins | $10 (Quarters)")
                st.write("Steel Bowls | 6")
                st.write("Banana Leaves | 4")
                st.write("Naivedyam (any variety)")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate, Scissors")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Regular Homam list.csv'),
                    file_name= "Regular Homam list.csv",
                    mime='text/csv'
                )
            st.image(resize_image('Chandi.jpeg',219,154))
            with st.expander('Chandi Homam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 40 each")
                st.write("Flower | 3 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 20")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Rice | 3 lbs")
                st.write("Kalasam | 1")
                st.write("Aluminium trays | 2 Big and small size")
                st.write("Sand | 5 lbs")
                st.write("Dry Coconut Pieces (Copra) | 12")
                st.write("Ghee | 1 lbs")
                st.write("Honey | One small bottle")
                st.write("Pomegranate fruits | 2")
                st.write("Camphor | One small packet")
                st.write("Small pumpkin | 1")
                st.write("White betel nuts | One small packet")
                st.write("Banana | 12")
                st.write("Guava fruits | 3")
                st.write("Towel | 1")
                st.write("Blouse Piece | 1")
                st.write("Coconuts | 2")
                st.write("Naivedyam (any variety)")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate, Scissors")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Chandi Homam list.csv'),
                    file_name= "Candi Homam list.csv",
                    mime='text/csv'
                )
            st.image(resize_image('hair.jpeg',219,219))
            with st.expander('Hair offering list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 10 each")
                st.write("Flower | 1 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 6")
                st.write("Kalasam | 1")
                st.write("Towel | 1")
                st.write("Blouse Piece (yellow) | 1")
                st.write("Coconuts | 2")
                st.write("Rice | 1 lbs")
                st.write("Coins | $5 (Quarters)")
                st.write("New Scissors")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Paper Towels, Scissors,Disposable Glasses,Bowl,Spoon")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Hair offering list.csv'),
                    file_name= "Hair Offering list.csv",
                    mime='text/csv'
                )
            st.image(resize_image("name_kid.jpeg",219,206))
            with st.expander('Namakaranam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 20 each")
                st.write("Flower | 3 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 20")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Kalasam | 1")
                st.write("Towel | 1")
                st.write("Blouse Piece | 1")
                st.write("Coconuts | 2")
                st.write("Rice | 3 lbs")
                st.write("Coins | $5 (Quarters)")
                st.write("Milk, Honey | Small Qty")
                st.write("Naivedyam (any variety)")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Paper Towels, Scissors,Disposable Glasses,Bowl,Spoon")
                st.write("One Big Plate (to Write the name)")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Namakaranam list.csv'),
                    file_name= "Namakaranam list.csv",
                    mime='text/csv'
                )
            st.image(resize_image("kalasha.jpeg",219,292))
            with st.expander('Punyahavachanam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 10 each")
                st.write("Flower | 1 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Fruits (Any Variety) | 6")
                st.write("Kalasam | 1")
                st.write("Towel | 1")
                st.write("Blouse Piece | 1")
                st.write("Coconuts | 2")
                st.write("Rice | 3 lbs")
                st.write("Coins | $5 (Quarters)")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate, Scissors")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Punyahavachanam list.csv'),
                    file_name= "Punyahavachanam list.csv",
                    mime='text/csv'
                )
            st.image(resize_image("food.jpeg",219,150))
            with st.expander('Hiranya sraddham list'):
                st.write("Name of the item | Quantity")
                st.write("Rice | 2 lbs")
                st.write("Fresh Vegetables | 3 or 5 varieties")
                st.write("Coins | $5 (Quarters)")
                st.write("Sesamee seeds | Small Packet")
                st.write("Dhoti, uttareeyam for wearing")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Hiranya sraddham list.csv'),
                    file_name= "Hiranya sraddham list.csv",
                    mime='text/csv'
                )
            st.image(resize_image('shiva.jpeg',219,219))
            with st.expander('Rudrabhishekam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 30 each")
                st.write("Flower | 2 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 20")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Rice | 1 lbs")
                st.write("Kalasam | 1")
                st.write("Milk | 3 Gallon")
                st.write("Yogurt | Small Qty")
                st.write("Ghee | Small Qty")
                st.write("Honey | 1 Bottle")
                st.write("Sugar | Small Qty")
                st.write("Fruit Juices | Small Qty")
                st.write("Camphor | One small packet")
                st.write("Rose Water | 1 Bottle")
                st.write("Gangajal | Small Bottle")
                st.write("Coconut Water | Small Bottle")
                st.write("Steel Big Basin | 1")
                st.write("Coins | $10 (Quarters)")
                st.write("White Thread Reel | 1")
                st.write("Coconuts | 2")
                st.write("Two Varieties of Prasadam")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate, Scissors")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Rudrabhishekam list.csv'),
                    file_name= "Rudrabhishekam list.csv",
                    mime='text/csv'
                )
        with col2_1:
            st.image(puja_icon("kid-sitting-at-desk.jpeg"))
            with st.expander('Aksharabhyasam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 20 each")
                st.write("Flower | 2 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 12")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Kalasam | 1")
                st.write("Towel | 1")
                st.write("Blouse Piece | 2")
                st.write("Coconuts | 2")
                st.write("Rice | 3 lbs")
                st.write("Coins | $5 (Quarters)")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Book, Pen, Pencil, Slate, White Chalk, Paper Towels, Scissor Disposable Glasses Spoons One Plate")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Aksharabhyasam_list.csv'),
                    file_name= "Aksharabhyasam list.csv",
                    mime='text/csv'
                )
            st.image(resize_image('engagement-rings.jpeg',219,220))
            with st.expander('Engagement list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 15 each")
                st.write("Flower | 2 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 12")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Flower Mala | 2")
                st.write("Coconuts | 2")
                st.write("Rice | 3 lbs")
                st.write("Coins | $5 (Quarters)")
                st.write("Sweets")
                st.write("New Clothes and Ornaments for Bride and Groom")
                st.write("White Paper for writing Wedding Card and Pen")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Book, Pen, Pencil, Slate, White Chalk, Paper Towels, Scissor Disposable Glasses Spoons One Plate")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Engagement list.csv'),
                    file_name= "Engagement list.csv",
                    mime='text/csv'
                )
            st.image(resize_image('kid_eating.jpeg',219,219))
            with st.expander('Annaprasana list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 20 each")
                st.write("Flower | 2 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 12")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Kalasam | 1")
                st.write("Towel | 1")
                st.write("Blouse Piece | 1")
                st.write("Coconuts | 2")
                st.write("Rice | 3 lbs")
                st.write("Coins | $5 (Quarters)")
                st.write("Naivedyam (any variety)")
                st.write("Rice Paayasam for Feeding")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write('Paper Towels, Scissors,Disposable Glasses,Spoons, One Plate')
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Annaprasana list.csv'),
                    file_name= "Annaprasana list.csv",
                    mime='text/csv'
                )
            st.image(resize_image('Home.jpeg',219,219))
            with st.expander('Gruha Pravesam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 20 each")
                st.write("Flower | 2 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 12")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Limes | 12")
                st.write("Red and White Pumpkins | 1 each")
                st.write("Milk | 1 Gallon")
                st.write("Navadhanyas | Small Packets Seperately")
                st.write("Kalasam | 1")
                st.write("Towel | 1")
                st.write("Blouse Piece | 1")
                st.write("Coconuts | 8 (Depends upon Rooms)")
                st.write("Rice | 3 lbs")
                st.write("Coins | $10 (Quarters)")
                st.write("New Pot for Boiling Milk")
                st.write("God’s Picture, Nadaswaram Cassette, Jasmine String Mala")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Prasadam as per family tradition")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate, Knife, Scissors, Mango Leaves")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Gruha Pravesam list.csv'),
                    file_name= "Gruha Pravesam list.csv",
                    mime='text/csv'
                )
            st.image(resize_image('kid_shoveling.jpeg',219,272))
            with st.expander('Bhu puja list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Betel leaves | 15 ")
                st.write("Betel nuts | 20 ")
                st.write("Sandalwood powder | One small tin")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 12")
                st.write("Camphor | One small packet")
                st.write("Coconuts | 5")
                st.write("Rice | 2 lbs")
                st.write("Milk | Small Qty")
                st.write("Mixed navadhanyams | 1 lb")
                st.write("Gold, silver, copper, coral, Pagadam | small pieces")
                st.write("Kalasam | 1")
                st.write("Vastram for kalasam | 1 towel & blouse piece")
                st.write("Sweets | 1 packet")
                st.write("Water | 1 bottle")
                st.write("Shovel | 1")
                st.write("Bricks | 9")
                st.write("Coins | $20(Quarters)")
                st.write("Nava ratnams")
                st.write("Flowers")
                st.write("Deeparadhana samagri (Deepam, oil, wicks, Match box)")
                st.write("God's photo")
                st.write("Napkins,tumbler, plate, spoon")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Bhu puja list.csv'),
                    file_name= "Bhu puja list.csv",
                    mime='text/csv'
                )
            st.image(resize_image('satya.jpeg',219,154))
            with st.expander('Sri Satyanarayana Swami Vratam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 30 each")
                st.write("Flower | 4 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 25")
                st.write("Flower String Mala (Jasmine or any) | 1 Box")
                st.write("Navadhanyas | Small Packets Seperately")
                st.write("Kalasam | 1")
                st.write("Towel | 1")
                st.write("Blouse Piece | 1")
                st.write("Coconuts | 2")
                st.write("Rice | 3 lbs")
                st.write("Coins | $10 (Quarters)")
                st.write("Panchamrutam (Milk, Yogurt, Ghee, Honey, Sugar) | Small Qty")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Prasadam as per family tradition")
                st.write("Satyanarayana Swamy Picture")
                st.write("Small Idol For Abhishekam (Vishnu / Krishna / Satyanarayana Swamy)")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate, Scissors")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Sri Satyanarayana Swami Vratam list.csv'),
                    file_name= "Sri Satyanarayana Swami Vratam list.csv",
                    mime='text/csv'
                )
            st.image(resize_image("kalyna.jpeg",224,398))
            with st.expander('Kalyna Utsvam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 20 each")
                st.write("Flower | 2 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 20")
                st.write("Flower String Mala (Jasmine or any) | 3 Box")
                st.write("Garlands for Swamy and Ammavaru | 3")
                st.write("Rice for Talambralu | 4lbs")
                st.write("Kalasam | 1")
                st.write("Paste of Jaggery and Jeera | Small Qty")
                st.write("Milk, Yogurt And Honey | Small Qty")
                st.write("Towel | 1")
                st.write("Blouse Piece | 1")
                st.write("Coins | $10 (Quarters)")
                st.write("White Thread Reel | 1")
                st.write("Coconuts | 2")
                st.write("Two Varieties of Prasadam")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate, Scissors")
                st.write("Vastram for Swamy and Ammavaru")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Kalyna Utsvam list.csv'),
                    file_name= "Kalyna Utsvam list.csv",
                    mime='text/csv'
                )
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