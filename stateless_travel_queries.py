"""
Basic Trip Planning Agent using Anthropic SDK
Uses the Messages API for stateless interactions.
"""

import os
import sys
from anthropic import Anthropic
from dotenv import load_dotenv

# Configure UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables from .env file
load_dotenv()
def run_paris_travel_query(prompt: str, client: Anthropic):
    """
    Send a single trip planning query to Claude.
    Each call is stateless - Claude won't remember previous queries.

    Args:
        prompt (str): The trip planning query to send to Claude.
        client (Anthropic): The Anthropic client instance.
    """
    print(f"\n{'='*60}")
    print(f"Query: {prompt}")
    print(f"{'='*60}\n")

    system_prompt = (
        "You are a helpful travel planning assistant specializing in European destinations. "
        "Provide concise, practical travel advice. You provide detailed recommendations for "
        "sightseeing, dining, and local experiences in Paris. Provide concise and relevant information."
    )

    # Execute the query using Messages API with streaming
    response_text = ""
    with client.messages.stream(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            response_text += text

    print("\n")  # Newline after response
    return response_text


def main():
    """
    Demonstrates stateless trip planning queries for Paris.
    Each query is independent with no memory of previous interactions.
    """
    # Initialize the Anthropic client
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    print("="*60)
    print("Paris Trip Planning Agent - Stateless Query Demo")
    print("="*60)
    print("Using Messages API: Each interaction is independent")
    print()

    # Example 1: General trip planning
    run_paris_travel_query(
        "I'm planning a 5-day trip to Paris. What are the must-see attractions?",
        client
    )

    # Example 2: Specific activity recommendation
    # Note: This is a NEW query - Claude won't remember the 5-day trip mentioned above
    run_paris_travel_query(
        "What are the best museums to visit in Paris for art lovers?",
        client
    )

    # Example 3: Practical travel info
    run_paris_travel_query(
        "What's the best way to get from Charles de Gaulle Airport to central Paris?",
        client
    )

    # Example 4: Restaurant recommendations
    run_paris_travel_query(
        "Can you recommend 3 authentic French restaurants in Paris for a romantic dinner?",
        client
    )

    # Example 5: Day itinerary
    run_paris_travel_query(
        "Plan a perfect day in Paris starting at the Eiffel Tower. What should I do?",
        client
    )

    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60)
    print("\nNote: Each query was independent (stateless).")
    print("Claude didn't remember context between queries.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("\nMake sure you have:")
        print("1. Installed the SDK: pip install anthropic python-dotenv")
        print("2. Created a .env file with your API key:")
        print("   ANTHROPIC_API_KEY=your-api-key-here")
