from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize the search tool
ddg_search_tool = DuckDuckGoSearchRun()


llm = ChatOllama(model="qwen3:4b")

agent = create_agent(
    model=llm,
    tools=[ddg_search_tool],
    system_prompt="You are a helpful assistant with access to web search. Use the search tool to find current information.",
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in Dubai today?"}]}
)

print("Complete Response: ", response, "\n")

print("Final Response:", response["messages"][-1].content)



