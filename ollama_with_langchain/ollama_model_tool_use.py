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
    """

    return True

@tool
def addition(numbers: List[int]) -> int:
    """Add a list of numbers together.
    
    Args:
        numbers (List[int]): A list of integers to add.
    """

    return sum(numbers)

@tool
def subtraction(a: int, b: int) -> int:
    """Subtract two numbers.
    
    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.
    """

    return a - b

@tool
def multiplication(a: int, b: int) -> int:
    """Multiply two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    """

    return a * b

@tool
def division(a: int, b: int) -> float:
    """Divide two numbers.
    
    Args:
        a (int): The numerator.
        b (int): The denominator.
    """

    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


llm = ChatOllama(
    model="llama3.2",
    validate_model_on_init=True,
    temperature=0,
).bind_tools([validate_user, addition, subtraction, multiplication, division])

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
    "Could you add the numbers 5, 10, and 15?"
)

print(result)

if isinstance(result, AIMessage) and result.tool_calls:
    print(result.tool_calls)


