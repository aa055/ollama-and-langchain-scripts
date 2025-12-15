from langchain.agents import create_agent
from langchain_ollama import ChatOllama


llm = ChatOllama(model="llama3.2")

agent = create_agent(
    model=llm,
    system_prompt="You are a helpful business and economics assistant",
)

# Run the agent
response = agent.invoke(
    {"messages": 
        [
            {"role": "user", "content": "what is the meaning of inflation and deflation. Explain with examples."}
        ]
    }
)

print(response)
# print(response["messages"][-1].content)

print()
# Filter for AIMessage type
from langchain_core.messages import AIMessage
ai_messages = [msg for msg in response["messages"] if isinstance(msg, AIMessage)]
print(ai_messages[-1].content)