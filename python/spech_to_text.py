import speech_recognition as sr
import pyttsx3
import pyaudio

r=sr.Recognizer()
def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
while(1):
    try:
        with sr.Microphone() as source2:
            print("speak now")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2,language='tr-TR')
            MyText = MyText.lower()
            print(MyText)
            speak_text(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
    
