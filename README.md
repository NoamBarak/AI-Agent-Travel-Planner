# 🤖 AI-Powered Travel Planning Agents

> **Next-generation intelligent travel assistants powered by Claude AI** | Multi-turn conversational AI | Context-aware recommendations

## 🚀 Overview

Harness the power of **large language models (LLMs)** to revolutionize travel planning with intelligent, context-aware AI agents built on Anthropic's cutting-edge **Claude Sonnet 4.5** foundation model. This repository showcases both **stateless query processing** and **stateful conversational AI** patterns using the official Claude Agent SDK.

### ✨ Key Features

- 🧠 **Advanced Context Memory** - Multi-turn conversations with persistent state management
- ⚡ **Real-time Streaming** - Lightning-fast responses with streaming API integration
- 🎯 **Prompt Engineering** - Production-grade system prompts for domain expertise
- 🔄 **Stateless & Stateful Modes** - Flexible architecture for different use cases
- 🌍 **Intelligent Recommendations** - Personalized itineraries powered by Claude AI
- 💬 **Natural Language Understanding** - Human-like conversational interactions
- 🛠️ **SDK** - Built with Anthropic's official Python SDK

## 🏗️ Architecture

### Conversational AI Agent (`conversational_trip_planner.py`)
**Enterprise-grade stateful agent** with conversation memory and context awareness. Ideal for complex, multi-turn dialogues requiring persistent state.

**Technologies:**
- Multi-message conversation history tracking
- Async/await pattern for concurrent operations
- Dynamic prompt injection
- Context window optimization

### Stateless Query Engine (`stateless_travel_queries.py`)
**High-performance stateless processor** for independent, one-shot queries. Perfect for microservices architectures and serverless deployments.


## 🚦 Quick Start

### Prerequisites
```bash
pip install claude-agent-sdk python-dotenv
```

### Configuration
```bash
# Create .env file
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
```

### Run Examples
```bash
# Stateless queries (independent interactions)
python stateless_travel_queries.py

# Conversational agent (multi-turn with memory)
python conversational_trip_planner.py
```


