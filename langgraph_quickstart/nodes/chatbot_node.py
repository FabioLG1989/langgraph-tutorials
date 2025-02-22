from states.state import State

class ChatbotNode:
    def __init__(self, llm, tools) -> None:
        if tools and len(tools) > 0:
            self.llm = llm.bind_tools(tools)
        else:
            self.llm = llm

    def __call__(self, state: State):
        return {"messages": [self.llm.invoke(state["messages"])]}

