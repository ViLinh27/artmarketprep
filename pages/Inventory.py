import streamlit as st
from inventory_db import (
    init_inventory_db,
    add_inventory_item,
    get_inventory_items,
    delete_inventory_item,
    update_inventory_stock,
    search_item_name,
    delete_all_inventory_items
)

st.title("Inventory Planner")

st.write("This is where you can track inventory items. You write down price per item, stock quantity and the works.")

init_inventory_db()  # Initialize the database for tracking inventory items

item_name = st.text_input("Enter Item Name...")
item_stock = st.number_input("Enter Stock Quantity...", min_value=0, step=1)
item_price = st.number_input("Enter Price per Item...", min_value=0.0, step=0.01)
item_notes = st.text_input("Enter any notes you'd like to add about this inventory item...")

if st.button("Add Inventory Item"):
    add_inventory_item(item_name, item_stock, item_price, item_notes)
    st.success("Inventory item added successfully!")

inventory_df = get_inventory_items()
st.dataframe(inventory_df)