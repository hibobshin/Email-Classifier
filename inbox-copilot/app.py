import streamlit as st
from data import emails
from graph import build_graph

st.title("📬 Inbox Triage Copilot")

selected_subject = st.selectbox("Select an email to triage:", [email["subject"] for email in emails])
selected_email = next(email for email in emails if email["subject"] == selected_subject)

st.write("### Email Body:")
st.write(selected_email["body"])

if st.button("Run AI Workflow"):
    graph = build_graph()
    output = graph.invoke({"email": selected_email["body"]})
    
    st.write("### ✨ Summary:")
    st.success(output["summary"])

    st.write("### 🧠 Intent:")
    st.info(output["label"])

    st.write("### 🤖 Action:")
    st.warning(output["action"])
