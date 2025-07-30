from pydub import AudioSegment

def normalize_audio(input_path: str, output_path: str, target_dBFS: float = -20.0):
    """
    Normalize audio volume and convert to mono WAV.
    
    Args:
        input_path: Path to input audio file (.mp3/.wav)
        output_path: Path to save normalized .wav
        target_dBFS: Target volume level in decibels (default -20.0)
    """
    sound = AudioSegment.from_file(input_path)

    # Convert to mono
    sound = sound.set_channels(1)

    # Normalize volume
    change_in_dBFS = target_dBFS - sound.dBFS
    normalized_sound = sound.apply_gain(change_in_dBFS)

    # Export as WAV for resampling
    normalized_sound.export(output_path, format="wav")
