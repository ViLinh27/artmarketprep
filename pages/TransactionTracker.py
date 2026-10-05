import streamlit as st
from transactions_db import (
    init_transactions,
    add_transaction, 
    get_transactions
)
st.title("Transaction Tracker")
st.write("List all your transactions from your markets here.")

#initalize database here
init_transactions()

item_bought = st.text_input("What item was bought? ",placeholder="Type your item name here")
item_price = st.number_input("What was the price of that item? ",placeholder="Type your price number here")
payment_method = st.selectbox(
    "How did the customer pay?",
    ("Card / Tap", "Cash", "Payment App (Cashapp,Paypal,etc...)"),
    index=None,
    placeholder="Select payment method..."
)
item_notes = st.text_input("Do you have any notes about this item? ",placeholder="Type your notes here")

#add transaction here
if st.button("Add Transaction"):
    add_transaction(item_bought, item_price, payment_method, item_notes)
    st.success("Transaction Added Successfully")

#view df here
st.divider()
t_df = get_transactions()
st.dataframe(t_df)