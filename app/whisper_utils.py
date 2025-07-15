import whisper
import tempfile
import ffmpeg

model = whisper.load_model("medium")

def convert_to_wav(input_path: str) -> str:
    output_path = tempfile.mktemp(suffix=".wav")
    ffmpeg.input(input_path).output(output_path).run(overwrite_output=True, quiet=True)
    return output_path

def transcribe_audio(file_path: str) -> dict:
    if not file_path.endswith(".wav"):
        file_path = convert_to_wav(file_path)

    # Solo transcribe, sin traducir, sin separar
    result = model.transcribe(file_path, task="transcribe", word_timestamps=True)

    return {
        "full_transcription": result["text"].strip(),
        "segments": result["segments"]  # Esto lo usará el frontend para dividir como quiera
    }
