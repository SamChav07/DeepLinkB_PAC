from playwright.sync_api import sync_playwright
from backend.config import Config

class BibliotecaScraper:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()
    
    def iniciar_sesion(self):
        self.page.goto(Config.URL_BIBLIOTECA)
        self.page.fill('input[name="user"]', Config.USUARIO)
        self.page.fill('input[name="pwd"]', Config.PASSWORD)
        self.page.click('.entrar')
        self.page.wait_for_timeout(2000)

    def buscar_libro(self, referencia: str, categoria: str = "General") -> dict:
        catalogos = Config.CATEGORIA_OPCIONES_WEB.get(categoria, Config.CATEGORIA_OPCIONES_WEB["General"])

        for nombre, xpath in catalogos.items():
            try:
                with self.page.expect_popup() as popup_info:
                    self.page.click(f"xpath={xpath}")
                popup = popup_info.value
                popup.wait_for_load_state()
                popup.wait_for_timeout(3000)

                try:
                    popup.fill('input[name="search"]', referencia)
                    popup.press('input[name="search"]', "Enter")
                    popup.wait_for_timeout(3000)

                    if "result" in popup.content():  # <-- AJUSTAR esto según resultado real
                        return {
                            "encontrado": True,
                            "fuente": nombre,
                            "url": popup.url
                        }

                except:
                    pass
                popup.close()
            except:
                continue

        return {
            "encontrado": False,
            "fuente": None,
            "url": None
        }

    def cerrar(self):
        self.browser.close()
        self.playwright.stop()