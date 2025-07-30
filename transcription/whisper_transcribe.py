# transcription/whisper_transcribe.py

import whisper
import os

model = whisper.load_model("base")  # You can try "small", "medium", etc. too

def transcribe_audio(file_path: str) -> str:
    print(f"[Whisper] Transcribing: {file_path}")
    result = model.transcribe(file_path)
    return result["text"]
