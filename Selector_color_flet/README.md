# 🎨 Selector de Colores RGB/HEX/HSL - Flet
<div style="display: flex; gap: 10px; margin: 15px 0;"> <img src="https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Flet-0.1.0-00B0FF?logo=flutter&logoColor=white" alt="Flet"> <img src="https://img.shields.io/badge/Platforms-Desktop|Mobile|Web-4BC0C0" alt="Multiplataforma"> </div>
Un selector de colores interactivo y moderno creado con [Flet (Python)] que te permite:


* Ajustar colores mediante **sliders RGB**
* Introducir valores manualmente en **RGB (0-255)**
* Usar códigos **HEX (#RRGGBB)**
* Visualizar equivalentes en **HSL**
* Ver el color seleccionado en tiempo real
* Diseño responsive para móvil y escritorio

## ✨ Características Principales

* **Interfaz intuitiva** con vista previa del color
* **Conversión automática** entre RGB, HEX y HSL
* **Color de texto adaptable** (blanco/negro) para mejor contraste
* **Diseño oscuro/ligero** que se adapta al color seleccionado
* **Validación de entrada** para todos los formatos
* **Totalmente responsive** (funciona en web, móvil y escritorio)

## 🎯 Funcionalidades Técnicas

```
# Ejemplo de código clave
def update_color(self, e: ControlEvent):
    if e.control == self.r_slider:
        self.r = int(e.control.value)
        self.r_text.value = str(self.r)
    # ... actualización similar para G y B
    self._update_display()  # Actualiza toda la UI
```

## 🌈 Por qué este proyecto?

* Perfecto para diseñadores y desarrolladores
* Demuestra el poder de Flet para aplicaciones GUI
* Código bien estructurado y documentado
* Fácil de extender (¡PRs son bienvenidos!)

## 🚀 Roadmap

* Añadir selector de color circular (HSV)
* Guardar colores favoritos
* Exportar paletas de colores
* Modo daltonismo

## 🤝 Contribuir

¡Todas las contribuciones son bienvenidas! Por favor:

1. Haz fork del proyecto
2. Crea tu branch (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Haz push al branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
