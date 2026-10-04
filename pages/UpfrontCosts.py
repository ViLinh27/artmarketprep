import streamlit as st

st.title("Upfront Costs")

st.write("This is where you track any upfront costs." \
"This can include vendor fees, food, new inventory, the works.")

#initialize db here

#enter costs info here:
upfront_fees = st.number_input("What upfront cost is this?", value=None, placeholder="Type a number...")
fee_due_date = st.text_input("When's the due date of the fee?", placeholder="YYYY-MM-DD")
payed_fee = st.toggle("Have you payed the fee? Toggle on For Yes, leave off for No")

# add cost here
if st.button("Add Upfront Cost"):
    st.succedss("Upfront Cost added successfully")
