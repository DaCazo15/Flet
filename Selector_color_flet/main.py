import flet as ft
from flet import *
import colorsys

class ColorSelectorRGB(Container):
    def __init__(self):
        super().__init__() # Inicializa el contenedor   
        self.r = 0 # Valor inicial del rojo
        self.g = 0 # Valor inicial del verde
        self.b = 0 # Valor inicial del azul
        self.hex_color = "000000" # Valor inicial del color hexadecimal
        
        self._initialize_components() # Inicializa los componentes
        
        self._setup_ui() # Configura la interfaz
# ------------------ inicializar componentes ---------------------
    def _initialize_components(self):
        # Sliders
        self.r_slider = Slider(
            min=0, max=255, value=self.r, 
            on_change=self.update_color,
            label="{value}",
            width=250,
            divisions=255)
        self.g_slider = Slider(
            min=0, max=255, value=self.g, 
            on_change=self.update_color,
            label="{value}",
            width=250,
            divisions=255)
        self.b_slider = Slider(
            min=0, max=255, value=self.b, 
            on_change=self.update_color,
            label="{value}",
            width=250,
            divisions=255)
        # Campos de texto para RGB
        self.r_text = TextField(
            value=str(self.r), 
            width=60, 
            on_change=self.update_color_from_text,
            input_filter=ft.InputFilter(r'^\d{0,3}$'),
            text_align=ft.TextAlign.CENTER,
            hint_text="0-255")
        self.g_text = TextField(
            value=str(self.g), 
            width=60, 
            on_change=self.update_color_from_text,
            input_filter=ft.InputFilter(r'^\d{0,3}$'),
            text_align=ft.TextAlign.CENTER,
            hint_text="0-255")
        self.b_text = TextField(
            value=str(self.b), 
            width=60, 
            on_change=self.update_color_from_text,
            input_filter=ft.InputFilter(r'^\d{0,3}$'),
            text_align=ft.TextAlign.CENTER,
            hint_text="0-255")
        # Campo de texto HEX
        self.hex_input = TextField(
            value=self.hex_color.replace("#", ""),
            width=100,
            on_change=self.update_color_from_hex,
            hint_text="RRGGBB",
            input_filter=ft.InputFilter(r'^[0-9a-fA-F#]{0,7}$'))
        # Textos
        self.hex = "HEX"
        self.rgb = "RGB"
        self.hsl = "HSL"
        # Elemento de visualización
        self.color_display = Container(
            width=100,
            height=50,
            bgcolor=f"#{self.hex_color}",
            border_radius=10,
            alignment=alignment.center,
            content=Text(f"#{self.hex_color}", color=self._get_contrast_color()))
        # Textos informativos con etiquetas en gris
        self.hex_text = Row([
            Text(self.hex, color=colors.GREY_500),
            Text(f"#{self.hex_color}")])
        
        self.rgb_text = Row([
            Text(self.rgb, color=colors.GREY_500),
            Text(f"{self.r}, {self.g}, {self.b}")])
        
        self.hsl_text = Row([
            Text(self.hsl, color=colors.GREY_500),
            Text("0°, 0%, 0%")])
        
        self.informacion = [self.color_display, self.hex_text, self.rgb_text, self.hsl_text] # Lista de elementos de visualización

        self.title = Text("Selector de Color RGB", size=24, weight="bold") # Título
        self.icono = Icon(icons.PALETTE, size=35, color=colors.WHITE)
