import numpy as np
import matplotlib.pyplot as plt

from config import *
from baseband import *
from modulation import *
from channel import *
from receivers_trf import trf_receiver
from receivers_superhet import superhet_receiver
from analysis import run_system

# ---------------------------------------------------------
# BASEBAND SIGNAL
# ---------------------------------------------------------

t, msg = generate_message(Fs)
msg = lowpass_filter(msg, B, Fs)
msg = msg / np.max(np.abs(msg))   # normalize for fair SNR

# ---------------------------------------------------------
# MODULATION
# ---------------------------------------------------------

am = am_modulate(msg, Fc, Fs)
nbfm = nbfm_modulate(msg, Fc, Fs, beta_nbfm, B)
wbfm = wbfm_armstrong(msg, Fc, Fs, beta_wbfm, B)

# ---------------------------------------------------------
# RF BANDWIDTHS (IMPORTANT)
# ---------------------------------------------------------

BW_AM   = 2 * B
BW_NBFM = 2 * (B + beta_nbfm * B)
BW_WBFM = 2 * beta_wbfm * B

# ---------------------------------------------------------
# FREQUENCY-DOMAIN PLOT FUNCTION
# ---------------------------------------------------------

def plot_frequency(x, Fs, title, fmax=None):
    N = len(x)
    X = np.fft.fftshift(np.fft.fft(x))
    f = np.fft.fftshift(np.fft.fftfreq(N, 1/Fs))

    plt.figure(figsize=(10, 4))
    plt.plot(f, 20*np.log10(np.abs(X) + 1e-12))
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)

    if fmax is not None:
        plt.xlim(-fmax, fmax)

    plt.tight_layout()
    plt.show()

# ---------------------------------------------------------
# TIME & FREQUENCY PLOTS
# ---------------------------------------------------------

plt.figure(figsize=(10, 4))
plt.plot(t, msg)
plt.title("Baseband Message Signal m(t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

plot_frequency(msg, Fs, "Message Spectrum", fmax=2*B)
plot_frequency(am, Fs, "AM Spectrum", fmax=2*Fc)
plot_frequency(nbfm, Fs, "NBFM Spectrum", fmax=2*Fc)
plot_frequency(wbfm, Fs, "WBFM Spectrum", fmax=2*Fc)

# ---------------------------------------------------------
# RECEIVER TEST (WBFM EXAMPLE)
# ---------------------------------------------------------

rx = awgn(wbfm, snr_db=5)

audio_trf = trf_receiver(rx, Fc, BW_WBFM, Fs, mode="FM")
audio_superhet = superhet_receiver(rx, Fc, IF, BW_WBFM, Fs, mode="FM")

plt.figure(figsize=(10, 4))
plt.plot(audio_trf)
plt.title("TRF Receiver Output (WBFM)")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(audio_superhet)
plt.title("Superheterodyne Receiver Output (WBFM)")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# PHASE 4 — OUTPUT SNR SWEEP
# ---------------------------------------------------------

snr_range = np.arange(-10, 31, 5)

results = {
    "AM_TRF": [],
    "AM_SUPER": [],
    "NBFM_TRF": [],
    "NBFM_SUPER": [],
    "WBFM_TRF": [],
    "WBFM_SUPER": []
}

for snr in snr_range:

    # --- AM ---
    results["AM_TRF"].append(
        run_system(am, msg, snr, trf_receiver,
                   Fc=Fc, B=BW_AM, Fs=Fs, mode="AM",
                   B_msg=B)
    )

    results["AM_SUPER"].append(
        run_system(am, msg, snr, superhet_receiver,
                   Fc=Fc, IF=IF, B=BW_AM, Fs=Fs, mode="AM",
                   B_msg=B)
    )

    # --- NBFM ---
    results["NBFM_TRF"].append(
        run_system(nbfm, msg, snr, trf_receiver,
                   Fc=Fc, B=BW_NBFM, Fs=Fs, mode="FM",
                   B_msg=B)
    )

    results["NBFM_SUPER"].append(
        run_system(nbfm, msg, snr, superhet_receiver,
                   Fc=Fc, IF=IF, B=BW_NBFM, Fs=Fs, mode="FM",
                   B_msg=B)
    )

    # --- WBFM ---
    results["WBFM_TRF"].append(
        run_system(wbfm, msg, snr, trf_receiver,
                   Fc=Fc, B=BW_WBFM, Fs=Fs, mode="FM",
                   B_msg=B)
    )

    results["WBFM_SUPER"].append(
        run_system(wbfm, msg, snr, superhet_receiver,
                   Fc=Fc, IF=IF, B=BW_WBFM, Fs=Fs, mode="FM",
                   B_msg=B)
    )

# ---------------------------------------------------------
# OUTPUT SNR PLOTS + FM THRESHOLD
# ---------------------------------------------------------

for key, values in results.items():

    plt.figure(figsize=(8, 5))
    plt.plot(snr_range, values, marker='o')
    plt.title(f"Output SNR vs Input SNR — {key.replace('_', ' ')}")
    plt.xlabel("Input SNR (dB)")
    plt.ylabel("Output SNR (dB)")
    plt.grid(True)

    # --- FM Threshold Detection ---
    if "WBFM" in key:
        slopes = np.gradient(values, snr_range)
        idx = np.argmax(slopes > 1.0)
        threshold_snr = snr_range[idx]

        plt.axvline(threshold_snr, color='red', linestyle='--',
                    label=f"FM Threshold ≈ {threshold_snr} dB")
        plt.legend()

    plt.tight_layout()
    plt.show()
