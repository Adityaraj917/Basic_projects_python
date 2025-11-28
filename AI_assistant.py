import pyttsx3 as p
import speech_recognition as sr
import pywhatkit
import os
import time

mic = sr.Recognizer()




while True:
    speaker = p.init()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Listening...")
        voice = mic.listen(source)

    try:
        text = mic.recognize_google(voice)
        print("User said:", text)

        if "open notepad" in text.lower():
            print("Opening notepad")
            speaker.say(" ok openeing notepad for you Aditya sir")
            speaker.runAndWait()
            os.system("notepad")
        elif "open chrome" in text.lower():
            print("opening chrome..")
            speaker.say(" ok openeing chrome for you Aditya sir")
            speaker.runAndWait()
            os.system(" start chrome")

        #elif "send message to home" in text:
            #print("sending message to home")
            #speaker.say(" ok sending message for you Aditya sir")
            #speaker.runAndWait()
            #pywhatkit.sendwhatmsg_instantly("+","bhgla ki")
            
        elif "jarvis stop" in text.lower():
            speaker.say(" ok Aditya sir,I would be always raedy to serve you next time ")
            speaker.runAndWait()
            break
       
       
        
        else:
            speaker.say("Command not recognized sir. Please try again.")
            speaker.runAndWait()

        speaker.stop()
        del speaker
        time.sleep(2)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
