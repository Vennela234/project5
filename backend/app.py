import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/api/content"

st.title("Adaptive Learning QA App")

context = st.text_area("Enter context (lesson notes, passage, etc.):")
question = st.text_input("Ask a question based on the context")

if st.button("Get Answer"):
    if not context or not question:
        st.warning("Please enter both context and question.")
    else:
        try:
            res = requests.post(f"{BACKEND_URL}/qa", json={
                "context": context,
                "question": question
            })
            if res.status_code == 200:
                answer = res.json()
                st.success(f"Answer: {answer['answer']}")
            else:
                st.error("Backend error. Try again.")
        except Exception as e:
            st.error(f"Request failed: {e}")
