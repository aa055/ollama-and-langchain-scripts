from typing import List

from langchain.messages import AIMessage
from langchain.tools import tool
from langchain_ollama import ChatOllama

## https://docs.langchain.com/oss/python/langchain/tools#customize-tool-properties

@tool
def validate_user(user_id: int, addresses: List[str]) -> bool:
    """Validate user using historical addresses.
    
    Args:
        user_id (int): the user ID.
        addresses (List[str]): Previous addresses as a list of strings.

    Returns:
        bool: True if the user is validated, False otherwise.
    """

    return True

@tool
def addition(numbers: List[int]) -> int:
    """Add a list of numbers together.
    
    Args:
        numbers (List[int]): A list of integers to add.

    Returns:
        int: The sum of the numbers.
    """

    return sum(numbers)

@tool
def subtraction(a: int, b: int) -> int:
    """Subtract two numbers.
    
    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.
    
    Returns:
        int: The result of the subtraction.
    """
    
    return a - b

@tool
def multiplication(a: int, b: int) -> int:
    """Multiply two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of the two numbers.
    """

    return a * b

@tool
def division(a: int, b: int) -> float:
    """Divide two numbers.
    
    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division.
    """

    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


llm = ChatOllama(
    model="qwen3:4b",
    validate_model_on_init=True,
    temperature=0.7,
    # reasoning=True
).bind_tools([validate_user, addition, subtraction, multiplication, division])

# Create a tool executor mapping
tools_map = {
    "validate_user": validate_user,
    "addition": addition,
    "subtraction": subtraction,
    "multiplication": multiplication,
    "division": division
}


from langchain_core.messages import HumanMessage, ToolMessage

messages = [
    HumanMessage(content="Could you add the numbers 5, 10, and 15? Then subtract 8 from the result, and multiply that by 2.")
]

# Agent loop
max_iterations = 10
for i in range(max_iterations):
    result = llm.invoke(messages)

    # print(f"\n--- Result {i} ---")
    # print(f"Result: {result}")

    messages.append(result)
    
    print(f"\n--- Iteration {i+1} ---")
    print(f"Response: {result.content}")
    
    # Check if there are tool calls
    if result.tool_calls:
        print(f"Tool calls: {result.tool_calls}")
        
        # Execute each tool
        for tool_call in result.tool_calls:
            tool_name = tool_call['name']
            tool_args = tool_call['args']
            
            # Execute the tool
            tool_result = tools_map[tool_name].invoke(tool_args)
            print(f"Tool {tool_name} result: {tool_result}")
            
            # Add tool result to messages
            messages.append(
                ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call['id']
                )
            )
    else:
        # No more tool calls, we're done
        print("\n--- Final Answer ---")
        print(result.content)
        break