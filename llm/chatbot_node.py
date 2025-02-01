
from langchain_ollama import ChatOllama
from tools.tools_node import tools
from state import State
from langgraph.graph.message import add_messages


llm_for_tools = ChatOllama(model="qwen2.5", base_url = "http://localhost:11434")
llm_with_tools = llm_for_tools.bind_tools(tools)


def chatbot(state: State):
    from langchain_core.messages import SystemMessage
    response = llm_with_tools.invoke(add_messages(SystemMessage("Você é um agente que deve fazer conforme o usuário pede. Use suas tools se necessário"),state["messages"]))
    return {"messages": [response]}
