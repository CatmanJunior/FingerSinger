import matplotlib.pyplot as plt
import numpy as np  

def plot_waveform(wave, sample_rate, title):
    """Plot the waveform."""
    plt.figure(figsize=(10, 4))
    freq = 440
    period = 1 / freq
    two_cycles_time = 2 * period
    samples_for_two_cycles = int(two_cycles_time * sample_rate)
    
    times = np.linspace(0, two_cycles_time, num=samples_for_two_cycles)
    plt.plot(times, wave[:samples_for_two_cycles])
    plt.title(title)
    plt.ylabel("Amplitude")
    plt.xlabel("Time (s)")
    plt.grid(True)
    plt.show()
    
#a function that plots a list of waveforms in one figure
def plot_waveforms(waves, sample_rate, titles):
    """Plot multiple waveforms in one figure."""
    plt.figure(figsize=(10, 6))
    freq = 440
    period = 1 / freq
    two_cycles_time = 2 * period
    samples_for_two_cycles = int(two_cycles_time * sample_rate)
    
    times = np.linspace(0, two_cycles_time, num=samples_for_two_cycles)
    for i, wave in enumerate(waves):
        plt.plot(times, wave[:samples_for_two_cycles], label=titles[i])
    plt.title("Waveforms")
    plt.ylabel("Amplitude")
    plt.xlabel("Time (s)")
    plt.legend()
    plt.grid(True)
    plt.show()