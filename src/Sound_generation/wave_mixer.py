import numpy as np

def mix_waves(wave1, wave2, level1=0.5, level2=0.5):
    """
    Mix two waveforms with specified levels.
    
    Parameters:
    - wave1: The first waveform as a numpy array.
    - wave2: The second waveform as a numpy array, should have the same length as wave1.
    - level1: The relative level of the first waveform, as a float. Default is 0.5.
    - level2: The relative level of the second waveform, as a float. Default is 0.5.
    
    Returns:
    - mixed_wave: The mixed waveform as a numpy array.
    """
    # Ensure the waves are of the same length
    if len(wave1) != len(wave2):
        raise ValueError("Waveforms must be of the same length to mix")
    
    # Adjust the amplitude of each wave based on the specified levels
    adjusted_wave1 = wave1 * level1
    adjusted_wave2 = wave2 * level2
    
    # Mix the waves
    mixed_wave = adjusted_wave1 + adjusted_wave2
    
    # Normalize mixed_wave to prevent clipping
    max_amplitude = np.max(np.abs(mixed_wave))
    if max_amplitude > 1.0:
        mixed_wave /= max_amplitude
    
    return mixed_wave

import numpy as np

def mix_multiple_waves(waves, levels=None):
    """
    Mix multiple waveforms with specified levels without clipping.
    
    Parameters:
    - waves: A list of waveforms, each as a numpy array of the same length.
    - levels: A list of relative levels for each waveform, as floats. 
              If None, all waveforms are mixed at equal levels.
    
    Returns:
    - mixed_wave: The mixed waveform as a numpy array.
    """
    # Validate input
    if not waves:
        raise ValueError("At least one waveform is required")
    
    if levels is None:
        levels = [1.0 / len(waves)] * len(waves)  # Equal level if not specified
    elif len(waves) != len(levels):
        raise ValueError("Each waveform must have a corresponding level")
    
    # Initialize mixed_wave with zeros of the same length as the first waveform
    mixed_wave = np.zeros_like(waves[0])
    
    # Mix the waves
    for wave, level in zip(waves, levels):
        if len(wave) != len(mixed_wave):
            raise ValueError("All waveforms must be of the same length")
        mixed_wave += wave * level
    
    # Normalize mixed_wave to prevent clipping
    max_amplitude = np.max(np.abs(mixed_wave))
    if max_amplitude > 1.0:
        mixed_wave /= max_amplitude
    
    return mixed_wave
