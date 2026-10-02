# artmarketprep

This is a web app made in streamlit that is meant to streamline the prep work for artist markets. This will be done in streamlit for availability and ease of access

## Process

### Ideation

I started concepting out some ideas and notes for what I wanted the app to do. This means writing down a list of features and asking some artists what is involved in both the vendor side of planning artist market events and the host side of those same events.

<details>
<summary> <h3>Visual Planning</h3> </summary>
After all the ideas are written down. I do some visual planning. I go onto Miro to help plan out those ideas in a way I could visually plan out.

This is the overall visual planning:
![flowchart](./assets/flowchart.jpg)

This is a closer loook at the payment tracker concept:
![trackers](./assets/flowchart-trackers.jpg)
![paymenttracker](./assets/flowchart-paymenttracker.jpg)

I added some useful reference links to, and had the idea of trying to integrate google maps into the app for a commute planner:
![reference links](/assets/flowchart-useful%20links.jpg)

</details>

<details>
<summary><h3>Prototyping</h3><summary>
After the flow chart is done, I go onto penpot.app (open source alternative to figma) and make some low fidelity prototypes.

#### First Version

This was the first prototype:
[![app prototype version 1](/assets/v2-homepage-prototype.jpg)](https://design.penpot.app/#/view?file-id=24d9d841-759d-81bc-8008-b57cbdfd7117&page-id=24d9d841-759d-81bc-8008-b57cbdfd7118&section=interactions&index=0&share-id=4d62b120-e9f3-4c78-8998-c4c923e34c6a)

#### Second Version

This was the second version:

[![App prototype version 2](./assets/v1-homepage-prototype.jpg)](https://design.penpot.app/#/view?file-id=a5ac146a-5787-80fa-8008-b6e4b0f11ed6&page-id=24d9d841-759d-81bc-8008-b57cbdfd7118&section=interactions&index=0&share-id=12794aee-2d06-4290-a9f8-69c020e2f920)

</details>

### Code

I build a basic skeleton. There's the Homepage.py file in the root folder. There's all the other pages in the pages folder(still inside the root folder).

<details>
<summary> <h4> Infinite Loop and Wrong File Structure </h4> </summary>
With my original project structure and the use of a dictionary to try to group my navigation pages I had an infinite loop on the homepage. The original file structure looked like this:

```
Root_Folder/
|--- Homepage.py
|---/pages/
|---|--- Calendar.py
|---|--- CommutePlanner.py
|---|--- Inventory.py
|---|--- Itinerary.py
|---|--- MarketsApplied.py
|---|--- Profits.py
|---|--- TransactionTracker.py
|---|--- UpfrontCosts.py
|---|--- VendorTracker.py
```

The dictionary looked like this when Homepage.py was still the entrypoint:

```
pages = {
    "Main":[
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
```

Since Homepage.py was in the dictionary, but also the entry point here, the page.run() made the entrypoint file call itself recursively (until the max number would be reached). So that's bad.

The simple fix was changing the entry point name to a main.py. THe Homepage.py in the Main group of the dictionary would be made into a new file inside the pages folder so the new file structure looked like this:

```
Root_Folder/
|--- main.py
|---/pages/
|---|--- Calendar.py
|---|--- CommutePlanner.py
|---|--- Homepage.py
|---|--- Inventory.py
|---|--- Itinerary.py
|---|--- MarketsApplied.py
|---|--- Profits.py
|---|--- TransactionTracker.py
|---|--- UpfrontCosts.py
|---|--- VendorTracker.py
```

Since Home is up top, it's still the first we page we land on when the main.py entry point is run.

</details>

<details>
<summary> <h4>The Homepage</h4> </summary>
The goal for this page is just a blurb for instructions and a place for a master to do list for the artist(user)'s planning process. The artist can add whatever task needs to be done. And check the task off when needed. The tasks are put into a queue (basically) so the delete button just deletes the last task put into the list for now. My goal is to make the delete button delete custom tasks eventually.

This is the code below the main title of the homepage:

```
st.write("This is a master to do list for prepping for the art market. ")
mytask = st.text_input("Enter any task you need to do here: ")

tasklist = st.session_state.get("tasks", [])
if st.button("Add Task"):
    tasklist.append(mytask)
    st.session_state.tasks = tasklist
    st.success("Task added!")

##------Figure out how to delete custom task later -------
deletetaskbtn = st.button("Delete Last Task")
if deletetaskbtn:
    if tasklist:
        tasklist.pop()
        st.session_state.tasks = tasklist
        st.success("Last task deleted!")
    else:
        st.warning("No tasks to delete.")

if tasklist:
    st.write("Master TO DO list:")
    for task in tasklist:
        st.checkbox(f" {task}")
```

1. First the user input.

The Text Input is where the user will type in the task for their master to do list. Pretty Self Explanatory. That task input gets put into a variable called mytask to use later.

2. The task list.

The tasklist is initialized as an array and given as a value to streamlit's session state. Th session state helps in persisting data and sharing variables and things between runs of the app. So giving the tasklist to the sesion state makes sense because we don't know if the user will go to other pages of the app and come back (for example).

Once there are things in the task list, the user will be able to see the task and a checkbox below the buttons (add and delete).

3. The Delete button

The delete button was put above the tasklist if statement because when I had it after, the list would not update after a deletion unless I refreshed the entire page. Streamlit goes top down when executing, so putting the delete button above the task list makes sure anything that is set to delete can be deleted from the task list before the user sees the new task list.

</details>

<details>
<summary> <h4>The Commute Planner Page </h4> </summary>
The commute planner
</details>

<details>
<summary> <h4>The Itinerary Page </h4> </summary>
The itinerary page is to help plan events. This works for both vendors and event organizers so everyone knows what to expect.

I'll have to eventually think about whether i want the itinerary to be a checklist and be able to rearrange the events or not.

##### Bug: if I put an earlier event after a later event, the event needs to automatically show before the later event

</details>

<details>
<summary> <h4>The Markets Applied Page </h4> </summary>
The markets applied page is to help track the markets an artist has applied to. This is the existing code.

```
import streamlit as st
from marketsapplied_db import (
    init_marketsapplied_db,
    add_market_application,
    get_market_applications,
    delete_market_application,
    update_market_application_status,
    search_market_name,
    delete_all_market_applications
)

st.title("Markets Applied")
st.write("This where you track markets you applied to and their statuses. You will be able to see which markets you get accepted to and know what to prepare for.")

init_marketsapplied_db() # Initialize the database for tracking market applications

market_name = st.text_input("Enter Market Name...")
market_theme = st.text_input("Enter Market Theme...")
market_host = st.text_input("Enter Market Host...")
market_location = st.text_input("Enter Market Location...")
application_date = st.date_input("Enter Application Date...")
market_status = st.selectbox("Select Market Status...", ["Pending", "Accepted", "Rejected"])
market_vendor_fee = st.number_input("Enter Market Vendor Fee...", min_value=0.0, step=0.01)
market_notes = st.text_input("Enter any notes you'd like to add about this market application...")

if st.button("Add Market Application"):
add_market_application(market_name, market_theme, market_host, market_location, application_date.strftime("%Y-%m-%d"), market_status, market_vendor_fee, market_notes)
st.success("Market application added successfully!")

## update market application status

market_update = st.text_input("Enter Market Name to Update Status...")
new_status = st.selectbox("Select New Status for Market Application...", ["Pending", "Accepted", "Rejected"])
if st.button("Update Market Application Status"):
update_market_application_status(market_update, new_status)
st.success("Market application status updated successfully!")

## Show market applications

markets_df = get_market_applications()
st.dataframe(markets_df)
#st.write("You can expand the database by hovering over it. You'll be able to see a little pop up, click the right symbol.")

```

I was having issues before (the status would not update) because my `def update_market_application_status(application_name, new_status)` used the id as a paramter instead of the name (not user friendly). I used the `update_vendor_status(vendor_name, new_status)` from the vendorTracker_db.py as a base and the marketsapplied_db.py functions work fine now (the one anyway).

</details>

<details>
<summary> <h4>The Inventory Page </h4> </summary>
The inventory page was for cataloguing inventory. It's just the one database so it was pretty self explanatory.
Here is the main code (outside of the imports):

```

st.title("Inventory Planner")

st.write("This is where you can track inventory items. You write down price per item, stock quantity and the works.")

init_inventory_db() # Initialize the database for tracking inventory items

item_name = st.text_input("Enter Item Name...")
item_stock = st.number_input("Enter Stock Quantity...", min_value=0, step=1)
item_price = st.number_input("Enter Price per Item...", min_value=0.0, step=0.01)
item_notes = st.text_input("Enter any notes you'd like to add about this inventory item...")

if st.button("Add Inventory Item"):
add_inventory_item(item_name, item_stock, item_price, item_notes)
st.success("Inventory item added successfully!")

inventory_df = get_inventory_items()
st.dataframe(inventory_df)

```

</details>

<details>
<summary> <h4>The Upfront Costs Page </h4> </summary>
The upfront costs
</details>

<details>
<summary> <h4>The Transaction Tracker Page </h4> </summary>
The transaction tracker page
</details>

<details>
<summary> <h4>The Profits Calculator Page </h4> </summary>
The profits calculator page
</details>

<details>
<summary> <h4>The Calendar Page </h4> </summary>
The calendar page
</details>

<details>
<summary> <h4>The Vendor Tracker Page </h4> </summary>
The vendor tracker page is for event planners. This page will help track applicants to their events. The event planners will be able to track applicant status and who among those approved payed their fees.

#### Starting out with the vendor tracker database

This is the code I started out with:

```

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
st.title("Vendor Tracker")

st.write("This is where you can track vendors who have applied to your market, including whether they are" \
" approved, pending, or rejected. You can also view their application details and contact information.")

init_db() # Initialize the database for tracking vendor applicants

vendorname = st.text_input("Enter Vendor Name...")
vendorIG = st.text_input("Enter Vendor Instagram Tag...")
vendorStatus = st.text_input("Enter Vendor Status (Approved, Pending, Rejected)...")
vendorNotes = st.text_input("Enter any notes you'd like to add about this vendor applicant...")

if st.button("Add Vendor"):
add_vendor(vendorname, vendorIG, vendorStatus, vendorNotes)
st.success("Vendor added successfully!")

if st.button("Delete All Vendors"):
delete_all_vendors()
st.success("All vendors have been deleted.")

st.write("Track Vendors")
vendors_df = get_vendors()
st.dataframe(vendors_df)

```

Overall it's a good start. I can enter in the appropriate vendor information. The dataframe displays it (mostly) correctly. The delee all vendors works (with some caveats). Now i need to think about two things (for now):

1. Updating individual vendor status

2. Using the values of approved vendors into the new database to track if vendor fees were payed

#### Updating the Vendor Status

This is the code for a successful vendor status update. I might need to mess with the order of how the buttons are arranged though:

```

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
st.title("Vendor Tracker")

st.write("This is where you can track vendors who have applied to your market, including whether they are" \
" approved, pending, or rejected. You can also view their application details and contact information.")

init_db() # Initialize the database for tracking vendor applicants

vendorname = st.text_input("Enter Vendor Name...")
vendorIG = st.text_input("Enter Vendor Instagram Tag...")
vendorStatus = st.text_input("Enter Vendor Status (Approved, Pending, Rejected)...")
vendorNotes = st.text_input("Enter any notes you'd like to add about this vendor applicant...")

if st.button("Add Vendor"):
add_vendor(vendorname, vendorIG, vendorStatus, vendorNotes)
st.success("Vendor added successfully!")

if st.button("Delete All Vendors"):
delete_all_vendors()
st.success("All vendors have been deleted.")

vendor_update = st.text_input("Enter Vendor Name to Update Status...")
new_status = st.text_input("Enter New Status for Vendor (Approved, Pending, Rejected)...")
if st.button("Update Vendor Status"):
update_vendor_status(vendor_update, new_status)
st.success("Vendor status updated successfully!")

st.write("Track Vendors")
vendors_df = get_vendors()
st.dataframe(vendors_df)

```

Now I need to see how to import approved vendors to a new database to track vendor fees.

</details>

### Styling & making the app look pretty

```

```

```

```

```

```
