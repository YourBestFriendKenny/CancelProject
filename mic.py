import speech_recognition as sr 
r = sr.Recognizer()
mic = sr.Microphone()

with mic as sourse:
    r.adjust_for_ambient_noise(sourse)
    audio = r.listen(sourse)


print(r.recognize_google (audio), language='ru-Ru')