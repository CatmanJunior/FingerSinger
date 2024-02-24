import numpy as np

def add_simple_reverb(wave, sample_rate, delay_ms=50, decay=0.5):
    """
    Add a simple reverb effect to a waveform.
    
    Parameters:
    - wave: The input waveform (numpy array).
    - sample_rate: The sampling rate of the waveform.
    - delay_ms: The delay of the echo in milliseconds.
    - decay: The decay factor of the echo.
    
    Returns:
    - The waveform with reverb added.
    """
    delay_samples = int(sample_rate * (delay_ms / 1000.0))
    output = np.copy(wave)
    
    # Apply the delay and decay
    for i in range(delay_samples, len(wave)):
        output[i] += decay * wave[i - delay_samples]
    
    # Normalize to prevent clipping
    max_amplitude = np.max(np.abs(output))
    if max_amplitude > 1.0:
        output /= max_amplitude
    
    return output

def apply_vibrato_to_waveform(y, fs, vibrato_rate, vibrato_depth):
    """
    Apply a vibrato effect to a waveform.

    Parameters:
    - y: The input waveform (numpy array).
    - fs: The sampling frequency of the waveform.
    - vibrato_rate: The rate of vibrato oscillations per second.
    - vibrato_depth: The depth of the vibrato effect in samples.

    Returns:
    - y_vibrato: The waveform with the vibrato effect applied.
    """
    # Time array
    t = np.arange(len(y))

    # Vibrato effect as a sine wave modulation of the time indices
    vibrato = vibrato_depth * np.sin(2 * np.pi * vibrato_rate * t / fs)

    # Interpolating the original waveform at new time indices with vibrato effect
    t_new = t + vibrato
    t_new = np.clip(t_new, 0, len(y) - 1)  # Ensure new indices are within bounds

    # Interpolate the waveform to apply the vibrato effect
    y_vibrato = np.interp(t_new, t, y)

    return y_vibrato