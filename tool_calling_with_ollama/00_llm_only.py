from shared import OllamaAgent, section

def main():
    # Initialize the agent (uses the model from shared.py)
    agent = OllamaAgent()
    
    # Simple user request without any tools
    messages = [
        {"role": "user", "content": "Tell me a very short joke about AI."}
    ]
    
    print(section("User Request"))
    print(messages[0]["content"])
    
    # Call the LLM directly
    response = agent.chat(messages)
    
    print(section("Model Response"))
    print(response.message.content)

if __name__ == "__main__":
    main()
