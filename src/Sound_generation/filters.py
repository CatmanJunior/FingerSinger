import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

def butter_highpass(cutoff, sample_rate, order=5):
    """Design a Butterworth high-pass filter."""
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def apply_highpass_filter(data, cutoff, sample_rate, order=5):
    """Apply a high-pass filter to a dataset."""
    b, a = butter_highpass(cutoff, sample_rate, order=order)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

