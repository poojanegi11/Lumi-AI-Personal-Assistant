from voice_mode import listen, speak

print("Say something...")

text = listen()

print("You said:", text)

if text:
    speak("You said " + text)