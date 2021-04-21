import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from playsound import playsound
import PyPDF2




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Night sir!")
    speak("I am Virtual Assistant, let me help you..!")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen (source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:

        speak("I didnt catch that, please say that again..")
        return "None"
    return query

if __name__ == '__main__':

    wishme()
    while True:
        query = takecommand().lower()
        if'wikipedia' in query:
            speak("Searching wikipedia....")
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif'sing me a song' in query:
            playsound('song.mp3')

        elif'sing me a poetry' in query:
            playsound('poems.mp3')
        elif'tell me a story' in query:
            speak("A lion was once sleeping in the jungle when a mouse started running up and down his body just for fun. This disturbed the lion’s sleep, and he woke up quite angry. He was about to eat the mouse when the mouse desperately requested the lion to set him free. “I promise you, I will be of great help to you someday if you save me.” The lion laughed at the mouse’s confidence and let him go.One day, a few hunters came into the forest and took the lion with them. They tied him up against a tree. The lion was struggling to get out and started to whimper. Soon, the mouse walked past and noticed the lion in trouble. Quickly, he ran and gnawed on the ropes to set the lion free. Both of them sped off into the jungle.Moral of the StoryA small act of kindness can go a long way")

        elif'open youtube' in query:
             webbrowser.open("https://www.youtube.com/query")
        elif'open instagram' in query:
             webbrowser.open("https://www.instagram.com/")
        elif'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'the time'in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir, the time is{strtime}")
        elif'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif'open class' in query:
            speak("please remember to turn off web cam and microphone")
            webbrowser.open("https://classroom.google.com/")
        elif 'thank you' in query:
            speak("Always here for you")
        elif 'stop' in query:
            break