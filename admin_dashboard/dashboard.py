import streamlit as st
import requests

st.title("Admin Dashboard")

user_id = st.text_input("Enter user ID")
if user_id:
    res = requests.get(f"http://localhost:8000/api/content/next-module/{user_id}")
    st.write("Recommended Module:", res.json()["module"])
