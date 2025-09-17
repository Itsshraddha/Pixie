import speech_recognition as sr
import webbrowser
import pyttsx3
import music as m
import google.generativeai as genai
genai.configure(api_key="AIzaSyDWRGLFsfkMkMz8IRHKdASuil6k8EZ1jDs")
model = genai.GenerativeModel('gemini-1.5-flash')
r = sr.Recognizer()
def speak(text):
    engine = pyttsx3.init()
    # set voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)  # female
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open('https://google.com')
    elif "open youtube" in c.lower():
        webbrowser.open('https://youtube.com')
    elif "open github" in c.lower():
        webbrowser.open('https://github.com')
    elif "open linkedin" in c.lower():
        webbrowser.open('https://linkedin.com')
    elif "open leetcode" in c.lower():
        webbrowser.open('https://leetcode.com')
    elif "play" in c.lower() :
        song = c[5:].lower()
        url = m.songs[song]
        speak(f"playing {song}")
        webbrowser.open(url)
    else :
        response = model.generate_content(c)
        print(response.text)
        speak(response.text)
        
    
     

if __name__ == "__main__":
    speak("Initializing Pixie  ")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source :
            print("Listening")
            audio =r.listen(source, timeout=5, phrase_time_limit=5)
        
        print("Recognizing...")
        try:
            word =r.recognize_google(audio)
            print(word)
            if "pixie" in word.lower():
                speak("Yes")
            elif "stop" in word.lower():
                speak("OKay")
                break
            processCommand(word)
            
        except Exception as  e :
            print("Please speak clear , I do not understand")
        