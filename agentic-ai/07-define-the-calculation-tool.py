def perform_calculation(expression: str) -> str:
    print(f"DEBUG: Calling perform_calculation for '{expression}'...")
  
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."
      
    except Exception as e:
        return f"Could not perform calculation for '{expression}': {e}"
