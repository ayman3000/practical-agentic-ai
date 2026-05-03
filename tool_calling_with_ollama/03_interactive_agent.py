import json
from shared import OllamaAgent, section

def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    data = {"London": "Cloudy", "Dubai": "Sunny", "New York": "Rainy"}
    return data.get(city, "Unknown")

def get_time(city: str) -> str:
    """Get the current time in a city."""
    data = {"London": "12:00 PM", "Dubai": "3:00 PM", "New York": "7:00 AM"}
    return data.get(city, "Unknown")

def main():
    agent = OllamaAgent()
    tools = [get_weather, get_time]
    tool_map = {"get_weather": get_weather, "get_time": get_time}
    
    messages = []
    
    print("Agent started. Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
            
        messages.append({"role": "user", "content": user_input})
        
        # Loop for tool execution
        while True:
            response = agent.chat(messages, tools=tools)
            
            # Add assistant message to history
            messages.append(response.message)
            
            if not response.message.tool_calls:
                print(f"Agent: {response.message.content}")
                break
                
            for call in response.message.tool_calls:
                print(f"[Tool Call] {call.function.name}({call.function.arguments})")
                
                func = tool_map.get(call.function.name)
                if func:
                    result = func(**call.function.arguments)
                    print(f"[Tool Result] {result}")
                    
                    # Add tool result to history
                    messages.append({
                        "role": "tool",
                        "content": str(result),
                        "name": call.function.name
                    })
                else:
                    print(f"[Error] Tool {call.function.name} not found.")

if __name__ == "__main__":
    main()
