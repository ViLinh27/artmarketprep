import streamlit as st

st.title("Profits Calculator")

st.write("Here you can calculate your net profits. " \
"This means you subtract the sum of your upfront costs from " \
"the market transaction totals to see what's leftover (that's the profit.)")

st.write("You have the option of just getting the profit from your most current market event, " \
"or cataloguing profits from different markets overtime to see how well you're doing financially with " \
"the art over time.")

st.header("Current Market Profit Calculator")
recent_tt = st.number_input("What's your transaction total from your most recent market?", placeholder="Type your most recent transaction total (sum) here...")
recent_uc = st.number_input("What's the Upfront costs from your most recent market? ", placeholder="Type Your Most Current UPfront costs...")
st.write("Net Profit From your most recent market:")
st.subheader(f"${recent_tt - recent_uc}")

st.header("Profits Over Time")