import flet as ft
import os

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: ft.Page):
    
    r = ft.Row(wrap=True, scroll="always")
    c = ft.ListView(expand=True, spacing=10) #место expand можно указать height и width
    r = c
    page.add(r)


    for i in range(1000):
        r.controls.append(
            ft.Container(
                ft.Text(f"item {i}"),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
                )
            )
        
        
        
        
        
        
        
        
    page.update()
ft.app(target=main)

