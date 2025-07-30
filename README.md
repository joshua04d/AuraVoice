# AuraVoice 🎙️
AI-powered audio processing and transcription system for insurance call automation.

---

## 🔧 Current Capabilities

- ✅ Normalize audio volume
- ✅ Convert to mono and resample to 16kHz
- ✅ Apply noise reduction to improve transcription quality

---

## 📂 Folder Structure

AuraVoice/
├── audio/
│ ├── raw/ # Original audio files (.mp3/.wav)
│ └── processed/ # Cleaned audio for transcription
├── preprocessing/
│ ├── normalize.py
│ ├── resample.py
│ ├── noise_reduction.py
│ └── pipeline.py
├── transcription/
│ └── whisper_transcribe.py # (To be implemented)
├── main.py
├── requirements.txt
└── README.md


---

## ▶️ How to Run Preprocessing

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Place your input file in `audio/raw/`  
   Example: `audio/raw/sample_call.mp3`

3. Run the pipeline:
    ```python
    from preprocessing.pipeline import preprocess_audio

    preprocess_audio(
        input_path="audio/raw/sample_call.mp3",
        output_path="audio/processed/clean_call.wav"
    )
    ```

---

## 📌 Next Steps

- Add Whisper-based transcription
- Detect sentiment & intent
- Summarize conversation & update CRM
