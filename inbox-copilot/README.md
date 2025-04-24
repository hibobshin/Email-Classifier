# 📬 Inbox Triage Copilot – Agentic Workflow Demo

> Built in a day using LangGraph, Hugging Face, and Streamlit  
> By Aryamann Marwaha & Team

---

## 🚀 Project Description

Inbox Triage Copilot is a lightweight agentic AI workflow that triages user emails using a chain of specialized agents. Each agent plays a role in understanding, classifying, and acting upon emails – simulating the way a human assistant might handle an inbox.

The project demonstrates how to orchestrate multiple AI agents using LangGraph’s stateful execution and Hugging Face’s language models in a modular and production-scalable format.

---

## 🧠 How It Works

1. **Summarizer Agent**  
   Uses a pre-trained transformer (`facebook/bart-large-cnn`) to summarize the raw email content.

2. **Classifier Agent**  
   Performs zero-shot intent classification (`facebook/bart-large-mnli`) to determine the appropriate action for each email: reply, schedule, archive, or flag as urgent.

3. **Action Agent**  
   Takes action based on the intent – for example, generating a reply, archiving, or suggesting a calendar event.

Each of these steps is orchestrated by a LangGraph agent graph and visualized through a simple Streamlit interface.

---

## 🛠️ Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph) – for agent orchestration  
- [Hugging Face Transformers](https://huggingface.co/models) – for summarization and classification  
- [Streamlit](https://streamlit.io) – for fast prototyping and UI  
- Python 3.10+

---

## 🧪 Demo

Run it locally:

```bash
git clone https://github.com/<your-username>/inbox-triage-copilot.git
cd inbox-triage-copilot
pip install -r requirements.txt
streamlit run app.py
