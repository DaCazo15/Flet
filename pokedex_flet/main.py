import flet as ft
from flet import *
import aiohttp, asyncio
from style.constants import *
from googletrans import Translator

class Pokedex(Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.title = Text("Pokedex", font_family=FONT_BOLD, size=SCALE["sizes"]["title"], color=STYLES["clrs"]["clr-txt-primary"])
        self.nombre = Text("Pokemon", font_family=FONT, size=SCALE["sizes"]["subtitle"], color=STYLES["clrs"]["clr-txt-secondary"])
        self.tipo = Text("Tipo", font_family=FONT, size=SCALE["sizes"]["subtitle"], color=STYLES["clrs"]["clr-txt-secondary"])
        self.pokemon_nombre = Text("---", font_family=FONT, size=SCALE["sizes"]["body"], color=STYLES["clrs"]["clr-txt-tertiary"])
        self.pokemon_tipo = Text("", font_family=FONT, size=SCALE["sizes"]["body"], color=STYLES["clrs"]["clr-txt-tertiary"])
        self.text_info = [self.nombre, self.pokemon_nombre, self.tipo, self.pokemon_tipo]
        self.current_pokemon, self.offset_x, self.opacity, self.scale = 0, 0, 1, 1
        self.pokemon_stats, self.stat_widgets = {}, []
        self.img_down_arrow = Image(src=IMG["down"], scale=0.6, opacity=1.0)
        self.img_up_arrow = Image(src=IMG["up"], scale=0.6, opacity=1.0)  

        self.dic_tipo = {
            "grass": "Planta", 
            "bug": "Bicho", 
            "electric": "Electrico", 
            "ground": "Tierra", 
            "psychic": "Psiquico", 
            "dark": "Siniestro",
            "dragon": "Dragon"
        }
        self.traducir, self.pantalla = True, True
        self.pokemon_image = Image(
            src=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.current_pokemon}.png",
            fit=ImageFit.CONTAIN,
            width=SCALE["sizes-img"]["img-pokemon"], height=SCALE["sizes-img"]["img-pokemon"],
            offset=transform.Offset(self.offset_x, 0),
            opacity=self.opacity,
            scale=transform.Scale(self.scale),
            animate_offset=animation.Animation(300, "easeOut"),
            animate_opacity=animation.Animation(300, "easeIn"),
            animate_scale=animation.Animation(300, "bounceOut"))
        self.btn_ui()
        self.create_ui()
# -------------------------------- Traductor -------------------------------
    async def traductor(self, texto):
        try:
            if self.traducir:
                translator = Translator()
                if texto in self.dic_tipo:
                    return self.dic_tipo[texto]
                else:
                    translation = translator.translate(texto, src='en', dest='es')  
                    return translation.text 
            else:
                return texto
        except Exception as e:
            print(f"Error en la traducción: {e}")
            return texto
# -------------------------------- UI -------------------------------
    def create_ui(self):
        self.containers()
        if self.pantalla:
            self.content = self.contenedor_superior
        else:
            self.content = self.contenedor_inf
        self.page.update()
