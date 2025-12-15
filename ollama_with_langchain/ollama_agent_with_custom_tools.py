from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.tools import tool


def addition(numbers: list[int]) -> int:
    """Add a list of numbers together.
    
    Args:
        numbers (list[int]): A list of integers to add.
    """

    return sum(numbers)

def subtraction(a: int, b: int) -> int:
    """Subtract two numbers.
    
    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.
    """

    return a - b

def multiplication(a: int, b: int) -> int:
    """Multiply two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    """

    return a * b

def division(a: int, b: int) -> float:
    """Divide two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    """

    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b



llm = ChatOllama(model="qwen3:4b")

agent = create_agent(
    model=llm,
    tools=[addition, subtraction, multiplication, division],
    system_prompt="You are a helpful mathematics assistant, that can perform basic arithmetic functions using tools",
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "Could you add the numbers 5, 10, and 15? and then multiply the result by 2 and then divide by 5."}]}
)

print("Response object:", response)
print("\nFinal Response: ", response["messages"][-1].content)
print()


from langchain_core.messages import AIMessage
ai_messages = [msg for msg in response["messages"] if isinstance(msg, AIMessage)]
for msg in ai_messages:
    print("AI message:", msg.content)
    # Print tool calls if they exist
    if hasattr(msg, 'tool_calls') and msg.tool_calls:
        for tool_call in msg.tool_calls:
            print(f"  Tool Call: {tool_call['name']} with args: {tool_call['args']}")

from langchain_core.messages import ToolMessage
tool_messages = [msg for msg in response["messages"] if isinstance(msg, ToolMessage)]
for msg in tool_messages:
    print("Tool Message: ", msg)

