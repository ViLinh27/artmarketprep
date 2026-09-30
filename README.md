# artmarketprep

This is a web app made in streamlit that is meant to streamline the prep work for artist markets. This will be done in streamlit for availability and ease of access

## Process

### Ideation

I started concepting out some ideas and notes for what I wanted the app to do. This means writing down a list of features and asking some artists what is involved in both the vendor side of planning artist market events and the host side of those same events.

<summary> <h3>Visual Planning</h3> </summary>
<details>
After all the ideas are written down. I do some visual planning. I go onto Miro to help plan out those ideas in a way I could visually plan out.

This is the overall visual planning:
![flowchart](./assets/flowchart.jpg)

This is a closer loook at the payment tracker concept:
![trackers](./assets/flowchart-trackers.jpg)
![paymenttracker](./assets/flowchart-paymenttracker.jpg)

I added some useful reference links to, and had the idea of trying to integrate google maps into the app for a commute planner:
![reference links](/assets/flowchart-useful%20links.jpg)

</details>

<summary> <h3>Prototyping</h3> <summary>
<details>
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

<summary> <h4> Infinite Loop and Wrong File Structure </h4> </summary>
<details>
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

<summary> <h4>The Homepage</h4> </summary>
<details>
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
