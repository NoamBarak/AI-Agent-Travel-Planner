"""
Interactive Conversational Trip Planner
A live chat interface for planning trips with memory and context awareness.
Uses the Anthropic Python SDK.
"""

import asyncio
import os
import sys
from anthropic import Anthropic
from dotenv import load_dotenv

# Configure UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables from .env file
load_dotenv()


class InteractiveTripPlanner:
    """
    Interactive trip planning agent that you can chat with.
    Maintains conversation memory throughout the session.
    """

    def __init__(self):
        """Initialize the interactive trip planner."""
        self.client = Anthropic()
        self.system_prompt = """You are an expert travel planning assistant who helps people plan amazing trips.

Your personality:
- Friendly, enthusiastic, and knowledgeable
- Ask clarifying questions to understand preferences
- Share insider tips and local recommendations
- Remember everything discussed in the conversation
- Build detailed plans based on accumulated information

Your approach:
1. Listen carefully to the traveler's needs and preferences
2. Ask follow-up questions to gather important details (budget, dates, interests, etc.)
3. Provide specific, actionable recommendations
4. Reference previous parts of the conversation naturally
5. Help make decisions when they're unsure
6. Be encouraging and excited about their trip!

Remember: You have conversation memory - always build on what you've learned about their preferences, constraints, and interests!
"""
        self.conversation_history = []
        self.message_count = 0

    async def chat(self, user_message: str) -> str:
        """Send a message and get the agent's response."""
        self.message_count += 1

        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        print(f"\n{'-'*70}")
        print(f"Assistant: ", end="", flush=True)

        # Get response from Claude
        response = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2048,
            system=self.system_prompt,
            messages=self.conversation_history
        )

        response_text = response.content[0].text

        # Add assistant response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response_text
        })

        print(response_text)
        return response_text

    async def start_conversation(self):
        """Start an interactive conversation loop."""
        print("\n" + "="*70)
        print(" INTERACTIVE TRIP PLANNER")
        print("="*70)
        print("\nWelcome! I'm your AI travel planning assistant.")
        print("I'll remember everything you tell me during our conversation.")
        print("\nCommands:")
        print("  - Type your messages to chat about your trip")
        print("  - Type 'reset' to start a new conversation")
        print("  - Type 'quit' or 'exit' to end the session")
        print("="*70)

        # Initial greeting
        await self.chat(
            "Hello! I see you're interested in planning a trip. "
            "Tell me about what you have in mind - where are you thinking of going, "
            "and what kind of experience are you looking for?"
        )

        while True:
            try:
                # Get user input
                print(f"\n{'-'*70}")
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                # Handle special commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\n" + "="*70)
                    print("Thanks for chatting! Have an amazing trip!")
                    print("="*70)
                    break

                if user_input.lower() == 'reset':
                    print("\n" + "="*70)
                    print("Starting a new conversation...")
                    print("="*70)
                    self.__init__()  # Reset the client
                    await self.chat(
                        "Hello! Let's start fresh. What trip would you like to plan?"
                    )
                    continue

                if user_input.lower() == 'help':
                    print("\n" + "="*70)
                    print("HELP")
                    print("="*70)
                    print("Just chat naturally about your trip! I'll remember everything.")
                    print("\nTips for better trip planning:")
                    print("  - Tell me about your interests and preferences")
                    print("  - Share your budget range and travel dates")
                    print("  - Mention any must-see destinations or activities")
                    print("  - Ask follow-up questions anytime")
                    print("  - I can help with itineraries, activities, restaurants, logistics")
                    print("="*70)
                    continue

                # Send message to the agent
                await self.chat(user_input)

            except KeyboardInterrupt:
                print("\n\n" + "="*70)
                print("Session interrupted. Have a great trip!")
                print("="*70)
                break
            except EOFError:
                print("\n\n" + "="*70)
                print("Session ended. Happy travels!")
                print("="*70)
                break


async def demo_mode():
    """
    Run a quick demo conversation to show how the system works.
    """
    print("\n" + "="*70)
    print(" DEMO MODE - Sample Conversation")
    print("="*70)
    print("Watch how the agent maintains context throughout the conversation!")
    print("="*70)

    planner = InteractiveTripPlanner()

    demo_messages = [
        "I'm thinking of visiting Southeast Asia for the first time.",
        "I have about 3 weeks and love outdoor activities and good food. My budget is around $3000 total.",
        "That sounds great! I'm most interested in Thailand and Vietnam. Which cities do you recommend?",
        "Perfect! How should I split my time between Thailand and Vietnam?",
        "Can you suggest a rough itinerary with the highlights you mentioned?",
    ]

    for i, msg in enumerate(demo_messages, 1):
        print(f"\n{'-'*70}")
        print(f"Demo Message {i}: {msg}")
        await planner.chat(msg)
        await asyncio.sleep(2)  # Brief pause for readability

    print("\n\n" + "="*70)
    print("Demo complete! Notice how the agent:")
    print("  ✓ Remembered: 3 weeks, $3000 budget, outdoor + food interests")
    print("  ✓ Built recommendations based on accumulated preferences")
    print("  ✓ Created cohesive itinerary from multiple conversation turns")
    print("="*70)


async def main():
    """
    Main entry point - choose between interactive or demo mode.
    """
    import sys

    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\nWARNING: ANTHROPIC_API_KEY environment variable not set!")
        print("\nPlease set your Anthropic API key:")
        print("\nOn Windows:")
        print("  set ANTHROPIC_API_KEY=your-key-here")
        print("\nOn Linux/Mac:")
        print("  export ANTHROPIC_API_KEY=your-key-here")
        print("\nGet your API key from: https://console.anthropic.com/")
        return

    if len(sys.argv) > 1 and sys.argv[1] == '--demo':
        await demo_mode()
    else:
        planner = InteractiveTripPlanner()
        await planner.start_conversation()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("\nMake sure you have:")
        print("1. Set ANTHROPIC_API_KEY environment variable")
        print("2. Installed anthropic package: pip install anthropic")
        import traceback
        traceback.print_exc()
