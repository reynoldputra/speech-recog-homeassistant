import speech_recognition as sr 
import os 
import time
from pygame import mixer
from gtts import gTTS
from datetime import datetime
import json

r = sr.Recognizer()

def playaudio(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    audiofile = "voice"+date_string+".mp3"
    myobj.save(audiofile)
    mixer.init()
    mixer.music.load(audiofile)
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.music.unload()
    os.remove(audiofile)

def intent_triger(intent):
    print("Trigering", intent)
    # create http request to triger intent script

def intent_handling(text):
    print("Text : " , text)
    print("Recognizing intent...")
    intentFile = open('intent.json')
    data = json.load(intentFile)

    for service in data["data"]:
        keyword = service["keyword"] 
        intents = service["intents"] 
        if(any(word in text for word in keyword)):
            for intent in intents :
                if(intent['action'] in text):
                    intent_triger(intent["intentName"])
                    return;
    print("Sorry, we can't recognize your command. Try to say it again.")
    intentFile.close()

# with sr.Microphone() as source:
print("================= Welcome! ===================")
# playaudio("Hello! Welcome to the lab of cyber security and smart city, department of information technology I T S. How can I help you?")
# audio_data = r.record(source, duration=7)
print("Recognizing speech...")
# text = r.recognize_google(audio_data)
text = "Turning on the lights" # for testing
intent_handling(text)
