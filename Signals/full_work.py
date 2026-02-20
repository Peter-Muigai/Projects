import matplotlib.pyplot as plt
import numpy as np

from config import *
from baseband import *
from modulation import *
from channel import *
from receivers_trf import trf_receiver
from receivers_superhet import superhet_receiver
from analysis import run_system

from scipy.signal import butter, lfilter, hilbert

# ---------------------------------------------------------
# FILTERS & DEMODULATORS
# ---------------------------------------------------------

def bandpass_filter(x, f_low, f_high, Fs, order=5):
    nyq = 0.5 * Fs
    low = f_low / nyq
    high = f_high / nyq
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, x)

def fm_demodulate(x, Fs):
    analytic = hilbert(x)
    phase = np.unwrap(np.angle(analytic))
    demod = np.diff(phase) * (Fs / (2*np.pi))
    demod = np.concatenate(([demod[0]], demod))
    return demod

def am_demodulate(x):
    analytic = hilbert(x)
    return np.abs(analytic)

def baseband_recovery(x, Fs, B, mode="FM"):
    if mode == "FM":
        bb = fm_demodulate(x, Fs)
    elif mode == "AM":
        bb = am_demodulate(x)
    else:
        raise ValueError("Invalid mode")

    # Post-detection LPF
    bb = lowpass_filter(bb, B, Fs)

    # DC removal
    bb = bb - np.mean(bb)

    # Normalize
    bb = bb / (np.max(np.abs(bb)) + 1e-12)

    return bb

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
# RECEIVER TEST (REFERENCE RECEIVERS)
# ---------------------------------------------------------

rx = awgn(wbfm, snr_db=5)

audio_trf = trf_receiver(rx, Fc, B, Fs, mode="FM")
audio_superhet = superhet_receiver(rx, Fc, IF, B, Fs, mode="FM")

plt.figure(figsize=(10,4))
plt.plot(audio_trf)
plt.title("TRF Receiver Output Audio")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,4))
plt.plot(audio_superhet)
plt.title("Superhet Receiver Output Audio")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# EXPLICIT SUPERHET BLOCK-BY-BLOCK VISUALIZATION
# ---------------------------------------------------------

# RF Bandpass Filter
rf_out = bandpass_filter(rx, Fc - B/2, Fc + B/2, Fs)
plot_frequency(rf_out, Fs, "After RF Bandpass Filter")

# Mixer (Down-conversion)
lo = np.cos(2 * np.pi * (Fc - IF) * t)
mixed = rf_out * lo
plot_frequency(mixed, Fs, "After Mixing (RF → IF)")

# IF Filter
if_out = bandpass_filter(mixed, IF - B/2, IF + B/2, Fs)
plot_frequency(if_out, Fs, "After IF Filter")

# Demodulation + Baseband Recovery
demod_out = baseband_recovery(if_out, Fs, B, mode="FM")

plt.figure(figsize=(10,4))
plt.plot(demod_out)
plt.title("Recovered Baseband Audio (Manual Superhet)")
plt.grid(True)
plt.tight_layout()
plt.show()

plot_frequency(demod_out, Fs, "Recovered Audio Spectrum")

print(f"IF Frequency: {IF} Hz")
print(f"IF Bandwidth: {B} Hz")
print(f"Image Frequency Rejected: {Fc + IF} Hz")

# ---------------------------------------------------------
# PHASE 4 — SNR SWEEP (MATCHES CODE A)
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

    results["AM_TRF"].append(
        run_system(am, msg, snr, trf_receiver, Fc=Fc, B=B, Fs=Fs, mode="AM")
    )
    results["AM_SUPER"].append(
        run_system(am, msg, snr, superhet_receiver, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="AM")
    )

    results["NBFM_TRF"].append(
        run_system(nbfm, msg, snr, trf_receiver, Fc=Fc, B=B, Fs=Fs, mode="FM")
    )
    results["NBFM_SUPER"].append(
        run_system(nbfm, msg, snr, superhet_receiver, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="FM")
    )

    results["WBFM_TRF"].append(
        run_system(wbfm, msg, snr, trf_receiver, Fc=Fc, B=B, Fs=Fs, mode="FM")
    )
    results["WBFM_SUPER"].append(
        run_system(wbfm, msg, snr, superhet_receiver, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="FM")
    )

# ---------------------------------------------------------
# OUTPUT SNR PLOTS + FM THRESHOLD
# ---------------------------------------------------------

for key, values in results.items():
    plt.figure(figsize=(8,5))
    plt.plot(snr_range, values, marker='o')
    plt.title(f"Output SNR vs Input SNR — {key.replace('_',' ')}")
    plt.xlabel("Input SNR (dB)")
    plt.ylabel("Output SNR (dB)")
    plt.grid(True)

    if "WBFM" in key:
        diffs = np.diff(values)
        threshold_index = np.argmax(diffs)
        threshold_snr = snr_range[threshold_index]

        plt.axvline(threshold_snr, color='red', linestyle='--',
                    label=f"FM Threshold ≈ {threshold_snr} dB")
        plt.legend()

    plt.tight_layout()
    plt.show()
