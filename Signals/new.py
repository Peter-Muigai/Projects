import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, hilbert

fs = 200000        # Sampling rate (200 kHz)
t = np.arange(0, 0.05, 1/fs)

# ----------------------------------------------------------
# 1. BASEBAND SIGNAL (m(t))
# ----------------------------------------------------------
fm1, fm2 = 400, 800      # Two-tone baseband example
m = 0.6*np.sin(2*np.pi*fm1*t) + 0.4*np.sin(2*np.pi*fm2*t)

# LPF to restrict baseband bandwidth
def butter_lowpass(fc, fs, order=6):
    b, a = butter(order, fc/(fs/2), btype="low")
    return b, a

b, a = butter_lowpass(fc=3000, fs=fs)
m_filt = lfilter(b, a, m)

# ----------------------------------------------------------
# 2. AM MODULATION
# ----------------------------------------------------------
fc = 20000
Ac = 1
AM = Ac * (1 + m_filt) * np.cos(2*np.pi*fc*t)

# ----------------------------------------------------------
# 3. NBFM (β << 1)
# ----------------------------------------------------------
kf_narrow = 50      # small deviation constant
NBFM = np.cos(2*np.pi*fc*t + kf_narrow*np.cumsum(m_filt)/fs)

# ----------------------------------------------------------
# 4. WBFM (β > 5)
# ----------------------------------------------------------
kf_wide = 5000       # large deviation constant (Armstrong method simplified)
WBFM = np.cos(2*np.pi*fc*t + kf_wide*np.cumsum(m_filt)/fs)

# ----------------------------------------------------------
# Plotting
# ----------------------------------------------------------
plt.figure(figsize=(12,10))
plt.subplot(4,1,1); plt.plot(t[:2000], m_filt[:2000]); plt.title("Baseband m(t)")
plt.subplot(4,1,2); plt.plot(t[:2000], AM[:2000]); plt.title("AM Signal")
plt.subplot(4,1,3); plt.plot(t[:2000], NBFM[:2000]); plt.title("NBFM Signal")
plt.subplot(4,1,4); plt.plot(t[:2000], WBFM[:2000]); plt.title("WBFM Signal")
plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, hilbert

fs = 200000        # Sampling rate (200 kHz)
t = np.arange(0, 0.05, 1/fs)

# ----------------------------------------------------------
# 1. BASEBAND SIGNAL (m(t))
# ----------------------------------------------------------
fm1, fm2 = 400, 800      # Two-tone baseband example
m = 0.6*np.sin(2*np.pi*fm1*t) + 0.4*np.sin(2*np.pi*fm2*t)

# LPF to restrict baseband bandwidth
def butter_lowpass(fc, fs, order=6):
    b, a = butter(order, fc/(fs/2), btype="low")
    return b, a

b, a = butter_lowpass(fc=3000, fs=fs)
m_filt = lfilter(b, a, m)

# ----------------------------------------------------------
# 2. AM MODULATION
# ----------------------------------------------------------
fc = 20000
Ac = 1
AM = Ac * (1 + m_filt) * np.cos(2*np.pi*fc*t)

# ----------------------------------------------------------
# 3. NBFM (β << 1)
# ----------------------------------------------------------
kf_narrow = 50      # small deviation constant
NBFM = np.cos(2*np.pi*fc*t + kf_narrow*np.cumsum(m_filt)/fs)

# ----------------------------------------------------------
# 4. WBFM (β > 5)
# ----------------------------------------------------------
kf_wide = 5000       # large deviation constant (Armstrong method simplified)
WBFM = np.cos(2*np.pi*fc*t + kf_wide*np.cumsum(m_filt)/fs)

# ----------------------------------------------------------
# Plotting
# ----------------------------------------------------------
plt.figure(figsize=(12,10))
plt.subplot(4,1,1); plt.plot(t[:2000], m_filt[:2000]); plt.title("Baseband m(t)")
plt.subplot(4,1,2); plt.plot(t[:2000], AM[:2000]); plt.title("AM Signal")
plt.subplot(4,1,3); plt.plot(t[:2000], NBFM[:2000]); plt.title("NBFM Signal")
plt.subplot(4,1,4); plt.plot(t[:2000], WBFM[:2000]); plt.title("WBFM Signal")
plt.tight_layout()
plt.show()

def awgn(signal, SNR_dB):
    Ps = np.mean(signal**2)
    SNR_linear = 10**(SNR_dB/10)
    Pn = Ps/SNR_linear
    noise = np.sqrt(Pn) * np.random.randn(len(signal))
    return signal + noise

def butter_bandpass(f1, f2, fs, order=5):
    b, a = butter(order, [f1/(fs/2), f2/(fs/2)], btype='band')
    return b, a

bTRF, aTRF = butter_bandpass(fc-3000, fc+3000, fs)

def envelope_detector(x):
    analytic = hilbert(x)
    return np.abs(analytic)

def fm_demod(x):
    diff = np.diff(np.unwrap(np.angle(x)))
    return np.concatenate([[0], diff]) * fs/(2*np.pi)

SNRin = 10  # example input SNR
rx = awgn(AM, SNRin)

# TRF bandpass
rx_bpf = lfilter(bTRF, aTRF, rx)

# AM demodulation
demod_am = envelope_detector(rx_bpf)

# LPF to recover audio
demod_am = lfilter(b, a, demod_am)

plt.plot(t[:2000], demod_am[:2000])
plt.title("TRF Output — AM Demodulated")
plt.show()
