import librosa

def resample_audio(input_path: str, target_sr: int = 16000):
    """
    Load and resample audio to target sample rate.

    Args:
        input_path: Path to .wav file
        target_sr: Target sample rate (default: 16000)

    Returns:
        Tuple (audio_array, sample_rate)
    """
    y, sr = librosa.load(input_path, sr=None)
    if sr != target_sr:
        y = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
    return y, target_sr
