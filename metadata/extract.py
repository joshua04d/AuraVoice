# metadata/extract.py

from pydub import AudioSegment
import wave

def extract_metadata(audio_path):
    audio = AudioSegment.from_file(audio_path)
    duration_sec = len(audio) / 1000
    channels = audio.channels
    sample_rate = audio.frame_rate
    return {
        "filename": audio_path,
        "duration_sec": duration_sec,
        "channels": channels,
        "sample_rate": sample_rate
    }
