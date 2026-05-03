import json
from shared import OllamaAgent, section

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

def print_messages(messages):
    """Helper to show the conversation history with roles."""
    print(section("Conversation History"))
    for msg in messages:
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        tool_calls = msg.get("tool_calls", None)
        
        print(f"[{role.upper()}]")
        if content:
            print(f"  {content}")
        if tool_calls:
            for call in tool_calls:
                # Accessing tool call info from the object or dict
                name = call.function.name if hasattr(call, 'function') else call['function']['name']
                args = call.function.arguments if hasattr(call, 'function') else call['function']['arguments']
                print(f"  * Tool Call: {name}({args})")
    print("=" * 30)

def main():
    agent = OllamaAgent()
    tools = [add, multiply]
    tool_map = {"add": add, "multiply": multiply}
    
    messages = []
    
    print(section("Math Agent with Explicit Roles"))
    print("Ask math questions (e.g., 'What is 5 + 3 and then multiply by 2?').")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nUser > ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
            
        messages.append({"role": "user", "content": user_input})
        
        while True:
            response = agent.chat(messages, tools=tools)
            
            # The response message has role 'assistant' and potentially 'tool_calls'
            assistant_msg = response.message
            messages.append(assistant_msg)
            
            if not assistant_msg.tool_calls:
                break
                
            for call in assistant_msg.tool_calls:
                result = tool_map[call.function.name](**call.function.arguments)
                
                # We add the result with role 'tool'
                messages.append({
                    "role": "tool",
                    "content": str(result),
                    # Native Ollama tool calling often requires the name or ID
                })
        
        print_messages(messages)
        print(f"\nFinal Agent Answer: {messages[-1]['content']}")

if __name__ == "__main__":
    main()
