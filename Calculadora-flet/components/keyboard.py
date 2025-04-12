import flet as ft

class Keyboard:
    def __init__(self, on_button_click):
        self.on_button_click = on_button_click
        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"],
        ]
        
    def create_button(self, text):
        return ft.ElevatedButton(
            text=text,
            width=80,
            height=80,
            on_click=lambda e: self.on_button_click(text),
            style=ft.ButtonStyle(
                bgcolor=ft.colors.BLUE_GREY if text not in ["C", "="] else ft.colors.RED,
                shape=ft.RoundedRectangleBorder(radius=8),
                text_style=ft.TextStyle(
                    size=30 if text not in ["C", "="] else 24
                )
            )
        )
        
    def get_keyboard(self):
        rows = []
        for row in self.buttons:
            btn_row = []
            for btn_text in row:
                btn_row.append(self.create_button(btn_text))
            rows.append(ft.Row(btn_row, spacing=10, alignment=ft.MainAxisAlignment.CENTER))
        return ft.Column(rows, spacing=10)