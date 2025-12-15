from ollama import chat, web_fetch, web_search

available_tools = {'web_search': web_search, 'web_fetch': web_fetch}

messages = [{'role': 'user', 'content': "what is ollama's latest model?"}]

while True:
  response = chat(
    model='qwen3:4b',
    messages=messages,
    tools=[web_search, web_fetch],
    think=True
    )
  
  print('\n--- Response --- \n', response, '\n--- End Response ---\n')

  if response.message.thinking:
    print('Thinking: ', response.message.thinking, '\n')

  if response.message.content:
    print('Content: ', response.message.content, '\n')
  
  messages.append(response.message)
  
  if response.message.tool_calls:
    print('Tool calls: ', response.message.tool_calls, '\n')
    
    for tool_call in response.message.tool_calls:
      function_to_call = available_tools.get(tool_call.function.name)
      
      if function_to_call:
        args = tool_call.function.arguments
        result = function_to_call(**args)
        print('Result: ', str(result)[:200]+'...', '\n')
        # Result is truncated for limited context lengths
        messages.append({'role': 'tool', 'content': str(result)[:2000 * 4], 'tool_name': tool_call.function.name})
      else:
        messages.append({'role': 'tool', 'content': f'Tool {tool_call.function.name} not found', 'tool_name': tool_call.function.name})
  
  else:
    break