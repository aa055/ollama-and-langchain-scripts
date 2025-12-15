import os
from langchain_ollama import ChatOllama

llm = ChatOllama(
        model="llama3.2",
        temperature=0.7
    )

messages = [
    (
        "system", "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    (
        "human", "I love programming."
    ),
]


response = llm.invoke(messages)

print(response.content)