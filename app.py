import streamlit as st
from groq_ai import ask_lumi
from voice_mode import listen, speak


# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="Lumi AI",
    page_icon="🤖",
    layout="centered"
)


# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "username" not in st.session_state:
    st.session_state.username = ""

if "mood" not in st.session_state:
    st.session_state.mood = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = []


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .main {
        background: linear-gradient(
            to bottom,
            #0f172a,
            #1e293b
        );
    }

    .title {
        text-align: center;
        font-size: 55px;
        color: #60A5FA;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: white;
        font-size: 22px;
    }

    .block {
        background: #1E293B;
        padding: 25px;
        border-radius: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# WELCOME PAGE
# ==================================================

if st.session_state.page == "welcome":

    st.markdown(
        "<div class='title'>🤖 Lumi AI</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Your Personal AI Companion</div>",
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        "<div class='block'>",
        unsafe_allow_html=True
    )

    st.header("👋 Hello!")

    st.write(
        """
I'm **Lumi AI** ❤️

I can help you with:

📚 Studies

💻 Coding

❤️ Emotional Support

🎯 Career Guidance

🌍 General Knowledge

✈️ Travel

😊 Motivation

🧠 Problem Solving

🌦️ Weather

🌐 Different Languages
"""
    )

    name = st.text_input(
        "👤 What's your Name?"
    )

    mood = st.selectbox(
        "😊 How are you feeling today?",
        [
            "😀 Happy",
            "😔 Sad",
            "😰 Stressed",
            "😴 Tired",
            "🤩 Excited",
            "🥺 Lonely",
            "😐 Normal"
        ]
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # ---------------- MOOD MESSAGE ----------------

    if mood == "😔 Sad":

        st.info(
            "💛 Don't worry. I'm always here for you."
        )

        st.write(
            "😂 Joke: Why don't programmers like nature? "
            "Because it has too many bugs!"
        )

    elif mood == "😰 Stressed":

        st.info(
            "🌸 You are stronger than you think. "
            "We'll solve everything together."
        )

    elif mood == "🥺 Lonely":

        st.info(
            "🤗 You are never alone. "
            "I'm always here to chat with you."
        )

    elif mood == "🤩 Excited":

        st.success(
            "🎉 I love your energy! "
            "Let's do something amazing today."
        )

    elif mood == "😀 Happy":

        st.success(
            "😄 Seeing you happy makes me happy too!"
        )

    st.write("")

    # ---------------- CONTINUE BUTTON ----------------

    if st.button(
        "✨ Continue",
        use_container_width=True
    ):

        if name.strip() == "":

            st.warning(
                "Please enter your name."
            )

        else:

            st.session_state.username = name.strip()

            st.session_state.mood = mood

            st.session_state.page = "chat"

            st.rerun()

    st.write("")

    st.caption(
        "Made with ❤️ by Pooja Negi"
    )


# ==================================================
# CHAT PAGE
# ==================================================

elif st.session_state.page == "chat":

    st.title("🤖 Lumi AI")

    st.success(
        f"Welcome {st.session_state.username} 👋"
    )

    st.write(
        f"😊 Mood: {st.session_state.mood}"
    )

    st.write("---")

    st.subheader(
        "💬 Chat with Lumi"
    )

    # ==================================================
    # SHOW PREVIOUS MESSAGES
    # ==================================================

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.write(
                message["content"]
            )

    # ==================================================
    # TEXT INPUT
    # ==================================================

    question = st.chat_input(
        "Ask me anything..."
    )


    # ==================================================
    # VOICE BUTTON
    # ==================================================

    voice_button = st.button(
        "🎤 Speak",
        use_container_width=True
    )


    # ==================================================
    # VOICE INPUT
    # ==================================================

    if voice_button:

        with st.spinner(
            "🎤 Listening..."
        ):

            try:

                voice_text = listen()

            except Exception as e:

                voice_text = ""

                st.error(
                    f"Microphone error: {e}"
                )

        if voice_text:

            question = voice_text

            st.success(
                f"You said: {voice_text}"
            )

        else:

            st.warning(
                "Sorry, I couldn't hear you. "
                "Please try again."
            )


    # ==================================================
    # PROCESS USER QUESTION
    # ==================================================

    if question:

        question = question.strip()

        if question:

            # ---------------- SAVE USER MESSAGE ----------------

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            # ---------------- SAVE MEMORY ----------------

            st.session_state.memory.append(
                question
            )

            # ---------------- SHOW USER MESSAGE ----------------

            with st.chat_message("user"):

                st.write(question)

            # ==================================================
            # ASK LUMI
            # ==================================================

            try:

                answer = ask_lumi(
                    st.session_state.messages,
                    st.session_state.username,
                    st.session_state.mood
                )

                # ---------------- SAVE AI MESSAGE ----------------

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

                # ---------------- SHOW AI MESSAGE ----------------

                with st.chat_message("assistant"):

                    st.write(answer)

                # ---------------- VOICE OUTPUT ----------------

                try:

                    speak(answer)

                except Exception as e:

                    st.warning(
                        f"Voice output unavailable: {e}"
                    )

            except Exception as e:

                st.error(
                    f"❌ Lumi AI Error: {e}"
                )


    # ==================================================
    # BOTTOM BUTTONS
    # ==================================================

    st.write("---")

    col1, col2 = st.columns(2)


    # ---------------- CLEAR CHAT ----------------

    with col1:

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):

            st.session_state.messages = []

            st.session_state.memory = []

            st.rerun()


    # ---------------- BACK HOME ----------------

    with col2:

        if st.button(
            "⬅️ Back",
            use_container_width=True
        ):

            st.session_state.page = "welcome"

            st.rerun()