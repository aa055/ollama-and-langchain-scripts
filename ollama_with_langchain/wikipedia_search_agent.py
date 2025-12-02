from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


# Configure the wrapper 
api_wrapper = WikipediaAPIWrapper(
    top_k_results=1, # number of top results to fetch
    doc_content_chars_max=1000 # max characters to fetch from each document
)

# Initialize the Wikipedia query tool
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)


llm = ChatOllama(model="qwen3:4b")

agent = create_agent(
    model=llm,
    tools=[wiki_tool],
    system_prompt="You are a helpful assistant with access to Wikipedia search. Use the search tool to find information on Wikipedia.",
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "Who was Albert Einstein?"}]}
)

print("Complete Response: ", response, "\n")

print("Final Response:", response["messages"][-1].content)



