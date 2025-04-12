import flet as ft

class Display:
    def __init__(self):
        self.control = ft.Text(value="0", size=48, color=ft.colors.WHITE)
        self.title = ft.Text("Calculadora", size=48, color=ft.colors.WHITE)
        
    def update(self, value):
        self.control.value = value
        
    def get_container(self):
        return ft.Container(
            content=self.control,
            bgcolor="#384143",
            padding=20,
            border_radius=10,
            width=400
        )