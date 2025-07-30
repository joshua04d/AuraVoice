import noisereduce as nr

def reduce_noise(y, sr):
    """
    Apply noise reduction using spectral gating.
    
    Args:
        y: Audio array
        sr: Sample rate

    Returns:
        Denoised audio array
    """
    reduced = nr.reduce_noise(y=y, sr=sr)
    return reduced
