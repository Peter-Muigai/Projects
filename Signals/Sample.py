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
