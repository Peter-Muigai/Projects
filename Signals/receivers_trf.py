from filters import bandpass_filter, lowpass_filter
import numpy as np
from scipy.signal import hilbert



def trf_receiver(x, Fc, B, Fs, mode="AM"):
    rf = bandpass_filter(x, Fc, B, Fs)
    analytic = hilbert(rf)
    if mode == "AM":
        demod = np.abs(rf)  # envelope
    else:
        # FM discriminator
        phase = np.unwrap(np.angle(analytic))
        demod = np.diff(phase) * Fs / (2 * np.pi)

    audio = lowpass_filter(demod, B, Fs)
    return audio
