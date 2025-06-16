import gspread
from google.oauth2.service_account import Credentials

# Conectar a Google Sheets
def conectar_hoja(nombre_hoja: str):
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_file(
        "google-credentials.json",  # ← cambia esto si tu JSON está en otro lugar
        scopes=SCOPES
    )
    cliente = gspread.authorize(creds)

    # Abre una hoja existente o la crea si no existe
    try:
        hoja = cliente.open(nombre_hoja)
    except gspread.SpreadsheetNotFound:
        hoja = cliente.create(nombre_hoja)

    # Abre o crea una hoja de trabajo
    try:
        worksheet = hoja.worksheet("Bibliografia")
    except gspread.exceptions.WorksheetNotFound:
        worksheet = hoja.add_worksheet(title="Bibliografia", rows="1000", cols="10")
        hoja.del_worksheet(hoja.sheet1)

    return worksheet

# Escribe una fila en la hoja
def agregar_filas(worksheet, filas: list):
    headers = ["Archivo", "Autor", "Facultad", "Categoría", "Referencia"]
    if worksheet.row_count == 0 or worksheet.cell(1, 1).value != "Archivo":
        worksheet.append_row(headers)

    for fila in filas:
        worksheet.append_row(fila)