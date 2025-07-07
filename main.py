# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
#     "requests",
#     "streamlit",
# ]
# ///

# I HAVE USED 'UV' - (PACKAGE MANAGER LIKE NPM BUT FOR PYTHON )
# There is a different way to execute scripts (like this) and projects when working with UV
# check README.md for the same

'''
Streamlit utilises python's declarative code.
'''
import streamlit as st
import pandas as pd
import requests

# Displying Text
st.title("Hellyo Streamlit")
st.subheader("made with love")
st.text("Welcome")  # Displays plain, preformatted text

st.write("How's your day going ?") # Displays almost anything—text, Markdown, dataframes, charts, etc.

############################################
st.title ("Flower Delivery")

name= st.text_input("Enter your name")

# Creates a Drop-down menu
# st.selectbox("Your fav flower: ",["Tulip", "Carnation", "Lotus","Rose"])
flower= st.selectbox("Which flower do you like to buy: ",["Tulip", "Carnation", "Lotus","Rose"])   # can also store the input in a variable

st.write(f"You chose {flower} , excellent !")
st.success("Here is your flower")  # there also exist error, warning and info commands

st.slider("Number of flowers in bouquet",5,20,10)
st.number_input("Number of bouquet : ",1,10,1)

note= st.checkbox("Add a note for your loved ones")

if note:
    flower_for=st.radio("Who are these flowers for ?", ['Parent', 'Sibling', 'Relative', 'Partner', 'Friend'])
    st.success(f"Note Added for your {flower_for}! ")

st.date_input("Select date of delivery")

if st.button("Order Now"):
    st.success("Your order has been placed.")

###############################################################

st.title('Vote for your favourite flower')

col1, col2 = st.columns(2)

with col1:
    st.header("TULIPS")
    st.image("https://images.unsplash.com/photo-1520763185298-1b434c919102?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dHVsaXB8ZW58MHx8MHx8fDA%3D", width=200)
    vote1= st.button("Tulips Janta Party")

with col2:
    st.header("CARNATIONS")
    st.image("https://images.unsplash.com/photo-1612589432434-bf513e5131a0?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2FybmF0aW9ufGVufDB8fDB8fHww", width=200)
    vote2= st.button("Carnations Nationl Congress")

if vote1:
    st.success("Thanku for voting for Tulips !")
elif vote2:
    st.info("Thanku for voting for Carnations !")
    
####################

name= st.sidebar.text_input("Enter your name")
email= st.sidebar.text_input("Enter your email")
age= st.sidebar.number_input("Enter your age",10,100,25 )

with st.expander("Single ? Learn how to gift flowers to someone."):
    st.write('''
    1. Approach the person you like
    2. Ask him/her/they/it... for a coffee date
    3. Get rejected upfront (u ain't getting one XD)  
    4. Order our flowers to wipe your tears (it will appear poetic and they do smell good ^_− )
''')
# We can also use markdown language in streamlit     
#st.markdown("")

#################################################################

# Working with pandas

st.title('Sales Analysis')

file= st.file_uploader('upload your csv file', type=['csv'] )

if file:
    df= pd.read_csv(file)  # or can use pf.read_csv("flowers.csv") directly ,in this case.
    st.subheader('Data Preview')
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())    

#########################################################

# API Handling

st.title("Live Currency converter")
amount = st.number_input("Enter the amount (in INR)", 1)

convert_to = st.selectbox("Convert to:", ['USD','EUR','GBP','JPY'])

if st.button('convert'):
    url="https://api.exchangerate-api.com/v4/latest/INR"
    response=requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][convert_to]
        converted = rate*amount
        st.success(f"{amount} INR = {converted} {convert_to}")
    else:
        st.error("Failed to fetch conversion rate")
