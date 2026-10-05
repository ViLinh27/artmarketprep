import streamlit as st

st.title("Transaction Tracker")
st.write("List all your transactions from your markets here.")

#initalize database here

item_bought = st.text_input("What item was bought? ",placeholder="Type your item name here")
item_price = st.number_input("What was the price of that item? ",placeholder="Type your price number here")
payment_method = st.selectbox(
    "How did the customer pay?",
    ("Card / Tap", "Cash", "Payment App (Cashapp,Paypal,etc...)")
)

#add transaction here

#view df here