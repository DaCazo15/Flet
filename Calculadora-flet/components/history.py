import flet as ft

class HistoryPanel:
    def __init__(self):
        self.control = ft.Column(
            [
                ft.Text("Historial", size=24, color=ft.colors.WHITE),
                ft.Divider(height=1, color=ft.colors.WHITE),
                ft.Column([], scroll=ft.ScrollMode.AUTO, expand=True)
            ],
            spacing=10,
            width=220,
            height=400
        )
        
    def add_entry(self, operation, result):
        history_item = ft.Text(
            f"{operation} = {result}",
            size=16,
            color=ft.colors.WHITE
        )
        self.control.controls[2].controls.insert(0, history_item)
        if len(self.control.controls[2].controls) > 10:
            self.control.controls[2].controls.pop()
            
    def get_container(self):
        return ft.Container(
            content=self.control,
            bgcolor="#384143",
            padding=15,
            border_radius=10,
            margin=ft.margin.only(right=20)
        )