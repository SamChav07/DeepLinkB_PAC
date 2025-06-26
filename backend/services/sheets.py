# backend/services/sheets.py

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
    headers = ["Archivo", "Autor", "Facultad", "Categoría", "Referencia"]
    if worksheet.cell(1, 1).value != "Archivo":
        worksheet.insert_row(headers, 1)

    for fila in filas:
        worksheet.append_row(fila)