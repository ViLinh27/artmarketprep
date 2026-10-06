import streamlit as st

st.title("Artist Market Prep")

st.write("Hello Visitor. This web app is designed for the purpose of being a one stop shop for artists who participate in in-person art / craft markets.")

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

st.divider()
st.subheader("Credits")
st.write("The calendar widget is from this im-perativa on the streamlit forums: " \
"https://discuss.streamlit.io/t/new-component-streamlit-calendar-a-new-way-to-create-calendar-view-in-streamlit/48383")
st.write("The documentation for that calendar widget: https://github.com/im-perativa/streamlit-calendar")