import numpy as np
from channel import awgn
from baseband import lowpass_filter


def measure_snr(reference, recovered, B_msg, Fs):
    """
    Measure output SNR over message bandwidth
    """

    # Length alignment
    L = min(len(reference), len(recovered))
    reference = reference[:L]
    recovered = recovered[:L]

    # Band-limit both signals
    reference = lowpass_filter(reference, B_msg, Fs)
    recovered = lowpass_filter(recovered, B_msg, Fs)

    # Remove DC
    reference -= np.mean(reference)
    recovered -= np.mean(recovered)

    # Noise estimate
    noise = recovered - reference

    return 10 * np.log10(
        np.mean(reference**2) / (np.mean(noise**2) + 1e-12)
    )


def run_system(mod_signal, msg, snr_db, receiver_fn, *, B_msg, Fs, **rx_kwargs):
    """
    Generic system runner for SNR evaluation
    """

    # Channel
    noisy = awgn(mod_signal, snr_db)

    # Receiver (Fs is mandatory for all receivers)
    recovered = receiver_fn(noisy, Fs=Fs, **rx_kwargs)

    # Output SNR
    return measure_snr(msg, recovered, B_msg, Fs)
