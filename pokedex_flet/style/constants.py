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
        "clr-btn-back": Colors.WHITE,

        "clr-txt-primary": Colors.GREY_800,
        "clr-txt-secondary": Colors.GREY_300,
        "clr-txt-tertiary": Colors.GREY_500,
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
    },
}

# Fuentes
FONT = "Tahoma"
FONT_BOLD = "Tahoma Bold"

# Pokemon-limite
TOP_POKEMON = 1025
