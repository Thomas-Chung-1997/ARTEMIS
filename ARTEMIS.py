#Libraries
import speech_recognition as speech
import pyaudio as audio
import pyttsx3 as textToSpeech

#Modules
from modules import youtube
from modules import google
from modules import apps
from modules import time
from modules import sound
from modules import weather
from modules import wiki
from modules import timer

#Variables
recognizer = speech.Recognizer()
microphone = speech.Microphone()
tts = textToSpeech.init()
exit = False

#Main functioning code
def main():
    TextToSpeechInit()
        
    Speak("Artemis Initialized.")
        
    with microphone as source:
        text = ""
        
        recognizer.adjust_for_ambient_noise(source)

        while not exit:
            userInput = recognizer.listen(source)
            
            try:
                text = recognizer.recognize_google(userInput)
                
                print(text.lower())
            
                CommandSelector(text.lower())
            except speech.UnknownValueError:
                pass
 
#Uses speech_recognition and pyaudio to get sounds input from user, and interpret it into language
def listener():
    text = ""
            
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        
        userInput = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(userInput)
            
            print(text)
        except speech.UnknownValueError:
            pass
            
    return text.lower()

#Setup pyttsx3 settings
def TextToSpeechInit():
    voices = tts.getProperty('voices')
    
    tts.setProperty('voice', voices[2].id)
    tts.setProperty('volume', 0.4)
    tts.setProperty('rate', 150)

#Uses the pyttsx3 to turn text into audio language
def Speak(text):
    if not isinstance(text, str):
        raise Exception("Variable is not a string.")
    
    tts.say(text)
    tts.runAndWait()

def NoCommandError():
    Speak("Sorry, I didn't quite get that.")    

def CommandSelector(text):
    if text ==  "":
        return
    
    if text.startswith('artemis'):
        text = text.replace("artemis ", "")
    else:
        return
          
    if text.startswith("youtube"):
        text = text.replace("youtube ", "")
        Speak(youtube.YoutubeSearch(text))
    elif text.startswith("google"):
        text = text.replace("google ", "")
        Speak(google.GoogleSearch(text))
    elif text.startswith("wiki"):
        text = text.replace("wiki", "")
        Speak(wiki.WikipediaSearch(text))
    elif text.startswith("open"):
        text = text.replace("open ", "")
        Speak(apps.OpenApp(text))
    elif "what" in text:
        if "time" in text:
            Speak(time.CurrentTime())
        elif "weather" in text:
            Speak(weather.WeatherSearch())
        elif "forecast" in text:
            Speak(weather.ForcastSearch())
        elif "temperature" in text:
            Speak(weather.TemperatureSearch())
        elif "day" in text:
            Speak(time.CurrentDay())
        else:
            NoCommandError()
    elif "volume" in text:
        text = text.replace("volume ", "")
        if "increase" in text:
            for i in range(5):
                sound.Sound.volume_up()
            Speak("Increasing volume")
        elif "lower" in text:
            for i in range(5):
                sound.Sound.volume_down()
            Speak("Lowering volume")
        elif "max" in text:
            sound.Sound.volume_max()
            Speak("Maxing out volume")
        elif "unmute" in text:
            if sound.Sound.is_muted():
                sound.Sound.mute()
                Speak("Unmuting volume")
        elif "mute" in text:
            if not sound.Sound.is_muted():
                sound.Sound.mute()
                Speak("Muting volume")
        else:
            NoCommandError()
    elif "timer" in text:
        Speak(timer.Timer(text))
    elif text == "turn off":
        print("turning off...")
        Speak("Artemis turning off.")
                    
        global exit
        exit = True
    else:
        NoCommandError()

if __name__ == "__main__":
    main()