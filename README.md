# AI Voice Assistant (Alexa/Jarvis/Google Assistant-like)

A Python-based voice assistant that responds to voice commands and provides spoken responses using text-to-speech technology.

## Features

- **Voice Interaction**: Text-to-speech responses using pyttsx3
- **Time Information**: Tells current time when asked
- **Knowledge Retrieval**: Fetches information from Wikipedia
- **Humor**: Tells jokes using pyjokes library
- **Greeting Recognition**: Responds to greetings like "good morning", "good night", "hi", "bye"
- **Personalized Responses**: Engaging and witty responses to specific queries

## Requirements

- Python 3.x
- pyttsx3 - Text-to-speech library
- wikipedia - Wikipedia API wrapper
- pyjokes - Joke library
- pyaudio - Audio I/O (for microphone input, optional for text input mode)

## Installation

Install the required packages:

```bash
pip install pyttsx3
pip install wikipedia
pip install pyjokes
pip install pyaudio
```

**Note for pyaudio installation errors:**
- If pyaudio installation fails, try: `pip install portaudio`
- If still failing, use pipwin: `pip install pipwin` then `pipwin install pyaudio`

## Usage

Run the assistant:

```bash
python sample.py
```

Type commands such as:
- "good morning" - Get a morning greeting
- "time" - Hear the current time
- "who the heck is [person name]" - Get information about someone
- "date" - Get a witty response
- "are you single" - Get a humorous response
- "joke" - Hear a random joke
- "hi" - Get a greeting
- "good night" / "good afternoon" - Get appropriate greetings
- "bye" - Exit the assistant

## How It Works

1. Prompts the user to type a command
2. Analyzes the command text for keywords
3. Generates an appropriate response
4. Uses text-to-speech to speak the response aloud
5. Continuously loops waiting for the next command

## Files

- `sample.py` - Main assistant code
- `README.md` - This file 
