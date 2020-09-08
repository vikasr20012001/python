import os
import pyttsx3 as a
import speech_recognition as b
import webbrowser as wp
print(format('---------------Wellcome To My  Tech Support I Am Robotech---------------', '^90'))
a.speak("wellcome to my  Tech Support i am robotech")
print("""HELLO USER   HOW I CAN HELP YOU""")
a.speak("HELLO USER  HOW I CAN HELP YOU")
print("1.LAUNCH GOOGLE BABA")
a.speak("LAUNCH GOOGLE BABA")
print("2.LAUNCH WHATSAPP WEB")
a.speak("LAUNCH WHATSAPP WEB")
print("3.LAUNCH FACEBOOK WEB")
a.speak("LAUNCH FACEBOOK WEB")
print("4.LAUNCH TWITTER WEB")
a.speak("LAUNCH TWITTER WEB")
print("5.LAUNCH AMAZON WEB")
a.speak("LAUNCH AMAZON WEB")
print("6.LAUNCH FLIPKART WEB")
a.speak("LAUNCH FLIPKART WEB")
print("7.LAUNCH YOUTUBE")
a.speak("LAUNCH YOUTUBE")
print("8.USE  GMAIL")
a.speak("USE GMAIL")
print("9.USE GOOGLE MAP")
a.speak("USE GOOGLE MAP") 
print("11.RUN MUSIC PLAYER")
a.speak("RUN MUSIC PLAYER")
print("12.USE GOOGLE TRANSLATOR")
a.speak("USE GOOGLE TRANSLATOR")

while True:
    r = b.Recognizer()
    with b.Microphone() as source:
      print("please speak  what you want to do:")
      a.speak("please speak  what you want to do")
      audio = r.listen(source)
      print("please wait your query is under process")
      a.speak("please wait your query is under process")
    p = r.recognize_google(audio)

    if (("dont " in p) or ("don't " in p) or ("not " in p) or ("Dont " in p) or ("Don't " in p) or ("Not " in p) or
            ("never " in p) or ("Never " in p) or ("DON'T " in p) or ("DONT " in p) or ("NOT " in p) or (
                    "NEVER " in p)):
        a.speak("your operation is  successfull")
        print("your operation is  successfull")
    elif (("run" in p) or ("Run" in p) or ("RUN" in p) or ("execute" in p) or ("Execute" in p) or ("EXECUTE" in p) or
          ("start" in p) or ("Start" in p) or ("START" in p) or ("open" in p) or ("Open" in p) or ("OPEN" in p)):     
            
            
        if ("WhatsApp" in p):
                        wp.open("https://web.whatsapp.com/")
                        a.speak("WELLCOME TO WHATSAPP")
            

        elif ("Amazon" in p):
                        wp.open("https://www.amazon.in/")
                        a.speak("WELLCOME TO AMAZON")
       
      
        elif ("Google" in p):
                      wp.open("https://www.google.com/")
                      a.speak("WELLCOME TO GOOGLE")
          
          
        elif ("Facebook" in p):
                      wp.open("https://www.facebook.com/")
                      a.speak("WELLCOME TO FACEBOOK")
        
        elif ("Twitter" in p):
                      wp.open("https://twitter.com/")
                      a.speak("WELLCOME TO TWITTER")
        
        elif ("Flipkart" in p):
                      wp.open("https://www.flipkart.com/")
                      a.speak("WELLCOME TO FLIPKART")
        
        elif ("YouTube" in p):
                      wp.open("https://www.youtube.com/")
                      a.speak("WELLCOME TO YOUTUBE")
        
        elif ("Gmail" in p):
                      wp.open("http://gmail.com/")
                      a.speak("WELLCOME TO GMAIL")
        
        elif (("Google" and "Map") in p):
                      wp.open("https://www.google.co.in/maps")
                      a.speak("WELLCOME TO GOOGLE MAP")
        
        elif (("music"and"player") in p):
                      wp.open("https://www.jiosaavn.com/featured/savan---sawan---saavan---saawan/jORiC1Lxp3Q_")
                      a.speak("WELLCOME TO JIO SAVAN")
        
        elif (("Google"and"translator") in p):
                      wp.open("https://translate.google.com/")
                      a.speak("WELLCOME TO GOOGLE TRANSLATOR")
        
        
        elif ("exit" in p) or ("Exit" in p) or ("EXIT" in p):
                      break
            
    
    
    
    else:
                    print()
                    print("SORRY I CANT UNDERSTAND")
                    a.speak("SORRY I CANT UNDERSTAND")
                   
                    print()
