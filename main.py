# main.py

import os
from preprocessing.pipeline import preprocess_audio
from transcription.whisper_transcribe import transcribe_audio

# --- Paths ---
INPUT_PATH = "audio/raw/sample_call.mp3"
PROCESSED_PATH = "audio/processed/sample_call_clean.wav"
TRANSCRIPT_PATH = "audio/processed/sample_call_transcription.txt"

def save_transcription(text: str, path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"[✔] Transcription saved to: {path}")

if __name__ == "__main__":
    print("\n[1] Preprocessing audio...")
    preprocess_audio(INPUT_PATH, PROCESSED_PATH)

    print("\n[2] Running Whisper transcription...")
    transcription = transcribe_audio(PROCESSED_PATH)

    print("\n[3] Saving transcription to file...")
    save_transcription(transcription, TRANSCRIPT_PATH)

    print("\n✅ Pipeline complete.")
