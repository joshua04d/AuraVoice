# main.py

import os
from preprocessing.pipeline import preprocess_audio
from transcription.whisper_transcribe import transcribe_audio
from analysis.analyze_transcript import analyze_transcript
from utils.metadata import extract_metadata
from utils.save_utils import save_text, save_json, save_csv

RAW_DIR = "audio/raw"
PROCESSED_DIR = "audio/processed"
REPORTS_DIR = "reports"

def process_batch():
    all_reports = []
    files = sorted([
        f for f in os.listdir(RAW_DIR)
        if f.endswith(".mp3") or f.endswith(".wav")
    ])

    for idx, filename in enumerate(files, start=1):
        call_id = f"call{idx}"
        input_path = os.path.join(RAW_DIR, filename)
        clean_path = os.path.join(PROCESSED_DIR, f"{call_id}_clean.wav")
        transcription_path = os.path.join(PROCESSED_DIR, f"{call_id}_transcription.txt")
        metadata_path = os.path.join(PROCESSED_DIR, f"{call_id}_metadata.json")

        print(f"\n🔄 Processing {filename} as {call_id}")

        # Step 1: Preprocess audio
        preprocess_audio(input_path, clean_path)

        # Step 2: Transcribe
        transcript = transcribe_audio(clean_path)
        save_text(transcript, transcription_path)

        # Step 3: Metadata
        metadata = extract_metadata(clean_path)
        save_json(metadata, metadata_path)

        # Step 4: NLP analysis
        analysis = analyze_transcript(transcript)

        # Collect for CSV report
        row = {
            "call_id": call_id,
            "filename": filename,
            **metadata,
            **analysis
        }
        all_reports.append(row)

    # Step 5: Save batch CSV report
    csv_path = os.path.join(REPORTS_DIR, "batch_analysis_report.csv")
    save_csv(all_reports, csv_path)
    print(f"\n✅ Batch processing complete. Report saved to: {csv_path}")

if __name__ == "__main__":
    process_batch()
