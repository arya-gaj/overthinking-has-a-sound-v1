async def call_llm(prompt: str) -> str:
    if API_KEY == "YOUR_API_KEY" or not API_KEY:
        print("Error: Please replace 'YOUR_API_KEY' with your actual API key.")
        return "API key not configured."

    model = genai.GenerativeModel('gemini-2.0-flash')

    try:
        chat_history = []
        chat_history.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })

        payload = {"contents": chat_history}

        api_url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"gemini-2.0-flash:generateContent?key={API_KEY}"
        )

        response = await model.generate_content_async(
            prompt,
            generation_config=genai.types.GenerationConfig(
                response_mime_type="text/plain"
            )
        )

        if (
            response.candidates
            and response.candidates[0].content
            and response.candidates[0].content.parts
        ):
            text = response.candidates[0].content.parts[0].text
            return text
        else:
            print("LLM response structure unexpected or content missing.")
            return "Could not get a valid response from the AI."

    except Exception as e:
        print(f"An error occurred during LLM call: {e}")
        return f"Error communicating with AI: {e}"
