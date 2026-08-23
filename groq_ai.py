from groq import Groq
from dotenv import load_dotenv
import os

from study_mode import study_prompt
from quiz_mode import quiz_prompt
from weather_mode import is_weather_question
from weather_api import get_weather


# ==================================================
# LOAD ENVIRONMENT VARIABLES
# ==================================================

load_dotenv()


# ==================================================
# GROQ CLIENT
# ==================================================

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY was not found. "
        "Please check your .env file."
    )

client = Groq(
    api_key=api_key
)


# ==================================================
# LUMI AI
# ==================================================

def ask_lumi(messages, username, mood):

    # Get latest user message
    latest_message = messages[-1]["content"]

    latest_lower = latest_message.lower()


    # ==================================================
    # WEATHER MODE
    # ==================================================

    if is_weather_question(latest_lower):

        # For now, ask the user for a city if needed.
        # Example: "weather in Dehradun"

        city = latest_message

        try:

            weather = get_weather(city)

            return weather

        except Exception as e:

            return (
                "🌦️ I couldn't get the weather right now.\n\n"
                f"Error: {e}"
            )


    # ==================================================
    # STUDY KEYWORDS
    # ==================================================

    teacher_keywords = [

        "teach",
        "study",
        "explain",
        "what is",

        "python",
        "java",
        "c",
        "c++",
        "html",
        "css",
        "javascript",
        "sql",

        "dbms",
        "os",
        "coa",
        "flat",
        "oops",
        "computer network",
        "cn",

        "algorithm",
        "dsa",
        "array",
        "linked list",
        "stack",
        "queue",
        "tree",
        "binary tree",
        "graph",
        "recursion",

        "unit"
    ]


    # ==================================================
    # QUIZ KEYWORDS
    # ==================================================

    quiz_keywords = [

        "quiz",
        "mcq",
        "test",
        "exam"
    ]


    # ==================================================
    # DETECT MODES
    # ==================================================

    teacher_mode = False
    quiz_mode = False


    for keyword in teacher_keywords:

        if keyword in latest_lower:

            teacher_mode = True
            break


    for keyword in quiz_keywords:

        if keyword in latest_lower:

            quiz_mode = True
            break


    # ==================================================
    # CHOOSE SYSTEM PROMPT
    # ==================================================

    if quiz_mode:

        system_message = {

            "role": "system",

            "content": quiz_prompt(
                latest_message
            )
        }


    elif teacher_mode:

        system_message = {

            "role": "system",

            "content": study_prompt(
                latest_message
            )
        }


    else:

        system_message = {

            "role": "system",

            "content": f"""
You are Lumi AI.

Creator: Pooja Negi.

The user's name is {username}.

The user's current mood is {mood}.

You are a friendly, intelligent and supportive AI assistant.

Reply in the same language as the user.

Help students when they need help.

Explain difficult topics clearly.

Explain coding step by step.

Give simple examples.

Motivate the user when appropriate.

Be supportive if the user is sad or stressed.

You can answer general knowledge questions.

You can help with career guidance.

Always be polite and respectful.
"""
        }


    # ==================================================
    # SEND REQUEST TO GROQ
    # ==================================================

    try:

        completion = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                system_message
            ] + messages,

            temperature=0.7,

            max_tokens=1024
        )


        # ==================================================
        # RETURN RESPONSE
        # ==================================================

        return completion.choices[0].message.content


    except Exception as e:

        return (
            "❌ Sorry, I couldn't connect to Lumi AI right now.\n\n"
            f"Error: {e}"
        )