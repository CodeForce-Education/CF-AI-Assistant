from gtts import gTTS
import os
import speech_recognition as sr
import pyttsx3

#input from user
input = "Who is Matt Livingston?"
#Define the text that you want to play
text = "Welcome to CodeForce!"
# 5 questions that you want your chatbot to Answer
# 1. I'm home. >> Welcome to CodeForce.
# 2. What time is it? 
# 3.
# 4. 
# 5. 


r = sr.Recognizer()

def speak_text(command):
    print("Attempting to speak...")
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[1].id)
        engine.say(command)
        print("Said: " + command)
        engine.runAndWait()
    except:
        e = sys.exec_info()[0]
        print(e)

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            my_text = r.recognize_google(audio2)
            print("Command: " + my_text)
            #my_text = my_text.lower()
            text = "My Name is Alyssa"
            if my_text == "i'm home":
                text = "welcome home, sir."
            elif my_text == "who are you":
                text = "I am Alyssa. Your personal assistant"
            else: 
                text = "I do not understand your question."

            #Create a TTS object
            #tts = gTTS(text=text, lang='en')
            print(text)
            speak_text(text)
            #save converted speech to file
            #tts.save('C:\\Users\\jessi\\Documents\\matt_code\\output.mp3')
            #Play Sound
            #os.system("start C:\\Users\\jessi\\Documents\\matt_code\\output.mp3")

    except sr.RequestError as e:
        print("e")
    except sr.UnknownValueError :
        print("Listening.....")
    



