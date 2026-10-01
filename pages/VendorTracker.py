import streamlit as st
from vendorTracker_db import(
    init_db,
    add_vendor,
    get_vendors,
    delete_vendor,
    update_vendor_status,
    search_vendor_name,
    delete_all_vendors
)
from vendorFeeTracker_db import (
    init_vendorfee_db,
    add_vendor_fee_info,
    get_vendor_fees
)

st.title("Vendor Tracker")

st.write("This is where you can track vendors who have applied to your market, including whether they are" \
" approved, pending, or rejected. You can also view their application details and contact information.")


init_db()  # Initialize the database for tracking vendor applicants
init_vendorfee_db()  # Initialize the database for tracking vendor fees

## Enter vendor applicant info here:
vendorname = st.text_input("Enter Vendor Name...")
vendorIG = st.text_input("Enter Vendor Instagram Tag...")
vendorStatus = st.text_input("Enter Vendor Status (Approved, Pending, Rejected)...")
vendorNotes = st.text_input("Enter any notes you'd like to add about this vendor applicant...")

if st.button("Add Vendor"):
    add_vendor(vendorname, vendorIG, vendorStatus, vendorNotes)
    st.success("Vendor added successfully!")


## updating vendor status in vendor applicant tracker
vendor_update = st.text_input("Enter Vendor Name to Update Status...")
new_status = st.text_input("Enter New Status for Vendor (Approved, Pending, Rejected)...")
if st.button("Update Vendor Status"):
    update_vendor_status(vendor_update, new_status)
    st.success("Vendor status updated successfully!")

## view vendors in vendor applicant tracker
st.write("Track Vendors")
## Delete button for all vendors. May need to move it
if st.button("Delete All Vendors"):
    delete_all_vendors()
    st.success("All vendors have been deleted.")

vendors_df = get_vendors()
st.dataframe(vendors_df)

if not vendors_df.empty:
    #debug
    st.write("Approved Vendors:")
    approved_vendors_df_demo = vendors_df[vendors_df['status'] == 'Approved']
    st.dataframe(approved_vendors_df_demo)

    if not vendors_df[vendors_df['status'] == 'Approved'].empty:
        st.write("Have the approved vendors paid their fees?")
        approved_vendors_df = vendors_df[vendors_df['status'] == 'Approved']

        for index, row in approved_vendors_df.iterrows():
            st.write("Vendor Name:", row['name'])#debug
            st.write("Vendor Instagram:", row['instagram'])#debug
            vendor_name = row['name']
            vendor_instagram = row['instagram']
            fee_status = "Pending"  # Default fee status for approved vendors
            
        add_vendor_fee_info(vendor_name, vendor_instagram, fee_status, "")

        st.dataframe(get_vendor_fees())

else:
    st.write("No vendors found.")