import speech_recognition as sr
import pygame
from MainMusicStart import Music1, Music2

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)

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
            if "включи песню bad blood" in command:
                Music1()
        if command:
            if "включи песню ocean eyes" in command:
                Music2()

if __name__ == "__main__":
    main()