# -------------------------------- Contenedores -------------------------------
    def containers(self):
        self.pokemon = Container(
            width=SCALE["scale-page"]["width"] - 70,
            height=215,
            border=border.all(2, color="#5d5d5d"),
            border_radius=10,
            margin=margin.only(left=10, top=10),
            bgcolor=STYLES["clrs"]["clr-screen"])
        
        self.poke_screen = Container(
            Container(
                Stack([
                    Container(
                        width=SCALE["scale-page"]["width"] - 50,
                        height=235 if self.pantalla else 175,
                        border_radius=10,
                        border=border.all(4, color="#5d5d5d"),
                        bgcolor=STYLES["clrs"]["clr-card-top"],
                    ),
                    self.pokemon,
                    Container(
                        content=self.pokemon_image,
                        width=200,
                        height=200,
                        alignment=alignment.center,
                        margin=SCALE["m-i-pokemon"]["scr-init"]
                    ),
                ]))
            )
        
        self.contenedor_top = Container(
            Column([
                Row([
                    *[item for item in self.btn_top],
                    Row(controls=[Container(
                        self.title, 
                        bgcolor=STYLES["clrs"]["clr-screen"],
                        width=150,
                        border_radius=25,
                        border=SCALE["borders"]["default"],
                        alignment=alignment.center,
                        margin=margin.only(left=10, top=5))]
                    )
                ]),
            ]),
            bgcolor=STYLES["clrs"]["clr-card-top"],
            width=SCALE["scale-page"]["width"] - 25,
            height=60,
            border_radius=10,
            margin=margin.only(top=25),
            alignment=alignment.center)

        self.contenedor_center = Container(
            self.poke_screen,
            bgcolor=STYLES["clrs"]["clr-card"],
            width=SCALE["scale-page"]["width"] - 25,
            height=260 if self.pantalla else 200, 
            border_radius=10,
            alignment=alignment.center)

        self.contenedor_bottom = Container(
            Row([
                Container(
                    Column([
                        Stack([
                            Container(
                                Container(
                                    Column([
                                        *[item for item in self.text_info]
                                    ],
                                    spacing=1.5,
                                    ),
                                    margin=margin.only(top=10, left=15)
                                ),
                                border=Border(bottom=BorderSide(2, color=STYLES["clrs"]["brd-ctrl"])),
                                width=SCALE["scale-page"]["width"] - 180,
                                height=110,
                                margin=margin.only(top=22, left=15),
                                border_radius=10,
                                bgcolor=STYLES["clrs"]["clr-card-inf"],
                            ),
                        ]),
                        self.btn_info
                    ]),
                    width=SCALE["scale-page"]["width"] - 150,
                    height=210,
                    bgcolor=STYLES["clrs"]["clr-card-top"],
                    border_radius=10,
                    margin=margin.only(left=13)
                ),
                Container(
                    Container(
                        Column([
                            *[item for item in self.btn_arrows]
                        ]), margin=margin.only(top=12)
                    ),
                    border=border.all(2, color=STYLES["clrs"]["brd-ctrl"]),
                    height=210,
                    width=90,
                    border_radius=10,
                    margin=margin.only(top=2), 
                ),
            ]),
            bgcolor=STYLES["clrs"]["clr-card"],
            width=SCALE["scale-page"]["width"] - 25,
            height=230,
            border_radius=10,
            alignment=alignment.center)

        self.contenedor_superior = Container(
            Column(
                [
                    self.contenedor_top,
                    self.contenedor_center,
                    self.contenedor_bottom
                ],
                alignment=alignment.top_center,
            ),
            width=SCALE["scale-page"]["width"],
            height=SCALE["scale-page"]["height"],
            bgcolor=STYLES["clrs"]["clr-bg"],
            alignment=alignment.top_center)

        # Contenedor para la vista de detalles
        self.contenedor_top_inf = Container(
            Column([
                Row([
                    self.btn_back,
                    Row(controls=[Container(
                        self.title, 
                        bgcolor=STYLES["clrs"]["clr-screen"],
                        width=150,
                        border_radius=25,
                        border=border.all(2, color="#5d5d5d"),
                        alignment=alignment.center,
                        margin=margin.only(left=129, top=4))]
                    )
                ])
            ]),
            bgcolor=STYLES["clrs"]["clr-card-top"],
            width=SCALE["scale-page"]["width"] - 25,
            height=60,
            border_radius=10,
            margin=margin.only(top=25),
            alignment=alignment.center)

        self.contenedor_inf = Container(
            width=SCALE["scale-page"]["width"],
            height=SCALE["scale-page"]["height"],
            bgcolor=STYLES["clrs"]["clr-bg"],
            alignment=alignment.top_center)
