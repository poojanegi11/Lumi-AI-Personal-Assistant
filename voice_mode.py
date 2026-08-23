import speech_recognition as sr
import pyttsx3


# ==================================================
# VOICE INPUT
# ==================================================

def listen():

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            print("🎤 Listening...")

            # Reduce background-noise problems
            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

        print("🔄 Converting speech to text...")

        text = recognizer.recognize_google(
            audio
        )

        print(f"🗣️ You said: {text}")

        return text

    except sr.WaitTimeoutError:

        print("⏰ No speech detected.")

        return ""

    except sr.UnknownValueError:

        print("❌ I couldn't understand your voice.")

        return ""

    except sr.RequestError as e:

        print(
            f"❌ Speech recognition service error: {e}"
        )

        return ""

    except Exception as e:

        print(
            f"❌ Microphone error: {e}"
        )

        return ""


# ==================================================
# VOICE OUTPUT
# ==================================================

def speak(text):

    try:

        engine = pyttsx3.init()

        engine.setProperty(
            "rate",
            165
        )

        engine.setProperty(
            "volume",
            1.0
        )

        engine.say(text)

        engine.runAndWait()

        engine.stop()

    except Exception as e:

        print(
            f"❌ Text-to-speech error: {e}"
        )