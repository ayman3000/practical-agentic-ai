import json
from shared import OllamaAgent, section

def get_weather(city: str) -> str:
    """
    Get the current weather for a city.
    
    Args:
        city: The name of the city to get weather for.
    """
    # Dummy data
    weather_data = {
        "London": "15°C, Cloudy",
        "Dubai": "35°C, Sunny",
        "New York": "20°C, Rain"
    }
    return weather_data.get(city, "Weather unknown")

def main():
    agent = OllamaAgent()
    
    messages = [
        # {"role": "system", "content": "You are a helpful assistant., use the available tools to answer the user's question."},
        {"role": "user", "content": "What is the weather in alex?"}
    ]
    
    print(section("User Request"))
    print(messages[0]["content"])
    
    # Call agent with tools
    response = agent.chat(messages, tools=[get_weather])
    
    print(section("Model Response"))
    print(response)
    print("="*20)
    if response.message.tool_calls:
        for call in response.message.tool_calls:
            print(f"Tool Call: {call.function.name}")
            print(f"Arguments: {json.dumps(call.function.arguments, indent=2)}")
            
            # Execute the tool
            if call.function.name == "get_weather":
                result = get_weather(**call.function.arguments)
                print(f"Result: {result}")
    else:
        print(response.message.content)

if __name__ == "__main__":
    main()
