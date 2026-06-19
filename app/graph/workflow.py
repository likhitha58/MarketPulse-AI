from langgraph.graph import StateGraph, START, END
from state.state import AgentState
from agents.research_agent import research_agent
from agents.financial_agent import financial_agent
from agents.news_agent import news_agent
from agents.bull_agent import bull_agent
from agents.bear_agent import bear_agent
from agents.committee_agent import committee_agent
from agents.risk_agent import risk_agent

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
def news_node(state):

    ticker = state["ticker"]

    report = news_agent(ticker)

    state["news_report"] = report

    return state

# node 5
def bull_node(state):

    result = bull_agent(state)

    return {
        "bull_case": result["bull_case"]
    }


# node 6
def bear_node(state):

    result = bear_agent(state)

    return {
        "bear_case": result["bear_case"]
    }


# node 7
def committee_node(state):

    return committee_agent(state)

#node 8
def risk_node(state):

    result = risk_agent(state)

    return {
        "risk_report": result["risk_report"]
    }

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
    "news",
    news_node
)

graph_builder.add_node(
    "bull",
    bull_node
)

graph_builder.add_node(
    "bear",
    bear_node
)

graph_builder.add_node(
    "committee",
    committee_node
)

graph_builder.add_node(
    "risk",
    risk_node
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
    "news"
)

graph_builder.add_edge(
    "news",
    "bull"
)

graph_builder.add_edge(
    "news",
    "bear"
)

graph_builder.add_edge(
    "news",
    "risk"
)

graph_builder.add_edge(
    "bull",
    "committee"
)

graph_builder.add_edge(
    "bear",
    "committee"
)

graph_builder.add_edge(
    "risk",
    "committee"
)

graph_builder.add_edge(
    "committee",
    END
)

#compile graph
graph = graph_builder.compile()
