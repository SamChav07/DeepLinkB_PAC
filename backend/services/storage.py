import shutil
from fastapi import UploadFile
from backend.config import Config
import os

def guardar_archivo(file: UploadFile) -> str:
    destino = os.path.join(Config.UPLOAD_DIR, file.filename)
    with open(destino, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return destino