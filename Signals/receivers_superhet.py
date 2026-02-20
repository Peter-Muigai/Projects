from filters import bandpass_filter, lowpass_filter
import numpy as np
from scipy.signal import hilbert

def superhet_receiver(x, Fc, IF, B, Fs, mode="AM"):
    t = np.arange(len(x)) / Fs

    # Local oscillator for down conversion
    lo = np.cos(2*np.pi*(Fc - IF)*t)
    mixed = x * lo

    # IF bandpass filter
    if_stage = bandpass_filter(mixed, IF, B, Fs)

    if mode == "AM":
        demod = np.abs(if_stage)

    else:  # FM demodulation
        analytic = hilbert(if_stage)
        phase = np.unwrap(np.angle(analytic))
        demod = np.diff(phase) * Fs / (2*np.pi)

    audio = lowpass_filter(demod, B, Fs)
    return audio