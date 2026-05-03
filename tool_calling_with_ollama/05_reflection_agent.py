from shared import OllamaAgent, section

def main():
    # We'll use the model configured in shared.py (currently glm-5.1:cloud)
    agent = OllamaAgent()
    
    topic = "Write a short Python function to calculate the factorial of a number."
    
    # --- Step 1: Generation ---
    print(section("Step 1: Initial Generation"))
    initial_prompt = f"Task: {topic}\nProvide a simple implementation."
    
    initial_draft = agent.chat([{"role": "user", "content": initial_prompt}])
    print(initial_draft.message.content)
    
    # --- Step 2: Reflection (Self-Critique) ---
    print(section("Step 2: Reflection (Self-Critique)"))
    reflection_prompt = (
        f"Review the following code and identify any potential issues, "
        f"edge cases (like negative numbers or zero), or style improvements:\n\n"
        f"{initial_draft.message.content}"
    )
    
    critique = agent.chat([{"role": "user", "content": reflection_prompt}])
    print(critique.message.content)
    
    # --- Step 3: Refinement ---
    print(section("Step 3: Refinement"))
    refinement_prompt = (
        f"Based on the following critique, provide a final, improved version of the code.\n\n"
        f"Critique: {critique.message.content}\n\n"
        f"Original Code: {initial_draft.message.content}"
    )
    
    final_version = agent.chat([{"role": "user", "content": refinement_prompt}])
    print(final_version.message.content)

if __name__ == "__main__":
    main()
