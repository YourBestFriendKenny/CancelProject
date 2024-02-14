import speech_recognition as sr
from MainMusicStart import Music1, Music2

# Создаем объект Recognizer
r = sr.Recognizer()

def recognize_speech():
    # Запускаем аудиопоток с микрофона
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        # Слушаем и записываем аудиофайл
        audio = r.listen(source)

    try:
        # Используем Google Web Speech API для распознавания аудио
        text = r.recognize_google(audio, language="ru-RU")
        print(f"Вы сказали: {text}")
        # Выполняем определенные действия на основе распознанного текста
        if "включи песню bad blood" in text.lower():
            Music1()# Пример действия
        elif "пока" in text.lower():
            print("До свидания!")  # Пример действия
        else:
            print("Я не могу распознать данное слово.")  # Обработка неизвестных команд
    except sr.UnknownValueError:
        print("Извините, не удалось распознать вашу речь.")

# Вызываем функцию при нажатии кнопки
recognize_speech()