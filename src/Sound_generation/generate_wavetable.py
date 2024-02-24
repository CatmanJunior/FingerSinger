#generate_wavetable.py
import numpy as np
# Common sampling rate for all waveforms
sampling_rate = 44100

def generate_empty_wave(duration):
    return np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

def generate_sine_wave(freq, duration):
    """Generate a sine wave for a given frequency and duration."""
    t = generate_empty_wave(duration)
    wave = np.sin(2 * np.pi * freq * t)
    return wave

def generate_square_wave(freq, duration):
    """Generate a square wave for a given frequency and duration."""
    t = generate_empty_wave(duration)
    wave = np.sign(np.sin(2 * np.pi * freq * t))
    return wave

def generate_sawtooth_wave(freq, duration):
    """Generate a sawtooth wave for a given frequency and duration."""
    t = generate_empty_wave(duration)
    wave = 2 * (t * freq - np.floor(1/2 + t * freq))
    return wave

def generate_noisy_sine_wave(freq, duration, noise_level=0.1):
    """Generate a sine wave with added noise."""
    t = generate_empty_wave(duration)
    clean_wave = np.sin(2 * np.pi * freq * t)
    noise = noise_level * np.random.normal(0, 1, len(t))
    noisy_wave = clean_wave + noise
    return noisy_wave