# ---------------------------- btn UI -------------------------------
    def btn_ui(self):
        self.boton_azul = Container(
            Icon(Icons.TRANSLATE, color=STYLES["clrs"]["clr-txt-primary"]),
            bgcolor=STYLES["clr-btn"]["blue"],
            width=50,
            height=50,
            border=SCALE["borders"]["b-btn"],
            border_radius=50,
            margin=margin.only(top=5, left=10, right=2.5),
            on_click=lambda e: self.toggle_traducir(e),
            on_hover=lambda e: self.hover_effect_btn_clrs(e, "blue")) 
        
        self.boton_rojo = Container(
            bgcolor=STYLES["clr-btn"]["red"],
            width=25,
            height=25,
            border=SCALE["borders"]["b-btn"],
            border_radius=50,
            margin=margin.only(top=25, right=2.5),
            on_click=lambda e: print("Botón rojo clickeado"),
            on_hover=lambda e: self.hover_effect_btn_clrs(e, "red"))
        
        self.boton_verde = Container(
            bgcolor=STYLES["clr-btn"]["green"],
            width=25,
            height=25,
            border=SCALE["borders"]["b-btn"],
            border_radius=50,
            margin=margin.only(top=25, right=2.5),
            on_click=lambda e: print("Botón verde clickeado"),
            on_hover=lambda e: self.hover_effect_btn_clrs(e, "green"))
        
        self.boton_amarillo = Container(
            bgcolor=STYLES["clr-btn"]["yellow"],
            width=25,
            height=25,
            border=SCALE["borders"]["b-btn"],
            border_radius=50,
            margin=margin.only(top=25, right=2.5),
            on_click=lambda e: print("Botón amarillo clickeado"),
            on_hover=lambda e: self.hover_effect_btn_clrs(e, "yellow"))
        
        self.btn_top = [self.boton_azul, self.boton_rojo, self.boton_verde, self.boton_amarillo]

        self.btn_arrow_down = Container(
            self.img_down_arrow,
            on_click=self.click_down,
            on_hover=lambda e: self.hover_effect_img(e, "down"))

        self.btn_arrow_up = Container(
            self.img_up_arrow,
            on_click=self.click_up,
            on_hover=lambda e: self.hover_effect_img(e, "up"))

        self.btn_arrows = [self.btn_arrow_up, self.btn_arrow_down]

        self.btn_info = Container(
            content=Text(
                "Mas info", 
                font_family=FONT, 
                size=SCALE["sizes"]["body"], 
                color=STYLES["clrs"]["clr-txt-secondary"]),
            width=100,
            height=50,
            alignment=alignment.center,
            bgcolor=STYLES["clrs"]["clr-btn-inf"],
            border_radius=10, 
            border=SCALE["borders"]["b-btn"],
            margin=margin.only(left=(230/2) - 50),
            on_click=lambda e: self.toggle_pantalla(e),
            on_hover=lambda e: self.hover_effect(e))
        
        self.btn_back = Container(
            IconButton(
                icon=Icons.ARROW_BACK,
                icon_color=STYLES["clrs"]["clr-btn-back"],
                on_click=self.toggle_pantalla,
                icon_size=30
            ),
            alignment=alignment.top_left,
            padding=5)
