import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

def generate_cat_sound(filename="cat_sound.wav", duration=2, fs=44100):
    """
    Generate a sound wave that mimics a cat's meow.

    Parameters:
    - filename: Name of the file to save the sound.
    - duration: Duration of the sound in seconds.
    - fs: Sampling frequency.
    """
    # Time array
    t = np.linspace(0, duration, int(fs * duration), False)

    # Frequency modulation to mimic a meow (starting high, going low)
    freq_modulation = 1000 * np.sin(2 * np.pi * 0.5 * t) + 1000  # Modulate around 1000 Hz

    # Generate base sound with frequency modulation
    y = np.sin(2 * np.pi * freq_modulation * t)

    # Add some noise to make it more realistic
    y += np.random.normal(0, 0.1, y.shape)

    # Normalize to 16-bit range
    y = np.int16(y / np.max(np.abs(y)) * 32767)

    # Save to WAV file
    write(filename, fs, y)

    return filename


def generate_bird_sound(filename="bird_sound.wav", duration=2, fs=44100):
    """
    Generate a sound wave that mimics a bird call.

    Parameters:
    - filename: Name of the file to save the sound.
    - duration: Duration of the sound in seconds.
    - fs: Sampling frequency.
    """
    t = np.linspace(0, duration, int(fs * duration), False)

    # Simple bird call characteristics
    base_freq = 880  # Base frequency for the bird call
    vibrato_freq = 2  # Frequency of the vibrato modulation
    vibrato_magnitude = 10  # Magnitude of frequency modulation for vibrato effect

    # Generate vibrato effect
    modulated_freq = base_freq + vibrato_magnitude * np.sin(2 * np.pi * vibrato_freq * t)

    # Generate the bird call sound with vibrato
    y = np.sin(2 * np.pi * modulated_freq * t)

    # Normalize to 16-bit range
    y = np.int16(y / np.max(np.abs(y)) * 32767)

    # Save to WAV file
    write(filename, fs, y)

    return filename

# Generate and save the bird sound
generate_bird_sound()


