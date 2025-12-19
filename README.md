# Ollama and LangChain Scripts

A comprehensive collection of Python scripts demonstrating AI agent development using **Ollama** (local LLM models) and **LangChain** framework. This repository includes examples of building agents with tool use, web search, weather information, and Wikipedia integration.

## Table of Contents

- [Project Structure](#project-structure)
- [Requirements & Setup](#requirements--setup)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Folder Overview](#folder-overview)
- [Getting Started](#getting-started)

## Project Structure

```
ollama-and-langchain-scripts/
├── ollama/                          # Direct Ollama client scripts
│   ├── client.py
│   ├── custom_weather_function_tool.py
│   ├── search_agent.py
│   └── web_search.py
├── ollama_with_langchain/           # LangChain-based agent scripts
│   ├── ollama_model.py
│   ├── ollama_agent.py
│   ├── ollama_agent_with_custom_tools.py
│   ├── ollama_model_tool_use.py
│   ├── weather_agent.py
│   ├── web_search_agent.py
│   └── wikipedia_search_agent.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements & Setup

### System Requirements
- Python 3.9+
- Ollama installed and running locally ([Download Ollama](https://ollama.ai))
- Internet connection (for web search and Wikipedia features)

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Dependencies

The project uses the following key libraries:

```
langchain==1.1.0               # LangChain framework
langchain-anthropic==1.2.0     # LangChain Anthropic integration
langchain-community==0.4.1     # LangChain community tools
langchain-ollama==1.0.0        # LangChain Ollama integration
ollama==0.6.1                  # Ollama Python client
wikipedia==1.4.0               # Wikipedia API wrapper
ddgs==9.9.2                    # DuckDuckGo search
```

## Configuration

### 1. Download Ollama Models

Before running the scripts, download the required LLM models:

```bash
# Download Llama 3.2 model (used in most examples)
ollama pull llama3.2

# Download Qwen 3 model (used in some examples)
ollama pull qwen3:4b
```

**Available models in scripts:**
- `llama3.2` - General purpose model
- `qwen3:4b` - Lightweight model for search/Wikipedia
- `gpt-oss:20b` - Advanced model with extended capabilities

### 2. Set Ollama API Key (Optional)

For scripts that use web search features, set your Ollama API key:

```bash
# Linux/macOS
export OLLAMA_API_KEY="your_api_key_here"

# Windows PowerShell
$env:OLLAMA_API_KEY="your_api_key_here"

# Windows Command Prompt
set OLLAMA_API_KEY=your_api_key_here
```

Add to `.env` file for persistent configuration (already in `.gitignore`):
```
OLLAMA_API_KEY=your_api_key_here
```

### 3. Start Ollama Server

Ensure Ollama is running locally:

```bash
ollama serve
```

## Folder Overview

### `ollama/` - Direct Ollama Client Scripts

These scripts use the **Ollama Python client** directly, without LangChain middleware.

| Script | Purpose |
|--------|---------|
| [client.py](ollama/client.py) | Basic chat with web search and fetch tools |
| [web_search.py](ollama/web_search.py) | Simple web search queries |
| [custom_weather_function_tool.py](ollama/custom_weather_function_tool.py) | Custom weather function tool with temperature lookup |
| [search_agent.py](ollama/search_agent.py) | Agentic loop with web search/fetch tools and thinking |

### `ollama_with_langchain/` - LangChain Agent Scripts

These scripts leverage **LangChain framework** for building structured AI agents with tools.

| Script | Purpose |
|--------|---------|
| [ollama_model.py](ollama_with_langchain/ollama_model.py) | Basic model invocation (English to French translation) |
| [ollama_agent.py](ollama_with_langchain/ollama_agent.py) | Simple agent for business/economics Q&A |
| [ollama_agent_with_custom_tools.py](ollama_with_langchain/ollama_agent_with_custom_tools.py) | Agent with arithmetic tools (add, subtract, multiply, divide) |
| [ollama_model_tool_use.py](ollama_with_langchain/ollama_model_tool_use.py) | Binding tools to models with tool calling |
| [weather_agent.py](ollama_with_langchain/weather_agent.py) | Agent with custom weather function |
| [web_search_agent.py](ollama_with_langchain/web_search_agent.py) | Agent with DuckDuckGo search integration |
| [wikipedia_search_agent.py](ollama_with_langchain/wikipedia_search_agent.py) | Agent with Wikipedia search capability |

## Getting Started

### 1. Clone/Setup
```bash
git clone <repository-url>
cd ollama-and-langchain-scripts
pip install -r requirements.txt
```

### 2. Download Models
```bash
ollama pull llama3.2
ollama pull qwen3:4b
```

### 3. Start Ollama
```bash
ollama serve
```

### 4. Run a Script
```bash
# Basic model example
python ollama_with_langchain/ollama_model.py

# Direct Ollama client
python ollama/search_agent.py
```

## Notes

- **Model Selection**: Larger models like `llama3.2` provide better responses but require more resources but for tool use `qwen` and `gpt-oss` performs better
- **API Key**: Only required for advanced web search features; basic local chat works without it
- **Temperature**: Controls randomness (0 = deterministic, 1 = creative)
- **Tool Binding**: LangChain agents automatically handle tool invocation and result processing

## Resources

- [Ollama Documentation](https://ollama.ai)
- [LangChain Documentation](https://python.langchain.com)
- [Available Ollama Models](https://ollama.ai/library)

---
