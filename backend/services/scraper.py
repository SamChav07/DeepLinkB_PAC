from backend.config import Config
from playwright.sync_api import sync_playwright, TimeoutError

class BibliotecaScraper:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def iniciar_sesion(self):
        self.page.goto(Config.URL_BIBLIOTECA)
        self.page.wait_for_selector("//input[@id='user']", timeout=10000)
        self.page.locator("//input[@id='user']").fill(Config.USUARIO)
        self.page.locator("//input[@id='pwd']").fill(Config.PASSWORD)
        self.page.locator("//form[@id='login']/div/div/div[2]/div[3]/div[2]/a/span/strong").click()
        self.page.wait_for_load_state("networkidle")

    def buscar_libro(self, referencia, categoria):
        catalogos = Config.CATEGORIA_OPCIONES_WEB.get(categoria, Config.CATEGORIA_OPCIONES_WEB["General"])

        for nombre_catalogo, xpath_icono in catalogos.items():
            try:
                self.page.locator(xpath_icono).click()
                self.context.wait_for_event("page")  # Esperar la nueva pestaña
                popup = self.context.pages[-1]
                popup.wait_for_load_state("load", timeout=10000)
            except Exception as e:
                continue

            config_formulario = Config.CATALOGOS_FORMULARIOS.get(nombre_catalogo)
            if not config_formulario:
                continue

            try:
                if "button_for_search_xpath" in config_formulario:
                    popup.locator(config_formulario["button_for_search_xpath"]).click()

                popup.locator(config_formulario["search_input_xpath"]).fill(referencia)

                if config_formulario["submit_action"] == "enter":
                    popup.locator(config_formulario["search_input_xpath"]).press("Enter")
                elif config_formulario["submit_action"] == "click":
                    popup.locator(config_formulario["submit_xpath"]).click()

                popup.wait_for_timeout(5000)  # Dar tiempo a resultados

                # Validar si se encontraron resultados
                encontrado = False
                if "result_xpath" in config_formulario:
                    encontrado = popup.locator(config_formulario["result_xpath"]).count() > 0

                return {
                    "encontrado": encontrado,
                    "fuente": nombre_catalogo,
                    "url": popup.url
                }

            except Exception as e:
                continue

        return {
            "encontrado": False,
            "fuente": "",
            "url": ""
        }

    def cerrar(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()