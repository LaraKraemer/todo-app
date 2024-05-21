import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo app")
st.subheader("This is my todo app")
st.text("This app helps you organize your daily tasks")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Add new Todo item...")