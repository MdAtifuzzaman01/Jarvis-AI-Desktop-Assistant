import pyttsx3
import datetime
import  itspeech_recognion as sr 
import wikipedia
import webbrowser
import os 
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice' , voices[1].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour>=12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis Sir. Please tell me how I may I help you!")
def take_command():
    # It takes microphone input from users and returns string output
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio , language='en-in')
            print(f"User said : {query}\n")
        except Exception as e:
        

            print("Say that again please..." )
            return "None"
        return query

        




def send_Email(to , content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com' , 'your-password')
    server.sendmail('youremail@gmail.com' , to , content)
    server.close()




if __name__ == "__main__":
   
    wish_me()
    while True:
        query = take_command().lower()

    #Logic for executing tasks based on the query
    if 'wikipedia' in query:
        speak('Searching wikipedia... ')
        query.replace('wikipedia' , "")
        results = wikipedia.summary(query , sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif  'open google' in query:
        webbrowser.open("google.com")
    elif  'open bing' in query:
        webbrowser.open("bing.com")
    elif  'open yahoo' in query:
        webbrowser.open("yahoo.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'play music' in query:
        music_dir ="D://Musics//Favourite Songs"
        songs =  os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir , songs[0]))
    elif 'the time' in query:
        Time = datetime.datetime.now().strftime("%H:%M:%S") 
        speak(f" Sir , the time is : {Time}")
    elif 'open code' in query:
        code_path = "C:\\Users\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
    elif 'email to yourname' in query:
        try:
            speak("What should I say?...")
            content = take_command() 
            to = yourname@gmail.com 
            speak("Email has been sent!")
        except Exception as e:
            
            speak("Sorry ! I am not beeing able to send email at this moment")







