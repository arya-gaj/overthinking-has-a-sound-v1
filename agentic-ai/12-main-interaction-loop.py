async def main():
    print("Welcome to the simple Agentic AI Demo!")
    print("Type 'exit' to quit.")
    print("Try queries like:")
    print("- What's the weather like in London?")
    print("- Send an email to alice@example.com about project update saying 'Meeting is tomorrow.'")
    print("- Calculate 55 * 12.")

    while True:
        user_input = input("\nYou: ")
      
        if user_input.lower() == 'exit':
            print("Exiting demo. Goodbye!")
            break

        agent_response = await run_agent(user_input)
        print(agent_response)
