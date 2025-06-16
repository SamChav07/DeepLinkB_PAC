import os
import re
import pdfplumber
from docx import Document
from backend.config import Config

# === Autor ===
def extraer_autor(texto: str):
    patrones = [
        re.compile(r"(Nombre del profesor|Docente|Profesor|Autor):\s*(.+)", re.I),
        re.compile(r"(Nombre del profesor|Docente|Profesor|Autor)\s+(.+)", re.I)
    ]
    for patron in patrones:
        match = patron.search(texto)
        if match:
            return match.group(2).strip()
    return "Desconocido"

# === Facultad ===
def extraer_unidad_academica(texto: str):
    patrones = [
        re.compile(r"(Facultad|Unidad académica|Administrada por|Departamento):\s*(.+)", re.I),
        re.compile(r"(Facultad|Unidad académica|Administrada por|Departamento)\s+(.+)", re.I)
    ]
    for patron in patrones:
        match = patron.search(texto)
        if match:
            return match.group(2).strip()

    siglas = re.findall(r"\b(FIA|FCAE|FCJHRI|FCM|FMDCC|FODO|LANGUAGE CENTER)\b", texto.upper())
    return siglas[0] if siglas else "Desconocida"

def clasificar_categoria(unidad):
    unidad = unidad.lower()
    for sigla, categoria in Config.MAPA_FACULTADES.items():
        if sigla in unidad:
            return categoria
    return "General"

# === Referencias ===
def extraer_referencias(texto: str):
    lineas = texto.splitlines()
    inicio = next((i for i, l in enumerate(lineas)
                   if any(k in l.lower() for k in ["bibliografía", "referencias", "references", "works cited"])), -1)
    if inicio == -1:
        return []

    refs, buffer = [], ""
    encabezados = ["obligatorias", "optativas", "complementarias"]

    for linea in lineas[inicio + 1:]:
        linea = linea.strip()
        if not linea or (any(p in linea.lower() for p in encabezados) and len(linea.split()) <= 3):
            continue

        nueva_ref = re.match(r".+\(\d{4}\)", linea) or re.match(r".+\(n\.d\.\)", linea) or \
                    (buffer.endswith(".") and re.match(r"^[A-ZÁÉÍÓÚÑ]", linea))

        if nueva_ref:
            if buffer:
                refs.append(buffer.strip())
            buffer = linea
        else:
            buffer += " " + linea

    if buffer:
        refs.append(buffer.strip())

    refs = [re.sub(r"\b[a-d]?\)?\s*(Obligatorias|Optativas|Complementarias)\b[\.:]?", "", r, flags=re.I).strip()
            for r in refs]
    return refs

# === Procesar archivo ===
def procesar_archivo(path: str):
    texto = ""
    if path.endswith(".pdf"):
        with pdfplumber.open(path) as pdf:
            texto = "\n".join([p.extract_text() or "" for p in pdf.pages])
    elif path.endswith(".docx"):
        doc = Document(path)
        texto = "\n".join([p.text for p in doc.paragraphs])
    else:
        return {"error": "Formato no compatible"}

    autor = extraer_autor(texto)
    unidad = extraer_unidad_academica(texto)
    categoria = clasificar_categoria(unidad)
    referencias = extraer_referencias(texto)

    return {
        "nombre_archivo": os.path.basename(path),
        "autor": autor,
        "unidad_academica": unidad,
        "categoria": categoria,
        "referencias": referencias
    }