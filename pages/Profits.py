import streamlit as st
from profit_db import (
    init_profits_db,
    add_profits,
    get_profits_overtime,
    delete_profits,
)

st.title("Profits Calculator")

st.write("Here you can calculate your net profits. " \
"This means you subtract the sum of your upfront costs from " \
"the market transaction totals to see what's leftover (that's the profit.)")

st.write("You have the option of just getting the profit from your most current market event, " \
"or cataloguing profits from different markets overtime to see how well you're doing financially with " \
"the art over time.")

init_profits_db() #initialize the data base for profits over time

st.header("Current Market Profit Calculator")
recent_tt = st.number_input("What's your transaction total from your most recent market?", placeholder="Type your most recent transaction total (sum) here...")
recent_uc = st.number_input("What's the Upfront costs from your most recent market? ", placeholder="Type Your Most Current UPfront costs...")
st.write("Net Profit From your most recent market:")
st.subheader(f"${recent_tt - recent_uc}")

st.divider()

st.header("Profits Over Time")

marketName = st.text_input("Enter Market Name",placeholder="Enter Market Name...")
marketUpfront = st.number_input("Enter Market's Upfront Costs", placeholder = "Enter Market's Upfront Cost...")
marketSales = st.number_input("Enter Market Sales Total", min_value=0)
marketProfit = marketSales - marketUpfront
st.subheader(f"You made a profit of ${marketProfit} at this market: {marketName}"  )
marketnotes = st.text_input("Do you have any notes to keep in mind about this market?",placeholder="Enter market Notes...")

#add button here
if st.button("Add market data"):
    # function for db here
    add_profits(marketName, marketUpfront, marketSales, marketProfit, marketnotes)
    st.success("Market Data added successfully")

st.write("This table will track profits of each market event entered.")
pot_df = get_profits_overtime()
st.dataframe(pot_df)

st.write("This graph tracks profits vs. sales.")
st.line_chart(
    pot_df,
    x="profits",
    y="sales_total",
    color="red"
)