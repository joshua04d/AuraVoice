import os
import soundfile as sf
from preprocessing.normalize import normalize_audio
from preprocessing.resample import resample_audio
from preprocessing.noise_reduction import reduce_noise

def preprocess_audio(input_path, output_path, temp_path="audio/processed/_temp.wav"):
    """
    Full preprocessing pipeline: Normalize, resample, noise reduce.
    
    Args:
        input_path: Raw input audio
        output_path: Clean output audio
        temp_path: Temp .wav file for intermediate save
    """
    # Step 1: Normalize + convert to mono
    normalize_audio(input_path, temp_path)

    # Step 2: Resample to 16kHz
    y, sr = resample_audio(temp_path, target_sr=16000)

    # Step 3: Noise reduction
    y_denoised = reduce_noise(y, sr)

    # Step 4: Save clean output
    sf.write(output_path, y_denoised, sr)
    os.remove(temp_path)
    print(f"✅ Preprocessed and saved: {output_path}")
