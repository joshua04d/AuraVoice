import os
from preprocessing.pipeline import preprocess_audio
from transcription.whisper_transcribe import transcribe_audio
from metadata.extract import extract_metadata
from analytics.analyze import analyze_transcript
from report.generate_csv import write_report


RAW_DIR = "audio/raw"
PROCESSED_DIR = "audio/processed"

for filename in os.listdir(RAW_DIR):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        raw_path = os.path.join(RAW_DIR, filename)
        base_name = os.path.splitext(filename)[0]
        cleaned_path = os.path.join(PROCESSED_DIR, base_name + "_clean.wav")
        transcript_path = os.path.join(PROCESSED_DIR, base_name + "_transcription.txt")

        print(f"\n[1] Preprocessing {filename}...")
        preprocess_audio(raw_path, cleaned_path)

        print(f"[2] Transcribing {filename}...")
        transcript = transcribe_audio(cleaned_path)

        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript)

        print(f"[3] Extracting metadata for {filename}...")
        meta = extract_metadata(cleaned_path)
        print(meta)

        print(f"[4] Analyzing transcript for {filename}...")
        stats = analyze_transcript(transcript_path)
        print(stats)
        
        report_data = []

for filename in os.listdir(RAW_DIR):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        raw_path = os.path.join(RAW_DIR, filename)
        base_name = os.path.splitext(filename)[0]
        cleaned_path = os.path.join(PROCESSED_DIR, base_name + "_clean.wav")
        transcript_path = os.path.join(PROCESSED_DIR, base_name + "_transcription.txt")

        print(f"\n[1] Preprocessing {filename}...")
        preprocess_audio(raw_path, cleaned_path)

        print(f"[2] Transcribing {filename}...")
        transcript = transcribe_audio(cleaned_path)

        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript)

        print(f"[3] Extracting metadata for {filename}...")
        meta = extract_metadata(cleaned_path)

        print(f"[4] Analyzing transcript for {filename}...")
        stats = analyze_transcript(transcript_path)

        # Combine all data for this file
        report_data.append({
            "filename": filename,
            **meta,
            **stats
        })

# After all files
write_report(report_data, "reports/audio_report.csv")
