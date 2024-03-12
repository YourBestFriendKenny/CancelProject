import speech_recognition as sr
from Recognitition.MainMusicStart import Music1, Music2








def recognize_speech(): #   функция распознования речи и включающая трек
    r = sr.Recognizer()


    #      Запускаем аудиопоток с микрофона
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")

    #       Слушаем и записываем аудиофайл
        audio = r.listen(source)
        print(r.recognize_google(audio, language="ru-RU"))


    commands = {"включи песню bad blood": Music1, "пока": exit}

    try:
            # Использую Google Web Speech API для распознавания аудио
        text = r.recognize_google(audio, language="ru-RU")
        if text.lower() in commands:
            Music1()
            
        else:
            print("я не могу распознать")
    except sr.UnknownValueError:
                print("Извините, не удалось распознать вашу речь.")



