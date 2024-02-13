import speech_recognition as sr
import pygame
import os


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)
        print(recognizer.recognize_google (audio, language='ru-RU'))

    try:
        print("Распознаю...")
        text = recognizer.recognize_google(audio, language="ru-RU")
        return text.lower()
    except sr.UnknownValueError:
            print("Невозможно распознать речь")
    except sr.RequestError as e:
            print("Ошибка сервиса распознавания речи; {0}".format(e))

def play_music():
    # Здесь ваш код для запуска музыки
    pass

def main():
    pygame.init()
    # Инициализация GUI и кнопки для запуска распознавания речи

while True:
        # Ожидание нажатия кнопки
        # Когда кнопка нажата:
        command = recognize_speech()
        if command:
            if "Привет" in command:
                print("OOOOOOOOOOOOOOOOOOOOO")
        if command:
            if "как" in command:
                print("АААААААААААААААААААААА")






if __name__ == "__main__":
    main()

