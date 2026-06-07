from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
from src.nodes.fetch_news import fetch_news_node
from src.nodes.summarize import summarize_node
from src.nodes.format import format_node
from src.nodes.send_telegram import send_telegram_node


class GraphInput(BaseModel):
    trigger: str = Field(default="daily", description="Trigger for the agent")


class GraphOutput(BaseModel):
    status: str = Field(description="Execution status")


class AgentState(BaseModel):
    articles: list[dict] = Field(default_factory=list)
    summaries: list[dict] = Field(default_factory=list)
    message: str = ""


builder = StateGraph(AgentState, input_schema=GraphInput, output_schema=GraphOutput)
builder.add_node("fetch_news", fetch_news_node)
builder.add_node("summarize", summarize_node)
builder.add_node("format", format_node)
builder.add_node("send_telegram", send_telegram_node)
builder.add_edge(START, "fetch_news")
builder.add_edge("fetch_news", "summarize")
builder.add_edge("summarize", "format")
builder.add_edge("format", "send_telegram")
builder.add_edge("send_telegram", END)

graph = builder.compile()
