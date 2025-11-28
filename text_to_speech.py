import pyttsx3
import time
names = ["pritam", "aditya", "Ayush"]

for i in names:
    speaker = pyttsx3.init()
    speaker.say(f"Hello {i}, how are you brother?")
    speaker.runAndWait()
    time.sleep(2)
    del speaker