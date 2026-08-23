# 🤖 Lumi AI — Personal AI Assistant

Lumi AI is a personal AI assistant developed using Python and Streamlit. It is designed to provide users with AI-based conversation, study assistance, voice interaction, weather information, web search, PDF-based learning, translation, and mood-based interaction.

## 🎯 Objectives

- Provide personal AI assistance.
- Help students with their studies.
- Provide voice-based interaction.
- Provide current information through web search.
- Provide weather information.
- Help users learn from PDF documents.
- Provide quizzes and educational assistance.
- Support multiple languages.

## ✨ Features

- 🤖 Normal AI Chat
- 📚 Study Mode
- 📝 Quiz Mode
- 📄 PDF Teacher
- 🌦 Weather Information
- 🌐 Web Search
- 🎤 Speech Recognition
- 🔊 Text-to-Speech
- 🌐 Translation
- 🧠 Conversation Memory
- 😊 Mood-Based Interaction

## 🛠 Technologies Used

- Python
- Streamlit
- Groq API
- Weather API
- Web Search API
- SpeechRecognition
- PyAudio
- pyttsx3
- PyPDF2
- deep-translator

## 📁 Project Files

- `app.py` — Main Streamlit application.
- `groq_ai.py` — Handles communication with the Groq AI API.
- `city_extractor.py` — Extracts city and location information.
- `study_mode.py` — Provides study assistance.
- `quiz_mode.py` — Provides quiz functionality.
- `teacher_mode.py` — Provides teacher-style learning assistance.
- `translator_mode.py` — Provides translation functionality.
- `voice_mode.py` — Handles speech recognition and text-to-speech.
- `weather_api.py` — Handles weather API requests.
- `weather_mode.py` — Handles weather-related requests.
- `Python_Notes.pdf` — Study material for PDF-based learning.

## 🚀 How to Run

### Step 1: Install Python

Install Python 3.x on your computer.

### Step 2: Install Dependencies

Open the terminal inside the project folder and run:

```bash
pip install -r requirements.txt

## Run the Application

```bash
streamlit run app.py