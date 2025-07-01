import gspread
from google.oauth2.service_account import Credentials
from backend.config import Config
import socket
import os

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def verificar_conexion(host="sheets.googleapis.com"):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

def conectar_hoja():
    if not verificar_conexion():
        raise ConnectionError("No se puede resolver el dominio sheets.googleapis.com. Revisa tu conexión a internet o DNS.")

    ruta_credenciales = os.getenv("GOOGLE_CREDENTIALS_PATH", "google-credentials.json")

    creds = Credentials.from_service_account_file(ruta_credenciales, scopes=SCOPES)
    cliente = gspread.authorize(creds)

    nombre_hoja = Config.NOMBRE_GOOGLE_SHEET

    try:
        hoja = cliente.open(nombre_hoja)
    except gspread.SpreadsheetNotFound:
        hoja = cliente.create(nombre_hoja)

    try:
        worksheet = hoja.worksheet("Bibliografia")
    except gspread.exceptions.WorksheetNotFound:
        worksheet = hoja.add_worksheet(title="Bibliografia", rows="1000", cols="10")
        if hoja.sheet1.title != "Bibliografia":
            hoja.del_worksheet(hoja.sheet1)

    return worksheet

def agregar_filas(worksheet, filas: list):
    headers = ["Archivo", "Autor", "Facultad", "Categoría", "Referencia", "Encontrado", "Fuente", "URL"]
    if worksheet.cell(1, 1).value != "Archivo":
        worksheet.insert_row(headers, 1)

    for fila in filas:
        worksheet.append_row(fila)

async def actualizar_resultados_sheet(worksheet, scraper):
    import time
    import asyncio  # <-- nuevo import

    records = worksheet.get_all_values()
    headers = records[0]
    rows = records[1:]

    col_archivo = headers.index("Archivo") + 1
    col_autor = headers.index("Autor") + 1
    col_ref = headers.index("Referencia") + 1

    col_encontrado = headers.index("Encontrado") + 1 if "Encontrado" in headers else None
    col_fuente = headers.index("Fuente") + 1 if "Fuente" in headers else None
    col_url = headers.index("URL") + 1 if "URL" in headers else None

    if col_encontrado is None or col_fuente is None or col_url is None:
        worksheet.update("F1", [["Encontrado", "Fuente", "URL"]])
        col_encontrado, col_fuente, col_url = 6, 7, 8

    for i, fila in enumerate(rows, start=2):
        if all(len(fila) >= idx and not fila[idx - 1].strip() for idx in [col_encontrado, col_fuente, col_url]):
            referencia = fila[col_ref - 1]
            categoria = fila[headers.index("Categoría")]
            resultado = {
                "Encontrado": "falla con el algoritmo",
                "Fuente": "",
                "URL": ""
            }
            try:
                busqueda = await scraper.buscar_libro(referencia, categoria)
                resultado["Encontrado"] = "Disponible" if busqueda["encontrado"] else "No encontrado"
                resultado["Fuente"] = busqueda["fuente"]
                resultado["URL"] = busqueda["url"]
            except Exception:
                pass

            worksheet.update(f"F{i}:H{i}", [[
                resultado["Encontrado"],
                resultado["Fuente"],
                resultado["URL"]
            ]])
            await asyncio.sleep(1)  # respetar límites de API