import streamlit as st
from itinerary_db import (
    init_itinerary_db,
    add_event,
    get_itinerary,
    delete_event,
    update_event_time,
    search_event_name,
    delete_all_events
)

st.title("Itinerary Planner")

st.write("This is where you can plan events for your market event. Whether you're the host, or you're just a vendor who wants to know what to expect during the day, you can write down what you need here.")

init_itinerary_db()  # Initialize the database for planning events

## enter event info here:
event_date = st.text_input("Enter Event Date (YYYY-MM-DD)...", placeholder="YYYY-MM-DD")
event_time = st.text_input("Enter Event Time (HH:MM)...")
event_name = st.text_input("Enter Event Name...")
event_location = st.text_input("Enter Event Location...")
event_description = st.text_input("Enter Event Description...")
event_notes = st.text_input("Enter any notes you'd like to add about this event...")

## Add event to itinerary
if st.button("Add Event"):
    add_event(event_date, event_time, event_name, event_location, event_description, event_notes)
    st.success("Event added successfully!")

## view events in itinerary
events_df = get_itinerary()
st.dataframe(events_df)