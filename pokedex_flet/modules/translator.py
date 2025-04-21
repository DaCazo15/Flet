from style.constants import *
from googletrans import Translator

class Traducir:
    def __init__(self):
        self.translator = Translator()
        self.dic_tipo = TIPO

    async def traductor(self, texto):
        try:
            if texto in self.dic_tipo:
                return self.dic_tipo[texto]
            else:
                    translation = self.translator.translate(texto, src='en', dest='es')  
                    return translation.text 
        except Exception as e:
            print(f"Error en la traducción: {e}")
            return texto
