import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()


def extract_city(question):
    """
    Extract city name from common weather questions.
    """

    question = question.strip()

    patterns = [
        r"weather\s+(?:of|in|at)\s+(.+)",
        r"temperature\s+(?:of|in|at)\s+(.+)",
        r"(?:what(?:'s| is)\s+)?the\s+weather\s+(?:of|in|at)\s+(.+)",
        r"(?:what(?:'s| is)\s+)?the\s+temperature\s+(?:of|in|at)\s+(.+)",
        r"(.+?)\s+weather",
    ]

    for pattern in patterns:
        match = re.search(pattern, question, re.IGNORECASE)

        if match:
            city = match.group(1).strip()

            # Remove common extra words
            city = re.sub(
                r"\b(today|tomorrow|now|please)\b",
                "",
                city,
                flags=re.IGNORECASE
            ).strip()

            if city:
                return city

    return question


def get_weather(question):

    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return "❌ Weather API key is missing."


    city = extract_city(question)


    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }


    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()


        if response.status_code != 200:

            return (
                f"❌ I couldn't find weather information "
                f"for **{city}**.\n\n"
                f"Please check the city name."
            )


        temperature = data["main"]["temp"]

        feels_like = data["main"]["feels_like"]

        humidity = data["main"]["humidity"]

        description = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        country = data["sys"]["country"]


        return f"""
🌦️ **Weather in {city}, {country}**

🌡️ Temperature: **{temperature}°C**

🤗 Feels like: **{feels_like}°C**

☁️ Condition: **{description.title()}**

💧 Humidity: **{humidity}%**

💨 Wind speed: **{wind_speed} m/s**
"""


    except requests.exceptions.RequestException:

        return (
            "❌ I couldn't connect to the weather service. "
            "Please check your internet connection."
        )


    except Exception as e:

        return f"❌ Weather error: {e}"