# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing
print("Welcome to RoboSpeaker 1.0 Created By Vedant A Nawale")
y = input("Enter your name : ")
while True:
      x = input("Enter What you want to speak: ")
      if x == "q":
            engine.say(f"Bye bye we meet soon {y}")
            engine.runAndWait()
            break
      engine.say(f"{x}")
      engine.setProperty('rate',100)
      engine.runAndWait()
