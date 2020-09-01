<<<<<<< HEAD
import os
import pyttsx3 as a
print(format('---------------Wellcome To My  Tech Support---------------', '^90'))
a.speak("wellcome to my  Tech Support")
print("""HELLO USER  I CAN HELP YOU TO RUN THE OS BASE PROGRAM""")
a.speak("HELLO USER  I CAN HELP YOU TO RUN THE OS BASE PROGRAM")
print("1.RUN NOTEPAD++ EDITOR")
a.speak("RUN NOTEPAD++ EDITOR")
print("2.RUN NOTEPAD")
a.speak("RUN NOTEPAD")
print("3.RUN CHROME BROWSER")
a.speak("RUN CHROME BROWSER")
print("4.RUN WINDOW MEDIA PLAYER")
a.speak("RUN WINDOW MEDIA PLAYER")
print("5.RUN PYTHON") ;;;
a.speak("RUN PYTHON ")
print("6.RUN VLC PLAYER")
a.speak("RUN VLC PLAYER")

while True:

   
    
    
    print("Please Enter What You Want To Do(If You Want To Close Type  Exit In Your Keyboard):", end=" ")
    
    a.speak("Please Enter What You Want To Do:")

    p = input()

    if (("dont " in p) or ("don't " in p) or ("not " in p) or ("Dont " in p) or ("Don't " in p) or ("Not " in p) or
            ("never " in p) or ("Never " in p) or ("DON'T " in p) or ("DONT " in p) or ("NOT " in p) or ("NEVER " in p)):
                a.speak("your operation is  successfull")
                print("your operation is  successfull")

    elif (("run" in p) or ("Run" in p) or ("RUN" in p) or ("execute" in p)or ("Execute" in p) or ("EXECUTE" in p) or
            ("start" in p) or ("Start" in p) or ("START" in p) or ("open" in p) or ("Open" in p) or ("OPEN" in p)):
            if (("notepad++" in p) or ("Notepad++" in p) or ("NOTEPAD++" in p) or ("Notepad++ editor" in p) or ("NOTEPAD++ editor" in p) or ("NOTEPAD++ EDITOR" in p)
                or ("notepad++ editor" in p)) and (("editor" in p) or ("EDITOR" in p) or ("Editor" in p)):
                os.system("notepad++")
                a.speak("WELLCOME TO NOTEPAD++ EDITOR")
                
            elif (("notepad" in p) or ("Notepad" in p) or ("NOTEPAD" in p) or ("editor" in p) or ("Editor" in p) or ("EDITOR" in p)
                or (("text" in p) or ("Text" in p) or ("TEXT" in p)) and (("editor" in p) or ("Editor" in p) or ("EDITOR" in p))):
                a.speak("WELLCOME TO NOTEPAD")
                os.system("notepad")
                
            elif (("browser" in p) or ("Browser" in p) or ("BROWSER" in p) or ("google" in p) or ("Google" in p) or ("GOOGLE" in p)
                or ("chrome" in p) or ("Chrome" in p) or ("CHROME" in p)):
                a.speak("WELLCOME TO CHROME BROWSER")
                os.system("chrome")    
                
            elif (((("media" in p) or ("Media" in p) or ("MEDIA" in p)) and (("player" in p) or ("Player" in p) or ("PLAYER" in p)))
                or ((("video" in p) or ("Video" in p) or ("VIDEO" in p)) and(("player" in p) or ("Player" in p) or ("PLAYER" in p)))
                or ("wmplayer" in p) or ("Wmplayer" in p) or ("Wmplayer" in p)):
                a.speak("WELLCOME TO WINDOW MEDIA PLAYER")
                os.system("wmplayer")
                
            elif (("python" in p) or ("Python" in p) or ("PYTHON" in p)):
                a.speak("WELLCOME TO PYTHON WORLD")
                os.system("python")
                
            elif (("VLC PLAYER" in p) or ("VLC MEDIA PLAYER" in p) or ("vlc media player" in p)or("Vlc Media Player")or("vlc player" in p)or("vlc" in p)):
                a.speak("WELLCOME TO VLC MEDIA PLAYER")
                os.system("vlc")
                
    elif ("exit" in p) or ("Exit" in p) or ("EXIT" in p):
        break
    else:
        print()
        print("***---***your input is invalid***---***")
        print("***---***please enter a valid input***--- ***")
        print()
