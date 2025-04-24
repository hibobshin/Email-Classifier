from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def summarizer_agent(state):
    email_text = state["email"]
    summary = summarizer(email_text, max_length=60, min_length=10, do_sample=False)[0]["summary_text"]
    return {**state, "summary": summary}

def classifier_agent(state):
    summary = state["summary"]
    labels = ["schedule meeting", "reply", "urgent", "archive"]
    result = classifier(summary, candidate_labels=labels)
    top_label = result["labels"][0]
    return {**state, "label": top_label}

def action_agent(state):
    label = state["label"]
    if label == "schedule meeting":
        action = "Suggested: Create calendar event"
    elif label == "reply":
        action = "Suggested: Auto-reply generated"
    elif label == "urgent":
        action = "Suggested: Notify user immediately"
    else:
        action = "Suggested: Archive this email"
    return {**state, "action": action}
