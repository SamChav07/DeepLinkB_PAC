from fastapi import APIRouter
import os
from backend.config import Config
from backend.services.processor import procesar_archivo
from backend.services.scraper import BibliotecaScraper
from backend.services.sheets import conectar_hoja, agregar_filas

router = APIRouter()

@router.get("/procesar-todo/")
def procesar_todo():
    archivos = [f for f in os.listdir(Config.UPLOAD_DIR) if f.endswith((".pdf", ".docx"))]
    scraper = BibliotecaScraper()
    scraper.iniciar_sesion()

    worksheet = conectar_hoja("BiblioPDFs 📚")
    resultados = []

    for archivo in archivos:
        datos = procesar_archivo(os.path.join(Config.UPLOAD_DIR, archivo))

        for ref in datos["referencias"]:
            if not ref.strip():
                continue

            resultado = scraper.buscar_libro(ref, datos["categoria"])
            fila = [
                datos["nombre_archivo"],
                datos["autor"],
                datos["unidad_academica"],
                datos["categoria"],
                ref,
                "Disponible" if resultado["encontrado"] else "No disponible",
                resultado["fuente"] or "",
                resultado["url"] or ""
            ]
            agregar_filas(worksheet, [fila])
            resultados.append(fila)

    scraper.cerrar()
    return {"procesados": len(resultados), "resultados": resultados}