=======
import os
import pyttsx3 as a

print(format('---------------Wellcome To My  Tech Support---------------', '^90'))
a.speak("wellcome to my  Tech Support")
print("""HELLO USER  I CAN HELP YOU TO RUN THE OS BASE PROGRAM""")
a.speak("HELLO USER  I CAN HELP YOU TO RUN THE OS BASE PROGRAM")
print("1.RUN NOTEPAD++ EDITOR")
a.speak("RUN NOTEPAD++ EDITOR")
print("2.RUN NOTEPAD")
a.speak("RUN NOTEPAD")
print("3.RUN CHROME BROWSER")
a.speak("RUN CHROME BROWSER")
print("4.RUN WINDOW MEDIA PLAYER")
a.speak("RUN WINDOW MEDIA PLAYER")
print("5.RUN PYTHON") 
a.speak("RUN PYTHON ")
print("6.RUN VLC PLAYER")
a.speak("RUN VLC PLAYER")

while True:

   
    
    
    print("Please Enter What You Want To Do(If You Want To Close Type  Exit In Your Keyboard):", end=" ")
    
    a.speak("Please Enter What You Want To Do:")

    p = input()

    if (("dont " in p) or ("don't " in p) or ("not " in p) or ("Dont " in p) or ("Don't " in p) or ("Not " in p) or
            ("never " in p) or ("Never " in p) or ("DON'T " in p) or ("DONT " in p) or ("NOT " in p) or ("NEVER " in p)):
                a.speak("your operation is  successfull")
                print("your operation is  successfull")

    elif (("run" in p) or ("Run" in p) or ("RUN" in p) or ("execute" in p)or ("Execute" in p) or ("EXECUTE" in p) or
            ("start" in p) or ("Start" in p) or ("START" in p) or ("open" in p) or ("Open" in p) or ("OPEN" in p)):
            if (("notepad++" in p) or ("Notepad++" in p) or ("NOTEPAD++" in p) or ("Notepad++ editor" in p) or ("NOTEPAD++ editor" in p) or ("NOTEPAD++ EDITOR" in p)
                or ("notepad++ editor" in p)) and (("editor" in p) or ("EDITOR" in p) or ("Editor" in p)):
                os.system("notepad++")
                a.speak("WELLCOME TO NOTEPAD++ EDITOR")
                
            elif (("notepad" in p) or ("Notepad" in p) or ("NOTEPAD" in p) or ("editor" in p) or ("Editor" in p) or ("EDITOR" in p)
                or (("text" in p) or ("Text" in p) or ("TEXT" in p)) and (("editor" in p) or ("Editor" in p) or ("EDITOR" in p))):
                a.speak("WELLCOME TO NOTEPAD")
                os.system("notepad")
                 
            elif (("browser" in p) or ("Browser" in p) or ("BROWSER" in p) or ("google" in p) or ("Google" in p) or ("GOOGLE" in p)
                or ("chrome" in p) or ("Chrome" in p) or ("CHROME" in p)):
                a.speak("WELLCOME TO CHROME BROWSER")
                os.system("chrome")    
                
            elif (((("media" in p) or ("Media" in p) or ("MEDIA" in p)) and (("player" in p) or ("Player" in p) or ("PLAYER" in p)))
                or ((("video" in p) or ("Video" in p) or ("VIDEO" in p)) and(("player" in p) or ("Player" in p) or ("PLAYER" in p)))
                or ("wmplayer" in p) or ("Wmplayer" in p) or ("Wmplayer" in p)):
                a.speak("WELLCOME TO WINDOW MEDIA PLAYER")
                os.system("wmplayer")
                
            elif (("python" in p) or ("Python" in p) or ("PYTHON" in p)):
                a.speak("WELLCOME TO PYTHON WORLD")
                os.system("python")
                
            elif (("VLC PLAYER" in p) or ("VLC MEDIA PLAYER" in p) or ("vlc media player" in p)or("Vlc Media Player")or("vlc player" in p)or("vlc" in p)):
                a.speak("WELLCOME TO VLC MEDIA PLAYER")
                os.system("vlc")
                
    elif ("exit" in p) or ("Exit" in p) or ("EXIT" in p):
        break
    else:
        print()
        print("***---***your input is invalid***---***")
        print("***---***please enter a valid input***--- ***")
        print()
>>>>>>> 0c60976a9ba084034bbf4ff21c1510b4cc5a54b3
