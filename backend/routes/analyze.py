from fastapi import APIRouter, Query
import os
from backend.services.processor import procesar_archivo
from backend.services.sheets import conectar_hoja, agregar_filas
from backend.config import Config

router = APIRouter()

@router.get("/analizar-todos/")
def analizar_todos():
    archivos = [
        f for f in os.listdir(Config.UPLOAD_DIR)
        if f.endswith(".pdf") or f.endswith(".docx")
    ]

    resultados = []
    filas = []

    for archivo in archivos:
        path = os.path.join(Config.UPLOAD_DIR, archivo)
        resultado = procesar_archivo(path)
        resultados.append(resultado)

        for ref in resultado["referencias"]:
            filas.append([
                resultado["nombre_archivo"],
                resultado["autor"],
                resultado["unidad_academica"],
                resultado["categoria"],
                ref
            ])

    worksheet = conectar_hoja()
    agregar_filas(worksheet, filas)

    return resultados