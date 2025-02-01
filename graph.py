from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import tools_condition
from typing import Union, Any, Literal
from pydantic import BaseModel
from langchain_core.messages import AnyMessage
from langgraph.graph import StateGraph
from state import State
from llm.chatbot_node import chatbot
from langgraph.prebuilt import ToolNode
from tools.tools_node import tools


memory = MemorySaver()

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)


tool_node = ToolNode(tools=tools)

graph_builder.add_node("tools",tool_node)


graph_builder.add_conditional_edges("chatbot", tools_condition)

graph_builder.add_edge("tools", "chatbot")


graph_builder.set_entry_point("chatbot")

graph_compiled = graph_builder.compile(checkpointer=memory)