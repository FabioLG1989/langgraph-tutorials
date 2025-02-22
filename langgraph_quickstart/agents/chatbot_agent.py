from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage
from graphs.chatbot_graph import ChatbotGraph

llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
config = {"configurable": {"thread_id": "1"}}
chatbot = ChatbotGraph(llm)

def stream_graph_updates(user_input: str):
    events = chatbot.graph.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        config,
        stream_mode="values",
    )

    for event in events:
        if isinstance(event["messages"][-1], AIMessage):
            print(event["messages"][-1].content)

def run_chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("User: ")
        if not user_input or user_input == "quit":
            print("Goodbye!")
            break

        stream_graph_updates(user_input)

def draw_chatbot():
    print(chatbot.draw())
