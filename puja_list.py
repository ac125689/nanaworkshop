import streamlit as st
from PIL import Image
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

def puja_list():
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
            st.image(resize_image('shiva.jpeg',195,195))
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
            st.image(resize_image("women.jpeg",219,175))
            with st.expander('Seemantam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 15 each")
                st.write("Flower | 2 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Camphor | One small packet")
                st.write("Rice | 2 lbs")
                st.write("Fruits | 12 Bananas and other fruits")
                st.write("Coconuts | 4")
                st.write("Ghee | Small Bottle")
                st.write("Aluminium trays | 1 Big size")
                st.write("Dry Coconut Pieces (Copra) | 4")
                st.write("Seemantam saree | 1")
                st.write("Milk | Small Qty")
                st.write("Flower garlands | 2")
                st.write("Coins | $15 (Quarters)")
                st.write("Vastram for kalasam | 1 towel & blouse piece")
                st.write("Kalasam | 1")
                st.write("Homa samagri | 1 Packet")
                st.write("Cooked rice | 1 Small cup")
                st.write("Sand | 4 lbs")
                st.write("Napkins,tumbler, spoon, and plate")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Seemantam list.csv'),
                    file_name= "Seemantam list.csv",
                    mime='text/csv'
                )
            st.image(resize_image("upanayanam.png",219,171))
            with st.expander('Upanayanam list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 15 each")
                st.write("Flower | 2 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 25")
                st.write("Dry Coconut Pieces (Copra) | 8")
                st.write("Milk | 1 Gallon")
                st.write("Navadhanyas | Small Packets Seperately")
                st.write("Kalasam | 1")
                st.write("Towel | 6")
                st.write("Blouse Piece | 4")
                st.write("Dhotis (9x5) | 2")
                st.write("Lungees | 2")
                st.write("Yagnopaveetam | 3 Pairs")
                st.write("Coconuts | 8")
                st.write("Rice | 3 lbs ")
                st.write("Coins | $20 (Quarters)")
                st.write("Silver Bowl (Bhiksha Patra) | 1")
                st.write("Earthen plates | 6")
                st.write("Earthen pots | 5")
                st.write("Mustard seeds | 50 grams")
                st.write("Lime paste (chunnam) | 1 Tin")
                st.write("Husk | 1/2 lbs")
                st.write("Aluminium Tray | 4 Big size")
                st.write("God’s Picture, Nadaswaram Cassette")
                st.write("Ring and Ear Rings")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Upanayanam list.csv'),
                    file_name= "Upanayanam list.csv",
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
            st.image(resize_image("kalyna.jpeg",219,389))
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
            st.image(resize_image("Birthday.png",219,292))
            with st.expander('60th or 80th Birthday list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 30 each")
                st.write("Flower | 4 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 25")
                st.write("Dry dates | 1 Packet")
                st.write("Coconuts | 10")
                st.write("Dry Coconut Pieces (Copra) | 8")
                st.write("Milk | 1 Gallon")
                st.write("Navadhanyas | Small Packets Seperately")
                st.write("Pradhana Kalasas | 3 (big)")
                st.write("Upa Kalasas | 9 (small)")
                st.write("Iron Pan (Bandlee) | 1")
                st.write("Sesame Oil | 2 lbs")
                st.write("Ghee | 1 lbs")
                st.write("Dhotis (9x5) | 2")
                st.write("Towels | 6")
                st.write("Blouse Pieces | 4 (1 Pattu)")
                st.write("Coconuts | 10")
                st.write("Rice | 10 lbs")
                st.write("Mixed Navadhanyams | 1 lbs")
                st.write("Photo of Lord Shiva")
                st.write("Sand | 5 lbs")
                st.write("Coins | $20 (Quarters)")
                st.write("White Thread Reel | 1")
                st.write("Aluminium trays | 4 Big size")
                st.write("Panchamrutam (milk, yogurt, ghee, honey, Sugar)")
                st.write("Panchagavyam (cow’s Dung, Urine, Milk, Yogurt, Ghee) ")
                st.write("Gold, Silver, Copper, Coral, Pagadam – Small Pieces Mangalyam")
                st.write("God’s Picture, Nadaswaram Cassette")
                st.write("New Clothes")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box) ")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate, Scissors, Mango Leaves, Cotton")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('60th or 80th Birthday list.csv'),
                    file_name= "60th or 80th Birthday list.csv",
                    mime='text/csv'
                )
            st.image(resize_image("wedding.jpeg",219,306))
            with st.expander('Wedding list'):
                st.write("Name of the item | Quantity")
                st.write("Turmeric powder  | One small packet")
                st.write("Kumkum           | One small packet")
                st.write("Sandalwood powder | One small tin")
                st.write("Betel leaves & nuts | 20 each")
                st.write("Flower | 2 Bunches")
                st.write("Incense Sticks (Agarbathi) | 1 Packet")
                st.write("Fruits (Any Variety) | 20")
                st.write("Garlands for Bride and Groom | 2")
                st.write("Rice for Talambralu | 4 lbs")
                st.write("Rice | 3 lbs")
                st.write("Kalasam | 1")
                st.write("Green Coconut | 2")
                st.write("Dry Coconut Pieces (Copra) | 8")
                st.write("Turmeric Roots | One small packet")
                st.write("Paste of Jaggery and Jeera | Small Qty")
                st.write("Milk, Yogurt And Honey | Small Qty")
                st.write("Panneeru Bottle | 1")
                st.write("Thread Reel | 1")
                st.write("Lime Paste (Sunnam) | 1")
                st.write("Towels | 4")
                st.write("Blouse Piece | 4")
                st.write("Coins | $20 (Quarters)")
                st.write("Umbrella, handstick, shoes, hand fan, mirror, bashikam, eyetex")
                st.write("Chamki garlands")
                st.write("Sweet packet")
                st.write("Sindhur")
                st.write("Madhu Parkam (New Clothes for Bride & Groom)")
                st.write("Ring")
                st.write("Wedding Card")
                st.write("Silver Sacred Thread")
                st.write("Scent Bottle")
                st.write("Black Beads and Gold Ball")
                st.write("Mangalyams and Toe Rings")
                st.write("Deeparadhana Samagri (Deepam, Oil, Wicks, Match Box)")
                st.write("Paper Towels, Disposable Glasses, Spoons, One Plate, Scissors, Milk, Yogurt, Mango Leaves, Cotton")
                st.download_button(
                    label="Download the list above",
                    data=puja_list_down('Wedding list.csv'),
                    file_name= "Wedding list.csv",
                    mime='text/csv'
                )