import aiohttp, asyncio

class Peticiones:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def peticion(self, url): 
        try:
            async with self.session.get(url) as response:
                response.raise_for_status()
                return await response.json()    
        except Exception as e:
            print(f"Error en la petición: {e}")
            return None
        