import streamlit as st

st.title("Calendar Planner")

st.text_input("Enter an event that needs to be remembered")

st.date_input("Enter the date of this event")

st.text_input("Enter any notes about this event to keep in mind.")