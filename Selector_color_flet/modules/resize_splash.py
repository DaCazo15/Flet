from PIL import Image
import os

# Configuración
base_image = "assets/splash.png"
output_dir = "build/flutter/android/app/src/main/res"
sizes = {
    "drawable-hdpi": (480, 800),
    "drawable-xhdpi": (720, 1280),
    "drawable-xxhdpi": (1080, 1920)
}

# Crear carpetas
os.makedirs(output_dir, exist_ok=True)
for folder in sizes.keys():
    os.makedirs(f"{output_dir}/{folder}", exist_ok=True)

# Redimensionar y guardar
img = Image.open(base_image)
for folder, (width, height) in sizes.items():
    resized_img = img.resize((width, height), Image.LANCZOS)
    resized_img.save(f"{output_dir}/{folder}/splash.png")
    print(f"✅ Generado: {output_dir}/{folder}/splash.png ({width}x{height})")