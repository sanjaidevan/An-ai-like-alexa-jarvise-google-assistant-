import pyttsx3
import datetime
import wikipedia
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("installing windows")
talk("windows ready")


def take_command():
    command=input("Type here:")
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'good morning' in command:
        talk('good morning sir')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hi' in command:
        talk("Hi sir")
    elif "bye" in command:
        talk("Take care sir")
        talk("See you soon sir")
    elif "good morning" in command:
        talk("good morning sir")
    elif "good night" in command:
        talk("good night sir")
    elif "good afternoon" in command:
        talk("good afternoon sir")
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
    


