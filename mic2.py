import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        audio = r.listen(source)
    print(r.recognize_google(audio, language='ru-Ru'))



def say():
    print("Hello")

while True:
    command = recognize_speech()
    if "Hello" in command:
        say()