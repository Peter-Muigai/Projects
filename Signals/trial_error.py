import matplotlib.pyplot as plt
from config import *
from baseband import *
from modulation import *
from channel import *
from receivers_trf import trf_receiver
from receivers_superhet import superhet_receiver
from analysis import run_system
import numpy as np

from scipy.signal import butter, lfilter

from scipy.signal import hilbert

def fm_demodulate(x, Fs):
    """
    FM demodulation using phase differentiation of analytic signal.
    """
    # Create analytic signal
    analytic = hilbert(x)
    # Instantaneous phase
    phase = np.unwrap(np.angle(analytic))
    # Differentiate phase -> frequency deviation
    demod = np.diff(phase) * (Fs / (2*np.pi))
    # Pad to same length
    demod = np.concatenate(([demod[0]], demod))
    return demod

def am_demodulate(x):
    """
    AM demodulation using envelope detection.
    """
    analytic = hilbert(x)
    envelope = np.abs(analytic)
    return envelope


def bandpass_filter(x, f_low, f_high, Fs, order=5):
    nyq = 0.5 * Fs
    low = f_low / nyq
    high = f_high / nyq
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, x)

# ---------------------------------------------------------
# BASEBAND + MODULATION
# ---------------------------------------------------------

t, msg = generate_message(Fs)
msg = lowpass_filter(msg, B, Fs)

am = am_modulate(msg, Fc, Fs)
nbfm = nbfm_modulate(msg, Fc, Fs, beta_nbfm)
wbfm = wbfm_armstrong(msg, Fc, Fs, beta_wbfm)

# ---------------------------------------------------------
# FREQUENCY PLOT FUNCTION
# ---------------------------------------------------------

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

# ---------------------------------------------------------
# TIME & FREQUENCY DOMAIN PLOTS
# ---------------------------------------------------------

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

plot_frequency(msg, Fs, "Message Spectrum")
plot_frequency(am, Fs, "AM Spectrum")
plot_frequency(nbfm, Fs, "NBFM Spectrum")
plot_frequency(wbfm, Fs, "WBFM Spectrum")

# ---------------------------------------------------------
# RECEIVER TEST
# ---------------------------------------------------------

rx = awgn(wbfm, snr_db=5)
audio_trf = trf_receiver(rx, Fc, B, Fs, mode="FM")
audio_superhet = superhet_receiver(rx, Fc, IF, B, Fs, mode="FM")

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

# ---------------------------------------------------------
# EXTRA VISUALIZATION FOR ONE TEST CASE (Superhet)
# ---------------------------------------------------------

# --- Bandpass Filter stage ---
bpf_out = bandpass_filter(rx, Fc-B/2, Fc+B/2, Fs)
plt.figure(figsize=(10,4))
plt.plot(bpf_out[:1000])
plt.title("After Bandpass Filter (RF stage)")
plt.grid(True)
plt.show()
plot_frequency(bpf_out, Fs, "Spectrum After BPF")

# --- Mixing stage (down-conversion) ---
lo = np.cos(2*np.pi*(Fc-IF)*t)   # Local oscillator
mixed = bpf_out * lo
plt.figure(figsize=(10,4))
plt.plot(mixed[:1000])
plt.title("After Mixing (Down-conversion to IF)")
plt.grid(True)
plt.show()
plot_frequency(mixed, Fs, "Spectrum After Mixing (Down-conversion)")

# --- IF Filter stage ---
if_out = bandpass_filter(mixed, IF-B/2, IF+B/2, Fs)
plt.figure(figsize=(10,4))
plt.plot(if_out[:1000])
plt.title("After IF Filter")
plt.grid(True)
plt.show()
plot_frequency(if_out, Fs, "Spectrum After IF Filter")

# --- Demodulation stage ---
demod_out = fm_demodulate(if_out, Fs)
demod_out = am_demodulate(if_out)

plt.figure(figsize=(10,4))
plt.plot(demod_out[:1000])
plt.title("After Demodulation (Recovered Audio)")
plt.grid(True)
plt.show()
plot_frequency(demod_out, Fs, "Spectrum of Demodulated Audio")

# Document IF filter parameters
print(f"IF Filter Center Frequency: {IF} Hz")
print(f"IF Bandwidth: {B} Hz")
print(f"Image Frequency Rejected: {Fc + IF} Hz")

# ---------------------------------------------------------
# PHASE 4 — SNR SWEEP
# ---------------------------------------------------------

snr_range = np.arange(-5, 31, 5)

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

# ---------------------------------------------------------
# SEPARATE PLOTS FOR EACH SYSTEM
# ---------------------------------------------------------

for key, values in results.items():
    plt.figure(figsize=(8, 5))
    plt.plot(snr_range, values, marker='o')
    plt.title(f"Output SNR vs Input SNR — {key.replace('_', ' ')}")
    plt.xlabel("Input SNR (dB)")
    plt.ylabel("Output SNR (dB)")
    plt.grid(True)

    # --- FM Threshold Detection (WBFM only) ---
    if "WBFM" in key:
        diffs = np.diff(values)
        threshold_index = np.argmax(diffs)
        threshold_snr = snr_range[threshold_index]

        plt.axvline(threshold_snr, color='red', linestyle='--',
                    label=f"FM Threshold ≈ {threshold_snr} dB")
        plt.legend()

    plt.tight_layout()
    plt.show()
