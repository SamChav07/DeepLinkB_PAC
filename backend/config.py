import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded_files")
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Si vas a usar esto después
    MAPA_FACULTADES = {
        "fia": "Ingeniería y Arquitectura",
        "fcae": "Ciencias Administrativas y Económicas",
        "fcjhri": "Ciencias Jurídicas y Relaciones Internacionales",
        "fcm": "Ciencias Médicas",
        "fmdcc": "Marketing, Diseño y Ciencias de la Comunicación",
        "fodo": "Odontología",
        "lenguage center": "Inglés",
    }
