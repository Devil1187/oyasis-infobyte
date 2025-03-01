import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
     #print(voices[1].id) 
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Mornig!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am  Hari. Plese tell me how may I help you")    

def takecommand():
    # it will take the input from the microphone and makes string as a output

    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Rechognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e :
        #print(e)
        print("Say that again plese....")
        return"None"
    return query


if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()

        #LOGIC FOR EXECUTING TASKS BASED ON QUERY

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia",)
            print(results)
           
            speak(results)
           

        elif 'open youtube ' in query:
            webbrowser.open("youtube.com")


        elif 'open google ' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = "D:\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")




           



            

    



