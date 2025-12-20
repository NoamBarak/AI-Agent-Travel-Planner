# Paris Trip Planning Agent

A basic Python agent using the Claude Agent SDK to demonstrate stateless trip planning queries.

## Overview

This agent uses the `query()` approach for one-off, stateless interactions. Each query is independent with no memory of previous conversations - perfect for simple question-and-answer scenarios.

## Features

- **Stateless interactions**: Each query is independent
- **Travel-focused examples**: 5 different Paris trip planning scenarios
- **Simple setup**: Uses basic query() approach without tools or memory
- **Clean output**: Formatted responses for easy reading

## Prerequisites

1. **Python 3.8+**
2. **Claude Agent SDK**:
   ```bash
   pip install claude-agent-sdk
   ```

3. **Claude Code CLI**:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

4. **Anthropic API Key**: Set up your API credentials for Claude Code CLI

## Installation

```bash
# Clone or download this project
cd ai_agent

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python trip_planner.py
```

## How It Works

The agent demonstrates 5 different trip planning queries:

1. **General Planning**: Must-see attractions for a 5-day Paris trip
2. **Museums**: Best museums for art lovers
3. **Transportation**: Getting from CDG Airport to central Paris
4. **Dining**: Authentic French restaurant recommendations
5. **Itinerary**: Planning a perfect day starting at the Eiffel Tower

### Key Code Structure

```python
from claude_agent_sdk import query, ClaudeAgentOptions

# Configure the agent
options = ClaudeAgentOptions(
    system_prompt="You are a helpful travel planning assistant...",
    allowed_tools=[]  # No tools needed for basic queries
)

# Make a stateless query
async for message in query(prompt="Plan my Paris trip", options=options):
    # Process the response
    ...
```

## Stateless vs Stateful

### This Example (Stateless - `query()`)
- ✅ Simple one-off questions
- ✅ Independent interactions
- ✅ No context needed between queries
- ❌ Cannot have follow-up conversations
- ❌ No memory of previous exchanges

### Future Enhancement (Stateful - `ClaudeSDKClient`)
When you need memory and conversation context:
- ✅ Multi-turn conversations
- ✅ Follow-up questions
- ✅ Context awareness
- ✅ Interactive chat sessions

## Next Steps

To add memory and tools in future iterations, you would:
1. Switch from `query()` to `ClaudeSDKClient`
2. Add MCP tools for data access
3. Enable conversation history
4. Implement custom tools for booking, weather, etc.

## Example Output

```
==============================================================
Query: I'm planning a 5-day trip to Paris. What are the must-see attractions?
==============================================================

For a 5-day trip to Paris, here are the essential attractions:

1. Eiffel Tower - Visit at sunset for breathtaking views
2. Louvre Museum - Home to the Mona Lisa and thousands of masterpieces
3. Notre-Dame Cathedral - Marvel at Gothic architecture
4. Champs-Élysées and Arc de Triomphe - Iconic Parisian boulevard
5. Sacré-Cœur and Montmartre - Artistic hilltop neighborhood
...
```

## Learn More

- [Claude Agent SDK Python Docs](https://platform.claude.com/docs/en/api/agent-sdk/python)
- [Claude Code Documentation](https://code.claude.com/docs)
