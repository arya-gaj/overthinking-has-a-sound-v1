print(f"\nAgent: Processing query: '{user_query}'...")
    llm_response = await call_llm(prompt)
    print(f"Agent: LLM raw response: {llm_response}")
