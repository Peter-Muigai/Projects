import numpy as np

def awgn(x, snr_db):
    x = x / np.sqrt(np.mean(x**2))  # normalize
    Pn = 1 / (10**(snr_db/10))
    noise = np.sqrt(Pn) * np.random.randn(len(x))
    return x + noise
