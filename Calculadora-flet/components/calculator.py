import flet as ft
from components.display import Display
from components.history import HistoryPanel
from components.keyboard import Keyboard
from components.layout import MainLayout

class Calculator:
    def __init__(self, page):
        self.page = page
        self._setup_page()
        
        self.resultado = 0
        self.operador = None
        self.operacion = ""
        
        # Componentes
        self.display = Display()
        self.history = HistoryPanel()
        self.keyboard = Keyboard(self.on_button_click)
        self.layout = MainLayout(self.display, self.history, self.keyboard)
        
        self._setup_ui()

    def _setup_page(self):
        self.page.title = "Calculadora"
        self.page.window_width = 650
        self.page.window_height = 700
        self.page.bgcolor = "#2A3132"
    
    def _setup_ui(self):
        self.page.add(self.layout.build())

    def on_button_click(self, text):
        try:
            if text.isdigit() or text == ".":
                if text == "." and "." in self.operacion:
                    return
                self.operacion += text
                self.display.update(self.operacion)
            elif text in "+-*/":
                if self.operacion:
                    self.resultado = float(self.operacion)
                self.operador = text
                self.operacion = ""
            elif text == "=":
                if self.operador and self.operacion:
                    if self.operador == "/" and float(self.operacion) == 0:
                        self.display.update("Error")
                    else:
                        operation = f"{self.resultado}{self.operador}{self.operacion}"
                        self.resultado = eval(operation)
                        self.history.add_entry(operation, self.resultado)
                        self.display.update(str(self.resultado))
                    self.operacion = ""
                    self.operador = None
            elif text == "C":
                self.resultado = 0
                self.operacion = ""
                self.operador = None
                self.display.update("0")
            self.page.update()
        except:
            self.display.update("Error")
            self.operacion = ""
            self.operador = None
            self.page.update()