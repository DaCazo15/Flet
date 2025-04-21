from flet import *
# --- ESTILOS GLOBALES ---
STYLES = {
    "clrs": {
        "clr-bg": Colors.GREY_900,
        "clr-card": Colors.GREY_500,
        "clr-card-top": Colors.GREY_700,
        "clr-card-inf": Colors.GREY_800,
        "clr-screen": Colors.TEAL_ACCENT_700,

        "brd-ctrl": Colors.BLACK87,

        "clr-btn-inf": Colors.GREY_800,
        "clr-btn-inf-hover": "#5d5d5d",
        "clr-btn": Colors.WHITE,

        "clr-txt-primary": Colors.GREY_800,
        "clr-txt-secondary": Colors.GREY_300,
        "clr-txt-tertiary": Colors.GREY_500,
    },
    "clr-btn-icon": {
        "azul": Colors.BLUE_900,
        "rojo": Colors.RED_900,
        "verde": Colors.GREEN_900,
        "amarillo": Colors.YELLOW_900,
    },
    "clr-div": {
        "gre-div": Colors.GREEN_500,
    },
    "clr-btn": {
        "blue": Colors.BLUE_500,
        "blue-hover": Colors.BLUE_600,
        "red": Colors.RED_600,
        "red-hover": Colors.RED_700,
        "green": Colors.GREEN_700,
        "green-hover": Colors.GREEN_800,
        "yellow": Colors.YELLOW_700,
        "yellow-hover": Colors.YELLOW_800,
    },
    "stts-br-clrs": {
        "stts-100": Colors.GREEN_ACCENT_400,
        "stts-75": Colors.LIGHT_GREEN_ACCENT_200,
        "stts-50": Colors.YELLOW_ACCENT_200,
        "stts-25": Colors.ORANGE_ACCENT_200,
        "stts-0": Colors.RED_ACCENT_200,
    }   
}

IMG = {
    "up": "assets/up.png",
    "up-def": 1.0,
    "up-hover": 0.4,
    "down": "assets/down.png",
    "down-def": 1.0,
    "down-hover": 0.4,

    "intro": "assets/Pokeball.png",
    "intro-def": 1.0,
    "intro-hover": 0.4,
}
# SCALE
SCALE = {
    "scale-page": {
        "height": 640,
        "width": 380,
    },
    "sizes": {
        "title": 30,
        "subtitle": 15,
        "body": 13,
    },
    "borders": {
        "default": border.all(2, "#5d5d5d"),
        "b-btn": Border(bottom=BorderSide(1, color=Colors.BLACK87))
    },
    "m-i-pokemon": {
        "scr-init": margin.only(top=15, left=125/2),
        "scr-inf": margin.only(top=2, left=125/2),
    },
    "sizes-img": {
        "img-pokemon": 130,
        "img-pokemon-inf": 100,
    }
}

MARGIN = {
    "mrg-top": {
        "margin-t-20": 20,
        "margin-t-40": 40,
        "margin-t-60": 60,
        "margin-t-80": 80,
        "margin-t-100": 100,
    },
    "mrg-left": {
        "margin-l-20": 20,
        "margin-l-40": 40,
        "margin-l-60": 60,
        "margin-l-80": 80,
        "margin-l-100": 100,
    },
    "mrg-right": {
        "margin-r-20": 20,
        "margin-r-40": 40,
        "margin-r-60": 60,
        "margin-r-80": 80,
        "margin-r-100": 100,
    },
    "mrg-bottom": {
        "margin-b-20": 20,
        "margin-b-40": 40,
        "margin-b-60": 60,
        "margin-b-80": 80,
        "margin-b-100": 100,
    }
}

TIPO = {
    "grass": "Planta", 
    "bug": "Bicho", 
    "electric": "Electrico", 
    "ground": "Tierra", 
    "psychic": "Psiquico", 
    "dark": "Siniestro",
    "dragon": "Dragon"
}

# Fuentes
FONT = "Tahoma"
FONT_BOLD = "Tahoma Bold"

# Pokemon-limite
TOP_POKEMON = 1025
