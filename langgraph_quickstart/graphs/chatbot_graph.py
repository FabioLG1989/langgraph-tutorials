from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from states.state import State
from nodes.chatbot_node import ChatbotNode
from tools.tavily import tavily_tool
from routers.tools_router import tools_router

class ChatbotGraph:
    def __init__(self, llm):
        llm = llm
        tools = [tavily_tool]
        graph_builder = StateGraph(State)
        chatbot_node = ChatbotNode(llm, tools)
        tools_node = ToolNode(tools=[tavily_tool])
        
        graph_builder.add_node("chatbot", chatbot_node)
        graph_builder.add_node("tools", tools_node)

        graph_builder.add_conditional_edges("chatbot", tools_condition)

        graph_builder.add_edge("tools", "chatbot")
        graph_builder.add_edge(START, "chatbot")

        memory = MemorySaver()

        self.graph = graph_builder.compile(checkpointer=memory)

    def draw(self):
        return self.graph.get_graph().draw_ascii()
