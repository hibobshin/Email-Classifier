from langgraph.graph import StateGraph
from agents import summarizer_agent, classifier_agent, action_agent

# Define the state graph
def build_graph():
    workflow = StateGraph()
    workflow.add_node("summarizer", summarizer_agent)
    workflow.add_node("classifier", classifier_agent)
    workflow.add_node("action", action_agent)
    workflow.set_entry_point("summarizer")
    workflow.add_edge("summarizer", "classifier")
    workflow.add_edge("classifier", "action")
    return workflow.compile()
