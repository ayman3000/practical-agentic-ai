import json
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from shared import OllamaAgent, section

def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    data = {"London": "Cloudy", "Dubai": "Sunny", "New York": "Rainy"}
    return data.get(city, "Unknown")

def get_stock_price(symbol: str) -> str:
    """Get the current stock price for a company symbol."""
    data = {"AAPL": "$150", "GOOGL": "$2800", "TSLA": "$700"}
    return data.get(symbol.upper(), "Symbol not found")

style = Style.from_dict({
    "prompt": "ansicyan bold",
    "agent": "ansigreen bold",
    "tool": "ansiyellow italic",
})

def main():
    agent = OllamaAgent()
    tools = [get_weather, get_stock_price]
    tool_map = {"get_weather": get_weather, "get_stock_price": get_stock_price}
    
    session = PromptSession(style=style)
    messages = []
    
    print(section("Advanced Ollama Agent"))
    
    while True:
        
        user_input = session.prompt([("class:prompt", "User > ")])

            
        if user_input.lower() in ["exit", "quit"]:
            break
            
        messages.append({"role": "user", "content": user_input})
        
        while True:
            response = agent.chat(messages, tools=tools)
            messages.append(response.message)
            
            if not response.message.tool_calls:
                print(f"\nAgent: {response.message.content}")
                break
                
            for call in response.message.tool_calls:
                print(f"\n  [Thinking] Calling {call.function.name}...")
                
                func = tool_map.get(call.function.name)
                if func:
                    result = func(**call.function.arguments)
                    print(f"  [Tool Result] {result}")
                    
                    messages.append({
                        "role": "tool",
                        "content": str(result),
                    })

if __name__ == "__main__":
    main()
