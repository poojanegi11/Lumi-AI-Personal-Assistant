def is_weather_question(message):
    weather_keywords = [
        "weather",
        "temperature",
        "forecast",
        "rain",
        "raining",
        "sunny",
        "cloudy",
        "cold",
        "hot"
    ]

    message = message.lower()

    for keyword in weather_keywords:
        if keyword in message:
            return True

    return False
