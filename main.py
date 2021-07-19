import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import nltk

listener = sr.Recognizer()
player = pyttsx3.init()

def listen():
    with sr.Microphone() as input_device:
        print("I am Flipo, Ask me  ....")
        voice_content = listener.listen(input_device)
        text_command = listener.recognize_google(voice_content)
        text_command = text_command.lower()
        print(text_command)
    return text_command

def talk(text):
    player.say(text)
    player.runAndWait()

def run_bot():
    command = listen()
    if 'hello' in command:
        talk("I am flipo, How can I help you. I can help you with cerdit-cards Imformation.Do you Want it")
    if 'no' in command:
        talk("I have different options for . Should I tell")
        if 'yes' in command :
            talk('We are not forcing you to pay this month only , you can pay later on. With Interest rates')
    elif 'yes' in command:
        talk("From where do you like to start to listen")
    elif 'play' in command:
        command = command.replace("Play","")
        pywhatkit.playonyt(command)
    else:
        talk("sorry I didn't get it , Please repeat again")


run_bot()








