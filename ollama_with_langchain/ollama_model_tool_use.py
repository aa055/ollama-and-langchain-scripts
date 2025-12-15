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
).bind_tools([addition, subtraction, multiplication, division])

# # Test user validation
# result = llm.invoke(
#     "Could you validate user 123? They previously lived at "
#     "123 Fake St in Boston MA and 234 Pretend Boulevard in "
#     "Houston TX."
# )
# print(result)
# print()

# Test arithmetic operations
result = llm.invoke(
    "Could you add the numbers 5, 10, and 15? "
)

print(result)

if isinstance(result, AIMessage) and result.tool_calls:
    print(result.tool_calls)

## Try out with multiple tool calls in a single response by asking to perform several math operations.

# result = llm.invoke(
#     "Could you add the numbers 5, 10, and 15? Then subtract 8 from the result, and multiply that by 2. "
# )
# # the result will not contain the final answer directly, but will have tool calls to perform each step
# # for that, we need to execute each tool call in sequence and feed the results back to the model 

## Try it out in a loop like in ollama_with_langchain/agent_loop.py
