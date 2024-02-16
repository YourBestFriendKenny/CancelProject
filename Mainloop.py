import flet as ft
import speech_recognition as sr
import MainRec as rec

#основная функция запуска программы граф интерфейса
def main(page):




    page.add(
        ft.ElevatedButton("Say hello!", on_click=lambda _: rec.recognize_speech())
    )




ft.app(target=main)