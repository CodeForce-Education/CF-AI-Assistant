from gtts import gTTS
import os
import speech_recognition as sr

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

if input == "I'm home":
    text = "Welcome home, sir."
elif input == "Who are you?":
    text = "I am Alyssa. Your personal assistant"
else: 
    text = "I do not understand your question."


while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            my_text = r.recognize_google(audio2)
            print("Command: " + my_text)

    except sr.RequestError as e:
        print("e")
    except sr.UnknownValueError :
        print("Listening")
    


#Create a TTS object
tts = gTTS(text=text, lang='en')
print(text)
#save converted speech to file
tts.save('C:\\Users\\jessi\\Documents\\matt_code\\output.mp3')
#Play Sound
os.system("start C:\\Users\\jessi\\Documents\\matt_code\\output.mp3")
