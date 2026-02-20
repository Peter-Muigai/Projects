import matplotlib.pyplot as plt
import numpy as np
from config import *
from baseband import generate_message
from modulation import am_modulate, nbfm_modulate, wbfm_armstrong
from channel import awgn
from filters import bandpass_filter, lowpass_filter
from receivers_trf import trf_receiver
from receivers_superhet import superhet_receiver
from analysis import run_system

# ---------------------------------------------------------
# BASEBAND + MODULATION
# ---------------------------------------------------------
t, msg = generate_message(Fs, duration=duration)
msg = lowpass_filter(msg, B, Fs)

am = am_modulate(msg, Fc, Fs)
nbfm = nbfm_modulate(msg, Fc, Fs, beta_nbfm)
wbfm = wbfm_armstrong(msg, Fc, Fs, beta_wbfm)

# ---------------------------------------------------------
# FREQUENCY PLOT FUNCTION
# ---------------------------------------------------------
def plot_frequency(x, Fs, title):
    N = len(x)
    X = np.fft.fftshift(np.fft.fft(x * np.hanning(N)))
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
plt.plot(t[:5000], msg[:5000])
plt.title("Message Signal m(t)")
plt.xlabel("Time (s)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,4))
plt.plot(t[:5000], am[:5000])
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
# PHASE 2.1 — TRF Receiver Stage Plots (AM)
# ---------------------------------------------------------
snr_test = 10
rx_am = awgn(am, snr_db=snr_test)
audio_am_trf, rf_stage_am, demod_am = trf_receiver(rx_am, Fc=Fc, B=B, Fs=Fs, mode="AM")

plt.figure(figsize=(10,4)); plt.plot(rf_stage_am[:5000]); plt.title("Phase 2.1: TRF — After BPF (AM)"); plt.grid(True); plt.tight_layout(); plt.show()
plt.figure(figsize=(10,4)); plt.plot(demod_am[:5000]); plt.title("Phase 2.1: TRF — Demodulated (AM)"); plt.grid(True); plt.tight_layout(); plt.show()
plt.figure(figsize=(10,4)); plt.plot(audio_am_trf[:5000]); plt.title("Phase 2.1: TRF — Audio (AM)"); plt.grid(True); plt.tight_layout(); plt.show()

# ---------------------------------------------------------
# PHASE 2.2 — Superhet Receiver Stage Plots (AM)
# ---------------------------------------------------------
rx_am_super = awgn(am, snr_db=snr_test)
audio_am_super, if_stage_am, demod_am_super = superhet_receiver(rx_am_super, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="AM")

plt.figure(figsize=(10,4)); plt.plot(if_stage_am[:5000]); plt.title("Phase 2.2: Superhet — IF Stage (AM)"); plt.grid(True); plt.tight_layout(); plt.show()
plt.figure(figsize=(10,4)); plt.plot(demod_am_super[:5000]); plt.title("Phase 2.2: Superhet — Demodulated (AM)"); plt.grid(True); plt.tight_layout(); plt.show()
plt.figure(figsize=(10,4)); plt.plot(audio_am_super[:5000]); plt.title("Phase 2.2: Superhet — Audio (AM)"); plt.grid(True); plt.tight_layout(); plt.show()

# ---------------------------------------------------------
# PHASE 2.3 — TRF Receiver Stage Plots (FM, NBFM)
# ---------------------------------------------------------
rx_fm = awgn(nbfm, snr_db=snr_test)
audio_fm_trf, rf_stage_fm, demod_fm = trf_receiver(rx_fm, Fc=Fc, B=B, Fs=Fs, mode="FM")

plt.figure(figsize=(10,4)); plt.plot(rf_stage_fm[:5000]); plt.title("Phase 2.3: TRF — After BPF (NBFM)"); plt.grid(True); plt.tight_layout(); plt.show()
plt.figure(figsize=(10,4)); plt.plot(demod_fm[:5000]); plt.title("Phase 2.3: TRF — Demodulated (NBFM)"); plt.grid(True); plt.tight_layout(); plt.show()
plt.figure(figsize=(10,4)); plt.plot(audio_fm_trf[:5000]); plt.title("Phase 2.3: TRF — Audio (NBFM)"); plt.grid(True); plt.tight_layout(); plt.show()

# ---------------------------------------------------------
# PHASE 2.4 — Superhet Receiver Stage Plots (FM, NBFM)
# ---------------------------------------------------------
rx_fm_super = awgn(nbfm, snr_db=snr_test)
audio_fm_super, if_stage_fm, demod_fm_super = superhet_receiver(rx_fm_super, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="FM")

plt.figure(figsize=(10,4)); plt.plot(if_stage_fm[:5000]); plt.title("Phase 2.4: Superhet — IF Stage (NBFM)"); plt.grid(True); plt.tight_layout(); plt.show()
plt.figure(figsize=(10,4)); plt.plot(demod_fm_super[:5000]); plt.title("Phase 2.4: Superhet — Demodulated (NBFM)"); plt.grid(True); plt.tight_layout(); plt.show()
plt.figure(figsize=(10,4)); plt.plot(audio_fm_super[:5000]); plt.title("Phase 2.4: Superhet — Audio (NBFM)"); plt.grid(True); plt.tight_layout(); plt.show()

# ---------------------------------------------------------
# PHASE 4 — SNR SWEEP (unchanged, but uses run_system)
# ---------------------------------------------------------
snr_range = np.arange(-5, 31, 5)
results = { "AM_TRF": [], "AM_SUPER": [], "NBFM_TRF": [], "NBFM_SUPER": [], "WBFM_TRF": [], "WBFM_SUPER": [] }

for snr in snr_range:
    results["AM_TRF"].append(run_system(am, msg, snr, trf_receiver, Fc=Fc, B=B, Fs=Fs, mode="AM"))
    results["AM_SUPER"].append(run_system(am, msg, snr, superhet_receiver, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="AM"))
    results["NBFM_TRF"].append(run_system(nbfm, msg, snr, trf_receiver, Fc=Fc, B=B, Fs=Fs, mode="FM"))
    results["NBFM_SUPER"].append(run_system(nbfm, msg, snr, superhet_receiver, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="FM"))
    results["WBFM_TRF"].append(run_system(wbfm, msg, snr, trf_receiver, Fc=Fc, B=B, Fs=Fs, mode="FM"))
    results["WBFM_SUPER"].append(run_system(wbfm, msg, snr, superhet_receiver, Fc=Fc, IF=IF, B=B, Fs=Fs, mode="FM"))

for key, values in results.items():
    plt.figure(figsize=(8,5))
    plt.plot(snr_range, values, marker='o')
    plt.title(f"Output SNR vs Input SNR — {key.replace('_', ' ')}")
    plt.xlabel("Input SNR (dB)")
    plt.ylabel("Output SNR (dB)")
    plt.grid(True)
    if "WBFM" in key:
        diffs = np.diff(values)
        threshold_index = np.argmax(diffs)
        threshold_snr = snr_range[threshold_index]
        plt.axvline(threshold_snr, color='red', linestyle='--', label=f"FM Threshold ≈ {threshold_snr} dB")
        plt.legend()
    plt.tight_layout()
    plt.show()
