import numpy as np
from scipy.signal import butter, lfilter

def lowpass_filter(x, cutoff, Fs, order=5):
    """
    Low-pass filter for audio/baseband recovery.
    cutoff: cutoff frequency in Hz
    Fs: sampling frequency
    """
    nyq = Fs / 2
    b, a = butter(order, cutoff / nyq, btype='low')
    return lfilter(b, a, x)

def bandpass_filter(x, center, bandwidth, Fs, order=5):
    """
    Band-pass filter for RF/IF stages.
    center: center frequency in Hz
    bandwidth: total bandwidth in Hz
    """
    nyq = Fs / 2
    low = max((center - bandwidth / 2) / nyq, 1e-6)
    high = min((center + bandwidth / 2) / nyq, 0.999)
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, x)