# ------------------ configurar UI ---------------------
    def _setup_ui(self):
        # Panel superior con información del color
        top_panel = Container(
            content=Column(
                controls=[
                    Container(
                        content=self.color_display,
                        alignment=alignment.center,
                        margin=margin.only(bottom=10)
                    ),
                    Row(
                        controls=[
                            self.rgb_text,
                            self.hsl_text
                        ],
                        alignment=MainAxisAlignment.SPACE_EVENLY,
                        spacing=10
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            padding=20,
            border_radius=10,
            margin=margin.only(bottom=20),
            bgcolor=colors.GREY_200)
        # Panel de controles
        controls_column = Column(
            controls=[
                Row(controls=[Text("R"), self.r_slider], spacing=10, alignment=MainAxisAlignment.CENTER),
                Row(controls=[Text("G"), self.g_slider], spacing=10, alignment=MainAxisAlignment.CENTER),
                Row(controls=[Text("B"), self.b_slider], spacing=10, alignment=MainAxisAlignment.CENTER),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        # Panel de visualización
        self.display_panel = Container(
            content=Column([
                Row(
                    controls=[
                        Row([Text("R", color=colors.WHITE), self.r_text], alignment=MainAxisAlignment.CENTER),
                        Row([Text("G", color=colors.WHITE), self.g_text], alignment=MainAxisAlignment.CENTER),
                        Row([Text("B", color=colors.WHITE), self.b_text], alignment=MainAxisAlignment.CENTER)
                    ],
                    spacing=15),
                Row([Row([Text("#", color=colors.WHITE), self.hex_input]), self.icono
                    ], 
                    spacing=50,
                    alignment=MainAxisAlignment.START)
            ]),
            padding=20,
            border_radius=10,
            bgcolor=colors.BLACK)
        # Contenido principal
        self.content = Column(
            controls=[
                Container(
                    content=self.title,
                    alignment=alignment.center,
                    margin=margin.only(bottom=40, top=30)),
                top_panel,
                Container(
                    content=Column([
                        controls_column,
                        Container(
                            content=self.display_panel,
                            alignment=alignment.center,
                            margin=margin.only(top=20)
                        )
                    ]), padding=10)],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
# ------------------ obtener color de contraste ---------------------
    def _get_contrast_color_from_rgb(self, r, g, b): 
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255 
        return colors.WHITE if luminance < 0.5 else colors.BLACK
# ------------------ obtener color de contraste ---------------------
    def _get_contrast_color(self) -> str: return self._get_contrast_color_from_rgb(self.r, self.g, self.b)
# ------------------ Metodos de actualizacion ---------------------
    def _update_display(self):
        self.hex_color = f"{int(self.r):02x}{int(self.g):02x}{int(self.b):02x}".upper() 
        self.color_display.bgcolor = f"#{self.hex_color}" 
        self.color_display.content.value = f"#{self.hex_color}" 
        self.color_display.content.color = self._get_contrast_color() 
        
        # Actualizar color del panel
        display_color = f"#{int(self.r * 0.7):02x}{int(self.g * 0.7):02x}{int(self.b * 0.7):02x}".upper() 
        self.display_panel.bgcolor = display_color   
        
        # Actualizar color del texto basado en el contraste
        text_color = self._get_contrast_color_from_rgb(int(self.r * 0.7), int(self.g * 0.7), int(self.b * 0.7))
        
        # Actualizar colores de texto en el panel
        for row in self.display_panel.content.controls:
            if isinstance(row, Row):
                for control in row.controls:
                    if isinstance(control, Row):
                        for subcontrol in control.controls:
                            if isinstance(subcontrol, Text):
                                subcontrol.color = text_color
                            elif isinstance(subcontrol, TextField):
                                subcontrol.text_style = TextStyle(color=text_color)
                    elif isinstance(control, Text):
                        control.color = text_color
                    elif isinstance(control, TextField):
                        control.text_style = TextStyle(color=text_color)
        
        # Actualizar valores manteniendo el color gris en las etiquetas
        self.hex_text.controls[1].value = f"#{self.hex_color}"
        self.rgb_text.controls[1].value = f"{int(self.r)}, {int(self.g)}, {int(self.b)}"
        self.hex_input.value = self.hex_color 
        
        try:
            h, l, s = colorsys.rgb_to_hls(self.r / 255, self.g / 255, self.b / 255)
            self.hsl_text.controls[1].value = f"{round(h * 360)}°, {round(s * 100)}%, {round(l * 100)}%"
        except:
            self.hsl_text.controls[1].value = " Error"
        self.update()
    
    def update_color(self, e: ControlEvent):
        try:
            if e.control == self.r_slider: # si el evento es slider rojo
                self.r = int(e.control.value) 
                self.r_text.value = str(self.r) 
            elif e.control == self.g_slider: # si el evento es slider verde       
                self.g = int(e.control.value) 
                self.g_text.value = str(self.g) 
            elif e.control == self.b_slider: # si el evento es slider azul    
                self.b = int(e.control.value) 
                self.b_text.value = str(self.b) 
            self._update_display()
        except Exception as ex:
            self._show_error(f"Error al actualizar color: {str(ex)}")
    
    def update_color_from_text(self, e: ControlEvent):
        try:
            value = int(e.control.value or 0) # si el evento es campo de texto
            clamped_value = max(0, min(255, value)) # restringe el valor a un rango de 0 a 255
            if e.control == self.r_text: # si  el evento es campo de texto rojo                 
                self.r_slider.value = self.r 
            elif e.control == self.g_text: # si el evento es campo de texto verde
                self.g = clamped_value 
                self.g_slider.value = self.g 
            elif e.control == self.b_text: # si el evento es campo de texto azul
                self.b = clamped_value 
                self.b_slider.value = self.b 
            self._update_display() 
        except ValueError:
            self._show_error("Por favor, ingresa un número válido entre 0 y 255.") 
            e.control.value = str(getattr(self, e.control.id[0])) 
    
    def update_color_from_hex(self, e: ControlEvent):
        try:
            hex_value = e.control.value.strip().lstrip('#')
            if len(hex_value) == 6 and all(c in '0123456789ABCDEFabcdef' for c in hex_value): #instancia si es un valor hexadecimal valido
                # Convertir valores hexadecimales a RGB
                rgb_values = [int(hex_value[i:i+2], 16) for i in (0, 2, 4)]
                components = ['r', 'g', 'b']
                for value, component in zip(rgb_values, components): # este for recorre el valor hexadecimal y lo convierte a rgb
                    setattr(self, component, value)  
                    slider = getattr(self, f"{component}_slider")
                    text_field = getattr(self, f"{component}_text")
                    slider.value = value  
                    text_field.value = str(value)  
                
                self._update_display()
            elif hex_value:
                raise ValueError("Formato HEX inválido")
        except Exception as ex:
            self._show_error("Por favor, ingresa un valor HEX válido (ej: FF0000 o #FF0000)") 
            e.control.value = self.hex_color 
# ------------------ mostrar error ---------------------
    def _show_error(self, message):
        if hasattr(self, 'page') and self.page: # instancia si es un contenedor de color
            self.page.snack_bar = ft.SnackBar( 
                content=ft.Text(message),
                behavior=ft.SnackBarBehavior.FLOATING  
            )
            self.page.snack_bar.open = True 
            self.page.update() 
def main(page: ft.Page):
    page.title = "Selector de Color RGB"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.bgcolor = colors.WHITE
    
    # Configuración para responsive design
    page.window_width = 400  # Ancho inicial de la ventana
    page.window_height = 700  # Alto inicial de la ventana
    page.window_resizable = True  # Permite redimensionar la ventana
    page.scroll = "adaptive"
    
    # Configuración específica para móvil
    page.window_maximizable = True
    page.window_minimizable = True
    
    selector = ColorSelectorRGB()
    page.add(selector)
    selector._update_display()

if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)
