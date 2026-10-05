import streamlit as st
from upfront_db import(
    init_upfront,
    add_upfront_cost,
    get_upfront_costs,
    update_fee_status
)
st.title("Upfront Costs")

st.write("This is where you track any upfront costs." \
"This can include vendor fees, food, new inventory, the works.")

#initialize db here
init_upfront()

#enter costs info here:
upfront_fees = st.number_input("What upfront cost is this?", value=None, placeholder="Type a number...")
fee_name = st.text_input("What is this fee? ", placeholder="Type in the fee description")
fee_due_date = st.text_input("When's the due date of the fee?", placeholder="YYYY-MM-DD")
payed_fee = st.toggle("Have you payed the fee? Toggle on For Yes, leave off for No")

# add cost here
if st.button("Add Upfront Cost"):
    add_upfront_cost(upfront_fees,fee_name,fee_due_date,payed_fee)
    st.success("Upfront Cost added successfully")

#update any fees here
fee_update_name = st.text_input("What's the fee that needs a status update? ")
if st.button("Update Fee Status"):
    update_fee_status(fee_update_name)

#view df here:
st.divider()
u_df = get_upfront_costs()
st.dataframe(u_df)