from fastapi import APIRouter, UploadFile, File
from backend.services.storage import guardar_archivo

router = APIRouter()

@router.post("/upload/")
async def subir_archivo(file: UploadFile = File(...)):
    path = guardar_archivo(file)
    return {"filename": file.filename, "saved_path": path}
