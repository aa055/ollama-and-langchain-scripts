
import os
from ollama import Client, web_fetch, web_search

# Get API key with a fallback or raise an error if not set
# # First set the environment variable in your system or terminal --- for powershell use -> ($env:OLLAMA_API_KEY="your_api_key")

api_key = os.environ.get('OLLAMA_API_KEY')
if not api_key:
    raise ValueError("OLLAMA_API_KEY environment variable is not set")


client = Client(
    # host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
)

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

response = client.chat(
    'gpt-oss:20b',
    messages=messages,
    tools=[web_search, web_fetch],
    think=True
)
print(response)

# # Streaming example
# for part in client.chat('gpt-oss:20b', messages=messages, tools=[web_search, web_fetch], stream=True):
#   print(part['message']['content'], end='', flush=True)