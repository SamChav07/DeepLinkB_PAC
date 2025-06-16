import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded_files")
os.makedirs(UPLOAD_DIR, exist_ok=True)