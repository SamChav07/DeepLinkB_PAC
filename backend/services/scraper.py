from backend.config import Config
from playwright.async_api import async_playwright, TimeoutError
import os
from backend.services.processor import procesar_archivo
from backend.services.sheets import conectar_hoja, agregar_filas
from fastapi import APIRouter

router = APIRouter()

class BibliotecaScraper:
    async def iniciar(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

    async def iniciar_sesion(self):
        await self.page.goto(Config.URL_BIBLIOTECA)
        await self.page.wait_for_selector("//input[@id='user']", timeout=10000)
        await self.page.locator("//input[@id='user']").fill(Config.USUARIO)
        await self.page.locator("//input[@id='pwd']").fill(Config.PASSWORD)
        await self.page.locator("//form[@id='login']/div/div/div[2]/div[3]/div[2]/a/span/strong").click()
        await self.page.wait_for_load_state("networkidle")

    async def buscar_libro(self, referencia, categoria):
        catalogos = Config.CATEGORIA_OPCIONES_WEB.get(categoria, Config.CATEGORIA_OPCIONES_WEB["General"])

        for nombre_catalogo, xpath_icono in catalogos.items():
            try:
                await self.page.locator(xpath_icono).click()
                popup = await self.context.wait_for_event("page")
                await popup.wait_for_load_state("load", timeout=10000)

                config_formulario = Config.CATALOGOS_FORMULARIOS.get(nombre_catalogo)
                if not config_formulario:
                    await popup.close()
                    continue

                # Si requiere presionar un botón antes de buscar
                if "button_for_search_xpath" in config_formulario:
                    await popup.locator(config_formulario["button_for_search_xpath"]).click()

                await popup.locator(config_formulario["search_input_xpath"]).fill(referencia)

                if config_formulario["submit_action"] == "enter":
                    await popup.locator(config_formulario["search_input_xpath"]).press("Enter")
                elif config_formulario["submit_action"] == "click":
                    await popup.locator(config_formulario["submit_xpath"]).click()

                await popup.wait_for_timeout(5000)

                encontrado = False
                if "result_xpath" in config_formulario:
                    encontrado = await popup.locator(config_formulario["result_xpath"]).count() > 0

                if encontrado:
                    return {
                        "encontrado": True,
                        "fuente": nombre_catalogo,
                        "url": popup.url
                    }

                await popup.close()

            except Exception:
                continue

        # Si ninguna fuente encontró
        return {
            "encontrado": False,
            "fuente": "",
            "url": ""
        }

    async def cerrar(self):
        await self.context.close()
        await self.browser.close()
        await self.playwright.stop()