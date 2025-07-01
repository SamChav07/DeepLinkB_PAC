from fastapi import APIRouter
import os
from backend.config import Config
from backend.services.processor import procesar_archivo
from backend.services.scraper import BibliotecaScraper
from backend.services.sheets import conectar_hoja, agregar_filas, actualizar_resultados_sheet

router = APIRouter()

@router.get("/procesar-pendientes/")
async def procesar_referencias_faltantes():
    worksheet = conectar_hoja()
    scraper = BibliotecaScraper()
    await scraper.iniciar()
    await scraper.iniciar_sesion()

    await actualizar_resultados_sheet(worksheet, scraper)

    await scraper.cerrar()
    return {"message": "Referencias pendientes procesadas y actualizadas"}