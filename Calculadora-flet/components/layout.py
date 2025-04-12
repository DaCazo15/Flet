import flet as ft
from .display import Display
from .history import HistoryPanel
from .keyboard import Keyboard

class MainLayout:
    def __init__(self, display, history, keyboard):
        self.display = display
        self.history = history
        self.keyboard = keyboard
        
    def build(self):
        calculator_area = ft.Column(
            [
                self.display.get_container(),
                self.keyboard.get_keyboard()
            ],
            spacing=20,
            width=400
        )
        
        return ft.Container(
            content=ft.Row(
                [
                    ft.Column([
                        self.display.title,
                        self.history.get_container()
                    ]),
                    calculator_area
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(top=50)
        )