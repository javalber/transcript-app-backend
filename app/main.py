from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
from .whisper_utils import transcribe_audio
from .file_utils import save_temp_file, cleanup_temp_file


app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Validar extensión
    if not file.filename.endswith((".mp3", ".mp4")):
        raise HTTPException(status_code=400, detail="Solo se aceptan archivos .mp3 o .mp4")

    # Guardar archivo temporal
    temp_path = save_temp_file(file)

    try:
        # Transcribir audio
        result = transcribe_audio(temp_path)
        return JSONResponse(content=result)

    finally:
        # Limpiar archivo temporal
        cleanup_temp_file(temp_path)



