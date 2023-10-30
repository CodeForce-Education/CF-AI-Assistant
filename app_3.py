import openai
import speech_recognition as sr
import pyttsx3
import sys

openai.api_key = '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'

messages = []
def send_to_chatGPT(messages, model='gpt-4-0613'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    message = response.choices[0].message.content
    print(message)
    #messages.append(response.choices[0].message)
    messages.append(message)
    return message
    
r = sr.Recognizer()
# Define the text that you want to play
text = "Welcome to CodeForce!"

def speak_text(command):
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        # engine.setProperty('voices', voices[1].id)
        engine.say(command)
        print("Said: " + command)
        engine.runAndWait()
    except:
        e = sys.exc_info()[0]
        print(e)


while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            my_text = r.recognize_google(audio2)
            my_text = my_text.lower()
            print("Command: " + my_text)
            messages.append({'role':'user', 'content': my_text})
            response = send_to_chatGPT(messages)
            if my_text == "i'm home":
                text = "Welcome home, sir."
            elif my_text == "who are you":
                text = "I am Alfred. Your personal assistant. How may I be of assistance today?"
            else: 
                text = "I do not understand your question." 
            print(response)
            speak_text(response)

    except sr.RequestError as e:
        print(e)
    except sr.UnknownValueError :
            print("Listening.....")
