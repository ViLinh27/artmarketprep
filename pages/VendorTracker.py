import streamlit as st
from vendorTracker_db import(
    init_db,
    add_vendor,
    get_vendors,
    delete_vendor,
    update_vendor_status,
    search_vendor_name,
    delete_all_vendors,
    get_approvedVendors
)
from vendorFeeTracker_db import (
    init_vendorfee_db,
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

## Delete button for all vendors. May need to move it
if st.button("Delete All Vendors"):
    delete_all_vendors()
    st.success("All vendors have been deleted.")

## view vendors in vendor applicant tracker
st.write("Track Vendors")

vendors_df = get_vendors()
st.dataframe(vendors_df)


st.divider()
st.subheader("Approved Vendors")
approved_df = get_approvedVendors()
st.dataframe(approved_df)