import streamlit as st

pages = {
    "":[
        st.Page("pages/Homepage.py", title="Home"),
        st.Page("pages/CommutePlanner.py", title="Commute Planner"),
        st.Page("pages/Itinerary.py", title="Itinerary"),
    ],
    "Vendor": [
        st.Page("pages/MarketsApplied.py", title="Markets Applied"),
        st.Page("pages/Inventory.py", title="Inventory"),
        st.Page("pages/UpfrontCosts.py", title="Upfront Costs"),
        st.Page("pages/TransactionTracker.py", title="Transaction Tracker"),
        st.Page("pages/Profits.py", title="Profits Calculator"),
    ],
    "Event Planner":[
        st.Page("pages/Calendar.py", title="Calendar"),
        st.Page("pages/VendorTracker.py", title="Vendor Tracker"),
    ]
}

page = st.navigation(pages)

page.run()