# ------------------------------ Funcionalidad --------------------
    #---------------- Hovers ----------
    def hover_effect_img(self, e, img):
        if img == "down":
            self.btn_arrow_down.content.opacity = IMG["down-hover"] if e.data == "true" else IMG["down-def"]
        elif img == "up":
            self.btn_arrow_up.content.opacity = IMG["up-hover"] if e.data == "true" else IMG["up-def"]
        e.control.update()

    def hover_effect(self, e):
        e.control.bgcolor = STYLES["clrs"]["clr-btn-inf-hover"] if e.data == "true" else STYLES["clrs"]["clr-btn-inf"]
        e.control.update()

    def hover_effect_btn_clrs(self, e, clr):
        if clr == "blue":
            e.control.bgcolor = STYLES["clr-btn"]["blue-hover"] if e.data == "true" else STYLES["clr-btn"]["blue"]
        elif clr == "red":
            e.control.bgcolor = STYLES["clr-btn"]["red-hover"] if e.data == "true" else STYLES["clr-btn"]["red"]
        elif clr == "green":
            e.control.bgcolor = STYLES["clr-btn"]["green-hover"] if e.data == "true" else STYLES["clr-btn"]["green"]
        elif clr == "yellow":
            e.control.bgcolor = STYLES["clr-btn"]["yellow-hover"] if e.data == "true" else STYLES["clr-btn"]["yellow"]
        e.control.update()

    #---------------- Cargar detalles ----------
    async def cargar_detalles(self):
        try:
            if not self.pokemon_stats.get(self.current_pokemon): 
                response = await self.peticion(f"https://pokeapi.co/api/v2/pokemon/{self.current_pokemon}")
                if response:
                    stats = {}
                    for stat in response['stats']:
                        stat_name = await self.traductor(stat['stat']['name'].replace('-', ' ')) 
                        stats[stat_name] = stat['base_stat'] 
                    print(f"Traducir está {'activado' if self.traducir else 'desactivado'}")

                    self.pokemon_stats[self.current_pokemon] = {
                        'height': response['height'] / 10,  # Convertir a metros
                        'weight': response['weight'] / 10,  # Convertir a kg
                        'stats': stats,
                        'types': [
                            await self.traductor(t['type']['name']) if self.traducir else t['type']['name'] 
                            for t in response['types']
                        ]
                    }
            self.create_detail_view()
        except Exception as e:
            print(f"Error cargando detalles: {e}")
            self.pokemon_stats[self.current_pokemon] = {}
    #---------------- Crear vista de detalles ----------
    def create_detail_view(self):
        self.stats = self.pokemon_stats.get(self.current_pokemon, {}) 
        
        self.stat_widgets = [ # Crear widgets para las estadísticas
            Column([
                    Text(f"Nombre: {self.pokemon_nombre.value}", size=16, weight=FontWeight.BOLD),
                    Divider(height=10, color=STYLES["clr-div"]["gre-div"]),
                    Row([
                    Text(f"Tipo(s):\n{', '.join(self.stats.get('types', ['Desconocido']))}", size=16),
                    Column([
                        Text(f"Altura: {self.stats.get('height', '?')} m", size=16),
                        Text(f"Peso: {self.stats.get('weight', '?')} kg", size=16),
                    ], spacing=2),
                ], spacing=50),
                Divider(height=10, color=STYLES["clr-div"]["gre-div"]),
                Text("Estadísticas:", size=18, weight=FontWeight.BOLD)
            ], spacing=2)]
       
        for stat_name, stat_value in self.stats.get('stats', {}).items(): # Agregar cada estadística
            self.stat_widgets.append(
                Row([
                    Text(f"{stat_name}:", size=12, width=150, color=STYLES["clrs"]["clr-txt-secondary"]),
                    Text(f"{str(stat_value)} ", size=12, weight=FontWeight.BOLD),
                    Container(
                        width=stat_value / 1.7,
                        height=10,
                        bgcolor=self.get_stat_color(stat_value),
                        border_radius=5
                    )
                ], spacing=2)
            )

        self.contenedor_inf.content = Container(
                Column(
                [
                    self.contenedor_top_inf,
                    self.contenedor_center,
                    
                    # Contenedor de información
                    Container(
                        Column(
                            self.stat_widgets,
                            spacing=0.5
                        ),
                        padding=10,
                        bgcolor=STYLES["clrs"]["clr-card-top"],
                        border_radius=10,
                        width=SCALE["scale-page"]["width"] - 25,
                        height=290
                    )
                ]))
        
        self.content = self.contenedor_inf
        self.page.update()

    def get_stat_color(self, value):
        if value >= 100:
            return STYLES["stts-br-clrs"]["stts-100"]
        elif value >= 75:
            return STYLES["stts-br-clrs"]["stts-75"]
        elif value >= 50:
            return STYLES["stts-br-clrs"]["stts-50"]
        elif value >= 25:
            return STYLES["stts-br-clrs"]["stts-25"]
        else:
            return STYLES["stts-br-clrs"]["stts-0"]
    #---------------- Eventos ----------
    def click_down(self, e):
        e.page.loop.create_task(self.evento(e, "abajo"))
    
    def click_up(self, e):
        e.page.loop.create_task(self.evento(e, "arriba"))

    async def peticion(self, url): # Peticion a la API
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status() 
                    return await response.json()
        except Exception as e:
            print(f"Error en la petición: {e}")
            return None
  
    async def evento(self, event, direction=None):
        try:
            if direction == "abajo": 
                if self.current_pokemon == TOP_POKEMON:
                    self.current_pokemon = 1
                else:
                    self.current_pokemon += 1
            elif direction == "arriba":
                if self.current_pokemon == 1 or self.current_pokemon == 0:   
                    self.current_pokemon = TOP_POKEMON
                else:
                    self.current_pokemon -= 1
            self.resultado = await self.peticion(f"https://pokeapi.co/api/v2/pokemon/{self.current_pokemon}")
            
            if self.resultado and "name" in self.resultado:
                nombre = self.resultado['name'].capitalize()
                tipos = [tipo['type']['name'] for tipo in self.resultado['types']]
                self.pokemon_nombre.value = nombre
                if self.traducir:
                    self.pokemon_tipo.value = ', '.join([await self.traductor(tipo if tipo not in self.dic_tipo else self.dic_tipo[tipo]) for tipo in tipos]).upper()
                else:
                    self.pokemon_tipo.value = ', '.join([tipo for tipo in tipos]).upper()
                
                self.pokemon_image.src = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.current_pokemon}.png"
                
                # Animación de entrada
                self.offset_x = 0
                self.opacity = 1
                self.scale = 1
                
                if direction == "abajo":
                    self.offset_x = 1  # Entra desde la derecha
                elif direction == "arriba":
                    self.offset_x = -1  # Entra desde la izquierda
                    
                self.page.update()
                
                # Pequeña pausa antes de centrar
                await asyncio.sleep(0.1)
                
                self.offset_x = 0
                self.page.update()
                
        except Exception as e:
            print(f"Error: {e}")
            self.pokemon_nombre.value = "Error al obtener el Pokémon"
            self.pokemon_tipo.value = ""
            self.page.update()

    def toggle_traducir(self, e): # traducir ~ no traducir
        self.traducir = not self.traducir
        e.page.loop.create_task(self.evento(e))

    def toggle_pantalla(self, e): 
        self.pantalla = not self.pantalla
        if not self.pantalla:

            self.contenedor_center.height = 200
            self.pokemon_image.height = SCALE["sizes-img"]["img-pokemon-inf"]
            self.pokemon_image.width = SCALE["sizes-img"]["img-pokemon-inf"]

            container = self.poke_screen.content  
            container.padding = margin.only(top=10)
            stack = container.content
            if isinstance(stack, Stack): 
                stack.controls[0].height = 180  
                stack.controls[1].height = 160 
                stack.controls[2].margin = SCALE["m-i-pokemon"]["scr-inf"]

            e.page.loop.create_task(self.cargar_detalles())
        else:
            self.contenedor_center.height = 260
            self.pokemon_image.height = SCALE["sizes-img"]["img-pokemon"]
            self.pokemon_image.width = SCALE["sizes-img"]["img-pokemon"]

            container = self.poke_screen.content  
            stack = container.content
            if isinstance(stack, Stack): 
                stack.controls[0].height = 235  
                stack.controls[1].height = 200 
                stack.controls[2].margin = SCALE["m-i-pokemon"]["scr-init"]
            self.create_ui()

async def main(page: ft.Page):
    page.title = "Pokedex"
    
    # Configuración de la ventana
    page.window.width = SCALE["scale-page"]["width"]
    page.window.height = SCALE["scale-page"]["height"]
    page.window.resizable = False
    page.padding = 0
    
    # Creación de la Pokedex
    pokedex = Pokedex(page)
    page.add(pokedex)

if __name__ == "__main__":
    ft.app(target=main)
