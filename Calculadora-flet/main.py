import flet as ft
from components.calculator import Calculator

def main(page: ft.Page):
    Calculator(page)

ft.app(target=main)