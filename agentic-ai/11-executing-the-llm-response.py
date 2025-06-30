try:
    if "```json" in llm_response and "```" in llm_response:
        json_start = llm_response.find("```json") + len("```json")
        json_end = llm_response.find("```", json_start)
        json_string = llm_response[json_start:json_end].strip()
        tool_call = json.loads(json_string)

        tool_name = tool_call.get("tool")
        tool_args = tool_call.get("args", {})

        if tool_name and tool_name in tools:
            print(f"Agent: Decided to use tool: {tool_name} with arguments: {tool_args}")
            tool_function = tools[tool_name]
            tool_result = tool_function(**tool_args)
            return f"Agent executed tool '{tool_name}'. Result: {tool_result}"
            
        else:
            return f"Agent: LLM suggested an unknown tool or no tool at all. LLM said: {llm_response}"
            
    else:
        return f"Agent: {llm_response.strip()}"

except json.JSONDecodeError as e:
    print(f"Agent: Could not parse LLM response as JSON tool call: {e}. Falling back to natural language.")
    return f"Agent: {llm_response.strip()}"

except Exception as e:
    print(f"Agent: An unexpected error occurred while processing tool call: {e}. LLM said: {llm_response}")
    return f"Agent: An internal error occurred. LLM said: {llm_response}"
