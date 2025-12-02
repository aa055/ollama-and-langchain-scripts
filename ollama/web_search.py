import ollama
import os

# # First set the environment variable in your system or terminal --- for powershell use -> ($env:OLLAMA_API_KEY="your_api_key")

# Create a client with the API key
client = ollama.Client(
    headers={
        'Authorization': 'Bearer '+ os.environ.get('OLLAMA_API_KEY')
    }
)

response = client.web_search("What is Ollama?")

print(response)