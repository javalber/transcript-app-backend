import tempfile
import shutil
import os
from fastapi import UploadFile

def save_temp_file(upload_file: UploadFile) -> str:
    # Crear archivo temporal
    suffix = os.path.splitext(upload_file.filename)[-1]  # .mp3 o .mp4
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    with temp_file as f:
        shutil.copyfileobj(upload_file.file, f)
    return temp_file.name

def cleanup_temp_file(path: str):
    try:
        os.remove(path)
    except Exception as e:
        print(f"Error al eliminar el archivo temporal: {e}")
