import numpy as np
from scipy.signal import butter, lfilter

def generate_message(Fs, duration=1.0):
    t = np.arange(0, duration, 1/Fs)
    msg = 0.6 * np.sin(2 * np.pi * 1000 * t) + 0.4 * np.sin(2 * np.pi * 4000 * t)
    return t, msg

def lowpass_filter(x, cutoff, Fs, order=5):
    b, a = butter(order, cutoff/(Fs/2), btype='low')
    return lfilter(b, a, x)
