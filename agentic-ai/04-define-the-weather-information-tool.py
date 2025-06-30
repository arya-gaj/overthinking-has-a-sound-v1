def get_current_weather(location: str) -> str:
    print(f"DEBUG: Calling get_current_weather for {location}...")
    mock_weather_data = {
        "New York": "Cloudy, 15°C with light rain.",
        "London": "Sunny, 20°C with gentle breeze.",
        "Tokyo": "Partly cloudy, 25°C and humid.",
        "Hyderabad": "Hot and sunny, 35°C."
    }
    return mock_weather_data.get(location, f"Weather data not available for {location}.")
