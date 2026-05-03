import json
from shared import OllamaAgent, section

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

def main():
    agent = OllamaAgent()
    tools = [add, multiply]
    
    # Example 1: Addition
    messages = [{"role": "user", "content": "What is 15 + 27?"}]
    print(section("Example 1: Addition"))
    response = agent.chat(messages, tools=tools)
    
    if response.message.tool_calls:
        for call in response.message.tool_calls:
            print(f"Calling: {call.function.name}({call.function.arguments})")
            
    # Example 2: Multiplication
    messages = [{"role": "user", "content": "What is 12 times 8?"}]
    print(section("Example 2: Multiplication"))
    response = agent.chat(messages, tools=tools)
    
    if response.message.tool_calls:
        for call in response.message.tool_calls:
            print(f"Calling: {call.function.name}({call.function.arguments})")

if __name__ == "__main__":
    main()
