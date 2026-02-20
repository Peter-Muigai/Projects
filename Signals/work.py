import matplotlib.pyplot as plt
from config import *
from baseband import *
from modulation import *
from channel import *
from receivers_trf import trf_receiver
from receivers_superhet import superhet_receiver
from analysis import run_system

t, msg = generate_message(Fs)
msg = lowpass_filter(msg, B, Fs)

am = am_modulate(msg, Fc, Fs)
nbfm = nbfm_modulate(msg, Fc, Fs, beta_nbfm)
wbfm = wbfm_armstrong(msg, Fc, Fs, beta_wbfm)

rx = awgn(wbfm, snr_db=5)

audio_trf = trf_receiver(rx, Fc, B, Fs, mode="FM")
audio_superhet = superhet_receiver(rx, Fc, IF, B, Fs, mode="FM")

def plot_frequency(x, Fs, title):
    N = len(x)
    X = np.fft.fftshift(np.fft.fft(x))
    f = np.fft.fftshift(np.fft.fftfreq(N, 1/Fs))

    plt.figure(figsize=(10,4))
    plt.plot(f, 20*np.log10(np.abs(X) + 1e-12))
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Time-domain plots
plt.figure(figsize=(10,4))
plt.plot(t, msg)
plt.title("Message Signal m(t)")
plt.xlabel("Time (s)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,4))
plt.plot(t, am)
plt.title("AM Signal")
plt.xlabel("Time (s)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Frequency-domain plots
plot_frequency(msg, Fs, "Message Spectrum")
plot_frequency(am, Fs, "AM Spectrum")
plot_frequency(nbfm, Fs, "NBFM Spectrum")
plot_frequency(wbfm, Fs, "WBFM Spectrum")

plt.figure(figsize=(10,4))
plt.plot(audio_trf)
plt.title("TRF Output Audio")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,4))
plt.plot(audio_superhet)
plt.title("Superhet Output Audio")
plt.grid(True)
plt.tight_layout()
plt.show()

snr_range = np.arange(-5, 31, 5)   # -5 dB to +30 dB

results = {
    "AM_TRF": [],
    "AM_SUPER": [],
    "NBFM_TRF": [],
    "NBFM_SUPER": [],
    "WBFM_TRF": [],
    "WBFM_SUPER": []
}

for snr in snr_range:
    # AM
    results["AM_TRF"].append(
        run_system(am, msg, snr, trf_receiver, Fc=Fc, B=B, Fs=Fs, mode="AM")
    )
    results["AM_SUPER"].append(
        run_system(am, msg, snr, superhet_receiver, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="AM")
    )

    # NBFM
    results["NBFM_TRF"].append(
        run_system(nbfm, msg, snr, trf_receiver, Fc=Fc, B=B, Fs=Fs, mode="FM")
    )
    results["NBFM_SUPER"].append(
        run_system(nbfm, msg, snr, superhet_receiver, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="FM")
    )

    # WBFM
    results["WBFM_TRF"].append(
        run_system(wbfm, msg, snr, trf_receiver, Fc=Fc, B=B, Fs=Fs, mode="FM")
    )
    results["WBFM_SUPER"].append(
        run_system(wbfm, msg, snr, superhet_receiver, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="FM")
    )

plt.figure(figsize=(12, 7))

