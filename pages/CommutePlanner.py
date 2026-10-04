import streamlit as st
from commute_db import(
    init_commute_db,
    add_commute_step,
    get_commute_plan,
    delete_commute_step,
    update_commute_step,
    delete_all_commute_plan,
)

st.title("Commute Planner")
st.write("This page will allow you to plan details in your commute. " \
"I'll hopefully get google maps to work on this thing so you don't have to go on a different tab/ app to plan. " \
"But that'll be later.")

init_commute_db() #initialize commute planner db

## enter info here:
commute_step = st.number_input(
    "What step in the commute plan is this? ", value=None, placeholder="Type a number..."
)
market_date = st.text_input("What's the date of the market?")
time_to_leave = st.text_input("When are you leaving?")
eta = st.text_input("When do you expect to get there?")
traffic = st.text_input("How's the traffic?")

## add step to commute plan
if st.button("Add to Commute Plan"):
    add_commute_step(commute_step,market_date,time_to_leave,eta,traffic)
    st.success("Step in Commute Plan Added Successfully")

#view db here
commute_df = get_commute_plan()
st.dataframe(commute_df)