async def run_agent(user_query: str) -> str:
    prompt = f"""
You are an intelligent assistant that can use tools.
When I give you a query, decide which tool is most appropriate and respond in the following JSON-like format:
```json
{{
  "tool": "tool_name",
  "args": {{
    "arg1_name": "arg1_value",
    "arg2_name": "arg2_value"
  }}
}}
