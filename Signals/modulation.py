import numpy as np

def am_modulate(msg, Fc, Fs, mu=0.7):
    t = np.arange(len(msg)) / Fs
    m_norm = msg / np.max(np.abs(msg))
    carrier = np.cos(2*np.pi*Fc*t)
    return (1 + mu * m_norm) * carrier

def nbfm_modulate(msg, Fc, Fs, beta, B):
    t = np.arange(len(msg)) / Fs
    integral = np.cumsum(msg) / Fs
    kf = beta * B
    return np.cos(2*np.pi*Fc*t + 2*np.pi*kf * integral)

def wbfm_armstrong(msg, Fc, Fs, beta, B):
    t = np.arange(len(msg)) / Fs

    # Step 1: Generate NBFM at low carrier
    kf = (beta / 10) * B
    integral = np.cumsum(msg) / Fs
    nbfm = np.cos(2*np.pi*(Fc/10)*t + 2*np.pi*kf * integral)

    # Step 2: Frequency multiplication
    wbfm = np.cos(10 * np.unwrap(np.angle(
        nbfm + 1j*np.sin(2*np.pi*(Fc/10)*t)
    )))

    return wbfm
