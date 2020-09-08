import os
import pyttsx3 as a
import speech_recognition as b
import webbrowser as wp
print(format('---------------Wellcome To My  Tech Support I Am Robotech---------------', '^90'))
a.speak("wellcome to my  Tech Support i am robotech")
print("""HELLO USER   HOW I CAN HELP YOU""")
a.speak("HELLO USER  HOW I CAN HELP YOU")
while True:
    r = b.Recognizer()
    with b.Microphone() as source:
      print("please speak  what you want to do:")
      a.speak("please speak  what you want to do")
      audio = r.listen(source)
      print("please wait your query is under process")
      a.speak("please wait your query is under process")
    p = r.recognize_google(audio)

    wp.open("https://google.com/?#q=" + p)
