from langgraph.graph import StateGraph, START, END
from state.state import AgentState
from agents.research_agent import research_agent
from agents.financial_agent import financial_agent
from agents.decision_agent import decision_agent

#node 1
def research_node(state):

    ticker = state["ticker"]

    report = research_agent(ticker)

    state["research_report"] = report

    return state

#node 2
def financial_node(state):

    ticker = state["ticker"]

    report = financial_agent(ticker)

    state["financial_report"] = report

    return state

#node 3
def decision_node(state):

    return decision_agent(state)

#creating graph builder
graph_builder = StateGraph(AgentState)

#registering nodes
graph_builder.add_node(
    "research",
    research_node
)

graph_builder.add_node(
    "financial",
    financial_node
)

graph_builder.add_node(
    "decision",
    decision_node
)

#adding edges
graph_builder.add_edge(
    START,
    "research"
)

graph_builder.add_edge(
    "research",
    "financial"
)

graph_builder.add_edge(
    "financial",
    "decision"
)

graph_builder.add_edge(
    "decision",
    END
)

#compile graph
graph = graph_builder.compile()
