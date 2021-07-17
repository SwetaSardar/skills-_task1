import pyfiglet
import pyttsx3
import webbrowser
import os

result = pyfiglet.figlet_format("<>==Menu Program==<>")
print(result)

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 0.9)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.say("welcome learners, I'm Alexa, tell me how can i help you")
engine.runAndWait()


while True:
    print()
    
    ch = input("Enter ur requirement : ")
    
    if(("launch" in ch) or ("open" in ch)) and (("chrome" in ch) or ("browser" in ch) or ("google chrome" in ch) or ("google" in ch)):
        pyttsx3.speak("please wait your google chrome is opening")
        os.system("chrome")
            
    elif(("launch" in ch) or ("open" in ch)) and ("camera" in ch):
        pyttsx3.speak("please wait your camera is opening")
        os.system("Start microsoft.windows.camera:")
    
    elif(("launch" in ch) or ("open" in ch)) and ("media player" in ch):
        pyttsx3.speak("please wait your windows media player is opening")
        os.system("wmplayer")
             
    elif(("launch" in ch) or ("open" in ch)) and (("vlc" in ch) or ("vlc player" in ch)):
        pyttsx3.speak("please wait your vlc player is opening")
        os.system("vlc")
            
    elif(("launch" in ch) or ("open" in ch)) and ("notepad" in ch):
        pyttsx3.speak("please wait your notepad is opening")
        os.system("notepad ")
            
    elif(("launch" in ch) or ("open" in ch)) and ("virtual box" in ch):
        pyttsx3.speak("please wait your oracle virtual box is opening")
        os.system("virtualbox")
    
    elif(("launch" in ch) or ("open" in ch)) and ("display setting" in ch): 
        pyttsx3.speak("please wait your display-setting is opening")
        os.system("Start ms-settings:display")
                
    elif(("launch" in ch) or ("open" in ch)) and ("bluetooth-setting" in ch):
        pyttsx3.speak("please wait your bluetooth-setting is opening")
        os.system("Start ms-settings:bluetooth")
            
    elif(("launch" in ch) or ("open" in ch)) and ("linkdin" in ch):
        pyttsx3.speak("please wait linkdin is opening")
        webbrowser.open("https://www.linkedin.com/")
            
    elif(("launch" in ch) or ("open" in ch)) and ("facebook" in ch):
        pyttsx3.speak("please wait facebook is opening")
        webbrowser.open("https://www.facebook.com/")
            
    elif(("launch" in ch) or ("open" in ch)) and (("instagram" in ch) or ("insta" in ch)):
        pyttsx3.speak("please wait instagram is opening")
        webbrowser.open("https://www.instagram.com/")
    
    elif(("launch" in ch) or ("open" in ch)) and ("youtube" in ch): 
        pyttsx3.speak("please wait youtube is opening")
        webbrowser.open("https://www.youtube.com/")
            
    elif(("launch" in ch) or ("create" in ch)) and (("instance" in ch) or ("new instance" in ch)):
        os.system('cmd /k "aws ec2 run-instances --image-id  ami-00bf4ae5a7909786c --instance-type t2.micro --count 1 --subnet-id subnet-1560697d --security-group-ids sg-00f472b011d3a896f  --key-name sweta02  "') 
        pyttsx3.speak("EC2 Instance is launched in AWS")
        
    elif(("exit" in ch) or ("stop" in ch) or ("quit" in ch) or ("close" in ch)):
        break


    else:
        pyttsx3.speak("sorry doesn't exist !")


