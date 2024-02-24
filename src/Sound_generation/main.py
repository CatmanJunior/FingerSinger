from pygame import rev
from wave_mixer import mix_waves, mix_multiple_waves
from plot_wavetable import plot_waveform, plot_waveforms
from wave_effects import add_simple_reverb, apply_vibrato_to_waveform
from filters import apply_highpass_filter
import matplotlib.pyplot as plt
from generate_wavetable import *
import sounddevice as sd
from pitch_calculator import *

def play_wave(wave, sample_rate=44100):
    """Play a wave using the default output device."""
    sd.play(wave, sample_rate)
    sd.wait()  # Wait until the wave is played completely
    
if __name__ == "__main__":
    # Parameters for the waveforms
    freq = 440  # Frequency in Hz (A4 note)
    duration = 1  # Duration in seconds
    sample_rate = 44100  # Sampling rate in Hz

    # Generate waveforms
    sine_wave = generate_sine_wave(freq, duration)
    square_wave = generate_square_wave(freq, duration)
    sawtooth_wave = generate_sawtooth_wave(freq, duration)
    noisy_sine_wave = generate_noisy_sine_wave(freq, duration)
    filtered_wave = apply_highpass_filter(noisy_sine_wave, 300, sample_rate)

    mixed_wave = mix_waves(sine_wave, square_wave, level1=0.11, level2=0.54)
    rev_wave = add_simple_reverb(mixed_wave, sample_rate, delay_ms=50, decay=0.5)

    # chord_name = "Adim"
    octave = 5
    # frequencies = get_chord_frequencies(chord_name, octave)
    # mixed_wave = mix_waves(*[generate_square_wave(f, duration) for f in frequencies])
    # play_wave(mixed_wave)
    
    #Create a wave that plays 4 chords in sequence
    chord_names = ["Adim", "D7", "E7", "A7"]
    chord_duration = 1
    mixed_wave = np.array([])
    for chord_name in chord_names:
        frequencies = get_chord_frequencies(chord_name, octave)
        #Create a square wave for each note in the chord
        wave_list = [generate_square_wave(f, chord_duration) for f in frequencies]

        mixed_wave = mix_multiple_waves(wave_list)
        mixed_wave = apply_vibrato_to_waveform(mixed_wave, sample_rate, 5, 100)
        play_wave(mixed_wave)
    
    
    #plot mixed_wave
    plot_waveform(mixed_wave, sample_rate, "Mixed Wave")
    
    # play_wave(sine_wave)
    # play_wave(square_wave)
    # # play_wave(sawtooth_wave)
    # play_wave(noisy_sine_wave)
    # play_wave(filtered_wave)
    # play_wave(mixed_wave)
    # play_wave(rev_wave)
    # Plot waveforms
    
    # plot_waveform(mixed_wave, sample_rate, "Mixed Wave")
    # plot_waveform(rev_wave, sample_rate, "Reverberated Mixed Wave")
    # plot_waveforms([sine_wave, square_wave, sawtooth_wave, noisy_sine_wave, filtered_wave], 
    #             sample_rate,
    #             ["Sine Wave", "Square Wave", "Sawtooth Wave", "Noisy Sine Wave", "Filtered Noisy Sine Wave"])
    
    