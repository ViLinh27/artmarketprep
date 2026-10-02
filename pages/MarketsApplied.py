import streamlit as st
from marketsapplied_db import (
    init_marketsapplied_db,
    add_market_application,
    get_market_applications,
    delete_market_application,
    update_market_application_status,
    search_market_name,
    delete_all_market_applications
)

st.title("Markets Applied")
st.write("This where you track markets you applied to and their statuses. You will be able to see which markets you get accepted to and know what to prepare for.")

init_marketsapplied_db()  # Initialize the database for tracking market applications

market_name = st.text_input("Enter Market Name...")
market_theme = st.text_input("Enter Market Theme...")
market_host = st.text_input("Enter Market Host...")
market_location = st.text_input("Enter Market Location...")
application_date = st.date_input("Enter Application Date...")
market_status = st.selectbox("Select Market Status...", ["Pending", "Accepted", "Rejected"])
market_vendor_fee = st.number_input("Enter Market Vendor Fee...", min_value=0.0, step=0.01)
market_notes = st.text_input("Enter any notes you'd like to add about this market application...")

if st.button("Add Market Application"):
    add_market_application(market_name, market_theme, market_host, market_location, application_date.strftime("%Y-%m-%d"), market_status, market_vendor_fee, market_notes)
    st.success("Market application added successfully!")

## update market application status
market_update = st.text_input("Enter Market Name to Update Status...")
new_status = st.selectbox("Select New Status for Market Application...", ["Pending", "Accepted", "Rejected"])
if st.button("Update Market Application Status"):
    update_market_application_status(market_update, new_status)
    st.success("Market application status updated successfully!")

## Show market applications
markets_df = get_market_applications()
st.dataframe(markets_df)
#st.write("You can expand the database by hovering over it. You'll be able to see a little pop up, click the right symbol.")
